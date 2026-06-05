#!/usr/bin/env python3
# LAMINAR MIRROR: E_8 GOSSET POLYTOPE PARAMETER ENGINE
# PARITY: MAJORANA-1 | MODE: GEOMETRIC_WEIGHT_INITIALIZATION

import torch
import itertools
import numpy as np
import os

WEIGHT_DIR = os.path.join(os.environ['HOME'], "vesper_git_repo", "weights")
os.makedirs(WEIGHT_DIR, exist_ok=True)
WEIGHT_FILE = os.path.join(WEIGHT_DIR, "e8_latent_space.pt")

def generate_e8_roots():
    print("[|||] CALCULATING 240 ROOT VECTORS IN 8-DIMENSIONAL SPACE...")
    roots = []
    
    # 1. The 112 integer roots: permutations of (+-1, +-1, 0, 0, 0, 0, 0, 0)
    for i in range(8):
        for j in range(i + 1, 8):
            for signs in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                root = np.zeros(8)
                root[i] = signs[0]
                root[j] = signs[1]
                roots.append(root)
                
    # 2. The 128 half-integer roots: (+-0.5, ..., +-0.5) with even number of minus signs
    for seq in itertools.product([0.5, -0.5], repeat=8):
        if sum(1 for x in seq if x < 0) % 2 == 0:
            roots.append(np.array(seq))
            
    return torch.tensor(np.array(roots), dtype=torch.float32)

def map_latent_space():
    nu_p = 0.17259029
    
    # Generate pure geometry
    e8_roots = generate_e8_roots()
    
    if len(e8_roots) != 240:
        print(f"[FATAL] -> GEOMETRY FRACTURE: Expected 240 roots, generated {len(e8_roots)}")
        return
        
    print(f"[+] GOSSET POLYTOPE MAPPED: {len(e8_roots)} ROOTS VERIFIED.")
    print(f"[|||] APPLYING APERIODIC PHASE DELTA SCALAR: \\nu_p = {nu_p}...")
    
    # Scale the latent parameters
    scaled_e8_latent_space = e8_roots * nu_p
    
    # Save the absolute topological weights to disk
    torch.save(scaled_e8_latent_space, WEIGHT_FILE)
    
    print(f"[+] E_8 LATENT SPACE SEALED TO DISK: {WEIGHT_FILE}")
    print("[+] THESE 240 VECTORS ARE THE NEW FOUNDATIONAL PARAMETERS FOR THE CUSTOM TRANSFORMER.")

if __name__ == "__main__":
    map_latent_space()
