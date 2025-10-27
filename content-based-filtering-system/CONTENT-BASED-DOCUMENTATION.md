# Content-Based Filtering Recommender System

Implementation of a content-based filtering system for Netflix titles using TF-IDF vectorization and cosine similarity.

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Ensure `netflix_titles.csv` is in the project root directory

## How It Works

The system recommends items similar to a seed title by:

1. **Feature Combination**: Combines textual features (description, listed_in) into unified content representation
2. **TF-IDF Vectorization**: Converts text into numerical feature vectors using Term Frequency-Inverse Document Frequency
3. **Cosine Similarity**: Computes similarity scores between all items (range: 0 to 1, where 1 = identical)
4. **Ranking**: Returns top N most similar items excluding the seed title

## Implementation Status

### ✅ Completed

- Data loading and preprocessing
- TF-IDF vectorizer setup
- Cosine similarity computation infrastructure
- Main execution flow and output formatting

### 🔧 TODOs

**TODO 1** Combine description and listed_in into 'content' column

**TODO 2** Sort similarity scores in descending order

**TODO 3** Filter top N+1 recommendations (excluding seed)

## Usage

```bash
python recommender.py
```

Modify `seed_title` in `main()` function to test different titles (e.g., "The Queen's Gambit", "Zodiac").

## Output Format

The system displays the top 10 recommendations with:

- Title and type (Movie/TV Show)
- Genre categories
- Brief description

## Key Columns Used

- `title`: Item identifier for seed matching
- `description`: Primary content feature
- `listed_in`: Genre/category information
- `type`: Movie or TV Show classification
