# Zero Trust Secure Channel using Post-Quantum Cryptography (PQC)

## Overview

This project implements a prototype of a Zero Trust Network Access (ZTNA) architecture secured with Post-Quantum Cryptography (PQC).

The system follows the principle:

"Never Trust, Always Verify"

Every client request must pass through:
- Identity verification
- Device validation
- Policy-based authorization
- Post-quantum secure session establishment

The project combines:
- Zero Trust principles
- Network Security
- Identity-aware access control
- Post-Quantum Cryptography
- Secure communication architecture

--------------------------------------------------

# Objectives

The main objectives of this project are:

- Design a secure Zero Trust communication architecture
- Protect internal services from direct exposure
- Implement post-quantum secure key exchange using Kyber
- Establish encrypted communication channels using AES-GCM
- Enforce access policies before granting access
- Demonstrate secure client-to-service communication
- Simulate enterprise-grade ZTNA concepts

--------------------------------------------------

# Architecture

```text
+------------------+
|      Client      |
| Identity + Token |
+---------+--------+
          |
          | Access Request
          v
+--------------------------+
|      ZTNA Gateway        |
|--------------------------|
| Identity Verification    |
| Device Validation        |
| Policy Engine            |
| PQC Handshake (Kyber)    |
| AES-GCM Secure Channel   |
+-------------+------------+
              |
              | Authorized Request
              v
+--------------------------+
|   Protected Service      |
+--------------------------+

```
--------------------------------------------------

# Core Security Features

## Zero Trust Access Control
- No implicit trust
- Every request is verified
- Policy-based authorization

## Post-Quantum Cryptography
- Kyber512 key encapsulation mechanism
- Hybrid-ready secure architecture
- Protection against future quantum attacks

## Secure Communication
- AES-GCM authenticated encryption
- HKDF session key derivation
- Replay protection using counters/nonces

## Identity & Device Validation
- User identity claims
- Device identification
- Access policy enforcement

--------------------------------------------------

# Technologies Used

- Python 3
- liboqs
- Kyber512
- AES-GCM
- HKDF
- Docker
- Docker Compose

--------------------------------------------------

# Project Structure

```text
ztna-pqc-secure-channel/
├── README.md
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .gitignore
├── docs/
│   ├── architecture.md
│   ├── protocol.md
│   └── threat_model.md
├── policies/
│   └── access_policy.json
└── src/
    ├── common/
    │   ├── __init__.py
    │   ├── crypto.py
    │   ├── hkdf.py
    │   └── message.py
    ├── client/
    │   ├── __init__.py
    │   └── client_app.py
    ├── gateway/
    │   ├── __init__.py
    │   ├── gateway_app.py
    │   └── policy_engine.py
    └── service/
        ├── __init__.py
        └── protected_service.py
```
--------------------------------------------------

# Threat Model

The project considers the following threats:

- Passive network interception
- Man-in-the-middle (MITM) attacks
- Unauthorized access attempts
- Replay attacks
- Future quantum adversaries
- Unauthorized lateral movement

--------------------------------------------------

# Security Goals

- Confidentiality
- Integrity
- Authentication
- Access control enforcement
- Quantum-resistant secure communication
- Secure session establishment

--------------------------------------------------

# How to Run

## Build and Start

docker-compose up --build

--------------------------------------------------

# Expected Output
```text
[gateway] ZTNA Gateway listening
[service] Protected service listening
[client] Sending identity claims
[gateway] Identity verified
[gateway] Policy decision: ALLOW
[gateway] PQC session established
[client] Secure request sent
[service] Protected resource accessed
```
--------------------------------------------------

# Future Improvements

- Mutual authentication
- JWT/OAuth2 integration
- Role-based access control (RBAC)
- Multi-factor authentication (MFA)
- SIEM integration
- Logging and auditing
- Hybrid PQC + TLS support
- Cloud deployment
- Kubernetes integration

--------------------------------------------------

# Potential Use Cases

- Zero Trust enterprise environments
- Secure IoT infrastructures
- Remote workforce protection
- Secure internal APIs
- Post-quantum secure networking
- Identity-aware secure access

--------------------------------------------------

# Educational Value

This project demonstrates practical knowledge in:

- Zero Trust Network Access (ZTNA)
- Network Security Architecture
- Post-Quantum Cryptography
- Secure Communication Protocols
- Dockerized Security Deployments
- Threat Modeling
- Applied Cryptography

--------------------------------------------------

# Author

Chokri Nouar, PhD

Cybersecurity Engineer | Cryptography Researcher | PQC & Network Security Enthusiast

GitHub:
https://github.com/chokripto

--------------------------------------------------

# License

MIT License
