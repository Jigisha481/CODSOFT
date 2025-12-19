movies = {
    "Avatar": ["space", "alien", "future"],
    "Titanic": ["romance", "ship", "love"],
    "Inception": ["dream", "mind", "heist"],
    "Interstellar": ["space", "time", "science"],
    "The Martian": ["space", "mars", "survival"]
}

def recommend(movie):
    if movie not in movies:
        return ["Movie not found"]

    movie_keywords = movies[movie]
    scores = {}

    
    for title, keywords in movies.items():
        if title == movie:
            continue
        
        
        score = len(set(movie_keywords) & set(keywords))
        scores[title] = score

    
    recommendations = sorted(scores, key=scores.get, reverse=True)

    return recommendations[:3]  # top 3 movies

# Example
print("Recommendations for Interstellar:")
print(recommend("Interstellar"))
