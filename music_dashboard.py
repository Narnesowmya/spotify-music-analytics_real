import streamlit as st
import pandas as pd
import plotly.express as px

# Load the data from CSV
df = pd.read_csv("spotify_top_tracks.csv")

st.set_page_config(page_title="🎵 Spotify Top Tracks Dashboard", layout="wide")

st.title("🎧 Spotify Top Tracks by Artist")

# Sidebar filter
selected_artist = st.sidebar.selectbox("Select an Artist", df['artist'].unique())

# Filter the data
filtered_df = df[df['artist'] == selected_artist]

# Display raw data
st.subheader(f"Top Tracks by {selected_artist}")
st.dataframe(filtered_df, use_container_width=True)

# Plot: Track Popularity
fig = px.bar(
    filtered_df,
    x='song_name',
    y='popularity',
    title=f"Popularity of Songs by {selected_artist}",
    labels={"popularity": "Popularity Score", "song_name": "Song Name"},
    color='popularity',
    color_continuous_scale='viridis'
)

st.plotly_chart(fig, use_container_width=True)
