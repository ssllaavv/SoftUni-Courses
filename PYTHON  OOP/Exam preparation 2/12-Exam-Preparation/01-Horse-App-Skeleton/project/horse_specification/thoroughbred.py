from project.horse_specification.horse import Horse


class Thoroughbred(Horse):

    TRAINING_SPEED_INCREASE = 3
    MAX_SPEEED = 140

    def train(self):
        self.speed += 3
        if self.speed > self.MAX_SPEEED:
            self.speed = self.MAX_SPEEED

