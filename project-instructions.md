Fifth Laboratory Activity: Recommender Systems Comparison
Each group is required to design and implement two (2) types of recommender systems: a
Rule-Based Model and a Content-Based Filtering Model using Python and the provided
netflix_titles.csv dataset. This laboratory activity aims to deepen students’ understanding of
fundamental recommender system architectures by emphasizing their differences in logic,
implementation, and practical applicability.
Each group shall create a private GitHub repository for this activity and add all group
members as collaborators. Proper use of version control is expected, including individual
contributions, commit documentation, and collaborative development practices. The complete
source code, along with supporting files and documentation, must be accessible through the
submitted repository link.
Implementation Requirements
The implementation shall consist of two components:

1. Rule-Based Recommender System
   A system that generates recommendations based on explicitly defined business rules using
   relevant dataset columns such as type, listed_in, date_added, and release_year.
   ● Rule 1: Recommend the top N movies (type='Movie') that were most recently added
   (date_added) and have a rating of “PG-13” or “TV-MA.”
   ● Rule 2: Recommend the top N TV shows (type='TV Show') categorized under
   “International TV Shows” in the listed_in column.
   Each rule must be implemented as a separate function that outputs a list of the top N
   recommended titles.
2. Content-Based Filtering Recommender System
   A system that recommends items similar to a user’s preference based on feature similarity.
   ● Combine relevant item features (e.g., description, listed_in) into a single textual
   content representation.
   ● Apply TF-IDF vectorization to convert the combined text into feature vectors.
   ● Compute Cosine Similarity between all items to identify related content.
   ● Implement a simulated user preference by accepting a Seed Title (e.g., “Zodiac” or
   “The Queen’s Gambit”), and display the top N similar items excluding the seed itself.
   Each system must display outputs demonstrating the top ten (10) recommendations generated
   under the following scenarios:
   ● Rule-Based (Rule 1): Top 10 Movies
   ● Rule-Based (Rule 2): Top 10 TV Shows
   ● Content-Based: Top 10 Similar Titles to the chosen Seed Title
   Documentation Requirements
   Each group shall prepare a Google Document containing the following sections:
3. Group Information and Repository Link
   ○ Course: CS412 – User Modelling
   ○ Group Members (with Student IDs)
   ○ GitHub Repository URL
4. Code Output Screenshots
   ○ Screenshots must show the three required outputs corresponding to the
   scenarios listed above.
5. Written Responses addressing the following guide questions:
   ○ Q1. What specific dataset columns were crucial for implementing the Rule-Based
   and Content-Based models?
   ○ Q2. Briefly explain the process (vectorizer and metric) used to generate similarity
   scores in the Content-Based Filtering system.
   ○ Q3. Based on your implementation, what is the main strength of the
   Content-Based Filtering approach compared to the Rule-Based approach?
   ○ Q4. How would the Cold Start Problem for a new item affect your Rule-Based
   and Content-Based systems?
   ○ Q5. Suggest one way to combine both models to create a more robust hybrid
   recommender.
   Submission Guidelines
   ● Only one member per group shall submit the final file through Google Classroom.
   ● The submission must include:
   ○ A DOCX derived from the Google Document.
   ○ A valid GitHub repository link containing the full implementation.
   ● Ensure the repository is private but accessible to the instructor for review.
   ● Submit it on or before October 27, 2025 (Monday) – 11:59 PM. Late submissions will
   be subject to corresponding penalties as stated in the course policies.
