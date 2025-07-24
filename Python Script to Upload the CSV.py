import mysql.connector
import pandas as pd

# Load CSV
df = pd.read_csv("top_artist_tracks.csv")

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sowmya@123",
    database="music_analytics"
)

cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS top_tracks (
    artist_name VARCHAR(100),
    track_name VARCHAR(255),
    album_name VARCHAR(255),
    popularity INT
)
""")

# Insert data
for i, row in df.iterrows():
    artist = row['artist']
    track = row['song_name']
    album = row['album']
    popularity = int(row['popularity'])

    print(f"Inserting: {artist}, {track}, {album}, {popularity}")

    cursor.execute("""
        INSERT INTO top_tracks (artist_name, track_name, album_name, popularity)
        VALUES (%s, %s, %s, %s)
    """, (artist, track, album, popularity))

conn.commit()
print("✅ Data loaded successfully into MySQL!")
conn.close()

