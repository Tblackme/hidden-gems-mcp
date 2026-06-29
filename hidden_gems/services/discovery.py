from hidden_gems.services.lastfm import similar_artists
from hidden_gems.services.scoring import hidden_gem_score


def hidden_gems(seed_artist, limit=25):

    artists = similar_artists(seed_artist, limit)

    for artist in artists:
        artist["score"] = hidden_gem_score(artist)

    artists.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return artists