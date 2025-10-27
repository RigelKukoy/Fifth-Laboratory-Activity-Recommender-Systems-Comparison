import pandas as pd
import numpy as np
from typing import List, Dict, Any


class RuleBasedRecommender:
    """Rule-based recommender system for movies with specific ratings."""
    
    def __init__(self, dataset_path: str):
        """Initialize the recommender with the dataset path."""
        self.dataset_path = dataset_path
        self.data = None
        self.load_data()
    
    def load_data(self):
        """Load and preprocess the Netflix titles dataset."""
        self.data = pd.read_csv(self.dataset_path)
        # Convert date_added to datetime, handling missing values
        self.data['date_added'] = pd.to_datetime(self.data['date_added'], errors='coerce')
        # Convert release_year to numeric, handling missing values
        self.data['release_year'] = pd.to_numeric(self.data['release_year'], errors='coerce')
        print(f"Dataset loaded: {len(self.data)} titles")
    
    def rule_1_recent_movies(self, n: int = 10) -> List[Dict[str, Any]]:
        """
        Rule 1: Recommend the top N movies that were most recently added
        and have a rating of "PG-13" or "TV-MA".
        
        Args:
            n (int): Number of recommendations to return
            
        Returns:
            List[Dict[str, Any]]: List of recommended movies with their details
        """
        print(f"\n=== Top {n} Recently Added Movies (PG-13/TV-MA) ===")
        
        # Filter movies with specified ratings
        movies = self.data[
            (self.data['type'] == 'Movie') & 
            (self.data['rating'].isin(['PG-13', 'TV-MA']))
        ].copy()
        
        # Remove rows with missing date_added
        movies = movies.dropna(subset=['date_added'])
        # Sort by date_added in descending order (most recent first)
        movies = movies.sort_values('date_added', ascending=False)
        # Get top N recommendations
        top_movies = movies.head(n)
        
        # Format results into structured data
        recommendations = []
        for idx, row in top_movies.iterrows():
            recommendation = {
                'title': row['title'],
                'type': row['type'],
                'rating': row['rating'],
                'date_added': row['date_added'].strftime('%Y-%m-%d'),
                'release_year': int(row['release_year']) if pd.notna(row['release_year']) else 'N/A',
                'duration': row['duration'],
                'listed_in': row['listed_in'],
                'description': row['description'][:100] + '...' if len(str(row['description'])) > 100 else row['description']
            }
            recommendations.append(recommendation)
        
        # Display results
        for i, rec in enumerate(recommendations, 1):
            print(f"{i}. {rec['title']} ({rec['rating']})")
            print(f"   Added: {rec['date_added']} | Released: {rec['release_year']}")
            print(f"   Duration: {rec['duration']}")
            print(f"   Categories: {rec['listed_in']}")
            print(f"   Description: {rec['description']}")
            print()
        
        return recommendations
    
    def rule_2_international_tv_shows(self, n: int = 10) -> List[Dict[str, Any]]:
        """
        Rule 2: Recommend the top N TV shows categorized under "International TV Shows".
        
        Args:
            n (int): Number of recommendations to return
            
        Returns:
            List[Dict[str, Any]]: List of recommended TV shows with their details
        """
        print(f"\n=== Top {n} International TV Shows ===")
        
        # Filter TV shows with "International TV Shows" in listed_in
        tv_shows = self.data[
            (self.data['type'] == 'TV Show') & 
            (self.data['listed_in'].str.contains('International TV Shows', na=False, case=False))
        ].copy()
        
        # Sort by release_year in descending order (most recent first)
        tv_shows = tv_shows.sort_values('release_year', ascending=False, na_position='last')
        # Get top N recommendations
        top_tv_shows = tv_shows.head(n)
        
        # Format results into structured data
        recommendations = []
        for idx, row in top_tv_shows.iterrows():
            recommendation = {
                'title': row['title'],
                'type': row['type'],
                'rating': row['rating'],
                'release_year': int(row['release_year']) if pd.notna(row['release_year']) else 'N/A',
                'duration': row['duration'],
                'country': row['country'] if 'country' in row and pd.notna(row['country']) else 'N/A',
                'listed_in': row['listed_in'],
                'description': row['description'][:100] + '...' if len(str(row['description'])) > 100 else row['description']
            }
            recommendations.append(recommendation)
        
        # Display results
        for i, rec in enumerate(recommendations, 1):
            print(f"{i}. {rec['title']} ({rec['rating']})")
            print(f"   Released: {rec['release_year']} | Country: {rec['country']}")
            print(f"   Duration: {rec['duration']}")
            print(f"   Categories: {rec['listed_in']}")
            print(f"   Description: {rec['description']}")
            print()
        
        return recommendations
    
    def get_dataset_statistics(self):
        """Display basic statistics about the dataset."""
        print("\n=== Dataset Statistics ===")
        print(f"Total titles: {len(self.data)}")
        print(f"Movies: {len(self.data[self.data['type'] == 'Movie'])}")
        print(f"TV Shows: {len(self.data[self.data['type'] == 'TV Show'])}")
        
        # Display rating distribution
        print("\nRating distribution:")
        rating_counts = self.data['rating'].value_counts()
        for rating, count in rating_counts.head(10).items():
            print(f"  {rating}: {count}")


def main():
    """Main function to demonstrate the rule-based recommender system."""
    print("Rule-Based Recommender System")
    print("=" * 50)
    
    # Initialize the recommender with dataset
    dataset_path = "netflix_titles.csv"
    recommender = RuleBasedRecommender(dataset_path)
    
    # Display dataset statistics
    recommender.get_dataset_statistics()
    
    # Apply Rule 1: Top 10 recently added movies with PG-13/TV-MA rating
    rule1_recommendations = recommender.rule_1_recent_movies(n=10)
    
    # Apply Rule 2: Top 10 international TV shows
    rule2_recommendations = recommender.rule_2_international_tv_shows(n=10)
    
    print("\n" + "=" * 50)
    print(f"Rule 1 generated {len(rule1_recommendations)} movie recommendations")
    print(f"Rule 2 generated {len(rule2_recommendations)} TV show recommendations")


if __name__ == "__main__":
    main()
