# Imports
from Constants import SPRITE_SCALING
import arcade

class Entity(arcade.Sprite):
    ''' Class used to access images for sprites'''
    def __init__(self, name_folder, name_file):
        super().__init__()

        self.scale = SPRITE_SCALING
        arcade.Sprite._set_scale = SPRITE_SCALING

        # Pathway for entity - 
        main_path = f"{name_folder}/{name_file}"
        self.texture = arcade.load_texture(main_path)