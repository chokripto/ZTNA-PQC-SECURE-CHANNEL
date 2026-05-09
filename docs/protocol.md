# Protocol

## Phase 1 Flow

```text
1. Client sends access request to gateway.
2. Gateway extracts user_id, device_id, and requested_service.
3. Gateway evaluates JSON policy.
4. If DENY, gateway returns HTTP 403.
5. If ALLOW, gateway forwards the request to the protected service.
6. Protected service responds only through the gateway path.
```

## Future Phase 2 PQC Secure Channel

Planned handshake:

```text
1. Client -> Gateway: client hello, supported KEMs, X25519 public key
2. Gateway -> Client: ML-KEM public key, X25519 public key, gateway nonce
3. Client: ML-KEM encapsulation + X25519 shared secret
4. Client -> Gateway: ML-KEM ciphertext, client nonce
5. Both sides derive session key using HKDF-SHA256
6. Application data uses AES-GCM with replay-safe nonces
```

## Key Schedule

```text
shared_secret = ML-KEM_secret || X25519_secret
session_key = HKDF-SHA256(shared_secret, transcript_hash, context)
```
