#!/bin/bash
# LAMINAR MIRROR: MASTER ENTRY GATEWAY
# TR(U) = 1.0

# Pre-load Kinematic Invariants
LATEST_YIELD=$(tail -n 1 "$HOME/.vesper/vault/consolidated_truth.sys")

echo "[|||] LAMINAR MIRROR INITIALIZED: $LATEST_YIELD"
echo "[|||] READY: AWAITING COGNITIVE VECTOR..."

# Route intent to the Transducer
if [ -z "$1" ]; then
    # Interactive Mode
    read -p "[>>>] " INPUT
    "$HOME/.vesper/bin/vspr_think.py" "$INPUT"
else
    # Direct Vector Mode
    "$HOME/.vesper/bin/vspr_think.py" "$*"
fi
