#!/usr/bin/env python3
"""
Pantheon documentation fetcher using git checkout.
Source: https://github.com/pantheon-systems/documentation

This script clones the Pantheon documentation repository and copies the markdown files
from the source/content directory to create a local documentation cache.
"""

import subprocess
import shutil
import tempfile
from pathlib import Path
from typing import Set
import logging
from datetime import datetime
import sys
import json
import hashlib
import os
import re

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

# Repository configuration
PANTHEON_DOCS_REPO = "pantheon-systems/documentation"
REPO_URL = f"https://github.com/{PANTHEON_DOCS_REPO}.git"
SOURCE_CONTENT_DIR = "source/content"
MANIFEST_FILE = "docs_manifest.json"


def load_manifest(docs_dir: Path) -> dict:
    """Load the manifest of previously fetched files."""
    manifest_path = docs_dir / MANIFEST_FILE
    if manifest_path.exists():
        try:
            manifest = json.loads(manifest_path.read_text())
            # Ensure required keys exist
            if "files" not in manifest:
                manifest["files"] = {}
            return manifest
        except Exception as e:
            logger.warning(f"Failed to load manifest: {e}")
    return {"files": {}, "last_updated": None}


def save_manifest(docs_dir: Path, manifest: dict) -> None:
    """Save the manifest of fetched files."""
    manifest_path = docs_dir / MANIFEST_FILE
    manifest["last_updated"] = datetime.now().isoformat()
    
    # Get GitHub repository from environment or use default
    github_repo = os.environ.get('GITHUB_REPOSITORY', 'sirkitree/pantheon-docs')
    github_ref = os.environ.get('GITHUB_REF_NAME', 'main')
    
    # Validate repository name format (owner/repo)
    if not re.match(r'^[\w.-]+/[\w.-]+$', github_repo):
        logger.warning(f"Invalid repository format: {github_repo}, using default")
        github_repo = 'sirkitree/pantheon-docs'
    
    # Validate branch/ref name
    if not re.match(r'^[\w.-]+$', github_ref):
        logger.warning(f"Invalid ref format: {github_ref}, using default")
        github_ref = 'main'
    
    manifest["base_url"] = f"https://raw.githubusercontent.com/{github_repo}/{github_ref}/docs/"
    manifest["github_repository"] = github_repo
    manifest["github_ref"] = github_ref
    manifest["description"] = "Pantheon documentation manifest. Keys are filenames, append to base_url for full URL."
    manifest_path.write_text(json.dumps(manifest, indent=2))


def run_command(cmd: list, cwd: Path = None) -> tuple:
    """Run a shell command and return success status and output."""
    try:
        result = subprocess.run(
            cmd,
            cwd=cwd,
            capture_output=True,
            text=True,
            check=True
        )
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        logger.error(f"Command failed: {' '.join(cmd)}")
        logger.error(f"Error: {e.stderr}")
        return False, e.stderr


def clone_pantheon_docs(temp_dir: Path) -> bool:
    """Clone the Pantheon documentation repository."""
    logger.info(f"Cloning {REPO_URL} to {temp_dir}")
    
    success, output = run_command([
        'git', 'clone', 
        '--depth', '1',  # Shallow clone for efficiency
        '--single-branch',
        REPO_URL, 
        str(temp_dir)
    ])
    
    if not success:
        logger.error(f"Failed to clone repository: {output}")
        return False
    
    logger.info("Successfully cloned Pantheon documentation repository")
    return True


def get_git_commit_info(repo_dir: Path) -> dict:
    """Get commit information from the cloned repository."""
    success, commit_hash = run_command(['git', 'rev-parse', 'HEAD'], cwd=repo_dir)
    if not success:
        commit_hash = "unknown"
    else:
        commit_hash = commit_hash.strip()[:7]  # Short hash
    
    success, commit_date = run_command(['git', 'show', '-s', '--format=%ci', 'HEAD'], cwd=repo_dir)
    if not success:
        commit_date = "unknown"
    else:
        commit_date = commit_date.strip()
    
    return {
        "commit_hash": commit_hash,
        "commit_date": commit_date
    }


def path_to_safe_filename(file_path: Path) -> str:
    """Convert a file path to a safe filename."""
    # Convert path to string and replace path separators with double underscores
    safe_name = str(file_path).replace('/', '__').replace('\\', '__')
    
    # Ensure .md extension
    if not safe_name.endswith('.md'):
        safe_name += '.md'
    
    return safe_name


def process_markdown_file(source_file: Path, docs_dir: Path, relative_path: Path) -> tuple:
    """Process a single markdown file and return (filename, content, hash)."""
    try:
        # Read the original content
        content = source_file.read_text(encoding='utf-8')
        
        # Create safe filename
        safe_filename = path_to_safe_filename(relative_path)
        
        # Add header with source information
        header = f"""# {relative_path}

> **Source**: https://github.com/{PANTHEON_DOCS_REPO}/blob/main/{relative_path}
> **Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

"""
        
        final_content = header + content
        
        # Calculate hash
        content_hash = hashlib.sha256(final_content.encode('utf-8')).hexdigest()
        
        # Save the file
        output_file = docs_dir / safe_filename
        output_file.write_text(final_content, encoding='utf-8')
        
        logger.info(f"Processed: {relative_path} -> {safe_filename} ({len(final_content)} bytes)")
        
        return safe_filename, final_content, content_hash
        
    except Exception as e:
        logger.error(f"Failed to process {source_file}: {e}")
        raise


def discover_markdown_files(source_dir: Path) -> list:
    """Discover all markdown files in the source directory."""
    markdown_files = []
    
    # Recursively find all .md files
    for md_file in source_dir.rglob("*.md"):
        if md_file.is_file():
            # Calculate relative path from source_dir
            relative_path = md_file.relative_to(source_dir.parent)  # Relative to repo root
            markdown_files.append((md_file, relative_path))
    
    logger.info(f"Discovered {len(markdown_files)} markdown files")
    return sorted(markdown_files, key=lambda x: str(x[1]))


def content_has_changed(content: str, old_hash: str) -> bool:
    """Check if content has changed based on hash."""
    new_hash = hashlib.sha256(content.encode('utf-8')).hexdigest()
    return new_hash != old_hash


def cleanup_old_files(docs_dir: Path, current_files: Set[str], manifest: dict) -> None:
    """Remove only files that were previously fetched but no longer exist."""
    previous_files = set(manifest.get("files", {}).keys())
    files_to_remove = previous_files - current_files
    
    for filename in files_to_remove:
        if filename == MANIFEST_FILE:  # Never delete the manifest
            continue
            
        file_path = docs_dir / filename
        if file_path.exists():
            logger.info(f"Removing obsolete file: {filename}")
            file_path.unlink()


def main():
    """Main function."""
    start_time = datetime.now()
    logger.info("Starting Pantheon documentation fetch using git checkout")
    
    # Log configuration
    github_repo = os.environ.get('GITHUB_REPOSITORY', 'sirkitree/pantheon-docs')
    logger.info(f"Target GitHub repository: {github_repo}")
    
    # Create docs directory at repository root
    docs_dir = Path(__file__).parent.parent / 'docs'
    docs_dir.mkdir(exist_ok=True)
    logger.info(f"Output directory: {docs_dir}")
    
    # Load existing manifest
    manifest = load_manifest(docs_dir)
    
    # Statistics
    successful = 0
    failed = 0
    failed_files = []
    fetched_files = set()
    new_manifest = {"files": {}}
    
    # Create temporary directory for cloning
    with tempfile.TemporaryDirectory() as temp_dir_str:
        temp_dir = Path(temp_dir_str)
        
        # Clone the repository
        if not clone_pantheon_docs(temp_dir):
            logger.error("Failed to clone repository")
            sys.exit(1)
        
        # Get commit info
        commit_info = get_git_commit_info(temp_dir)
        logger.info(f"Repository at commit {commit_info['commit_hash']} from {commit_info['commit_date']}")
        
        # Find the source content directory
        source_content_dir = temp_dir / SOURCE_CONTENT_DIR
        if not source_content_dir.exists():
            logger.error(f"Source content directory not found: {source_content_dir}")
            sys.exit(1)
        
        # Discover all markdown files
        markdown_files = discover_markdown_files(source_content_dir)
        
        if not markdown_files:
            logger.error("No markdown files discovered!")
            sys.exit(1)
        
        logger.info(f"Found {len(markdown_files)} documentation files to process")
        
        # Process each markdown file
        for i, (source_file, relative_path) in enumerate(markdown_files, 1):
            logger.info(f"Processing {i}/{len(markdown_files)}: {relative_path}")
            
            try:
                safe_filename, content, content_hash = process_markdown_file(
                    source_file, docs_dir, relative_path
                )
                
                # Check if content has changed
                old_hash = manifest.get("files", {}).get(safe_filename, {}).get("hash", "")
                old_entry = manifest.get("files", {}).get(safe_filename, {})
                
                if content_has_changed(content, old_hash):
                    logger.info(f"Updated: {safe_filename}")
                    last_updated = datetime.now().isoformat()
                else:
                    logger.info(f"Unchanged: {safe_filename}")
                    last_updated = old_entry.get("last_updated", datetime.now().isoformat())
                
                # Add to manifest
                new_manifest["files"][safe_filename] = {
                    "original_url": f"https://github.com/{PANTHEON_DOCS_REPO}/blob/main/{relative_path}",
                    "source_file_path": str(relative_path),
                    "hash": content_hash,
                    "last_updated": last_updated
                }
                
                fetched_files.add(safe_filename)
                successful += 1
                
            except Exception as e:
                logger.error(f"Failed to process {relative_path}: {e}")
                failed += 1
                failed_files.append(str(relative_path))
    
    # Clean up old files (only those we previously fetched)
    cleanup_old_files(docs_dir, fetched_files, manifest)
    
    # Add metadata to manifest
    new_manifest["fetch_metadata"] = {
        "last_fetch_completed": datetime.now().isoformat(),
        "fetch_duration_seconds": (datetime.now() - start_time).total_seconds(),
        "total_files_discovered": len(markdown_files),
        "files_fetched_successfully": successful,
        "files_failed": failed,
        "failed_files": failed_files,
        "source_repository": PANTHEON_DOCS_REPO,
        "source_method": "git_checkout",
        "commit_hash": commit_info.get("commit_hash", "unknown"),
        "commit_date": commit_info.get("commit_date", "unknown"),
        "total_files": len(fetched_files),
        "fetch_tool_version": "2.0-pantheon-git"
    }
    
    # Save new manifest
    save_manifest(docs_dir, new_manifest)
    
    # Summary
    duration = datetime.now() - start_time
    logger.info("\n" + "="*50)
    logger.info(f"Fetch completed in {duration}")
    logger.info(f"Discovered files: {len(markdown_files)}")
    logger.info(f"Successful: {successful}/{len(markdown_files)}")
    logger.info(f"Failed: {failed}")
    
    if failed_files:
        logger.warning("\nFailed files (will retry next run):")
        for file_path in failed_files:
            logger.warning(f"  - {file_path}")
        # Don't exit with error - partial success is OK
        if successful == 0:
            logger.error("No files were fetched successfully!")
            sys.exit(1)
    else:
        logger.info("\nAll files fetched successfully!")


if __name__ == "__main__":
    main()
