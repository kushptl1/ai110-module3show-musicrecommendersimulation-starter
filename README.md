# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

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

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



