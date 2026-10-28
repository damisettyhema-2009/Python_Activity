teams = ["A", "B", "C", "D"]

matches = [
    ("A", "B", 2, 1),
    ("C", "D", 1, 1),
    ("A", "C", 0, 2),
    ("B", "D", 3, 0)
]

points = {team: 0 for team in teams}
gd = {team: 0 for team in teams}

for t1, t2, g1, g2 in matches:

    gd[t1] += g1 - g2
    gd[t2] += g2 - g1

    if g1 > g2:
        points[t1] += 3
    elif g2 > g1:
        points[t2] += 3
    else:
        points[t1] += 1
        points[t2] += 1

ranking = sorted(
    teams,
    key=lambda t: (points[t], gd[t]),
    reverse=True
)

print("Tournament Ranking:")

for rank, team in enumerate(ranking, 1):
    print(
        rank,
        team,
        "Points:", points[team],
        "Goal Difference:", gd[team]
    )