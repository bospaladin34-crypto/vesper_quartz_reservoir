from typing import List, Dict

BLOCK_TYPES: List[str] = [
    "OPERATOR",
    "TENSOR",
    "INGEST",
    "MANIFOLD",
]

COMMON_KEYS: List[str] = [
    "PHASE_DELTA",
    "PARITY",
    "L0",
    "DIV_TERM",
    "RENORM_TERM",
    "FGR_TERM",
    "CH_TERM",
]

OPERATORS: List[str] = [
    "LAMINAR.KINETIC(dq/dt)",
    "TURBULENT.POTENTIAL(q)",
    "PULLBACK(Φ_renorm(q) -> NODE[0,0,0,0])",
    "DELTA(ρ_b(ω), 15.965Hz)",
    "STEP(M_semantic > M_Chandra)",
    "∇·F_thermo",
]

def get_completion_items() -> Dict[str, List[str]]:
    return {
        "blockTypes": BLOCK_TYPES,
        "keys": COMMON_KEYS,
        "operators": OPERATORS,
    }