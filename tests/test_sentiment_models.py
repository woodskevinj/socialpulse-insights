from src.sentiment_models import VaderSentimentModel, TransformersSentimentModel


def test_vader_sentiment_model_basic():
    model = VaderSentimentModel()

    texts = [
        "I absolutely love this!",   # clearly positive
        "I really hate this thing.", # clearly negative
    ]
    results = model.predict(texts)

    assert len(results) == 2
    for res in results:
        assert res["label"] in {"positive", "negative", "neutral"}
        assert isinstance(res["score"], float)


def test_transformers_sentiment_model_basic():
    """
    Smoke test: ensure the HF model runs and returns labels & scores.

    This may be a bit slower on first run (model download),
    but should be fine for normal local development
    """
    model = TransformersSentimentModel()

    texts = [
        "This product is amazing!",
        "This is the worst experience I've ever had.",
    ]
    results = model.predict(texts)

    assert len(results) == 2
    for res in results:
        assert res["label"] in {"positive", "negative", "neutral", "pos", "neg"}
        assert 0.0 <= res["score"] <= 1.0