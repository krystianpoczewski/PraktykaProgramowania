class Player:
    def __init__(self, player_name: str, score: int = 0):
        self.player_name = player_name
        self.score = score


class TennisGame1:
    def __init__(self, player1_name, player2_name):
        self.p1 = Player(player1_name)
        self.p2 = Player(player2_name)

    def won_point(self, player_name):
        if player_name == self.p1.player_name:
            self.p1.score += 1
        else:
            self.p2.score += 1
    def win_or_advantage(self):
        p_difference = self.p1.score - self.p2.score
        if p_difference == 1:
            return f"Advantage {self.p1.player_name}"
        elif p_difference == -1:
            return f"Advantage {self.p2.player_name}"
        elif p_difference >= 2:
            return f"Win for {self.p1.player_name}"
        else:
            return f"Win for {self.p2.player_name}"

    def deuce_or_all(self, score_labels):
        if self.p1.score >= 3:
            return "Deuce"
        return f"{score_labels[self.p1.score]}-All"

    def score(self):
        score_labels = ["Love", "Fifteen", "Thirty", "Forty"]
        if self.p1.score == self.p2.score:
            return self.deuce_or_all(score_labels)
        elif self.p1.score >= 4 or self.p2.score >= 4:
            return self.win_or_advantage()
        else:
            return f"{score_labels[self.p1.score]}-{score_labels[self.p2.score]}"
