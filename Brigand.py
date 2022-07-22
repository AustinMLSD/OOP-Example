from Enemy import Enemy
import random

class Brigand(Enemy):
    """
    Enmy with high health will prioritize the player and citizens. Will attack the inn will nto steal.
    """
    BRIGAND_SPEED = random.choice([1, 1.5, 2, 2.5])
    def __init__(self):
        super().__init__("Images", "Brigand-1.png")

        self.name = "Brigand"
        self.health = 100

    def prioritize_target(self, player, building):
        dist_player = abs(self.center_x-player.center_x) + abs(self.center_y-player.center_y)
        #dist_inn = abs(self.center_x-building.center_x) + abs(self.center_y-building.center_y)
        if dist_player <= 400:
            self.follow_target(player, self.BRIGAND_SPEED)
        else:
            self.follow_target(building, self.BRIGAND_SPEED)

    def update(self, player, building):
        self.prioritize_target(player, building)