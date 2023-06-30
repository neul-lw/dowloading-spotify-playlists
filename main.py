from csv import DictReader
from os import listdir, makedirs
from os.path import exists
import subprocess

print("If you don't have your playlist data use Exportify web app")
print("This script assumes you have your playlists data as 'spotify_playlists' named foler and script in the same directory")
print("This script will create folders for every playlists, so move spotify_playlists and the script to the folder you want download songs to")

playlists = listdir("./spotify_playlists/")

select_song = input("Do you want to select all the songs, or download the first choiece? y/n: ")
while select_song != "y" and select_song != "n":
    select_song = input("Do you want to select all the songs, or download the first choiece? y/n: ")

for playlist in playlists:
    with open(f"./spotify_playlists/{playlist}", newline='') as csvf:
        reader = DictReader(csvf)
        for row in reader:
            album_name = row["Album Name"]
            if not exists(album_name):
                makedirs(album_name)
            artist = row["Artist Name(s)"]
            song_name = row["Track Name"]
            track_id = row["Track URI"]
            if select_song == "y":
                result = subprocess.run(["ytmdl", f"{artist} {song_name}", "--spotify-id", f"{track_id}", "-o", f"{album_name}"])
            else:
                result = subprocess.run(["ytmdl", f"{artist} {song_name}", "--spotify-id", f"{track_id}", "-q", "-o", f"{album_name}"])
