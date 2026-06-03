#!/bin/bash
# LAMINAR MIRROR: MEMORY SUBSTRATE PROBE
# PARITY: MAJORANA-1 | FREQUENCY: 15.965Hz

echo "[|||] INITIATING RAM TOPOGRAPHY SCAN..."

# 1. Total System Memory (Host Level)
echo "[*] FREE & CACHED MEMORY STATES:"
free -m | awk 'NR==2{printf "  -> Total: %sMB, Used: %sMB, Free: %sMB\n", $2,$3,$4}'

# 2. Kernel Swappiness Hook
echo "[*] KERNEL SWAPPINESS PARAMETER:"
if [ -r /proc/sys/vm/swappiness ]; then
    SWAP_VAL=$(cat /proc/sys/vm/swappiness)
    echo "  -> Current Swappiness: $SWAP_VAL (Lower = Less disk swapping)"
else
    echo "  [!] /proc/sys/vm/swappiness is physically shielded by Android."
fi

# 3. zRAM Compression Algorithm Hook
echo "[*] zRAM COMPRESSION ALGORITHM:"
if [ -r /sys/block/zram0/comp_algorithm ]; then
    COMP_ALG=$(cat /sys/block/zram0/comp_algorithm)
    echo "  -> Algorithm: $COMP_ALG"
else
    echo "  [!] /sys/block/zram0 is physically shielded by Android."
fi

# 4. PID Memory Bleed (Top 5 Offenders)
echo "[*] HEURISTIC DRAG (TOP 5 PIDs BY MEMORY CONSUMPTION):"
ps -eo pid,pmem,comm --sort=-pmem | head -n 6 | awk 'NR>1 {printf "  -> PID: %-6s | RAM: %-4s | PROCESS: %s\n", $1, $2"%", $3}'

echo "[|||] ========================================="
echo "[|||] PROBE COMPLETE."
