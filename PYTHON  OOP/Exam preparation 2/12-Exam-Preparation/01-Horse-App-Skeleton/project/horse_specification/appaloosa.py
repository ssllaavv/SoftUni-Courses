from project.horse_specification.horse import Horse


class Appaloosa(Horse):

    TRAINING_SPEED_INCREASE = 2
    MAX_SPEEED = 120

    def train(self):
        self.speed += 2
        if self.speed > self.MAX_SPEEED:
            self.speed = self.MAX_SPEEED

