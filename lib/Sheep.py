import random
import logging


class Sheep:
    def __init__(self, x, y, id):
        self.x = x
        self.y = y
        self.id = id
        logging.info('pozycja początkowa sheep id: ' + str(id) + 'x: ' + str(x) + 'y: ' + str(y))

    def move(self, sheep_move_dist):
        direction = random.randint(1, 4)
        if direction == 1:
            self.y += sheep_move_dist
        elif direction == 2:
            self.x += sheep_move_dist
        elif direction == 3:
            self.y -= sheep_move_dist
        else:
            self.x -= sheep_move_dist
        logging.debug('sheep move():' + str(sheep_move_dist))
        logging.info('pozycja  sheep id: ' + str(self.id) + 'x: ' + str(self.x) + 'y: ' + str(self.y))
