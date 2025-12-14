"""
Configuration for tracked public figures and topics.

Each entity has:
- name: canonical display name
- type: "person" or "topic"
- aliases: list of lowercase strings to match in text
"""

TRACKED_ENTITIES = [
    {
        "name": "sean carter",
        "type": "person",
        "aliases": ["jay z", "hov", "hova", "@sc"],
    },
    {
        "name": "beyonce knowles-carter",
        "type": "person",
        "aliases": ["beyonce", "sasha fierce", "@beyonce"],
    },
    {
        "name": "bitcoin",
        "type": "topic",
        "aliases": ["bitcoin", "btc", "#bitcoin"],
    },
    {
        "name": "electric vehicles",
        "type": "topic",
        "aliases": [
            "electric vehicle",
            "electric car",
            "evs",
            "ev",
            "electric vehicles",
        ],
    },
]