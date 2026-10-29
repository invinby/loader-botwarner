from typing import TypedDict, Optional, Dict, Any

class ComponentContract076(TypedDict):
    id: int
    name: str
    enabled: bool
    metadata: Dict[str, Any]
    fallback_level: Optional[int]
