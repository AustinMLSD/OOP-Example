from Entity import Entity

class Structures(Entity):
    def __init__(self, name_folder, name_file):
        super().__init__(name_folder, name_file)

        self.health = 0