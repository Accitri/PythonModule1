


def pointAssigner (teamA, teamB):
    win = 2
    draw = 1
    loss = 0
    pointsA = input("How many points does", teamA, "have? ")
    pointsB = input("How many points does", teamB, "have? ")
    scoreA = input("How many goals did", teamA, "score: ")
    scoreB = input("How many goals did", teamA, "score: ")
    if (scoreA > scoreB):
        pointsA = pointsA + win
        pointsB = pointsB + loss
        print(teamA, "won", teamB, "lost")
    if (scoreA == scoreB):
        pointsA = pointsA + draw
        pointsB = pointsB + draw
        print(teamA, "and", teamB, "drew")
    if (scoreA < scoreB):
        pointsA = pointsA + loss
        pointsB = pointsB + win
        print(teamB, "won", teamA, "lost")
    return scoreA, scoreB

pointAssigner("a", "b")






