from Entity import Entity
import random
import math

class Enemy(Entity):
    def __init__(self, name_folder, name_file):
        super().__init__(name_folder, name_file)

        self.health = 0

    def follow_target(self, target, speed):
        """ Follow the target of priority """
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Random chance to wander approx 5% chance to follow target per tick
        if random.randrange(100) <= 20:
            start_x = self.center_x
            start_y = self.center_y

            dest_x = target.center_x
            dest_y = target.center_y

            # Math to calculate movement angle
            x_diff = dest_x - start_x
            y_diff = dest_y - start_y
            angle = math.atan2(y_diff, x_diff)

            # Account for angle and vector
            self.change_x = math.cos(angle) * speed
            self.change_y = math.sin(angle) * speed