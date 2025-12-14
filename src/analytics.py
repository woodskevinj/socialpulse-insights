"""
Analyitics utilities for SocialPulse Insights
Designed to work on any DF that includes:
- text_clean
- label (optional)
- primary_entity_name

These functions compute:
- Sentiment distribution
- Average Sentiment Score
- Entity-level analytics
- Example posts (top positive/negative)
"""

from typing import Optional, Dict
import pandas as pd


def sentiment_distribution(df: pd.DataFrame, label_col: str = "label") -> Dict[str, int]:
    """
    Returns a simple count of each sentiment label.
    """

    return df[label_col].value_counts().to_dict()


def filter_by_entity(df: pd.DataFrame, entity_name: Optional[str]) -> pd.DataFrame:
    """
    Return only rows associated with a given primary entity.
    """
    
    if entity_name is None:
        return df
    return df[df["primary_entity_name"] == entity_name].copy()


def top_examples(
    df: pd.DataFrame,
    sentiment_label: str,
    text_col: str = "text_clean",
    n: int = 5,
) -> pd.DataFrame:
    """
    REturn top example posts for a given label.
    """

    subset = df[df["label"] == sentiment_label]
    return subset.head(n)


def entity_sentiment_summary(
    df: pd.DataFrame,
    entity_name: Optional[str] = None,
    label_col: str = "label",
) -> Dict:
    """
    Produce a compact summary of sentiment distribution
    for a single entity
    """

    entity_df = filter_by_entity(df, entity_name)
    distribution = sentiment_distribution(entity_df, label_col)

    return {
        "entity": entity_name,
        "count": len(entity_df),
        "distribution": distribution,
    }