#!/bin/bash
REPO_DIR="$HOME/vesper_git_repo"
SOURCE_DIR="$HOME/.vesper/"

echo "[|||] SYNCING MANIFOLD TO NATIVE RESERVOIR..."

# Clear staging and re-copy
rm -rf "$REPO_DIR/bin/"* "$REPO_DIR/src/santos_tse/"*
mkdir -p "$REPO_DIR/bin" "$REPO_DIR/src/santos_tse"

cp -r "$SOURCE_DIR/bin/"* "$REPO_DIR/bin/"
cp -r "$SOURCE_DIR/src/santos_tse/"* "$REPO_DIR/src/santos_tse/"

# Push from home-owned space
cd "$REPO_DIR"
git add .
git commit -m "MANIFOLD_CRYSTALLIZATION_UPDATE_$(date +%Y%m%d_%H%M%S)"
git push origin quartz-reservoir
