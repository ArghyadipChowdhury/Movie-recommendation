import streamlit as st
import pickle
movies_list = pickle.load(open('movies.pkl','rb'))
movies_list=movies_list['title'].values
st.title('Movie Recommendation Syatem')

selected_movie_name = st.selectbox('How would you like to be connected?',
                                   movies_list )
def recommend(movie):
    movie_index=movies_list[movies_list['title']==movie].index[0]
    distance = similarity[movie_index]
    movies_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
    for i in movies_list:
        print(new_df.iloc[i[0]].title)


if st.button('Recommend'):
    recommend(selected_movie_name)
    st.write(selected_movie_name)



