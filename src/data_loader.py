from typing import Optional
import pandas as pd
from .config import SENTIMENT140_PATH

def load_sentiment140(path: Optional[str] = None) -> pd.DataFrame:
    """
    Load the Sentiment140 dataset and return a DataFram with normalized columns.

    Expected raw columns (canonical Sentiment140):
    0 - target (0 = negative, 4 = positive)
    1 - ids
    2 - date
    3 - flag
    4 - user
    5 - text
    """
    csv_path = path or SENTIMENT140_PATH

    df = pd.read_csv(
        csv_path,
        encoding="latin-1",
        header=None,
        names=["target", "ids", "date", "flag", "user", "text"],
    )

    # Map labels to [-1, 1] or "negative"/"positive"
    label_map = {0: "negative", 4: "positive"}
    df["label"] = df["target"].map(label_map)

    # Normalize columns we care about
    df = df[["text", "label", "date", "user", "ids"]]

    return df
