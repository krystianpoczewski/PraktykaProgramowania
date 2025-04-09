class Player:
    def __init__(self, player_name: str, points: int = 0):
        self.player_name = player_name
        self.points = points
    def score(self):
        self.points += 1

class TennisGame3:
    def __init__(self, player1_name, player2_name):
        self.p1 = Player(player1_name)
        self.p2 = Player(player2_name)

    def won_point(self, n):
        if n == self.p1.player_name:
            self.p1.score()
        else:
            self.p2.score()

    def win_advantage_or_deuce(self):
        if self.p1.points == self.p2.points:
            return "Deuce"
        s=""
        if self.p1.points > self.p2.points:
            s = self.p1.player_name
        else:
            s = self.p2.player_name
        return (
            "Advantage " + s
            if ((self.p1.points - self.p2.points) * (self.p1.points - self.p2.points) == 1)
            else "Win for " + s
        )

    def all_or_normal(self):
        score_labels = ["Love", "Fifteen", "Thirty", "Forty"]
        message = score_labels[self.p1.points]
        if self.p1.points == self.p2.points:
            message += "-All"
        else:
            message += "-" + score_labels[self.p2.points]
        return message

    def score(self):
        if (self.p1.points < 4 and self.p2.points < 4) and (self.p1.points + self.p2.points < 6):
            return self.all_or_normal()
        else:
            return self.win_advantage_or_deuce()


