import streamlit as st

st.set_page_config(
    page_title="Netflix",
    page_icon="🎬",
    layout="wide"
)

# CSS
st.markdown("""
<style>

.stApp{
    background-color:#141414;
}

.navbar{
    display:flex;
    justify-content:space-between;
    align-items:center;
    background:#000;
    padding:15px 40px;
    border-radius:10px;
}

.logo{
    color:#E50914;
    font-size:35px;
    font-weight:bold;
}

.nav-links{
    display:flex;
    gap:30px;
    color:white;
}

.hero{
    margin-top:20px;
    height:500px;
    border-radius:20px;
    background-image:url('https://images.unsplash.com/photo-1489599849927-2ee91cede3ba');
    background-size:cover;
    background-position:center;
    display:flex;
    align-items:flex-end;
    padding:50px;
}

.hero-title{
    color:white;
    font-size:60px;
    font-weight:bold;
}

.section-title{
    color:white;
    font-size:30px;
    margin-top:30px;
}

img:hover{
    transform:scale(1.08);
    transition:0.3s;
}

</style>
""", unsafe_allow_html=True)

# NAVBAR
st.markdown("""
<div class="navbar">
    <div class="logo">NETFLIX</div>

    <div class="nav-links">
        <span>Home</span>
        <span>TV Shows</span>
        <span>Movies</span>
        <span>Trending</span>
        <span>My List</span>
    </div>
</div>
""", unsafe_allow_html=True)

# HERO
st.markdown("""
<div class="hero">
    <div class="hero-title">
        Stranger Things
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<div class='section-title'>Trending Now</div>",
            unsafe_allow_html=True)

cols = st.columns(6)

movies = [
    "https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg",
    "https://image.tmdb.org/t/p/w500/8UlWHLMpgZm9bx6QYh0NFoq67TZ.jpg",
    "https://image.tmdb.org/t/p/w500/6DrHO1jr3qVrViUO6s6kFiAGM7.jpg",
    "https://image.tmdb.org/t/p/w500/vZloFAK7NmvMGKE7VkF5UHaz0I.jpg",
    "https://image.tmdb.org/t/p/w500/7WsyChQLEftFiDOVTGkv3hFpyyt.jpg",
    "https://image.tmdb.org/t/p/w500/cezWGskPY5x7GaglTTRN4Fugfb8.jpg"
]

for i,col in enumerate(cols):
    with col:
        st.image(movies[i])