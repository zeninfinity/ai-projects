import os
import librosa
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from tabulate import tabulate 
import aud_essentia as es

# Path to folder with mp3 files
FOLDER_PATH = "/Users/z/git/zz/ai/ai-projects/vibalyze/mp3/TheBeatles"

file_path = r"./mp3/TheBeatles/The Beatles - Love Me Do.mp3"
es.analyze_full_essentia(file_path)
file_path = r"./mp3/TheBeatles/The Beatles - Yesterday.mp3"
es.analyze_full_essentia(file_path)
#    tools.analyze_full_essentia("./mp3/TheBeatles/The Beatles - Yesterday.mp3")
