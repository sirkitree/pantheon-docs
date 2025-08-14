# Pantheon Documentation Mirror

[![Last Update](https://img.shields.io/github/last-commit/sirkitree/pantheon-docs/main.svg?label=docs%20updated)](https://github.com/sirkitree/pantheon-docs/commits/main)
[![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Linux-blue)]()
[![Beta](https://img.shields.io/badge/status-early%20beta-orange)](https://github.com/sirkitree/pantheon-docs/issues)

Local mirror of Pantheon documentation files from https://docs.pantheon.io, updated every 3 hours.

## ⚠️ Early Beta Notice

**This is an early beta release**. There may be errors or unexpected behavior. If you encounter any issues, please [open an issue](https://github.com/sirkitree/pantheon-docs/issues) - your feedback helps improve the tool!

## 🆕 Version 1.0 - Initial Release

**New in this version:**
- 📋 **Pantheon Documentation Mirror**: Access Pantheon documentation locally
- 🍎 **Full macOS compatibility**: Native support for Mac users
- 🐧 **Linux support**: Tested on Ubuntu, Debian, and other distributions
- 🔧 **Auto-updating system**: Keeps documentation current automatically

## Why This Exists

- **Faster access** - Reads from local files instead of fetching from web
- **Automatic updates** - Attempts to stay current with the latest documentation
- **Track changes** - See what changed in docs over time
- **Better Claude integration** - Allows Claude to explore documentation more effectively
- **Offline access** - Documentation available even without internet connection

## Platform Compatibility

- ✅ **macOS**: Fully supported (tested on macOS 12+)
- ✅ **Linux**: Fully supported (Ubuntu, Debian, Fedora, etc.)
- ⏳ **Windows**: Not yet supported - [contributions welcome](#contributing)!

### Prerequisites

This tool requires the following to be installed:
- **git** - For cloning and updating the repository (usually pre-installed)
- **jq** - For JSON processing in the auto-update hook (pre-installed on macOS; Linux users may need `apt install jq` or `yum install jq`)
- **curl** - For downloading the installation script (usually pre-installed)
- **Claude Code** - Obviously :)

## Installation

Run this single command:

```bash
curl -fsSL https://raw.githubusercontent.com/sirkitree/pantheon-docs/main/install.sh | bash
```

This will:
1. Install to `~/.pantheon-docs` (or migrate existing installation)
2. Create the `/pantheon-docs` slash command to pass arguments to the tool and tell it where to find the docs
3. Set up a 'PreToolUse' 'Read' hook to enable automatic git pull when reading docs from the `~/.pantheon-docs`

**Note**: The command is `/pantheon-docs (user)` - it will show in your command list with "(user)" after it to indicate it's a user-created command.

## Usage

The `/pantheon-docs` command provides instant access to documentation with optional freshness checking.

### Default: Lightning-fast access (no checks)
```bash
/pantheon-docs drupal        # Instantly read Drupal documentation
/pantheon-docs wordpress     # Instantly read WordPress documentation
/pantheon-docs migrate       # Instantly read migration documentation
```

You'll see: `📚 Reading from local docs (run /pantheon-docs -t to check freshness)`

### Check documentation sync status with -t flag
```bash
/pantheon-docs -t           # Show sync status with GitHub
/pantheon-docs -t drupal    # Check sync status, then read Drupal docs
/pantheon-docs -t wordpress # Check sync status, then read WordPress docs
```

### See what's new
```bash
/pantheon-docs what's new   # Show recent documentation changes with diffs
```

### Uninstall
```bash
/pantheon-docs uninstall    # Get command to remove pantheon-docs completely
```

### Creative usage examples
```bash
# Natural language queries work great
/pantheon-docs what hosting options does Pantheon support?
/pantheon-docs explain the differences between environments

# Search across all docs
/pantheon-docs find all mentions of SSL
/pantheon-docs how do I set up custom domains?
```

## How Updates Work

The documentation attempts to stay current:
- GitHub Actions runs periodically to fetch new documentation
- When you use `/pantheon-docs`, it checks for updates
- Updates are pulled when available
- You may see "🔄 Updating documentation..." when this happens

Note: If automatic updates fail, you can always run the installer again to get the latest version.

## Updating from Previous Versions

Since this is version 1.0, there are no previous versions. However, for future updates, simply run:

```bash
curl -fsSL https://raw.githubusercontent.com/sirkitree/pantheon-docs/main/install.sh | bash
```

The installer will handle updates automatically.

## Troubleshooting

### Command not found
If `/pantheon-docs` returns "command not found":
1. Check if the command file exists: `ls ~/.claude/commands/pantheon-docs.md`
2. Restart Claude Code to reload commands
3. Re-run the installation script

### Documentation not updating
If documentation seems outdated:
1. Run `/pantheon-docs -t` to check sync status and force an update
2. Manually update: `cd ~/.pantheon-docs && git pull`
3. Check if GitHub Actions are running: [View Actions](https://github.com/sirkitree/pantheon-docs/actions)

### Installation errors
- **"git/jq/curl not found"**: Install the missing tool first
- **"Failed to clone repository"**: Check your internet connection
- **"Failed to update settings.json"**: Check file permissions on `~/.claude/settings.json`

## Uninstalling

To completely remove the docs integration:

```bash
/pantheon-docs uninstall
```

Or run:
```bash
~/.pantheon-docs/uninstall.sh
```

See [UNINSTALL.md](UNINSTALL.md) for manual uninstall instructions.

## Security Notes

- The installer modifies `~/.claude/settings.json` to add an auto-update hook
- The hook only runs `git pull` when reading documentation files
- All operations are limited to the documentation directory
- No data is sent externally - everything is local
- **Repository Trust**: The installer clones from GitHub over HTTPS. For additional security, you can:
  - Fork the repository and install from your own fork
  - Clone manually and run the installer from the local directory
  - Review all code before installation

## What's New

### v1.0 (Latest)
- Initial release of Pantheon documentation mirror
- Full macOS and Linux support
- Automatic documentation fetching and updates
- Claude Code integration with `/pantheon-docs` command

## Contributing

**Contributions are welcome!** This is a community project and we'd love your help:

- 🪟 **Windows Support**: Want to help add Windows compatibility? [Fork the repository](https://github.com/sirkitree/pantheon-docs/fork) and submit a PR!
- 🐛 **Bug Reports**: Found something not working? [Open an issue](https://github.com/sirkitree/pantheon-docs/issues)
- 💡 **Feature Requests**: Have an idea? [Start a discussion](https://github.com/sirkitree/pantheon-docs/issues)
- 📝 **Documentation**: Help improve docs or add examples

You can also use Claude Code itself to help build features - just fork the repo and let Claude assist you!

## Known Issues

As this is an early beta, you might encounter some issues:
- Auto-updates may occasionally fail on some network configurations
- Some documentation links might not resolve correctly
- Pantheon's documentation structure may change, requiring updates to the fetcher

If you find any issues not listed here, please [report them](https://github.com/sirkitree/pantheon-docs/issues)!

## Inspiration

This project is inspired by and adapted from [claude-code-docs](https://github.com/ericbuess/claude-code-docs) by Eric Buess. Thanks for the excellent foundation!

## License

Documentation content belongs to Pantheon.
This mirror tool is open source - contributions welcome!
