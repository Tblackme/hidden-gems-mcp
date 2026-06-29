import streamlit as st

st.write("Secrets loaded:")

st.write("LASTFM_API_KEY:", "✅" if "LASTFM_API_KEY" in st.secrets else "❌")
st.write("LASTFM_SHARED_SECRET:", "✅" if "LASTFM_SHARED_SECRET" in st.secrets else "❌")

st.write("Secrets loaded:")

st.write("LASTFM_API_KEY:", "✅" if "LASTFM_API_KEY" in st.secrets else "❌")
st.write("LASTFM_SHARED_SECRET:", "✅" if "LASTFM_SHARED_SECRET" in st.secrets else "❌")

from hidden_gems.services.multi_seed import discover

st.set_page_config(
    page_title="Hidden Gems AI",
    page_icon="🎵",
    layout="wide",
)

st.title("🎵 Hidden Gems AI")
st.caption("Discover underrated artists with AI-powered recommendations.")

st.divider()

st.header("Seed Artists")

default_text = """Josiah Queen
Benjamin William Hastings
Chris Renzema"""

seed_text = st.text_area(
    "Enter one artist per line",
    value=default_text,
    height=150,
)

limit = st.slider(
    "Artists to search per seed",
    min_value=5,
    max_value=50,
    value=20,
)

if st.button("🔍 Discover Hidden Gems", type="primary"):

    seed_artists = [
        artist.strip()
        for artist in seed_text.splitlines()
        if artist.strip()
    ]

    with st.spinner("Searching Last.fm..."):
        artists = discover(seed_artists, limit=limit)

    st.success(f"Found {len(artists)} recommendations!")

    st.divider()

    for artist in artists:

        with st.container(border=True):

            col1, col2, col3 = st.columns([5, 2, 2])

            with col1:
                st.subheader(artist.name)

            with col2:
                st.metric("⭐ Score", f"{artist.score:.1f}")

            with col3:
                st.metric("👥 Listeners", f"{artist.listeners:,}")

            st.progress(min(artist.score / 100, 1.0))

            st.write(f"**Similarity:** {artist.similarity:.2f}")
            st.write(f"**Matched Seeds:** {artist.matches}")

st.divider()
st.caption("Hidden Gems MCP • Powered by Last.fm")