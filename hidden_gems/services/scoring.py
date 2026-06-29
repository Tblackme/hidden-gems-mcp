from hidden_gems.models.artist import Artist


def hidden_gem_score(artist: Artist) -> float:
    """
    Calculate a Hidden Gem Score (0-100).
    """

    similarity_score = artist.similarity * 35

    seed_score = min(artist.matches * 10, 30)

    listeners = artist.listeners

    if listeners <= 5000:
        hidden_score = 25
    elif listeners <= 25000:
        hidden_score = 20
    elif listeners <= 50000:
        hidden_score = 15
    elif listeners <= 100000:
        hidden_score = 8
    else:
        hidden_score = 0

    freshness_score = 0

    artist.score = round(
        similarity_score
        + seed_score
        + hidden_score
        + freshness_score,
        2,
    )

    return artist.score