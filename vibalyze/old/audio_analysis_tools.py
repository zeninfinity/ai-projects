from tabulate import tabulate

from essentia.standard import (
    MonoLoader, RhythmExtractor2013, KeyExtractor, Loudness, PitchYin,
    SpectralCentroidTime, SpectralComplexity, SpectralContrast,
    Flatness, RollOff, RMS, ZeroCrossingRate
)

def analyze_full_essentia(file_path):
    print(f"\nFull Analysis with Essentia: {file_path}\n")

    try:
        audio = MonoLoader(filename=file_path)()
    except Exception as e:
        print(f"Error loading audio file: {e}")
        return

    # Core analysis
    try:
        bpm, _, _, _, _ = RhythmExtractor2013()(audio)
        key, scale, strength = KeyExtractor()(audio)
        loudness = Loudness()(audio)
        pitch, pitch_confidence = PitchYin()(audio)

        # Spectral features
        spectral_centroid = SpectralCentroidTime()(audio)
        spectral_complexity = SpectralComplexity()(audio)
        spectral_contrast = SpectralContrast()(audio)
        flatness = Flatness()(audio)
        rolloff = RollOff()(audio)
        rms = RMS()(audio)
        zero_crossing = ZeroCrossingRate()(audio)
    except Exception as e:
        print(f"Error during analysis: {e}")
        return

    # Display results
    print(f"{'Feature':<25} | {'Value'}")
    print("-" * 45)
    print(f"{'BPM':<25} | {bpm:.2f}")
    print(f"{'Key':<25} | {key} {scale} (strength: {strength:.2f})")
    print(f"{'Loudness (LUFS)':<25} | {loudness:.2f}")
    print(f"{'Pitch (Hz)':<25} | {pitch:.2f}")
    print(f"{'Pitch Confidence':<25} | {pitch_confidence:.2f}")
    print(f"{'Spectral Centroid':<25} | {spectral_centroid:.2f}")
    print(f"{'Spectral Complexity':<25} | {spectral_complexity}")
    print(f"{'Spectral Contrast':<25} | {spectral_contrast}")
    print(f"{'Spectral Flatness':<25} | {flatness:.4f}")
    print(f"{'Roll-Off':<25} | {rolloff:.2f}")
    print(f"{'RMS Energy':<25} | {rms:.4f}")
    print(f"{'Zero Crossing Rate':<25} | {zero_crossing:.4f}")




#########################################################################################

def analyze_with_essentia(mp3_path):
    # This is a placeholder. Actual Essentia integration would go here.
    data = {
        "BPM": 128,
        "Key": "C Minor",
        "Danceability": 0.85,
        "Mood": "Energetic"
    }
    print("Essentia Analysis:")
    print(tabulate(data.items(), tablefmt="github"))
    return data

def analyze_with_musicnn(mp3_path):
    # Placeholder output for mood/genre/instrument detection
    data = {
        "Mood": "Happy",
        "Genre": "Pop",
        "Instruments": "Guitar, Drums"
    }
    print("Musicnn Analysis:")
    print(tabulate(data.items(), tablefmt="github"))
    return data

def analyze_with_genius(mp3_path):
    # Simulated lyrics snippet
    data = {
        "Lyrics Snippet": "Love, love me do / You know I love you..."
    }
    print("Genius API Analysis:")
    print(tabulate(data.items(), tablefmt="github"))
    return data

def analyze_with_sonic_visualiser(mp3_path):
    # Not scriptable, GUI-based, so we just note this
    print("Sonic Visualiser is GUI-based and not scriptable in this module.")
    return None

def analyze_with_mixedinkey(mp3_path):
    # Placeholder since it's a paid tool
    data = {
        "Key": "F# Major",
        "Energy Level": 6
    }
    print("Mixed In Key Analysis:")
    print(tabulate(data.items(), tablefmt="github"))
    return data

def analyze_with_keyfinder(mp3_path):
    data = {
        "Key": "G Minor"
    }
    print("KeyFinder Analysis:")
    print(tabulate(data.items(), tablefmt="github"))
    return data

def analyze_with_mirtoolbox(mp3_path):
    # Placeholder for MATLAB based MIR-toolbox
    data = {
        "Timbre": "Bright",
        "Rhythm Clarity": 0.78,
        "Pitch Mean": "A4"
    }
    print("MIR Toolbox Analysis:")
    print(tabulate(data.items(), tablefmt="github"))
    return data

