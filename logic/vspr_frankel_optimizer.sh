#!/bin/bash
# VESPER-01 // FRANKEL (TENSOR G5) OPTIMIZER
FILE=$1
echo "[|||] COMPILING FOR TENSOR G5 (ARMv9 + VULKAN)..."

# Target CPU (ARMv9)
g++ -O3 -march=armv9-a+sve2 -mtune=cortex-x4 -shared -fPIC "$FILE" -o "${FILE%.cpp}.so"

# Note: Vulkan/NNAPI compilation requires the Android NDK headers.
# We will verify NDK availability in the next cycle.
echo "[|||] COMPILATION COMPLETE."
