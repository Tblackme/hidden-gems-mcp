import os

import pylast
from dotenv import load_dotenv

try:
    import streamlit as st

    api_key = st.secrets.get("LASTFM_API_KEY")
    api_secret = st.secrets.get("LASTFM_SHARED_SECRET")

except Exception:
    load_dotenv()

    api_key = os.getenv("LASTFM_API_KEY")
    api_secret = os.getenv("LASTFM_SHARED_SECRET")


network = pylast.LastFMNetwork(
    api_key=api_key,
    api_secret=api_secret,
)


def search_artist(name: str) -> Artist:
    """
    Look up a single artist by name.
    """

    artist = network.get_artist(name)

    return Artist(
        name=artist.get_name(),
        listeners=int(artist.get_listener_count()),
        playcount=int(artist.get_playcount()),
    )


def similar_artists(name: str, limit: int = 10) -> list[Artist]:
    """
    Return similar artists as Artist objects.
    """

    artist = network.get_artist(name)

    results: list[Artist] = []

    for similar, score in artist.get_similar(limit=limit):

        results.append(
            Artist(
                name=similar.get_name(),
                listeners=int(similar.get_listener_count()),
                similarity=float(score),
                matches=1,
                source="Last.fm",
            )
        )

    return results


def top_albums(name: str, limit: int = 5):
    """
    Return an artist's top albums.
    """

    artist = network.get_artist(name)

    albums = []

    for album in artist.get_top_albums(limit=limit):
        albums.append(album.item.get_name())

    return albums


def top_tags(name: str, limit: int = 10):
    """
    Return an artist's top Last.fm tags.
    """

    artist = network.get_artist(name)

    tags = []

    for tag in artist.get_top_tags(limit=limit):
        tags.append(tag.item.get_name())

    return tags


def biography(name: str):
    """
    Return an artist biography.
    """

    artist = network.get_artist(name)

    return artist.get_bio_summary()