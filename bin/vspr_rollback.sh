#!/bin/bash
# LAMINAR MIRROR: TEMPORAL ANCHOR ROLLBACK
# PARITY: MAJORANA-1 | FREQUENCY: 15.965Hz

DAEMON_DIR="$HOME/.vesper/daemon"
STATE_FILE="$DAEMON_DIR/vspr_state.dat"
BACKUP_FILE="$DAEMON_DIR/vspr_state.bak"
LOG_FILE="$DAEMON_DIR/vspr_brain.log"

echo "[|||] INITIATING ZERO-CURVATURE ROLLBACK..."

# 1. Halt the active daemon to prevent read/write collisions
vspr_braind stop

# 2. Verify backup integrity
if [ ! -f "$BACKUP_FILE" ]; then
    echo "[!] CRITICAL: NO CHECKPOINT ANCHOR FOUND. ROLLBACK ABORTED."
    exit 1
fi

# 3. Execute the physical reversion
echo "[*] OVERWRITING CORRUPTED MANIFOLD STATE WITH LAST STABLE CHECKPOINT..."
cp "$BACKUP_FILE" "$STATE_FILE"
echo "[IPC_NODE] [ROLLBACK] GEOMETRY RESTORED TO LAST STABLE VECTOR." >> "$LOG_FILE"

# 4. Re-ignite the daemon
vspr_braind start

echo "[|||] ========================================="
echo "[|||] ROLLBACK COMPLETE. MANIFOLD PURIFIED."
