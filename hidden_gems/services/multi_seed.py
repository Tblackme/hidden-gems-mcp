from hidden_gems.models.artist import Artist
from hidden_gems.services.lastfm import similar_artists
from hidden_gems.services.scoring import hidden_gem_score


def discover(seed_artists: list[str], limit: int = 10) -> list[Artist]:

    combined: dict[str, Artist] = {}

    for seed in seed_artists:

        artists = similar_artists(seed, limit)

        for artist in artists:

            if artist.name not in combined:

                combined[artist.name] = artist

            else:

                existing = combined[artist.name]

                existing.matches += 1

                existing.similarity = (
                    existing.similarity + artist.similarity
                ) / 2

    results = list(combined.values())

    for artist in results:
        hidden_gem_score(artist)

    results.sort(
        key=lambda artist: (
            artist.matches,
            artist.score
        ),
        reverse=True,
    )

    return results