# Threat Model

## Assets

- Protected internal service
- Access policies
- User and device identity attributes
- Future session keys
- Gateway audit logs

## Adversary Capabilities

- Attempts to access the protected service directly
- Uses unknown or stolen device identifiers
- Attempts service enumeration
- Attempts replay of access requests
- Attempts man-in-the-middle interception

## Current Mitigations

- Gateway-mediated access
- Default-deny policy enforcement
- User/device/service authorization checks
- Docker network isolation between components

## Planned Mitigations

- ML-KEM/Kyber + X25519 hybrid key establishment
- HKDF-SHA256 session key derivation
- AES-GCM authenticated encryption
- Replay protection with nonces and timestamps
- Signed identity assertions
- Device posture scoring
