from dataclasses import dataclass, asdict
from typing import Any, Dict


@dataclass(frozen=True)
class AccessRequest:
    user_id: str
    device_id: str
    requested_service: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
