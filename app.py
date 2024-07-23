import streamlit as st
import pickle

#Here the requests used is different from flask request,
#this one is used to call api from sites
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index=movies[movies['title']==movie].index[0]
    distances=sorted(list(enumerate(similarity[index])),reverse=True,key=lambda x:x[1])
    recommended_names=[]
    recommended_movie_posters = []

    for i in distances[1:6]:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_names.append(movies.iloc[i[0]].title)

    return recommended_names,recommended_movie_posters

st.header('Movie recommender System')
movies=pickle.load(open('movie_list.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))

movie_list=movies['title'].values
selected_movies=st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_names,recommended_movie_posters = recommend(selected_movies)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_names[2])
        st.image(recommended_movie_posters[2])

    with col4:
        st.text(recommended_names[3])
        st.image(recommended_movie_posters[3])
        
    with col5:
        st.text(recommended_names[4])
        st.image(recommended_movie_posters[4])
       

    