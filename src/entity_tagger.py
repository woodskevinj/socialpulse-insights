# this will scan text_clean for aliases and tag each row with an entity.

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
    
    text_lower = text.lower()
    matches = []

    for entity in entities:
        aliases = entity.get("aliases", [])
        for alias in aliases:
            if alias in text_lower:
                matches.append({"name": entity["name"], "type": entity["type"]})
                break # avoid duplicate matches for the same entity

    return matches


def tag_entities(
        df: pd.DataFrame,
        text_col: str = "text_clean",
        entities: Optional[List[Dict[str, Any]]] = None,
) -> pd.DataFrame:
    """
    Tag each row with matched entities based on aliases.
    
    Adds:
    - entities (list of {name, type})
    - primary_entity_name (str or None)
    - primary_entity_type (str or None)
    """

    df = df.copy()
    entities = entities or ENTITIES
    
    matches = df[text_col].apply(lambda t: find_entities_in_text(t, entities))
    df["entities"] = matches
    
    # Choose first matched entity as "primary" (simple heuristic)
    df["primary_entity_name"] = df["entities"].apply(
        lambda ms: ms[0]["name"] if ms else None
    )
    df["primary_entity_type"] = df["entities"].apply(
        lambda ms: ms[0]["type"] if ms else None
    )

    return df

