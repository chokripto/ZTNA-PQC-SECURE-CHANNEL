# ZTNA-PQC-SECURE-CHANNEL

This project implements a Zero Trust Network Access prototype using post-quantum cryptography.

The client is never trusted by default. Every access request must pass through identity verification, device validation, policy evaluation, and a post-quantum secure channel establishment.

## Core Concepts

- Zero Trust Network Access
- Post-Quantum Cryptography
- Kyber-based key establishment
- AES-GCM secure channel
- Identity-based access control
- Policy-based authorization
- Dockerized deployment

## Security Goals

- Never trust, always verify
- Protect internal services from direct exposure
- Establish quantum-resistant secure communication
- Enforce access policies before granting service access
- Log access decisions

## Technologies

- Python
- liboqs
- Kyber512
- AES-GCM
- HKDF
- Docker
- Docker Compose
- 
