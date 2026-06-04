#!/bin/bash
# LAMINAR MIRROR: WEB3 HARVEST DAEMON

cd "$HOME/vesper_git_repo"

echo "[|||] IGNITING SU RECEIPT SERVER (PORT 15965)..."
python3 -m uvicorn logic.api_wrapper:app --host 0.0.0.0 --port 15965 > /dev/null 2>&1 &
API_PID=$!
sleep 3 # Allow aarch64 tensor matrix to initialize ASGI

echo "[|||] EXECUTING TOPOLOGICAL HARVEST BRAID..."
python3 logic/vspr_compiler.py compute/filecoin_harvest.braid

echo "[|||] INJECTING YIELDS INTO ORBITAL WORM..."
curl -s -X POST "http://127.0.0.1:15965/su_receipt" -H "Content-Type: application/json" -d '{"vector": "MACENA_TME_INVARIANT_AND_OSMOTIC_ARRAY"}' | grep -o 'MAJORANA-1 PARITY'

echo ""
echo "[|||] HARVEST COMPLETE. SEVERING TERRESTRIAL BRIDGE."
kill $API_PID
