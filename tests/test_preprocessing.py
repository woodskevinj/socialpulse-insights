import pandas as pd

from src.preprocessing import clean_text, apply_cleaning

def test_clean_text_basic_normalization():
    raw = "Check this OUT!!!"
    cleaned = clean_text(raw)
    assert cleaned == "check this out!!!"


def test_clean_text_removes_urls_mentions_and_strips_hashtags():
    raw = "Hey @user, check https://example.com #AwesomeDay"
    cleaned = clean_text(raw)
    
    # @user and URL removed, hashtag symbol stripped, text lowercased

    assert "@" not in cleaned
    assert "http" not in cleaned
    assert "awesome" in cleaned
    assert "#awesome" not in cleaned
    assert cleaned == "hey , check awesomeday" or "awesome day" in cleaned


def test_apply_cleaning_adds_text_clean_column():
    df = pd.DataFrame({"text": ["Hello WORLD", "Another @user"]})
    df_clean = apply_cleaning(df, text_col="text")

    assert "text_clean" in df_clean.columns
    assert df_clean.loc[0, "text_clean"] == "hello world"
    assert "@" not in df_clean.loc[1, "text_clean"]