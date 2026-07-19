# 🎵 Music Recommender Simulation

## Project Summary

This project builds a small content-based music recommender. It reads a catalog of songs, compares each one to a user profile, and ranks the best matches. The system is simple, explainable, and designed to show how recommender systems make choices from structured data.

---

## How The System Works

This recommender uses a simple content-based approach. Each song is represented by a few features, with energy as the main focus because it strongly reflects how intense or upbeat a track feels. I also use genre and mood as simple descriptive features so the system can make more meaningful matches. The user profile stores a preferred genre, a preferred mood, and a target energy level. To score a song, the recommender compares the song’s energy to the user’s target energy and gives higher scores to songs that are closer to that preference. It also adds points when the song matches the user’s preferred genre and mood. After scoring all songs, the recommender ranks them from highest to lowest and returns the top results. This makes the system easy to explain, easy to implement, and well-suited for a small music dataset.


Input (User Preferences) → Process (Loop through every song in the CSV and score it) → Output (Rank the songs and return the top K recommendations)

Algorithm Recipe:
1. Read the user’s preferences from the UserProfile.
2. For each song in the CSV, compare it to those preferences.
3. Give a strong score for matching genre and mood.
4. Score energy by how closely the song’s energy matches the user’s target energy.
5. Add a small bonus if the song matches the user’s preference for acousticness.
6. Combine these feature scores into one total score for the song.
7. Repeat this process for every song in the dataset.
8. Sort the songs from highest to lowest score.
9. Return the top K songs as recommendations.

Potential Biases:
- This system may over-prioritize genre and mood, which could cause it to miss songs that match the user’s energy or acoustic preferences but belong to a different style.
- Because the dataset is small, the recommendations may feel repetitive or limited.
- The system may favor a narrow set of common categories in the data and overlook more unusual but still relevant songs.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

```
Loaded songs: 20

Top recommendations:

Sunrise City - Score: 5.98
Because: genre match (+2.0); mood match (+2.0); energy closeness (+0.98); acoustic preference (+1.0)

Rooftop Lights - Score: 3.96
Because: mood match (+2.0); energy closeness (+0.96); acoustic preference (+1.0)

Gym Hero - Score: 3.87
Because: genre match (+2.0); energy closeness (+0.87); acoustic preference (+1.0)

Silver Static - Score: 1.98
Because: energy closeness (+0.98); acoustic preference (+1.0)

Sunlit Harbor - Score: 1.96
Because: energy closeness (+0.96); acoustic preference (+1.0)


Adversarial profiles:

- Conflicting energy and mood
  Reason: High energy but sad mood can create tension in matching logic.
  Preferences: {'genre': 'pop', 'mood': 'sad', 'energy': 0.9, 'likes_acoustic': False}

- Extreme acoustic preference
  Reason: Strong acoustic preference may dominate softer tracks.
  Preferences: {'genre': 'indie', 'mood': 'chill', 'energy': 0.3, 'likes_acoustic': True}

- Unknown genre with clear energy target
  Reason: A missing genre should not prevent energy-based ranking.
  Preferences: {'genre': 'unknown', 'mood': 'happy', 'energy': 0.6, 'likes_acoustic': False}

- Noisy preference values
  Reason: Out-of-range energy values test whether the scorer clamps or misbehaves.
  Preferences: {'genre': 'rock', 'mood': 'angry', 'energy': 1.2, 'likes_acoustic': True}
```

---

## Experiments You Tried

I tested the recommender with a few different user profiles. I checked a normal profile with clear genre and mood preferences, and I also tested edge cases with conflicting preferences such as high energy and a sad mood. I looked at whether the explanations made sense and whether the top results felt reasonable for each profile.

---

## Limitations and Risks

This recommender only works on a small music catalog, so it may not generalize well to a larger library. It does not use listening history, lyrics, or cultural context, so it can miss important parts of a user’s taste. It may also over-focus on a few simple features such as genre and mood, which can create narrow or repetitive recommendations.

---

## Reflection

Read `model_card.md`:

[**Model Card**](model_card.md)

This project helped me understand how recommender systems turn simple features into predictions. I learned that even a small scoring rule can strongly shape what a user sees, and that bias can show up when the system rewards only a narrow set of patterns. It also made me think about how recommendation systems can feel helpful while still limiting a user’s exposure to new ideas.



