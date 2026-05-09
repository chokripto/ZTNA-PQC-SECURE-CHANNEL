"""
Cryptographic utilities for the ZTNA secure channel.

Phase 1 keeps the project runnable and focuses on ZTNA flow, policy decisions,
and service isolation. Phase 2 should replace the demo key agreement with a real
hybrid PQC handshake using ML-KEM via liboqs-python + X25519.
"""

import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def generate_demo_session_key() -> bytes:
    """Generate a 256-bit symmetric key for the demo secure channel."""
    return AESGCM.generate_key(bit_length=256)


def encrypt_json_bytes(key: bytes, plaintext: bytes, aad: bytes = b"ztna-pqc-demo") -> dict:
    nonce = os.urandom(12)
    ciphertext = AESGCM(key).encrypt(nonce, plaintext, aad)
    return {
        "nonce": nonce.hex(),
        "ciphertext": ciphertext.hex(),
        "aad": aad.decode("utf-8")
    }


def decrypt_json_bytes(key: bytes, envelope: dict) -> bytes:
    nonce = bytes.fromhex(envelope["nonce"])
    ciphertext = bytes.fromhex(envelope["ciphertext"])
    aad = envelope.get("aad", "ztna-pqc-demo").encode("utf-8")
    return AESGCM(key).decrypt(nonce, ciphertext, aad)
