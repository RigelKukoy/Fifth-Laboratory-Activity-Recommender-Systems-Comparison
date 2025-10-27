import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class ContentBasedRecommender:
    def __init__(self, dataset_path):
        self.df = pd.read_csv(dataset_path)
        self.tfidf_matrix = None
        self.cosine_sim = None
        self.vectorizer = TfidfVectorizer(stop_words='english')

    def preprocess_data(self):
        self.df['description'] = self.df['description'].fillna('')
        self.df['listed_in'] = self.df['listed_in'].fillna('')
        self.df['title'] = self.df['title'].fillna('')

        # TODO: Enhance by adding more features
        self.df['content'] = self.df['description'] + ' ' + self.df['listed_in']

    def build_similarity_matrix(self):
        self.tfidf_matrix = self.vectorizer.fit_transform(self.df['content'])
        self.cosine_sim = cosine_similarity(self.tfidf_matrix, self.tfidf_matrix)

    def get_recommendations(self, seed_title, top_n=10):
        if seed_title not in self.df['title'].values:
            return f"Title '{seed_title}' not found in dataset."

        idx = self.df[self.df['title'] == seed_title].index[0]

        sim_scores = list(enumerate(self.cosine_sim[idx]))

        # TODO: Enhance
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # TODO: Enhance 
        sim_scores = sim_scores[1:top_n+1]

        movie_indices = [i[0] for i in sim_scores]

        recommendations = self.df.iloc[movie_indices][['title', 'type', 'listed_in', 'description']]
        return recommendations


def main():
    recommender = ContentBasedRecommender('./netflix_titles.csv')

    print("=== Content-Based Filtering Recommender System ===\n")

    recommender.preprocess_data()
    recommender.build_similarity_matrix()
    # TODO: Enhance by making this into a user input function
    seed_title = "Zodiac"
    print(f"Top 10 recommendations similar to '{seed_title}':\n")
    recommendations = recommender.get_recommendations(seed_title, top_n=10)

    if isinstance(recommendations, pd.DataFrame):
        for idx, row in enumerate(recommendations.itertuples(), 1):
            print(f"{idx}. {row.title} ({row.type})")
            print(f"   Genre: {row.listed_in}")
            print(f"   Description: {row.description[:100]}...\n")
    else:
        print(recommendations)


if __name__ == "__main__":
    main()
