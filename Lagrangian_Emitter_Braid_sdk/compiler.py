from .model import BraidDocument, SantosLagrangian

def build_santos_lagrangian(doc: BraidDocument) -> SantosLagrangian:
    L = SantosLagrangian()
    for block in doc.blocks.values():
        for key, op in block.operators.items():
            ku = key.upper()
            if ku == "L0":
                L.L0 = op
            elif "DIV" in ku:
                L.divergence = op
            elif "RENORM" in ku:
                L.renorm = op
            elif "FGR" in ku:
                L.fgr = op
            elif "CH" in ku:
                L.chandra = op
    return L