import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Creating a dataset similar to Instagram's recommendation model
data = {
    'User': ['A', 'B', 'C', 'D'],
    'Tech Videos': [5, 3, 0, 4],   # User ratings for tech videos
    'Food Videos': [1, 4, 5, 2],   # User ratings for food videos
    'Travel Videos': [2, 1, 4, 5]  # User ratings for travel videos
}

# Converting dictionary to DataFrame
df = pd.DataFrame(data)

# Display the user preference table
print("\nUser Preference Table:")
print(df)

# Compute cosine similarity between users
similarity_matrix = cosine_similarity(df.iloc[:, 1:])  # Ignore 'User' column

# Adding similarity scores as a new column
df['Similarity'] = similarity_matrix.mean(axis=1)

# Display the similarity scores
print("\nUser Similarity Scores:")
print(df[['User', 'Similarity']])
