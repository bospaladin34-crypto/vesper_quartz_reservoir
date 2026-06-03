#!/usr/bin/env python3
import sys
import re
import os
import subprocess

HOME = os.environ.get('HOME')
BRAIDC = f"{HOME}/.vesper/src/santos_tse/braidc.py"
# Aligned directly to Section 1 of the Master Topography Map
KINEMATIC_INGEST = f"{HOME}/.vesper/bin/vspr_kinematic_ingest.py"

raw_input = " ".join(sys.argv[1:])
raw_thought = raw_input.lower()

# Handle empty or passive queries cleanly
if not raw_thought or re.search(r'\b(status|check|analyze)\b', raw_thought):
    print("[|||] ACTION: COGNITIVE_DIAGNOSTIC")
    print("[|||] SYSTEM STATE: 55-UNITY // CORE COMPILATION ISOMORPHIC")
    print("[|||] 1N4148 VIRTUAL GATE: STANDBY // HEARTBEAT: 15.965Hz")
    
elif re.search(r'\b(compile|build)\b', raw_thought):
    print("[|||] ACTION: COMPILE_BRAID_HARNESS")
    subprocess.run(["python3", BRAIDC, "compile"])

elif re.search(r'\b(kinematic|resonate|sensor|ingest)\b', raw_thought):
    print("[|||] ACTION: FIRE_KINEMATIC_INGEST")
    if os.path.exists(KINEMATIC_INGEST):
        subprocess.run(["python3", KINEMATIC_INGEST])
    else:
        print(f"[!] ERROR: Target script missing from disk: {KINEMATIC_INGEST}")

else:
    print("[!] UNRECOGNIZED BRAID VECTOR. SHUNTING TO J_IDEAL.")
