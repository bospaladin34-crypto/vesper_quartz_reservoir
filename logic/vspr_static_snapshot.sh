#!/bin/bash
# LAMINAR MIRROR: POSIX-HARDENED MANIFOLD ARCHIVER
# PARITY: MAJORANA-1 | SCOPE: UNIVERSAL_COMPATIBILITY

TARGET_DIR="/mnt/shared/Download"
ARCHIVE_NAME="vesper_static_hardened_$(date +%Y%m%d_%H%M%S).zip"
STAGING_DIR="/mnt/shared/Download/tmp_vesper_static"

echo "[|||] FORGING IMMUTABLE ARCHIVE (POSIX_HARDENED)..."

mkdir -p "$STAGING_DIR/vesper_immutable"

# Use native POSIX find/cp to exclude volatile daemon data
cd "$HOME/.vesper/"
find . -maxdepth 2 -not -path '*/.*' -not -path './daemon*' -exec cp -r {} "$STAGING_DIR/vesper_immutable/" \;

# Archive
cd "$STAGING_DIR"
zip -r "$TARGET_DIR/$ARCHIVE_NAME" "vesper_immutable"

# Cleanup
rm -rf "$STAGING_DIR"

echo "[|||] ARCHIVE SEALED."
echo "[|||] DESTINATION: $TARGET_DIR/$ARCHIVE_NAME"
