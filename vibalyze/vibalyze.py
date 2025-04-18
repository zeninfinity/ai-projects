import os
import librosa
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from tabulate import tabulate 

# Path to folder with mp3 files
FOLDER_PATH = "/Users/z/git/zz/ai/ai-projects/vibalyze/mp3/TheBeatles"

def get_mp3_files(folder):
    return [f for f in os.listdir(folder) if f.endswith('.mp3')]

def detect_bpm(file_path):
    y, sr = librosa.load(file_path, duration=60)  # Limit to 60 seconds for speed
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    return round(float(tempo.item()))

def get_lyrics(file_path):
    try:
        audio = MP3(file_path, ID3=EasyID3)
        return audio.get("lyrics", [""])[0]
    except Exception:
        return "Lyrics not found"

def detect_feeling(bpm, lyrics):
    # Placeholder logic: use real ML/NLP model or API here
    if bpm > 120:
        feeling = "Energetic"
    elif bpm > 90:
        feeling = "Groovy"
    else:
        feeling = "Chill"

    if "love" in lyrics.lower():
        feeling += " / Romantic"
    elif "sad" in lyrics.lower():
        feeling += " / Melancholic"
    return feeling

def process_files(folder):
    files = get_mp3_files(folder)
    results = []
    for filename in files:
        path = os.path.join(folder, filename)
        bpm = detect_bpm(path)
        lyrics = get_lyrics(path)
        feeling = detect_feeling(bpm, lyrics)
        results.append({
            "file": filename,
            "bpm": bpm,
            "feeling": feeling,
            "lyrics_snippet": lyrics[:100] + "..." if lyrics else "N/A"
        })
    return results

# Output the results

if __name__ == "__main__":
    summary = process_files(FOLDER_PATH)

    table = []
    for info in summary:
        table.append([
            info['file'],
            info['bpm'],
            info['feeling'],
            info['lyrics_snippet']
        ])

    headers = ["Title", "BPM", "Feeling", "Lyrics"]
    print(tabulate(table, headers=headers, tablefmt="fancy_grid"))
