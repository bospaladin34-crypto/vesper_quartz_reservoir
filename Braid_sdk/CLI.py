import argparse
from pathlib import Path
from .parser import parse_braid
from .compiler import build_santos_lagrangian

def main():
    ap = argparse.ArgumentParser(prog="braid", description="Braid Syntax tools")
    ap.add_argument("file", help=".sys / .braid file")
    args = ap.parse_args()

    text = Path(args.file).read_text(encoding="utf-8")
    doc = parse_braid(text)
    L = build_santos_lagrangian(doc)

    print("Santos Lagrangian:")
    print("  L0       :", L.L0)
    print("  DIV      :", L.divergence)
    print("  RENORM   :", L.renorm)
    print("  FGR      :", L.fgr)
    print("  CHANDRA  :", L.chandra)

if __name__ == "__main__":
    main()