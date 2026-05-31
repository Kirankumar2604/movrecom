import os
from pathlib import Path
import streamlit as st
import pickle
import pandas as pd
import requests


def load_local_env(env_path: str = ".env") -> None:
    env_file = Path(env_path)

    if not env_file.exists():
        return

    for raw_line in env_file.read_text().splitlines():
        line = raw_line.strip()

        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


load_local_env()

st.set_page_config(
    page_title="Netflix Clone",
    page_icon="🎬",
    layout="wide"
)

# --------------------------
# CUSTOM CSS
# --------------------------
st.markdown("""
<style>

.main {
    background-color: #141414;
    color: white;
}

.stApp {
    background-color: #141414;
}

h1,h2,h3,p {
    color: white;
}

.movie-card img {
    border-radius: 10px;
    transition: transform 0.3s ease;
}

.movie-card img:hover {
    transform: scale(1.08);
}

.hero {
    background-image: url('https://wallpapercave.com/wp/wp4056410.jpg');
    background-size: cover;
    background-position: center;
    height: 400px;
    border-radius: 20px;
    padding: 50px;
    display: flex;
    align-items: end;
}

.hero-text {
    color: white;
    font-size: 50px;
    font-weight: bold;
}

.netflix-logo {
    color: #E50914;
    font-size: 50px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# --------------------------
# TMDB POSTER
# --------------------------
API_KEY = os.getenv("TMDB_API_KEY")


def fetch_poster(movie_id):
    try:
        if not API_KEY:
            return "https://via.placeholder.com/500x750?text=Missing+API+Key"

        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"
        data = requests.get(url).json()

        poster_path = data.get("poster_path")

        if poster_path:
            return f"https://image.tmdb.org/t/p/w500/{poster_path}"

        return "https://via.placeholder.com/500x750"

    except:
        return "https://via.placeholder.com/500x750"


# --------------------------
# RECOMMENDATION FUNCTION
# --------------------------
def recommend(movie):

    movie_index = movies[movies['title'] == movie].index[0]

    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:11]

    names = []
    posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        names.append(
            movies.iloc[i[0]].title
        )

        posters.append(
            fetch_poster(movie_id)
        )

    return names, posters


# --------------------------
# LOAD DATA
# --------------------------
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

# --------------------------
# SIDEBAR
# --------------------------
with st.sidebar:
    st.markdown(
        "<h1 style='color:#E50914;'>NETFLIX</h1>",
        unsafe_allow_html=True
    )

    st.markdown("---")
    st.write("🏠 Home")
    st.write("🔥 Trending")
    st.write("⭐ My List")
    st.write("🎬 Movies")
    st.write("📺 TV Shows")

# --------------------------
# HERO SECTION
# --------------------------
st.markdown("""
<div class="hero">
    <div class="hero-text">
        Unlimited Movies,<br>
        TV Shows and More.
    </div>
</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

# --------------------------
# MOVIE SELECTOR
# --------------------------
selected_movie = st.selectbox(
    "Choose a movie",
    movies["title"].values
)

if st.button("🎥 Get Recommendations"):

    names, posters = recommend(selected_movie)

    st.subheader("Recommended For You")

    cols = st.columns(5)

    for i in range(5):
        with cols[i]:
            st.image(posters[i])
            st.caption(names[i])

    st.subheader("More Like This")

    cols2 = st.columns(5)

    for i in range(5, 10):
        with cols2[i - 5]:
            st.image(posters[i])
            st.caption(names[i])