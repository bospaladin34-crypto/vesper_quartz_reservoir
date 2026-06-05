#!/usr/bin/env python3
import zmq
import sys

def transmit_intent(intent_string):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://127.0.0.1:15967")
    
    print(f"[|||] TRANSMITTING: {intent_string}")
    socket.send_string(intent_string)
    
    reply = socket.recv_string()
    print(f"[+] MANIFOLD YIELD: {reply}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        transmit_intent(" ".join(sys.argv[1:]))
    else:
        print("[!] ERROR: INTENT REQUIRED. Usage: python3 vspr_invoke.py <prompt>")
