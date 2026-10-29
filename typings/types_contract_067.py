from typing import TypedDict, Optional, Dict, Any

class ComponentContract067(TypedDict):
    id: int
    name: str
    enabled: bool
    metadata: Dict[str, Any]
    fallback_level: Optional[int]
