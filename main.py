# Imports Modules and Files
import arcade
from Brigand import Brigand
from Constants import (SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
from Player import Player
from Inn import Inn
from Thief import Thief

class MyGame(arcade.Window):
  
    def __init__(self, width, height, title):
        # Call the parent class initializer
        super().__init__(width, height, title)

        # Setup the scene
        self.scene = None

        # Set up the player info and sprite infor
        self.player_sprite = None
        self.inn_sprite = None
        self.thief_sprite = None
        self.brigand_sprite = None

        # Setup the physics engine
        self.physics_engine_player = None
        self.physics_engine_enemy = None
        # Set number of Enemies
        self.num_enemy = 1
        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variables. """
        # Setup the scene // Will replce the Sprite Lists
        self.scene = arcade.Scene()
        self.scene.add_sprite_list("Player")
        self.scene.add_sprite_list("Buildings", use_spatial_hash=True)
        self.scene.add_sprite_list("Enemies")
        self.scene.add_sprite_list("Citizens")

        #Setup sprite for Inn / Temp
        self.inn_sprite = Inn()
        self.inn_sprite.center_x = 125
        self.inn_sprite.center_y = 125
        self.scene.add_sprite("Buildings", self.inn_sprite)

        # Setup Enemies
        for enemy in range(self.num_enemy):
            self.thief_sprite = Thief()
            self.thief_sprite.center_x = SCREEN_WIDTH/2
            self.thief_sprite.center_y = 100 + (100*enemy)
            self.scene.add_sprite("Enemies", self.thief_sprite)
        for enemy in range(self.num_enemy):
            self.brigand_sprite = Brigand()
            self.brigand_sprite.center_x = 100 + 100*enemy
            self.brigand_sprite.center_y = SCREEN_HEIGHT/2
            self.scene.add_sprite("Enemies", self.brigand_sprite)

        # Set up the player
        self.player_sprite = Player(self.scene.get_sprite_list("Enemies"))
        self.player_sprite.center_x = 250
        self.player_sprite.center_y = 250
        self.scene.add_sprite("Player", self.player_sprite)

        self.physics_engine_player = arcade.PhysicsEngineSimple(self.player_sprite, 
        self.scene.get_sprite_list("Buildings"))

    def on_draw(self):
        """ Render the screen. """
        # Clear the screen
        self.clear()
        self.scene.draw()

    def on_update(self, delta_time):
        """ Movement and game logic """
        self.player_sprite.update(self.physics_engine_player)
        for enemy in self.scene.get_sprite_list("Enemies"):
            enemy.update(self.player_sprite, self.inn_sprite)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        self.player_sprite.on_key_press(key, modifiers)

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        self.player_sprite.on_key_release(key, modifiers)

       
def main():
    """ Main function """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()