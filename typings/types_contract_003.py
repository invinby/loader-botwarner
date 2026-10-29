from typing import TypedDict, Optional, Dict, Any

class ComponentContract003(TypedDict):
    id: int
    name: str
    enabled: bool
    metadata: Dict[str, Any]
    fallback_level: Optional[int]
