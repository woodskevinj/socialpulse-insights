"""
Sentiment modeling utilities for SocialPulse Insights

This module provides:
- A VADER-based sentiment analyzer (baseline)
- A Hugging Face transformer-based sentiment classifier

Both are wrapped with simple interfaces so the rest of the 
pipeline can call `predict_sentiment(text)` uniformly.
"""

from typing import List, Dict, Union
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from transformers import pipeline
from .config import HF_SENTIMENT_MODEL

class VaderSentimentModel:
    """
    Wrapper around VADER sentiment analyzer.
    """

    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def predict(self, texts: Union[str, List[str]]) -> List[Dict]:
        """
        Predict sentiment for a single text or list of texts.
        Output format:
            
        [
            {"label": "positive", "score": 0.92},
            ...
        ]
        """
        if isinstance(texts, str):
            texts = [texts]

        results = []
        for t in texts:
            scores = self.analyzer.polarity_scores(t)
            compound = scores["compound"]

            if compound >= 0.05:
                label = "positive"
            elif compound <= -0.05:
                label = "negative"
            else:
                label = "neutral"

            results.append({"label": label, "score": compound})

        return results


class TransformersSentimentModel:
    """
    Hugging Face transformer sentiment model.
    Defaults to DistilBERT fine-tuned on SST-2.
    """

    def __init__(self, model_name: str = HF_SENTIMENT_MODEL):
        # Pipeline handles tokenization + inference
        self.model = pipeline("sentiment-analysis", model=model_name)

    def predict(self, texts: Union[str, List[str]]) -> List[Dict]:
        if isinstance(texts, str):
            texts = [texts]

        results = self.model(texts)

        # Normalized output structure
        normalized = []
        for r in results:
            label = r["label"].lower() # e.g., POSITIVE -> positive
            score = float(r["score"])
            normalized.append({"label": label, "score": score})

        return normalized
    
