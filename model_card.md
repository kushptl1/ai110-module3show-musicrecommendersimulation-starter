# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

This system is called VibeMatch 1.0.

---

## 2. Intended Use

This recommender is meant for classroom use and simple music taste demos. It suggests songs based on a user’s favorite genre, mood, energy level, and acoustic preference. It assumes that users want songs that match their stated taste fairly closely.

---

## 3. How the Model Works

The model looks at a song’s genre, mood, energy, and acousticness. It also looks at the user’s preferences for those same areas. Songs get points when they match the user’s genre and mood. They also get points when their energy level is close to the target energy. If the user likes acoustic songs, the model gives extra credit to songs with high acousticness. The system is simple, but it gives a clear explanation for each recommendation.

---

## 4. Data

The dataset has 20 songs. It includes a mix of pop, lofi, rock, indie, jazz, electronic, and other genres. The moods range from happy and chill to intense and rebellious. The catalog is small, so it does not cover every style or every kind of listener.

---

## 5. Strengths

The model works well for simple, clear preferences. It does a good job when a user has one main genre, one main mood, and a clear energy target. It also gives useful explanations, so it is easy to see why a song was recommended.

---

## 6. Limitations and Bias

This system can be biased because it relies on a few simple features. It may overvalue exact genre and mood matches and ignore more nuanced tastes. It can also struggle with users who have conflicting preferences, like wanting both high energy and a sad mood. The small dataset may also make some genres and moods feel underrepresented.

---

## 7. Evaluation

I tested the recommender with a few example user profiles, including a normal profile and several edge cases. I checked whether the top recommendations made sense and whether the explanations were clear. I also tested profiles with unusual or conflicting preferences to see where the system became less reliable.

---

## 8. Future Work

I would like to add more features, such as tempo, danceability, or user history. I would also like to make the scoring less rigid so it can handle mixed tastes better. A more diverse set of recommendations would also help reduce filter bubbles.

---

## 9. Personal Reflection

This project showed me how recommender systems can seem simple but still have important bias and fairness issues. I learned that small scoring choices can strongly shape what a user sees. It also made me think about how music apps can accidentally narrow a person’s experience if they only reward familiar patterns.
