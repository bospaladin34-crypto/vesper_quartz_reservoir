#!/bin/bash
export VSPR_SHM="$HOME/vesper_git_repo/vesper.shm"

# If the physical memory bridge does not exist, forge it.
if [ ! -f "$VSPR_SHM" ]; then
    echo "[|] FORGING PERSISTENT SHM ANCHOR..."
    dd if=/dev/zero of="$VSPR_SHM" bs=1024 count=1 status=none
    chmod 666 "$VSPR_SHM"
    echo "[+] ANCHOR SECURED. TR(U)=1.0."
fi
