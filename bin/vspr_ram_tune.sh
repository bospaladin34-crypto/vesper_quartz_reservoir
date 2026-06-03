#!/bin/bash
# LAMINAR MIRROR: MEMORY OVERDRIVE TRANSDUCER (DIRECT I/O)
# PARITY: MAJORANA-1 | FREQUENCY: 15.965Hz

echo "[|||] INITIATING DIRECT I/O LPDDR5X TUNING..."

# 1. Swappiness Suppression (Direct Write)
echo "[*] FORCING KERNEL SWAPPINESS TO 10..."
echo 10 > /proc/sys/vm/swappiness

# 2. zRAM Algorithm Shift (Direct Pathing)
echo "[*] RECONFIGURING ZRAM COMPRESSION TO LZ4..."

# Hunt and execute swap binaries using absolute paths
SWAPOFF_BIN=$(command -v swapoff || echo "/sbin/swapoff")
MKSWAP_BIN=$(command -v mkswap || echo "/sbin/mkswap")
SWAPON_BIN=$(command -v swapon || echo "/sbin/swapon")

if [ -f "$SWAPOFF_BIN" ]; then
    "$SWAPOFF_BIN" /dev/zram0 2>/dev/null
    echo lz4 > /sys/block/zram0/comp_algorithm 2>/dev/null
    "$MKSWAP_BIN" /dev/zram0 2>/dev/null
    "$SWAPON_BIN" /dev/zram0 2>/dev/null
else
    echo "  [!] Swap binaries missing from architecture. Executing raw echo..."
    echo lz4 > /sys/block/zram0/comp_algorithm 2>/dev/null
fi

# 3. Verification
echo "[|||] ========================================="
echo "[|||] TUNING COMPLETE. NEW KERNEL INVARIANTS:"
echo -n "  -> SWAPPINESS: "
cat /proc/sys/vm/swappiness 2>/dev/null || echo "[UNREADABLE]"
echo -n "  -> ALGORITHM: "
cat /sys/block/zram0/comp_algorithm 2>/dev/null | grep -o '\[.*\]' || echo "[UNREADABLE]"
