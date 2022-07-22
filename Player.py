import arcade
from Citizen import Citizen
from Constants import (MOVEMENT_SPEED, SCREEN_HEIGHT, SCREEN_WIDTH)

class Player(Citizen):
    TEXTURE_LEFT = 0
    TEXTURE_RIGHT = 1
    TEXTURE_ATTACK_LEFT = 2
    TEXTURE_ATTACK_RIGHT = 3

    def __init__(self, enemy_sprites):
        super().__init__("Images", "Hero.png")

        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.enemy_sprites = enemy_sprites
        self.enemy_distance_from_player = None

        # Setup the animation
        self.textures = []

        # Load texture pairs / directional
        texture = arcade.load_texture("Images/Hero.png", flipped_horizontally=False)
        self.textures.append(texture)
        texture = arcade.load_texture("Images/Hero.png", flipped_horizontally=True)
        self.textures.append(texture)

        # Load texture pairs / Combat
        texture = arcade.load_texture("Images/Hero-Attack.png", flipped_horizontally=False)
        self.textures.append(texture)
        texture = arcade.load_texture("Images/Hero-Attack.png", flipped_horizontally=True)
        self.textures.append(texture)
        # Default Texture
        self.texture = self.textures[self.TEXTURE_LEFT]

    def setup(self):
        pass

    def player_attack_direction(self):
        """ Attacks in the direction the player is facing"""
        if self.texture == self.textures[self.TEXTURE_RIGHT]:
            self.texture = self.textures[self.TEXTURE_ATTACK_RIGHT]
        elif self.texture == self.textures[self.TEXTURE_LEFT]:
            self.texture = self.textures[self.TEXTURE_ATTACK_LEFT]

    def player_post_attack_direction(self):
        """ Returns the player to its previously faced direction"""
        if self.texture == self.textures[self.TEXTURE_ATTACK_RIGHT]:
             self.texture = self.textures[self.TEXTURE_RIGHT]
        elif self.texture == self.textures[self.TEXTURE_ATTACK_LEFT]:
            self.texture = self.textures[self.TEXTURE_LEFT]

    def check_player_facing_enemy(self, enemy):
        """ Check if the plyer is facign the enemy before attack """
        if self.texture == self.textures[self.TEXTURE_ATTACK_RIGHT] and self.center_x < enemy.center_x:
            return True
        if self.texture == self.textures[self.TEXTURE_ATTACK_LEFT] and self.center_x > enemy.center_x:
            return True
        else:
            return False
            
    def attack(self):
        """ Method handles combat. """
        # Check initial direction of the player texture
        self.player_attack_direction()

        # Check player has hit enemy and remove enemy if dead
        for enemy in self.enemy_sprites:
            self.enemy_distance_from_player = (abs(self.center_x-enemy.center_x) 
                                            + abs(self.center_y-enemy.center_y))
            if self.check_player_facing_enemy(enemy):
                if self.enemy_distance_from_player < 75:
                    enemy.health -= 20
                    print(f"{enemy.name}'s health = {enemy.health}")
                    if enemy.health <= 0:
                        enemy.remove_from_sprite_lists()
        

    def update_player_speed(self):

        # Calculate speed based on the keys pressed
        self.change_x = 0
        self.change_y = 0

        if self.up_pressed and not self.down_pressed:
            self.change_y = MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.change_y = -MOVEMENT_SPEED
        if self.left_pressed and not self.right_pressed:
            self.change_x = -MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.change_x = MOVEMENT_SPEED
            

    def update(self, physics):
        """ Move the player """
        physics.update()
        if self.change_x < 0:
            self.texture = self.textures[self.TEXTURE_LEFT]
        elif self.change_x > 0:
            self.texture = self.textures[self.TEXTURE_RIGHT]

        # Check for out-of-bounds
        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        
        if key == arcade.key.W:
            self.up_pressed = True
            self.update_player_speed()
        elif key == arcade.key.S:
            self.down_pressed = True
            self.update_player_speed()
        elif key == arcade.key.A:
            self.left_pressed = True
            self.update_player_speed()
        elif key == arcade.key.D:
            self.right_pressed = True
            self.update_player_speed()
        if key == arcade.key.SPACE:
            self.attack()
            
    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.W:
            self.up_pressed = False
            self.update_player_speed()
        elif key == arcade.key.S:
            self.down_pressed = False
            self.update_player_speed()
        elif key == arcade.key.A:
            self.left_pressed = False
            self.update_player_speed()
        elif key == arcade.key.D:
            self.right_pressed = False
            self.update_player_speed()
        if key == arcade.key.SPACE:
            self.player_post_attack_direction()
            
        