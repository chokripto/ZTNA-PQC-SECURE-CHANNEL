from flask import Flask, jsonify, request

app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify({"status": "ok", "component": "protected-service"})


@app.get("/resource")
def resource():
    forwarded_user = request.headers.get("X-ZTNA-User", "unknown")
    print(f"[SERVICE] Protected resource accessed by user={forwarded_user}", flush=True)
    return jsonify({
        "service": "internal-api",
        "message": "Protected resource accessed through ZTNA gateway",
        "user": forwarded_user
    })


if __name__ == "__main__":
    print("[SERVICE] Starting protected service on port 7000", flush=True)
    app.run(host="0.0.0.0", port=7000)
