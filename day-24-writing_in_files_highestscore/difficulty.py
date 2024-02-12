from random import choice

REFRESH_RATE = {'super_easy': 0.5,
                'easy': 0.1,
                'medium': 0.05,
                'hard': 0.03,
                'crazy': 0.015
                }


class Difficulty():

    def __init__(self):
        self.game_speed = None

    def set_difficulty(self, level):
        if level == "random":
            refresh_rate_values = list(REFRESH_RATE.values())
            self.game_speed = choice(refresh_rate_values)
        else:
            self.game_speed = REFRESH_RATE[level]


