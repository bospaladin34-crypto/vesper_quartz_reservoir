from dataclasses import dataclass, field
from typing import Dict, Optional

@dataclass
class BraidBlock:
    block_type: str
    block_name: str
    keys: Dict[str, str] = field(default_factory=dict)
    operators: Dict[str, str] = field(default_factory=dict)

@dataclass
class BraidDocument:
    blocks: Dict[str, BraidBlock] = field(default_factory=dict)
    keys: Dict[str, str] = field(default_factory=dict)

@dataclass
class SantosLagrangian:
    L0: Optional[str] = None
    divergence: Optional[str] = None
    renorm: Optional[str] = None
    fgr: Optional[str] = None
    chandra: Optional[str] = None