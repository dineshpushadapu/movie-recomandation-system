import pickle
import streamlit as st
import requests
import pandas as pd
import numpy as np
from config import TMDB_API_KEY, OMDB_API_KEY  # Import the API keys
import time

@st.cache_data  # Cache poster results to avoid repeated API calls
def fetch_poster(movie_title):
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={OMDB_API_KEY}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        poster = data.get('Poster')
        if poster and poster != 'N/A':
            return poster
        else:
            return None
    except requests.exceptions.Timeout:
        print(f"Timeout failed for {movie_title}")
    except requests.exceptions.ConnectionError:
        print(f"Connection error for {movie_title}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch poster for {movie_title}: {e}")
    return None

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        movie_title = movies.iloc[i[0]].title
        recommended_movie_posters.append(fetch_poster(movie_title))
        recommended_movie_names.append(movie_title)
    return recommended_movie_names, recommended_movie_posters

# Streamlit UI
st.set_page_config(page_title="Movie Recommender", layout="wide")
st.header('Movie Recommender System')

movies = pickle.load(open('model/movie_list.pkl','rb'))
similarity = pickle.load(open('model/similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)  # updated for new streamlit version

    # keep your logic exactly as it is — just add size and null check
    with col1:
        st.text(recommended_movie_names[0])
        if recommended_movie_posters[0]:
            st.image(recommended_movie_posters[0], width=250)
        else:
            st.warning("Image not available")

    with col2:
        st.text(recommended_movie_names[1])
        if recommended_movie_posters[1]:
            st.image(recommended_movie_posters[1], width=250)
        else:
            st.warning("Image not available")

    with col3:
        st.text(recommended_movie_names[2])
        if recommended_movie_posters[2]:
            st.image(recommended_movie_posters[2], width=250)
        else:
            st.warning("Image not available")

    with col4:
        st.text(recommended_movie_names[3])
        if recommended_movie_posters[3]:
            st.image(recommended_movie_posters[3], width=250)
        else:
            st.warning("Image not available")

    with col5:
        st.text(recommended_movie_names[4])
        if recommended_movie_posters[4]:
            st.image(recommended_movie_posters[4], width=250)
        else:
            st.warning("Image not available")

