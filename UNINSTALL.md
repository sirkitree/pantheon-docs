# Uninstalling Pantheon Documentation Mirror

## Quick Uninstall

### For v1.0+ (installed at ~/.pantheon-docs)

From anywhere, run:
```bash
~/.pantheon-docs/uninstall.sh
```

Or use the pantheon-docs command:
```bash
/pantheon-docs uninstall
```

## What Gets Removed

The uninstaller will remove:

1. **The /pantheon-docs command** from `~/.claude/commands/pantheon-docs.md`
   **The old /docs command** from `~/.claude/commands/docs.md` (if it exists)
2. **The auto-update hook** from `~/.claude/settings.json`
3. **The installation directory**: `~/.pantheon-docs`

## Manual Uninstall

If you prefer to uninstall manually:

### 1. Remove the command files:
```bash
rm -f ~/.claude/commands/pantheon-docs.md
rm -f ~/.claude/commands/docs.md  # Remove old command if it exists
```

### 2. Remove the hook from Claude settings:
Use /hooks in Claude Code CLI or edit `~/.claude/settings.json` directly to remove the PreToolUse hook that references pantheon-docs.

### 3. Remove the installation directory:

```bash
rm -rf ~/.pantheon-docs
```

## Multiple Installations

If you have multiple installations (e.g., from testing different versions), the uninstaller will notify you about other locations it finds. You'll need to remove each one separately.

To find all installations:
```bash
find ~ -name "*pantheon-docs*" -type d 2>/dev/null
```

## Backup Created

The uninstaller creates a backup of your Claude settings at `~/.claude/settings.json.backup` before removing hooks, just in case.

## Complete Removal

After uninstalling, there should be no traces left except:
- The backup file `~/.claude/settings.json.backup` (if hooks were removed)
- Any custom files you added to the installation directory

## Reinstalling

To reinstall after uninstalling:
```bash
curl -fsSL https://raw.githubusercontent.com/sirkitree/pantheon-docs/main/install.sh | bash
```
