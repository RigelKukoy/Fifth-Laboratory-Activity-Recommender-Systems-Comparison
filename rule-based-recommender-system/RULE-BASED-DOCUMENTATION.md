# Rule-Based Recommender System Documentation

## Overview

This document describes the implementation of a Rule-Based Recommender System for the Fifth Laboratory Activity on Recommender Systems Comparison. The system generates recommendations based on explicitly defined business rules using the Netflix titles dataset.

## System Architecture

### Core Components

- **RuleBasedRecommender Class**: Main class that implements the rule-based recommendation logic
- **Rule 1**: Recent Movies with Specific Ratings

### Dataset Requirements

The system uses the `netflix_titles.csv` dataset with the following key columns:

- `type`: Movie or TV Show
- `rating`: Content rating (PG-13, TV-MA, etc.)
- `date_added`: When the title was added to Netflix
- `release_year`: Year the title was originally released
- `listed_in`: Categories/genres the title belongs to
- `title`: Name of the title
- `description`: Brief description of the content

## Implementation Details

### Rule 1: Recent Movies with Specific Ratings

**Objective**: Recommend the top N movies that were most recently added and have a rating of "PG-13" or "TV-MA"

**Implementation Steps**:

1. Filter dataset for movies (`type == 'Movie'`)
2. Filter for specific ratings (`rating` in ['PG-13', 'TV-MA'])
3. Remove entries with missing `date_added` values
4. Sort by `date_added` in descending order (most recent first)
5. Return top N recommendations

**Key Features**:

- Handles missing data gracefully
- Provides detailed output including title, rating, date added, release year, duration, categories, and description
- Returns structured data for further processing

### Rule 2: International TV Shows

**Objective**: Recommend the top N TV shows categorized under "International TV Shows"

**Implementation Steps**:

1. Filter dataset for TV shows (`type == 'TV Show'`)
2. Filter for titles containing "International TV Shows" in the `listed_in` column
3. Sort by `release_year` in descending order (most recent first)
4. Return top N recommendations

**Key Features**:

- Uses string matching to identify international TV shows
- Provides comprehensive information including country of origin
- Handles missing data appropriately

## Usage Instructions

### Prerequisites

1. Install required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Ensure the Netflix dataset is available at the specified path

### Running the System

```bash
python rule_based_recommender.py
```

### Expected Output

The system will generate:

1. Dataset statistics showing total titles, movies vs TV shows, rating distribution
2. Top 10 recently added movies (PG-13/TV-MA)

## Technical Specifications

### Dependencies

- `pandas >= 1.3.0`: Data manipulation and analysis
- `numpy >= 1.21.0`: Numerical computing support

### Data Processing

- Automatic handling of missing values in date and numeric fields
- Type conversion for proper sorting and filtering
- String operations for category matching

### Output Format

Each recommendation includes:

- Title and type
- Rating and release information
- Duration and categories
- Truncated description (100 characters)
- Additional relevant metadata

## Strengths of Rule-Based Approach

1. **Transparency**: Rules are explicit and easily understandable
2. **Interpretability**: Each recommendation can be traced back to specific criteria
3. **Control**: Business logic can be easily modified
4. **Reliability**: Consistent results based on predefined criteria
5. **Efficiency**: Fast execution with minimal computational overhead

## Limitations

1. **Static Rules**: Cannot adapt to user preferences automatically
2. **Limited Personalization**: Same rules apply to all users
3. **Cold Start**: New items may not fit existing rules
4. **Maintenance**: Rules need manual updates as business requirements change

## Future Enhancements

1. Dynamic rule weighting based on user feedback
2. Integration with user preference data
3. Hybrid approach combining rule-based and content-based filtering
4. Real-time rule updates based on trending content
