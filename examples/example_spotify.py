import numpy as np
import pandas as pd
import streamlit as st

# Data sources: 
# https://www.kaggle.com/datasets/asaniczka/top-spotify-songs-in-73-countries-daily-updated?resource=download
# https://developers.google.com/public-data/docs/canonical/countries_csv

# Functions to load, clean, and process data
def load_countries_by_code():
    return pd.read_csv('spotify/countries_coordinates.csv', 
                            sep='\t',
                            index_col='code').to_dict(orient='index')

def load_countries_by_name():
    return pd.read_csv('spotify/countries_coordinates.csv', 
                            sep='\t',
                            index_col='name').to_dict(orient='index')

def load_songs():
    df = pd.read_csv('spotify/universal_top_spotify_songs.csv')
    df = df[['name', 'artists', 'album_name', 'country', 'daily_rank']]
    df.drop_duplicates(inplace=True)
    df.country.replace('', np.nan, inplace=True)
    df.dropna(inplace=True)
    df.drop(df[df.daily_rank > 3].index, inplace=True)

    # Replace country code with full name
    country_codes = load_countries_by_code()
    df.country = df.country.apply(lambda x: country_codes[x]['name'])

    return df

# Initialize variables in session state
if 'country_coordinates' not in st.session_state:
    st.session_state.country_coordinates = load_countries_by_name()
if 'df_songs' not in st.session_state:
    st.session_state.df_songs = load_songs()

# Streamlit layout
st.title("Travel Suggestions Based on Your Favorite Songs")

con_1 = st.container()
con_2 = st.container()
con_3 = st.container()

with con_1:
    st.header("Current top-3 songs world wide")
    st.dataframe(st.session_state.df_songs.head(500),
                 hide_index=True)

with con_2:
    st.header("Get travel suggestions based on your favourite songs")
    song1 = st.text_input("Enter the title of your 1st favorite song:")
    song2 = st.text_input("Enter the title of your 2nd favorite song:")
    song3 = st.text_input("Enter the title of your 3rd favorite song:")

with con_3:
    if st.button("Get Travel Suggestions"):
        if song1 or song2 or song3:
            user_songs = [song1, song2, song3]

            # Create set and add all matching countries
            # The comparision is more reliable when strings are all lowercase and stripped of any whitespace
            matching_countries = set()
            for song in user_songs:
                matching_songs = st.session_state.df_songs[st.session_state.df_songs['name'].str.lower().str.strip() == song.lower().strip()]
                if not matching_songs.empty:
                    matching_countries.update(matching_songs['country'].unique())

            if matching_countries:
                # Create a dictionary for all matching countries that includes their coordinates
                matching_countries_with_coordinates = {k: v for k, v in st.session_state.country_coordinates.items() 
                                                    if k in matching_countries and v is not None}
                
                if matching_countries_with_coordinates:
                    st.write("Countries where your favorite songs are popular:")

                    # Display a list of matching countries and a corresponding map
                    col_1, col_2 = st.columns(spec=[0.2, 0.8])
                    with col_1:
                        st.dataframe(matching_countries_with_coordinates.keys(), 
                                     hide_index=True,
                                     column_config={'0': 'Country'})
                    with col_2:
                        # Transpose (.T) the data frame to switch rows with columns,
                        # because st.map() asks for langitude and latitude data in columns
                        st.map(pd.DataFrame(matching_countries_with_coordinates).T)
                    
                    st.write("You might want to travel somewhere there?")
            else:
                # Find the song that is popular in the most countries
                most_popular_song = st.session_state.df_songs['name'].value_counts().idxmax()
                st.write(f"""No matches found. You might enjoy listening to the song '{most_popular_song}', 
                         which is popular in the most countries at the moment.""")
        else:
            st.write("Please enter at least one of your favorite songs.")
