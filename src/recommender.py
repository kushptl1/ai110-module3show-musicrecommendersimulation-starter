import csv
from pathlib import Path
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        scored_songs = []
        for song in self.songs:
            song_dict = {
                "id": song.id,
                "title": song.title,
                "artist": song.artist,
                "genre": song.genre,
                "mood": song.mood,
                "energy": song.energy,
                "tempo_bpm": song.tempo_bpm,
                "valence": song.valence,
                "danceability": song.danceability,
                "acousticness": song.acousticness,
            }
            user_prefs = {
                "genre": user.favorite_genre,
                "mood": user.favorite_mood,
                "energy": user.target_energy,
                "likes_acoustic": user.likes_acoustic,
            }
            score, _ = score_song(user_prefs, song_dict)
            scored_songs.append((score, song))

        scored_songs.sort(key=lambda item: item[0], reverse=True)
        return [song for _, song in scored_songs[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        song_dict = {
            "id": song.id,
            "title": song.title,
            "artist": song.artist,
            "genre": song.genre,
            "mood": song.mood,
            "energy": song.energy,
            "tempo_bpm": song.tempo_bpm,
            "valence": song.valence,
            "danceability": song.danceability,
            "acousticness": song.acousticness,
        }
        user_prefs = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy,
            "likes_acoustic": user.likes_acoustic,
        }
        _, reasons = score_song(user_prefs, song_dict)
        return "; ".join(reasons)

def build_adversarial_profiles() -> List[Dict]:
    """
    Create a handful of deliberately tricky user profiles to stress-test the scorer.
    These are designed to surface edge cases such as conflicting preferences,
    extreme values, or ambiguous acoustic settings.
    """
    return [
        {
            "name": "Conflicting energy and mood",
            "user_prefs": {
                "genre": "pop",
                "mood": "sad",
                "energy": 0.9,
                "likes_acoustic": False,
            },
            "reason": "High energy but sad mood can create tension in matching logic.",
        },
        {
            "name": "Extreme acoustic preference",
            "user_prefs": {
                "genre": "indie",
                "mood": "chill",
                "energy": 0.3,
                "likes_acoustic": True,
            },
            "reason": "Strong acoustic preference may dominate softer tracks.",
        },
        {
            "name": "Unknown genre with clear energy target",
            "user_prefs": {
                "genre": "unknown",
                "mood": "happy",
                "energy": 0.6,
                "likes_acoustic": False,
            },
            "reason": "A missing genre should not prevent energy-based ranking.",
        },
        {
            "name": "Noisy preference values",
            "user_prefs": {
                "genre": "rock",
                "mood": "angry",
                "energy": 1.2,
                "likes_acoustic": True,
            },
            "reason": "Out-of-range energy values test whether the scorer clamps or misbehaves.",
        },
    ]


def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    path = Path(csv_path)
    songs: List[Dict] = []

    with path.open(newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            song = dict(row)
            for field in [
                "id",
                "energy",
                "tempo_bpm",
                "valence",
                "danceability",
                "acousticness",
            ]:
                song[field] = float(song[field])
            songs.append(song)

    print(f"Loaded songs: {len(songs)}")
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    score = 0.0
    reasons: List[str] = []

    genre_pref = user_prefs.get("genre") or getattr(user_prefs, "favorite_genre", None)
    mood_pref = user_prefs.get("mood") or getattr(user_prefs, "favorite_mood", None)
    energy_pref = user_prefs.get("energy") or getattr(user_prefs, "target_energy", None)
    likes_acoustic = user_prefs.get("likes_acoustic")
    if likes_acoustic is None:
        likes_acoustic = getattr(user_prefs, "likes_acoustic", False)

    if genre_pref and song.get("genre") == genre_pref:
        score += 2.0
        reasons.append("genre match (+2.0)")

    if mood_pref and song.get("mood") == mood_pref:
        score += 2.0
        reasons.append("mood match (+2.0)")

    if energy_pref is not None:
        energy_diff = abs(float(song.get("energy", 0.0)) - float(energy_pref))
        energy_score = max(0.0, 1.0 - energy_diff)
        score += energy_score
        reasons.append(f"energy closeness (+{energy_score:.2f})")

    if likes_acoustic is not None and likes_acoustic:
        if float(song.get("acousticness", 0.0)) >= 0.6:
            score += 1.0
            reasons.append("acoustic preference (+1.0)")
    elif likes_acoustic is not None and not likes_acoustic:
        if float(song.get("acousticness", 0.0)) <= 0.4:
            score += 1.0
            reasons.append("acoustic preference (+1.0)")

    return score, reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    scored_songs = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "; ".join(reasons) if reasons else "No strong matches"
        scored_songs.append((song, score, explanation))

    scored_songs.sort(key=lambda item: item[1], reverse=True)
    return scored_songs[:k]
