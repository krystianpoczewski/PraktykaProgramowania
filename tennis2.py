class Player:
    def __init__(self, player_name: str, points: int = 0):
        self.player_name = player_name
        self.points = points
    def score(self):
        self.points += 1

class TennisGame2:
    def __init__(self, player1_name, player2_name):
        self.p1 = Player(player1_name)
        self.p2 = Player(player2_name)

    def won_point(self, player_name):
        if player_name == self.p1.player_name:
            self.p1.score()
        else:
            self.p2.score()

    def deuce_or_all(self, score_labels):
        if self.p1.points >= 3:
            return "Deuce"
        return f"{score_labels[self.p1.points]}-All"

    def score(self):
        result = ""
        score_labels = ["Love", "Fifteen", "Thirty", "Forty"]
        if self.p1.points == self.p2.points:
            result = self.deuce_or_all(score_labels)

        if 4 > self.p1.points > 0 == self.p2.points or 4 > self.p2.points > 0 == self.p1.points:
            result = score_labels[self.p1.points] + "-" + score_labels[self.p2.points]

        if 0 < self.p2.points < self.p1.points < 4 or 0 < self.p1.points < self.p2.points < 4:
            result = score_labels[self.p1.points] + "-" + score_labels[self.p2.points]

        if self.p1.points > self.p2.points >= 3:
            result = f"Advantage {self.p1.player_name}"

        if self.p2.points > self.p1.points >= 3:
            result = f"Advantage {self.p2.player_name}"

        if (
            self.p1.points >= 4
            and self.p2.points >= 0
            and (self.p1.points - self.p2.points) >= 2
        ):
            result = f"Win for {self.p1.player_name}"
        if (
            self.p2.points >= 4
            and self.p1.points >= 0
            and (self.p2.points - self.p1.points) >= 2
        ):
            result = f"Win for {self.p2.player_name}"
        return result

    def set_p1_score(self, number):
        for i in range(number):
            self.p1.score()

    def set_p2_score(self, number):
        for i in range(number):
            self.p2.score()
