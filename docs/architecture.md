# Architecture

## Goal

The goal is to demonstrate a Zero Trust Network Access flow where a client cannot directly access an internal service. Every request must pass through a gateway that verifies identity, device trust, and authorization policy.

## Logical Architecture

```text
Client
  |
  | POST /access
  v
ZTNA Gateway
  |
  | GET /resource with trusted forwarding header
  v
Protected Service
```

## Trust Boundaries

1. Client zone: untrusted by default.
2. Gateway zone: policy enforcement point.
3. Service zone: protected internal resource.

## Default Security Principle

The gateway follows a default-deny model. Access is granted only when all checks pass:

- Known user
- Trusted device
- Allowed service
- Required role present
