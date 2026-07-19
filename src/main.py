"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

try:
    from recommender import load_songs, recommend_songs, build_adversarial_profiles
except ImportError:
    from src.recommender import load_songs, recommend_songs, build_adversarial_profiles


def format_recommendation_table(recommendations):
    """Render top recommendations as a simple ASCII table with reasons."""
    headers = ["Rank", "Song", "Score", "Reasons"]
    rows = []
    for index, (song, score, explanation) in enumerate(recommendations, start=1):
        rows.append([
            str(index),
            song["title"],
            f"{score:.2f}",
            explanation,
        ])

    widths = []
    for column_index in range(len(headers)):
        values = [headers[column_index]] + [row[column_index] for row in rows]
        widths.append(max(len(str(value)) for value in values))

    # Give the reasons column extra space so it can display fully.
    widths[3] = max(widths[3], 80)

    border = "+" + "+".join("-" * (width + 2) for width in widths) + "+"
    header_row = "| " + " | ".join(headers[index].ljust(widths[index]) for index in range(len(headers))) + " |"
    separator = border

    lines = [separator, header_row, separator]
    for row in rows:
        lines.append("| " + " | ".join(str(row[index]).ljust(widths[index]) for index in range(len(headers))) + " |")
    lines.append(separator)
    return "\n".join(lines)


def main() -> None:
    songs = load_songs("data/songs.csv")

    # Starter example profile
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop recommendations:\n")
    print(format_recommendation_table(recommendations))

    print("\nAdversarial profiles:\n")
    for profile in build_adversarial_profiles():
        print(f"- {profile['name']}")
        print(f"  Reason: {profile['reason']}")
        print(f"  Preferences: {profile['user_prefs']}")
        print()


if __name__ == "__main__":
    main()
