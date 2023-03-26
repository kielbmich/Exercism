class Alien:
    total_aliens_created = 0

    def __init__(self, x_coord, y_coord):
        self.x_coordinate = x_coord
        self.y_coordinate = y_coord
        self.health = 3
        Alien.total_aliens_created += 1

    def hit(self):
        if self.health > 1:
            self.health -= 1
        else:
            self.health = 0

    def is_alive(self):
        return self.health > 0

    def teleport(self, new_x, new_y):
        self.x_coordinate = new_x
        self.y_coordinate = new_y

    def collision_detection(self, other_object):
        pass

def new_aliens_collection(self):
    return [Alien(coordinates[0], coordinates[1]) for coordinates in self]
