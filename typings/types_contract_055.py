from typing import TypedDict, Optional, Dict, Any

class ComponentContract055(TypedDict):
    id: int
    name: str
    enabled: bool
    metadata: Dict[str, Any]
    fallback_level: Optional[int]
