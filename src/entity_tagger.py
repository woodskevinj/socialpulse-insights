# this will scan text_clean for aliases and tag each row with an entity.

import re
from typing import List, Dict, Any, Optional, Tuple
import pandas as pd

from .config import ENTITIES


def compile_entity_patterns(entities: List[Dict[str, Any]]) -> List[Tuple[Dict[str, str], List[re.Pattern]]]:
    """
    Precompile regex patterns for each entity's aliases so we don't recompile per row.
    Returns a list of (entity_meta, patterns).
    """
    compiled = []
    for e in entities:
        patterns = []
        for alias in e.get("aliases", []):
            alias = alias.strip().lower()
            if not alias:
                continue
            patterns.append(re.compile(rf"\b{re.escape(alias)}\b"))
        compiled.append(({"name": e["name"], "type": e["type"]}, patterns))
    return compiled


def _alias_pattern(alias: str) -> re.Pattern:
    """
    Build a safe regex pattern for alias matching.

    Uses word boundaries to avoid substring false positives.
    Example:  'ev' should not match 'believe'.
    """
    alias = alias.strip().lower()
    escaped = re.escape(alias)

    # Word boundary match for most aliases
    # This is important for short aliases like 'ev', 'btc'
    return re.compile(rf"\b{escaped}\b")

def find_entities_in_text_compiled(text: str, compiled_entities) -> List[Dict[str, str]]:

    if not isinstance(text, str) or not text:
        return []
    
    matches = []
    text_lower = text.lower()
    

    # for entity in entities:
    #     aliases = entity.get("aliases", [])
    #     for alias in aliases:
    #         pattern = _alias_pattern(alias)
    #         if pattern.search(text_lower):
    #             matches.append({"name": entity["name"], "type": entity["type"]})
    #             break # avoid duplicate matches for the same entity

    for meta, patterns in compiled_entities:
        for pat in patterns:
            if pat.search(text_lower):
                matches.append(meta)
                break

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

    compiled = compile_entity_patterns(entities)
    
    # matches = df[text_col].apply(lambda t: find_entities_in_text(t, entities))
    df["entities"] = df[text_col].apply(lambda t: find_entities_in_text_compiled(t, compiled))

    # Choose first matched entity as "primary" (simple heuristic)
    df["primary_entity_name"] = df["entities"].apply(
        lambda ms: ms[0]["name"] if ms else None
    )
    df["primary_entity_type"] = df["entities"].apply(
        lambda ms: ms[0]["type"] if ms else None
    )

    return df

