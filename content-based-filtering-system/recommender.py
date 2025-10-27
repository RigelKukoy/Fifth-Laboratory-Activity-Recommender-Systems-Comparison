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
        self.df['director'] = self.df['director'].fillna('Unknown')
        self.df['cast'] = self.df['cast'].fillna('Unknown')
        self.df['rating'] = self.df['rating'].fillna('Not Rated')

        
        self.df['content'] = self.df['description'] + ' ' + self.df['listed_in'] + ' ' + self.df['director'] + ' ' + self.df['cast'] + ' ' + self.df['rating']

    def build_similarity_matrix(self):
        self.tfidf_matrix = self.vectorizer.fit_transform(self.df['content'])
        self.cosine_sim = cosine_similarity(self.tfidf_matrix, self.tfidf_matrix)

    def get_recommendations(self, seed_title, top_n=10):
        if seed_title not in self.df['title'].values:
            return f"Title '{seed_title}' not found in dataset."

        idx = self.df[self.df['title'] == seed_title].index[0]

        sim_scores = list(enumerate(self.cosine_sim[idx]))
        
        sim_scores = [(i, score) for i, score in sim_scores if i != idx]
      
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[:top_n]

        movie_indices = [i[0] for i in sim_scores]

        recommendations = self.df.iloc[movie_indices][['title', 'type', 'listed_in', 'description', 'director', 'cast', 'rating']]
        return recommendations


def main():
    recommender = ContentBasedRecommender('./netflix_titles.csv')

    print("=== Content-Based Filtering Recommender System ===\n")

    recommender.preprocess_data()
    recommender.build_similarity_matrix()
    # TODO: Enhance by making this into a user input function
    seed_title = "Naruto Shippuden the Movie: Blood Prison"
    print(f"Top 10 recommendations similar to '{seed_title}':\n")
    recommendations = recommender.get_recommendations(seed_title, top_n=10)

    if isinstance(recommendations, pd.DataFrame):
        for idx, row in enumerate(recommendations.itertuples(), 1):
            print(f"{idx}. {row.title} ({row.type})")
            print(f"   Genre: {row.listed_in}")
            print(f"   Description: {row.description[:100]}...")
            print(f"   Director: {row.director}")
            
            # Clean cast
            cast_list = row.cast.split(',') 
            cast_list = [c.strip() for c in cast_list]  
            max_cast = 5  # maximum number of actors to show
            if len(cast_list) > max_cast:
                cast_display = ', '.join(cast_list[:max_cast]) + f", and {len(cast_list)-max_cast} more"
            else:
                cast_display = ', '.join(cast_list)
            print(f"   Cast: {cast_display}")
            
            print(f"   Rating: {row.rating}\n")
    else:
        print(recommendations)


if __name__ == "__main__":
    main()
