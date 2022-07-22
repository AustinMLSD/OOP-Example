from Enemy import Enemy
import random

class Thief(Enemy):
    """ 
    Enemy with low health high DPS will priotitize targeting the Inn or attackign the player
    Will not target citizens Wants to steal money or weapons from the Inn
    """
    THIEF_SPEED = random.choice([2, 2.5, 3, 3.5, 4, 4.5])
    def __init__(self):
        super().__init__("Images", "Thief-1.png")

        self.name = "Thief"
        self.health = 25

    def prioritize_target(self, player, building):
        #dist_player = abs(self.center_x-player.center_x) + abs(self.center_y-player.center_y)
        dist_inn = abs(self.center_x-building.center_x) + abs(self.center_y-building.center_y)
        #dist_target = abs(abs(dist_player) - abs(dist_inn))
        if dist_inn <= 200:
            self.follow_target(building, self.THIEF_SPEED)
        else:
            self.follow_target(player, self.THIEF_SPEED)

    def update(self, player, building):
        self.prioritize_target(player, building)