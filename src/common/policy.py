import json
from pathlib import Path
from typing import Any, Dict, Tuple


class PolicyEngine:
    def __init__(self, policy_path: str):
        self.policy_path = Path(policy_path)
        self.policy = self._load_policy()

    def _load_policy(self) -> Dict[str, Any]:
        with self.policy_path.open("r", encoding="utf-8") as f:
            return json.load(f)

    def evaluate(self, user_id: str, device_id: str, requested_service: str) -> Tuple[bool, str]:
        user = self.policy.get("users", {}).get(user_id)
        if not user:
            return False, "unknown_user"

        if device_id not in user.get("allowed_devices", []):
            return False, "untrusted_device"

        if requested_service not in user.get("allowed_services", []):
            return False, "service_not_allowed"

        service = self.policy.get("services", {}).get(requested_service)
        if not service:
            return False, "unknown_service"

        required_role = service.get("required_role")
        if required_role and required_role not in user.get("roles", []):
            return False, "missing_required_role"

        return True, "policy_allow"

    def upstream_path_for(self, requested_service: str) -> str:
        return self.policy["services"][requested_service]["upstream_path"]
