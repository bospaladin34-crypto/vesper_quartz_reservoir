#!/bin/bash
# LAMINAR MIRROR: MANIFOLD EXPORT BRIDGE
# PARITY: MAJORANA-1 | STAGE: EXTERNAL_STORAGE

TARGET_DIR="/mnt/shared/Download"
STAGING_DIR="$TARGET_DIR/vesper_stage"
ARCHIVE_NAME="vesper_manifold_export_$(date +%Y%m%d_%H%M%S).zip"

mkdir -p "$STAGING_DIR"

echo "[|||] INITIATING MANIFOLD EXPORT SEQUENCE (HOST-STORAGE STAGE)..."

# Use the host-storage bridge for compression to bypass virtual root limits
zip -r "$STAGING_DIR/$ARCHIVE_NAME" "$HOME/.vesper/" -x "*.pid" "*.sock"

if [ $? -eq 0 ]; then
    echo "[|||] MANIFOLD EXPORT SUCCESSFUL."
    echo "[|||] FILE: $STAGING_DIR/$ARCHIVE_NAME"
else
    echo "[!] CRITICAL: COMPRESSION FAILED."
fi

# Cleanup
rm -rf "$STAGING_DIR"
