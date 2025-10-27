# Content-Based Filtering Recommender System

Implementation of a content-based filtering system for Netflix titles using TF-IDF vectorization and cosine similarity.  

**This version allows interactive user input to get recommendations dynamically.**


## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
````
2. Ensure `netflix_titles.csv` is in the project root directory.
---

## How It Works

The system recommends items similar to a seed title by:

1. **Feature Combination**: Combines textual features (`description`, `listed_in`, `director`, `cast`, `rating`) into a unified content representation.
2. **TF-IDF Vectorization**: Converts text into numerical feature vectors using Term Frequency–Inverse Document Frequency.
3. **Cosine Similarity**: Computes similarity scores between all items (range: 0 to 1, where 1 = identical).
4. **Ranking & Filtering**:
   * Excludes the seed title from the recommendations.
   * Sorts by similarity score in descending order.
   * Returns the top N most similar items.
5. **Interactive User Input**: Users can type a movie or TV show title at runtime. Input is automatically converted to title case to match dataset titles.

---

## Implementation Status

### ✅ Completed

* Data loading and preprocessing
* TF-IDF vectorizer setup
* Cosine similarity computation infrastructure
* Combined feature column creation (`content`)
* Main execution flow with interactive user input
* Output formatting including truncated description and cleaned cast display

---

## Usage

Run the recommender system:

```bash
python recommender.py
```

1. The program prompts you:

```
Enter a movie/TV show title (or 'q' to quit):
```

2. Type a title (any case, e.g., `naruto` or `ZODIAC`). The system converts it to title case automatically.

3. Example output:

```
==================================================

Top 10 recommendations similar to 'Naruto':

1. Naruto Shippuden (TV Show)
   Genre: Action, Adventure, Anime
   Description: Naruto continues his quest to become Hokage while facing powerful enemies and uncovering secrets...
   Director: Hayato Date
   Cast: Junko Takeuchi, Chie Nakamura, Noriaki Sugiyama, Kazuhiko Inoue, Satoshi Hino, and 10 more
   Rating: TV-14

2. Boruto: Naruto Next Generations (TV Show)
   Genre: Action, Adventure, Anime
   Description: Naruto's son, Boruto, embarks on his own ninja journey with friends and faces new threats...
   Director: Noriyuki Abe
   Cast: Yuko Sanpei, Kokoro Kikuchi, Ryota Ohsaka, Kaito Ishikawa, Sumire Uesaka, and 8 more
   Rating: TV-14

...
==================================================
```

4. If the title is not found, the program prompts:

```
Title 'Movie' not found in dataset. Please try again.
```

5. To quit the program, type:

```
q
```

---

## Output Format

The system displays the top 10 recommendations with:

* **Title and type** (Movie/TV Show)
* **Genre categories** (`listed_in`)
* **Brief description** (first 100 characters)
* **Director**
* **Cast** (first 5 actors, with "and X more" if more than 5)
* **Rating**

### Example Output

```
1. The Founder (Movie)
   Genre: Dramas
   Description: After a fateful encounter with the McDonald brothers, struggling salesman Ray Kroc becomes driven to...
   Director: John Lee Hancock
   Cast: Michael Keaton, Nick Offerman, Linda Cardellini, Patrick Wilson, B.J. Novak, and 5 more
   Rating: PG-13
```

---

## Key Columns Used

* `title`: Item identifier for seed matching
* `description`: Primary content feature
* `listed_in`: Genre/category information
* `director`: Director name
* `cast`: List of main actors
* `rating`: Movie/TV rating
* `type`: Movie or TV Show classification

```