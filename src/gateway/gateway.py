import os
import requests
from flask import Flask, jsonify, request

from src.common.policy import PolicyEngine

app = Flask(__name__)

POLICY_PATH = os.getenv("POLICY_PATH", "policies/access_policy.json")
PROTECTED_SERVICE_URL = os.getenv("PROTECTED_SERVICE_URL", "http://service:7000")
policy_engine = PolicyEngine(POLICY_PATH)


@app.get("/health")
def health():
    return jsonify({"status": "ok", "component": "ztna-gateway"})


@app.post("/access")
def access():
    payload = request.get_json(force=True)
    user_id = payload.get("user_id")
    device_id = payload.get("device_id")
    requested_service = payload.get("requested_service")

    print("[GATEWAY] Access request received", flush=True)
    print(f"[GATEWAY] user={user_id} device={device_id} service={requested_service}", flush=True)

    allowed, reason = policy_engine.evaluate(user_id, device_id, requested_service)
    decision = "ALLOW" if allowed else "DENY"
    print(f"[GATEWAY] Policy decision: {decision} reason={reason}", flush=True)

    if not allowed:
        return jsonify({"decision": decision, "reason": reason}), 403

    upstream_path = policy_engine.upstream_path_for(requested_service)
    upstream_url = f"{PROTECTED_SERVICE_URL}{upstream_path}"
    response = requests.get(upstream_url, headers={"X-ZTNA-User": user_id}, timeout=5)

    return jsonify({
        "decision": decision,
        "reason": reason,
        "upstream_status": response.status_code,
        "upstream_response": response.json()
    }), response.status_code


if __name__ == "__main__":
    print("[GATEWAY] Starting ZTNA gateway on port 8000", flush=True)
    app.run(host="0.0.0.0", port=8000)
