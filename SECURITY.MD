# Security Policy

## System Nature

This project implements a **Deterministic Physics‑Driven Computational Framework**.  
It is **not** a cryptographic system and does **not** rely on keys, entropy, or randomness.

## Security Model

The system is:

- Deterministic and reversible  
- Geometry‑constrained  
- Parity‑preserving  
- Low‑entropy and laminar  

There are:

- no cryptographic keys  
- no encryption or decryption  
- no hashing or MACs  
- no random number generators  

## Reporting a Vulnerability

If you believe you have found a security issue related to:

- operational misuse  
- configuration errors  
- integration behavior  

please open a **private issue** or contact the maintainer via the repository’s preferred contact channel.

Issues related to:

- cryptographic weaknesses  
- key compromise  
- randomness failures  

are **not applicable**, as the system does not implement cryptographic functions.

## Scope

In‑scope:

- deterministic behavior  
- operator correctness  
- manifold configuration  
- thermodynamic and geometric consistency  

Out‑of‑scope:

- cryptographic analysis  
- entropy or randomness testing  
- key management