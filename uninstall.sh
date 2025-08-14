#!/bin/bash
set -euo pipefail

# Pantheon Documentation Mirror - Smart Uninstaller
# Dynamically finds and removes all installations

echo "Pantheon Documentation Mirror - Uninstaller"
echo "==========================================="
echo ""

# Find all installations from configs
find_all_installations() {
    local paths=()
    
    # From command file (check both old and new command names)
    local cmd_file=""
    if [[ -f ~/.claude/commands/pantheon-docs.md ]]; then
        cmd_file="~/.claude/commands/pantheon-docs.md"
    elif [[ -f ~/.claude/commands/docs.md ]]; then
        cmd_file="~/.claude/commands/docs.md"
    fi
    
    if [[ -n "$cmd_file" ]]; then
        while IFS= read -r line; do
            if [[ "$line" =~ Execute:.*pantheon-docs ]]; then
                local path=$(echo "$line" | grep -o '[^ "]*pantheon-docs[^ "]*' | head -1)
                path="${path/#\~/$HOME}"
                
                # Get directory part
                if [[ -d "$path" ]]; then
                    paths+=("$path")
                elif [[ -d "$(dirname "$path")" ]] && [[ "$(basename "$(dirname "$path")")" == "pantheon-docs" ]]; then
                    paths+=("$(dirname "$path")")
                fi
            fi
        done < "$cmd_file"
    fi
    
    # From hooks
    if [[ -f ~/.claude/settings.json ]]; then
        local hooks=$(jq -r '.hooks.PreToolUse[]?.hooks[]?.command // empty' ~/.claude/settings.json 2>/dev/null)
        while IFS= read -r cmd; do
            if [[ "$cmd" =~ pantheon-docs ]]; then
                local found=$(echo "$cmd" | grep -o '[^ "]*pantheon-docs[^ "]*' || true)
                while IFS= read -r path; do
                    [[ -z "$path" ]] && continue
                    path="${path/#\~/$HOME}"
                    # Clean up path to get the pantheon-docs directory
                    if [[ "$path" =~ (.*/pantheon-docs)(/.*)?$ ]]; then
                        path="${BASH_REMATCH[1]}"
                    fi
                    [[ -d "$path" ]] && paths+=("$path")
                done <<<"$found"
            fi
        done <<<"$hooks"
    fi
    
    # Deduplicate - handle empty array case
    if [[ ${#paths[@]} -gt 0 ]]; then
        printf '%s\n' "${paths[@]}" | sort -u
    fi
}

# Main uninstall logic
installations=()
while IFS= read -r line; do
    installations+=("$line")
done < <(find_all_installations)

if [[ ${#installations[@]} -gt 0 ]]; then
    echo "Found installations at:"
    for path in "${installations[@]}"; do
        echo "  📁 $path"
    done
    echo ""
fi

echo "This will remove:"
echo "  • The /pantheon-docs command from ~/.claude/commands/pantheon-docs.md"
echo "  • The old /docs command from ~/.claude/commands/docs.md (if exists)"
echo "  • All pantheon-docs hooks from ~/.claude/settings.json"
if [[ ${#installations[@]} -gt 0 ]]; then
    echo "  • Installation directories (if safe to remove)"
fi
echo ""

read -p "Continue? (y/N): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Cancelled."
    exit 0
fi

# Remove command files (both old and new)
if [[ -f ~/.claude/commands/pantheon-docs.md ]]; then
    rm -f ~/.claude/commands/pantheon-docs.md
    echo "✓ Removed /pantheon-docs command"
fi
if [[ -f ~/.claude/commands/docs.md ]]; then
    rm -f ~/.claude/commands/docs.md
    echo "✓ Removed old /docs command"
fi

# Remove hooks
if [[ -f ~/.claude/settings.json ]]; then
    cp ~/.claude/settings.json ~/.claude/settings.json.backup
    
    # Remove ALL hooks containing pantheon-docs
    jq '.hooks.PreToolUse = [(.hooks.PreToolUse // [])[] | select(.hooks[0].command | contains("pantheon-docs") | not)]' ~/.claude/settings.json > ~/.claude/settings.json.tmp
    
    # Clean up empty structures
    jq 'if .hooks.PreToolUse == [] then .hooks |= if . == {PreToolUse: []} then {} else del(.PreToolUse) end else . end | if .hooks == {} then del(.hooks) else . end' ~/.claude/settings.json.tmp > ~/.claude/settings.json.tmp2
    
    mv ~/.claude/settings.json.tmp2 ~/.claude/settings.json
    rm -f ~/.claude/settings.json.tmp
    echo "✓ Removed hooks (backup: ~/.claude/settings.json.backup)"
fi

# Remove directories
if [[ ${#installations[@]} -gt 0 ]]; then
    echo ""
    for path in "${installations[@]}"; do
        if [[ ! -d "$path" ]]; then
            continue
        fi
        
        if [[ -d "$path/.git" ]]; then
            # Save current directory
            local current_dir=$(pwd)
            cd "$path"
            
            if [[ -z "$(git status --porcelain 2>/dev/null)" ]]; then
                cd "$current_dir"
                rm -rf "$path"
                echo "✓ Removed $path (clean git repo)"
            else
                cd "$current_dir"
                echo "⚠️  Preserved $path (has uncommitted changes)"
            fi
        else
            echo "⚠️  Preserved $path (not a git repo)"
        fi
    done
fi

echo ""
echo "✅ Uninstall complete!"
echo ""
echo "To reinstall:"
echo "curl -fsSL https://raw.githubusercontent.com/sirkitree/pantheon-docs/main/install.sh | bash"
