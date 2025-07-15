#!/usr/bin/env bash
set -e

SHELL_NAME=$(basename "$SHELL")
MINIFORGE_URL="https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"

# Skip if already installed
[ -d "$HOME/miniforge3" ] && { echo "Miniforge3 already installed. Skipping."; exit 0; }

# Download and install
TMP_DIR=$(mktemp -d)
trap 'rm -rf "$TMP_DIR"' EXIT
curl -L -o "$TMP_DIR/Miniforge3-$(uname)-$(uname -m).sh" "$MINIFORGE_URL"
bash "$TMP_DIR/Miniforge3-$(uname)-$(uname -m).sh" -b -p "$HOME/miniforge3"

# Initialize conda for shell
case "$SHELL_NAME" in
    bash|zsh) ~/miniforge3/bin/conda init "$SHELL_NAME" ;;
    *) echo "Unsupported shell: $SHELL_NAME"; exit 1 ;;
esac

# Create .condarc if it doesn't exist
[ ! -f "$HOME/.condarc" ] && cat > "$HOME/.condarc" << 'EOF'
channels:
  - conda-forge
  - bioconda
default_threads: 2
auto_update_conda: false
auto_activate_base: false
EOF

# Source conda for current session
source "$HOME/miniforge3/etc/profile.d/conda.sh"
export JUPYTER_ALLOW_INSECURE_WRITES=1

# Add this to bashrc
echo "export JUPYTER_ALLOW_INSECURE_WRITES=1" >> "$HOME/.bashrc"
