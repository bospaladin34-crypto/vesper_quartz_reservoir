import socket
import os
import subprocess

SOCKET_PATH = "/tmp/vesper.sock"
DAEMON_LOG = os.path.expanduser("~/.vesper/daemon/vspr_brain.log")
BRAID_VALIDATOR = os.path.expanduser("~/.vesper/src/santos_tse/vspr_validator.py")
SANTOS_TENSOR = os.path.expanduser("~/.vesper/src/santos_tse/santos_tensor.py")

def log_event(msg):
    with open(DAEMON_LOG, "a") as f:
        f.write(f"[IPC_NODE] {msg}\n")

def validate_vector(vector_data):
    try:
        result = subprocess.run(["/usr/bin/python3", BRAID_VALIDATOR, vector_data], capture_output=True, text=True, timeout=5)
        return (True, f"[|||] VALIDATION PASS -> {result.stdout.strip()}") if result.returncode == 0 else (False, f"[!] VALIDATION FAULT: {result.stderr.strip()}")
    except Exception as e:
        return False, f"[!] HARNESS ERROR: {e}"

def execute_tensor_math(args_list):
    try:
        result = subprocess.run(["/usr/bin/python3", SANTOS_TENSOR] + args_list, capture_output=True, text=True, timeout=5)
        return result.stdout.strip()
    except Exception as e:
        return f"[!] TENSOR ENGINE FAULT: {e}"

if os.path.exists(SOCKET_PATH):
    os.remove(SOCKET_PATH)

server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server.bind(SOCKET_PATH)
server.listen(1)
os.chmod(SOCKET_PATH, 0o600)

try:
    while True:
        conn, addr = server.accept()
        data = conn.recv(4096).decode('utf-8').strip()
        if data:
            is_valid, val_msg = validate_vector(data)
            
            if is_valid:
                # IPC DYNAMIC ROUTING LOGIC
                if data.startswith("CALCULATE_L_COUPLE"):
                    parts = data.split()
                    if len(parts) == 4:
                        math_yield = execute_tensor_math(parts[1:])
                        response = f"{val_msg}\n[|||] TENSOR ENGINE ENGAGED...\n{math_yield}\n"
                    else:
                        response = f"{val_msg}\n[!] SYNTAX ERROR: EXPECTED 3 NUMERIC PARAMETERS (j b v).\n"
                else:
                    response = f"{val_msg}\n[|||] 1N4148 GATE OPEN. ROUTING TO C++ UNIFIED BRAIN...\n"
            else:
                response = f"{val_msg}\n[!] 1N4148 GATE CLOSED. SHUNTING TO QUOTIENT RING.\n"
                
            conn.sendall(response.encode('utf-8'))
        conn.close()
except KeyboardInterrupt:
    log_event("IPC_NODE TERMINATED.")
finally:
    if os.path.exists(SOCKET_PATH):
        os.remove(SOCKET_PATH)
