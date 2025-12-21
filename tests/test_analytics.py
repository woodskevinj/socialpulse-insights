import pandas as pd

from src.analytics import (
    sentiment_distribution,
    filter_by_entity,
    top_examples,
    entity_sentiment_summary,
)

def _sample_df():
    return pd.DataFrame(
        {
            "text_clean": [
                "beyonce is great",
                "beyonce is terrible",
                "bitcoin to the moon",
                "bitcoin is a scam",
            ],
            "label": ["positive", "negative", "positive", "negative"],
            "primary_entity_name": ["beyonce", "beyonce", "bitcoin", "bitcoin"],
        }
    )


def test_sentiment_distribution():
    df = _sample_df()
    dist = sentiment_distribution(df, label_col="label")
    assert dist["positive"] == 2
    assert dist["negative"] == 2


def test_filter_by_entity():
    df = _sample_df()
    beyonce_df = filter_by_entity(df, "beyonce")
    bitcoin_df = filter_by_entity(df, "bitcoin")

    assert len(beyonce_df) == 2
    assert all(beyonce_df["primary_entity_name"] == "beyonce")

    assert len(bitcoin_df) == 2
    assert all(bitcoin_df["primary_entity_name"] == "bitcoin")


def test_top_examples_returns_subset():
    df = _sample_df()
    top_pos = top_examples(df, sentiment_label="positive", n=1)

    assert len(top_pos) == 1
    assert top_pos.iloc[0]["label"] == "positive"


def test_entity_sentiment_summary():
    df = _sample_df()
    summary = entity_sentiment_summary(df, entity_name="bitcoin", label_col="label")

    assert summary["entity"] == "bitcoin"
    assert summary["count"] == 2
    assert summary["distribution"]["positive"] == 1
    assert summary["distribution"]["negative"] == 1