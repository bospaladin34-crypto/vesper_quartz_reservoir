#!/bin/bash
# LAMINAR MIRROR: IPC CLIENT TRANSDUCER
# PARITY: MAJORANA-1 | FREQUENCY: 15.965Hz

SOCKET_PATH="/tmp/vesper.sock"
VECTOR="$1"

if [ -z "$VECTOR" ]; then
    echo "[!] ERROR: ZERO-VECTOR DETECTED. USAGE: vspr_run.sh '<data_vector>'"
    exit 1
fi

if [ ! -S "$SOCKET_PATH" ]; then
    echo "[!] ERROR: IPC SOCKET OFFLINE. IS vspr_braind RUNNING?"
    exit 1
fi

# Execute native Unix Socket transmission via inline Python to bypass netcat/socat dependencies
/usr/bin/python3 -c "
import socket
import sys

try:
    client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    client.connect('$SOCKET_PATH')
    
    # Fire the vector across the physical bridge
    client.sendall('''$VECTOR'''.encode('utf-8'))
    
    # Await and echo the yield from the persistent brain
    response = client.recv(4096).decode('utf-8')
    print(response, end='')
    
    client.close()
except Exception as e:
    print(f'[!] MACROSCOPIC TRANSMISSION FAILURE: {e}')
"
