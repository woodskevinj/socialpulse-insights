# 📊 SocialPulse Insights

**SocialPulse Insights** is an offline social-sentiment analytics project that simulates a real-world **social listening / brand monitoring** tool using public benchmark datasets.

The goal is to analyze social-media-style text (e.g., tweets) and estimate sentiment around **public figures** and **topics** — without scraping live platforms or tracking private individuals.

---

## 🎯 Project Goals

- Build an end-to-end **sentiment analytics pipeline** on social-media-like text.
- Track sentiment for:
  - **Public figures** (e.g., well-known CEOs, artists, athletes)
  - **Topics / ideas** (e.g., “electric vehicles”, “bitcoin”, “student loans”)
- Compare different sentiment engines:
  - Rule-based (VADER)
  - Transformer-based models (Hugging Face)
- Provide aggregate analytics that feel like a lightweight **social listening dashboard**:
  - Sentiment distribution (positive / neutral / negative)
  - Trends over time (if timestamps are available)
  - Example posts per sentiment & entity

All analysis is performed on **offline, public datasets** for learning and portfolio purposes.

---

## 🧩 High-Level Architecture

Planned modules (under `src/`):

- `config.py`  
  Global configuration (paths, model names, tracked entities).

- `data_loader.py`  
  Load raw datasets (e.g., Sentiment140) and normalize column names (`text`, `label`, timestamps, etc.).

- `preprocessing.py`  
  Text cleaning and normalization:

  - Lowercasing
  - URL / mention / hashtag handling
  - Emoji/character normalization

- `entity_tagger.py`  
  Tag each post with one or more **entities**:

  - Public figures (people)
  - Topics / ideas
    using an alias-based matching system.

- `sentiment_models.py`  
  Interfaces for:

  - VADER-based sentiment
  - Transformer-based sentiment via Hugging Face

- `analytics.py`  
  Aggregate sentiment by entity/topic:

  - Sentiment distribution
  - Trends over time
  - Top positive / negative example posts

- `api.py` _(later phase)_  
  Optional FastAPI layer for querying sentiment analytics programmatically.

---

## 🛠 Tech Stack

Core tools and libraries:

- **Python 3.10+**
- **Pandas**, **NumPy** – data handling
- **VADER Sentiment** – rule-based baseline
- **Hugging Face Transformers** – deep-learning sentiment models
- **spaCy** – optional NLP preprocessing (tokenization, etc.)
- **Scikit-learn** – evaluation, utilities
- **FastAPI** + **Uvicorn** _(planned)_ – simple API layer
- **PyTest** – unit testing for core modules

---

## 📚 Dataset

Initial focus:

- **Sentiment140**  
  A large Twitter sentiment dataset with labeled positive and negative tweets.

You’ll place the raw dataset under:

```bash
data/
  raw/
    sentiment140.csv              # or similar filename
  processed/
    tweets_with_entities.parquet  # (created during preprocessing)
```

🔐 Note: This project does not scrape live social media. It uses offline public datasets to simulate social listening behavior.

---

## 🚀 Getting Started

1. Clone the repository

```bash
git clone https://github.com/<your-username>/socialpulse-insights.git
cd socialpulse-insights
```

2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
# .\venv\Scripts\activate     # Windows
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Download and place the dataset

- Download the **Sentiment140** dataset (or another Twitter-style sentiment dataset).

- Save it to:

```bash
data/raw/sentiment140.csv
```

5. Run initial exploration (planned)

Open the first notebook:

```bash
jupyter lab
```

```bash
notebooks/01_eda_and_entity_tagging.ipynb
```

This notebook will:

- Load the raw dataset

- Run basic EDA

- Apply initial entity tagging for public figures/topics

- Perform a first pass of VADER-based sentiment

---

## 🧠 Tracked Entities (Public Figures & Topics)

The project uses a configuration-based approach for entities to monitor, e.g.:

- Public figures (e.g., `sean carter`, `beyonecé knowles-carter`)

- Topics / ideas (e.g., `bitcoin`, `electric vehicles`)

You’ll find the stub configuration in src/config_entities.py (see below for initial example).

---

## ✅ Testing

Unit tests will live under `tests/`:

- tests/test_preprocessing.py

- tests/test_entity_tagger.py

- tests/test_sentiment_models.py

Run tests with:

```bash
pytest
```

---

## 🔍 Roadmap (Planned Phases)

1. Phase 1 – Data & Baseline

- Load dataset

- Clean text

- Implement VADER sentiment

- Basic EDA & entity tagging

2. Phase 2 – Transformers & Analytics

- Add Hugging Face sentiment model

- Compare models on labeled data

- Build analytics helpers for entities & topics

3. Phase 3 – API & Dashboard (Optional)

- FastAPI endpoints (e.g., `/entities/{name}/sentiment`)

- Lightweight dashboard to visualize trends and distributions

---

## ⚖️ Ethical Use

SocialPulse Insights is an **educational and portfolio project**:

- Uses **offline public datasets** only.

- Focuses on **aggregated sentiment** around public figures and topics.

- Not intended for:

  - Tracking private individuals

  - Harassment, targeting, or doxxing of any kind

If extended to live data in the future, it must comply with all relevant platform **Terms of Service**, privacy requirements, and ethical guidelines.

---

## 👨‍💻 Author

### Kevin Woods

Applied ML Engineer

AWS Certified AI Practitioner

AWS Machine Learning Certified Engineer – Associate

- 🔗 [GitHub: woodskevinj](https://github.com/woodskevinj)
