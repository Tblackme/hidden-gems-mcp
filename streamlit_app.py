import streamlit as st

from hidden_gems.services.multi_seed import discover

st.set_page_config(
    page_title="Hidden Gems AI",
    page_icon="🎵",
    layout="wide",
)

# -----------------------------
# Sidebar
# -----------------------------

with st.sidebar:

    st.title("🎛️ Discovery Filters")

    limit = st.slider(
        "Artists per Seed",
        5,
        50,
        20,
    )

    max_listeners = st.slider(
        "Maximum Listeners",
        1000,
        500000,
        50000,
        step=1000,
    )

    min_score = st.slider(
        "Minimum Hidden Gem Score",
        0,
        100,
        50,
    )

    min_similarity = st.slider(
        "Minimum Similarity",
        0.0,
        1.0,
        0.40,
        step=0.05,
    )

    min_matches = st.slider(
        "Minimum Seed Matches",
        1,
        5,
        1,
    )

    sort_by = st.selectbox(
        "Sort By",
        [
            "Hidden Gem Score",
            "Similarity",
            "Listeners",
            "Seed Matches",
        ],
    )

# -----------------------------
# Main Page
# -----------------------------

st.title("🎵 Hidden Gems AI")
st.caption("Discover underrated artists with AI-powered recommendations.")

st.divider()

seed_text = st.text_area(
    "Enter one artist per line",
    value="""Josiah Queen
Benjamin William Hastings
Chris Renzema""",
    height=150,
)

if st.button("🔍 Discover Hidden Gems", type="primary"):

    seed_artists = [
        artist.strip()
        for artist in seed_text.splitlines()
        if artist.strip()
    ]

    with st.spinner("Searching Last.fm..."):

        artists = discover(seed_artists, limit=limit)

    # -----------------------------
    # Filters
    # -----------------------------

    artists = [
        artist
        for artist in artists
        if artist.listeners <= max_listeners
        and artist.score >= min_score
        and artist.similarity >= min_similarity
        and artist.matches >= min_matches
    ]

    # -----------------------------
    # Sorting
    # -----------------------------

    if sort_by == "Hidden Gem Score":
        artists.sort(key=lambda a: a.score, reverse=True)

    elif sort_by == "Similarity":
        artists.sort(key=lambda a: a.similarity, reverse=True)

    elif sort_by == "Listeners":
        artists.sort(key=lambda a: a.listeners)

    elif sort_by == "Seed Matches":
        artists.sort(key=lambda a: a.matches, reverse=True)

    st.success(f"Found {len(artists)} artists")

    st.divider()

    for artist in artists:

        with st.container(border=True):

            c1, c2, c3 = st.columns([5, 2, 2])

            with c1:
                st.subheader(artist.name)

            with c2:
                st.metric("⭐ Score", f"{artist.score:.1f}")

            with c3:
                st.metric("👥 Listeners", f"{artist.listeners:,}")

            st.progress(min(artist.score / 100, 1.0))

            st.write(f"**Similarity:** {artist.similarity:.2f}")
            st.write(f"**Matched Seeds:** {artist.matches}")

st.divider()
st.caption("Hidden Gems AI • Powered by Last.fm")