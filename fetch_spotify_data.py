import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

# Spotify API credentials
client_id = 'c3bf4d9637c9440ab4866b23ff057d68'
client_secret = 'bf953fc71984438f9946df1c37d46cb2'

# Authenticate
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

# 🎤 Artists to search
artists = ['Sid Sriram', 'Devi Sri Prasad', 'Shreya Ghoshal']
all_tracks = []

for artist_name in artists:
    print(f"\n🎧 Fetching top tracks for: {artist_name}")
    
    # Search for the artist
    result = sp.search(q=f'artist:{artist_name}', type='artist')
    if not result['artists']['items']:
        print(f"❌ Artist not found: {artist_name}")
        continue

    artist_id = result['artists']['items'][0]['id']
    
    # Get top tracks (market = India)
    top_tracks = sp.artist_top_tracks(artist_id, country='IN')

    for track in top_tracks['tracks']:
        all_tracks.append({
            'artist': artist_name,
            'song_name': track['name'],
            'album': track['album']['name'],
            'release_date': track['album']['release_date'],
            'popularity': track['popularity'],
            'preview_url': track['preview_url'],
            'spotify_url': track['external_urls']['spotify']
        })

# ✅ Convert to DataFrame
if all_tracks:
    df = pd.DataFrame(all_tracks)
    print("\n📄 Top Tracks by Artists:")
    print(df.head())

    # Save CSVs
    df.to_csv("top_artist_tracks.csv", index=False)
    df.to_csv("spotify_top_hits.csv", index=False)
    df.to_csv(r"D:\pythonfile\spotify_top_tracks.csv", index=False)
    print("\n✅ CSVs saved successfully!")
else:
    print("\n⚠️ No tracks were found to save.")
