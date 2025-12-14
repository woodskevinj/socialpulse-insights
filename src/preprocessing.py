import re
from typing import Iterable
import pandas as pd

URL_PATTERN = re.compile(r"http\S+|www\.\S+")
MENTION_PATTERN = re.compile(r"@\w+")
HASHTAG_SYMBOL_PATTERN = re.compile(r"#")


def clean_text(text: str) -> str:
    """
    Basic text cleaning for social-media-style text.
    
    - Lowercase
    - Remove URLS
    - Remove @mentions
    - Strip hashtag symbol (keep the word)
    - Collapse extra whitespace
    """

    if not isinstance(text, str):
        return ""
    
    text = text.lower()
    text = URL_PATTERN.sub(" ", text)
    text = MENTION_PATTERN.sub(" ", text)

    # Keep hastag words but remove "#"
    text = HASHTAG_SYMBOL_PATTERN.sub("", text)

    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text).strip()

    return text


def apply_cleaning(df: pd.DataFrame, text_col: str = "text") -> pd.DataFrame:
    """
    Apply `clean_text` to the specified text column and create a new column
    """

    df = df.copy()
    df["text_clean"] = df[text_col].apply(clean_text)
    return df

