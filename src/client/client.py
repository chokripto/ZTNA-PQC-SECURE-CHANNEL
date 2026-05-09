import os
import time
import requests

from src.common.messages import AccessRequest

GATEWAY_URL = os.getenv("GATEWAY_URL", "http://gateway:8000")
USER_ID = os.getenv("USER_ID", "chokri")
DEVICE_ID = os.getenv("DEVICE_ID", "trusted-laptop")
REQUESTED_SERVICE = os.getenv("REQUESTED_SERVICE", "internal-api")


def wait_for_gateway() -> None:
    for _ in range(20):
        try:
            response = requests.get(f"{GATEWAY_URL}/health", timeout=2)
            if response.status_code == 200:
                return
        except requests.RequestException:
            time.sleep(1)
    raise RuntimeError("Gateway is not reachable")


def main() -> None:
    wait_for_gateway()
    access_request = AccessRequest(
        user_id=USER_ID,
        device_id=DEVICE_ID,
        requested_service=REQUESTED_SERVICE,
    )

    print("[CLIENT] Sending access request", flush=True)
    response = requests.post(f"{GATEWAY_URL}/access", json=access_request.to_dict(), timeout=10)
    print(f"[CLIENT] Gateway status: {response.status_code}", flush=True)
    print(f"[CLIENT] Response: {response.json()}", flush=True)


if __name__ == "__main__":
    main()
