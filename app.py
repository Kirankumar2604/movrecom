# import streamlit as st
# import pickle
# import pandas as pd
# import requests
#
# def fetch_poster(movie_id):
#     response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=97ed594278b0492669a30bc5075f0e7f&&language=en-US'.format(movie_id))
#     data = response.json()
#     print(data)
#     return "https://image.tmdb.org/t/p/500/" + data['poster_path']
#
# def recommend(movie):
#     movie_index = movies[movies['title'] == movie].index[0]
#     distances = similarity[movie_index]
#     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
#
#     recommended_movies = []
#     recommended_movies_poster = []
#     for i in movies_list:
#         movie_id = i[0]
#         recommended_movies.append(movies.iloc[i[0]].title)
#         recommended_movies_poster.append(fetch_poster(movie_id))
#     return recommended_movies, recommended_movies_poster
#
# movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
# movies = pd.DataFrame(movies_dict)
#
# similarity = pickle.load(open('similarity.pkl', 'rb'))
# st.title("Movie Recommender System")
#
# selected_movie_name = st.selectbox(
#     "Select Movie Recommender System",
#     movies['title'].values
# )
#
# if st.button("Recommend"):
#     names,posters = recommend(selected_movie_name)
#
#     col1, col2, col3 = st.beta_columns(3)
#     with col1:
#         st.header("A cat")
#     st.image("https://static.streamlit.io/examples/cat.jpg")
#     with col2:
#         st.header("A cat")
#     st.image("https://static.streamlit.io/examples/cat.jpg")
#     with col3:
#         st.header("A cat")
#     st.image("https://static.streamlit.io/examples/cat.jpg")
#
#     # for i in recommendations:
#     #     st.write(i)
import streamlit as st
import pickle
import pandas as pd
import requests

# TMDB API Key
API_KEY = "97ed5942b0492669a30bc5075f0e7f"


def fetch_poster(movie_id):
    """
    Fetch movie poster from TMDB API.
    """
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=97ed594278b0492669a30bc5075f0e7f&language=en-US"
        response = requests.get(url)
        data = response.json()

        poster_path = data.get("poster_path")

        if poster_path:
            return f"https://image.tmdb.org/t/p/w500/{poster_path}"

        # Default image if no poster exists
        return "https://via.placeholder.com/500x750?text=No+Poster"

    except Exception as e:
        print("Error:", e)
        return "https://via.placeholder.com/500x750?text=Error"


def recommend(movie):
    """
    Get top 5 similar movies.
    """
    movie_index = movies[movies["title"] == movie].index[0]

    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:

        # IMPORTANT:
        # Use actual TMDB movie_id column
        movie_id = movies.iloc[i[0]]["movie_id"]

        recommended_movies.append(
            movies.iloc[i[0]]["title"]
        )

        recommended_movies_posters.append(
            fetch_poster(movie_id)
        )

    return recommended_movies, recommended_movies_posters


# Load data
movies_dict = pickle.load(open("movie_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open("similarity.pkl", "rb"))

# Streamlit UI
st.title("🎬 Movie Recommender System")

selected_movie_name = st.selectbox(
    "Select a Movie",
    movies["title"].values
)

if st.button("Recommend"):

    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])