from typing import List, Dict, Any, Optional
import pandas as pd
from .config import ENTITIES

def find_entities_in_text(text: str, entities: List[Dict[str, Any]]) -> List[Dict[str, str]]:
    """
    Return a list of matched entities for a given text.

    Each match is a dict wit:
    - name
    - type
    """

    if not isinstance(text, str) or not text:
        return []