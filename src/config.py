# This will centralize paths, model names, etc., and import your TRACKED_ENTITIES.

from pathlib import Path

from .config_entities import TRACKED_ENTITIES

# Project root (assumes this file lives in src/)
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Data paths
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# Specific dataset paths
SENTIMENT140_PATH = RAW_DATA_DIR / "sentiment140.csv"

# Processed artifacts
CLEANED_TWEETS_PATH = PROCESSED_DATA_DIR / "sentiment140_cleaned.parquet"
TWEETS_WITH_ENTITIES_PATH = PROCESSED_DATA_DIR / "tweets_with_entities.parquet"

# Hugging Face model names (can be tweaked later)
HF_SENTIMENT_MODEL = "distilbert-base-uncased-finetuned-sst-2-english"

# Tracked entities (public figures + topics)
ENTITIES = TRACKED_ENTITIES
