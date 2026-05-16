import re
from typing import List, Optional
from .model import BraidBlock, BraidDocument

TOKEN_SPEC = [
    ("BLOCK_HEADER", r"\[(?P<block_type>[A-Z_]+)\s*:\s*(?P<block_name>[A-Z0-9_]+)\]"),
    ("ASSIGN",       r"::="),
    ("IDENT",        r"[A-Za-z0-9_\.\-]+"),
    ("NUMBER",       r"[+-]?\d+(\.\d+)?([eE][+-]?\d+)?"),
    ("HASH",         r"#.*"),
    ("NEWLINE",      r"\n"),
    ("SKIP",         r"[ \t\r]+"),
]

MASTER_REGEX = "|".join(f"(?P<{name}>{pattern})" for name, pattern in TOKEN_SPEC)
TOKEN_RE = re.compile(MASTER_REGEX)

class Token:
    def __init__(self, type_: str, value: str):
        self.type = type_
        self.value = value

def tokenize(text: str) -> List[Token]:
    tokens = []
    for match in TOKEN_RE.finditer(text):
        kind = match.lastgroup
        value = match.group(0)
        if kind in ("SKIP", "HASH", "NEWLINE"):
            continue
        tokens.append(Token(kind, value.strip()))
    return tokens

class BraidParser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.pos = 0

    def current(self) -> Optional[Token]:
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def accept(self, *types: str) -> Optional[Token]:
        tok = self.current()
        if tok and tok.type in types:
            self.pos += 1
            return tok
        return None

    def expect(self, *types: str) -> Token:
        tok = self.current()
        if not tok or tok.type not in types:
            raise SyntaxError(f"Expected {types}, got {tok.type if tok else 'EOF'}")
        self.pos += 1
        return tok

    def parse(self) -> BraidDocument:
        doc = BraidDocument()
        while self.current():
            tok = self.current()
            if tok.type == "BLOCK_HEADER":
                block = self.parse_block()
                key = f"{block.block_type}:{block.block_name}"
                doc.blocks[key] = block
            elif tok.type == "IDENT":
                k, v = self.parse_assignment()
                doc.keys[k] = v
            else:
                self.pos += 1
        return doc

    def parse_block(self) -> BraidBlock:
        header = self.expect("BLOCK_HEADER")
        block_type, block_name = header.value.strip("[]").split(":")
        block = BraidBlock(block_type.strip(), block_name.strip())

        while self.current() and self.current().type != "BLOCK_HEADER":
            if self.current().type == "IDENT":
                k, v = self.parse_assignment()
                if "(" in v or "." in v:
                    block.operators[k] = v
                else:
                    block.keys[k] = v
            else:
                self.pos += 1

        return block

    def parse_assignment(self):
        ident = self.expect("IDENT")
        self.expect("ASSIGN")
        value = self.parse_value()
        return ident.value, value

    def parse_value(self) -> str:
        tok = self.current()
        if not tok:
            return ""
        self.pos += 1
        return tok.value

def parse_braid(text: str) -> BraidDocument:
    return BraidParser(tokenize(text)).parse()