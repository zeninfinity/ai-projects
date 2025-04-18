from tabulate import tabulate
import os

from essentia.standard import (
    MonoLoader, RhythmExtractor2013, KeyExtractor, EqualLoudness, Loudness, PitchYin,
    SpectralCentroidTime, SpectralComplexity, SpectralContrast,
    Flatness, RollOff, RMS, ZeroCrossingRate,Spectrum, Windowing, FrameGenerator
)

def analyze_full_essentia(file_path):
    # Validate file path
    if not os.path.exists(file_path):
        print(f"Error: The file at {file_path} does not exist.")
        return
    
    if not os.path.isfile(file_path):
        print(f"Error: The path {file_path} is not a valid file.")
        return
    
    print(f"\nFull Analysis with Essentia: {file_path}\n")

    try:
        audio = MonoLoader(filename=file_path)()
        mp3_louder = EqualLoudness()(audio)
        frames = FrameGenerator(audio, frameSize=2048, hopSize=1024, startFromZero=True)

        for frame in frames:
             windowed = Windowing()(frame)
             spectrum = Spectrum()(windowed)
             flatness = Flatness()(spectrum)
    except Exception as e:
                 print(f"Error loading audio file: {e}")
                 return


    # Core analysis
    try:
        bpm, _, _, _, _ = RhythmExtractor2013()(audio)
        key, scale, strength = KeyExtractor()(audio)
        loudness = Loudness()(audio)
        #try:
        #    pitch, pitch_confidence = PitchYin()(mp3_louder)
        #    print(f"Pitch extracted: {pitch:.2f} Hz, Confidence: {pitch_confidence:.2f}")
        #except Exception as e:
        #    print(f"Error during PitchYin extraction: {e}")
        #    pitch, pitch_confidence = None, None
        

        # Spectral features
        spectral_centroid = SpectralCentroidTime()(audio)
        spectral_complexity = SpectralComplexity()(audio)
        #spectral_contrast = SpectralContrast()(audio)
        spectrum = Spectrum()(Windowing()(frame))
        flatness = Flatness()(spectrum)
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
    #print(f"{'Pitch (Hz)':<25} | {pitch:.2f}")
    #print(f"{'Pitch Confidence':<25} | {pitch_confidence:.2f}")
    print(f"{'Spectral Centroid':<25} | {spectral_centroid:.2f}")
    print(f"{'Spectral Complexity':<25} | {spectral_complexity}")
    #print(f"{'Spectral Contrast':<25} | {spectral_contrast}")
    print(f"{'Spectral Flatness':<25} | {flatness:.4f}")
    print(f"{'Roll-Off':<25} | {rolloff:.2f}")
    print(f"{'RMS Energy':<25} | {rms:.4f}")
    print(f"{'Zero Crossing Rate':<25} | {zero_crossing:.4f}")
