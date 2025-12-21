import pandas as pd

from src.entity_tagger import tag_entities, find_entities_in_text
from src.config import ENTITIES

def test_find_entities_in_text_matches_aliases():
    text = "I think bitcoin and btc are the future.  Also, I like @beyonce and @sc."
    matches = find_entities_in_text(text, ENTITIES)

    names = {m["name"] for m in matches}
    assert "bitcoin" in names or any("bitcoin" in n for n in names)
    assert "sean carter" in names

    def test_tag_entities_adds_columns_and_primary_entity():
        df = pd.DataFrame(
            {
                "text_clean": [
                    "Beyonce is changing the game",
                    "I love bitcoin and btc!",
                    "Just a random tweet",
                ]
            }
        )

        tagged = tag_entities(df, text_col="text_clean", entities=ENTITIES)

        # Ensure new columns exist
        assert "entities" in tagged.columns
        assert "primary_entity_name" in tagged.columns
        assert "primary_entity_type" in tagged.columns

        # Row 0 should match some "beyonce" alias
        assert tagged.loc[0, "primary_entity_name"] == "beyonce"
        assert tagged.loc[0, "primary_entity_type"] == "person"

        # Row 1 should be the bitcoin topic
        assert tagged.loc[1, "primary_entity_name"] == "bitcoin"
        assert tagged.loc[1, "primary_entity_type"] == "topic"

        # Row 2 should have no entities
        assert tagged.loc[2, "entities"] == []
        assert tagged.loc[1, "primary_entity_name"] is None
        assert tagged.loc[1, "primary_entity_type"] is None


def test_short_alias_does_not_match_inside_words():
    entities = [
        {"name": "electrice vehicles", "type": "topic", "aliases": ["ev"]}
    ]

    # 'ev' should NOT match inside 'believe'
    text = "i believe this will work"
    matches = find_entities_in_text(text, entities)
    assert matches == []