class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def score_point(self):
        self.score += 1