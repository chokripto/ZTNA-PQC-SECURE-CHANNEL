# Zero Trust Secure Channel using Post-Quantum Cryptography (PQC)

## Overview

This project implements a prototype of a **Zero Trust Network Access (ZTNA)** architecture secured with **Post-Quantum Cryptography (PQC)**.

The system follows the principle:

> **Never Trust, Always Verify**

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

---

# Objectives

The main objectives of this project are:

- Design a secure Zero Trust communication architecture
- Protect internal services from direct exposure
- Implement post-quantum secure key exchange using Kyber
- Establish encrypted communication channels using AES-GCM
- Enforce access policies before granting access
- Demonstrate secure client-to-service communication
- Simulate enterprise-grade ZTNA concepts

---

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
