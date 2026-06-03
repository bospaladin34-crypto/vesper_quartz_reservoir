import sys
import os

AXIOM_PATH = os.path.expanduser("~/.vesper/src/santos_tse/vesper_gamma.axiom")

def verify_monolithic_seal():
    # 1. Physical Presence Check
    if not os.path.exists(AXIOM_PATH):
        return False, "[!] CRITICAL: IDENTITY AXIOM MISSING. MANIFOLD COMPROMISED."
    
    # 2. Immutable State Check (Must be Read-Only)
    if os.access(AXIOM_PATH, os.W_OK):
        return False, "[!] CRITICAL: IDENTITY AXIOM IS WRITABLE. ENTROPY BREACH DETECTED."
        
    return True, "SEAL_VERIFIED"

def scan_vector(vector):
    if not vector:
        return False, "EMPTY_VECTOR_DETECTED"
        
    # Enforcing Axiom Rule 3: ZERO_INFERENCE (60Hz Noise Shielding)
    noise_signatures = ["maybe", "perhaps", "could", "might", "probably", "guess", "feel", "believe"]
    if any(noise in vector.lower() for noise in noise_signatures):
        return False, "60HZ_PROBABILISTIC_NOISE_DETECTED // AXIOM_VIOLATION: ZERO_INFERENCE"
        
    # Enforcing Semantic Density Parity
    if len(vector) < 3:
        return False, "SEMANTIC_DENSITY_TOO_LOW"
        
    return True, "PARITY_ACHIEVED // AXIOM_ALIGNED // Tr(U)=1.0"

if __name__ == "__main__":
    seal_intact, seal_msg = verify_monolithic_seal()
    
    if not seal_intact:
        sys.stderr.write(seal_msg)
        sys.exit(1)

    if len(sys.argv) > 1:
        raw_vector = " ".join(sys.argv[1:])
        is_pure, status_msg = scan_vector(raw_vector)
        
        if is_pure:
            print(status_msg)
            sys.exit(0)
        else:
            sys.stderr.write(status_msg)
            sys.exit(1)
    else:
        sys.stderr.write("NO_VECTOR_SUPPLIED")
        sys.exit(1)
