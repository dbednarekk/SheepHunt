import math
import logging


def calc_nearest_sheep(sheeps, wolf):
    nearest = math.sqrt(((sheeps[0].x - wolf.x) ** 2) + ((sheeps[0].y - wolf.y) ** 2))
    nearest_sheep = sheeps[0]
    for sheep in sheeps:
        calc = math.sqrt(((sheep.x - wolf.x) ** 2) + ((sheep.y - wolf.y) ** 2))
        if calc < nearest:
            nearest = calc
            nearest_sheep = sheep
    logging.debug('calc_nearest_sheep():' + str(sheeps) + str(wolf) + 'return: ' + str(nearest_sheep) + str(nearest))
    return nearest_sheep, nearest


class Wolf:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        logging.info('pozycja początkowa wilka 0.0,0.0')

    def move(self, sheeps, wolf_move_distance):
        nearest_sheep, nearest = calc_nearest_sheep(sheeps, self)
        self.x += wolf_move_distance * ((nearest_sheep.x - self.x) / nearest)
        self.y += wolf_move_distance * ((nearest_sheep.y - self.y) / nearest)
        if nearest <= wolf_move_distance:
            out = [idx for idx, element in enumerate(sheeps) if element.id == nearest_sheep.id]
            del sheeps[out[0]]
            print("Pożarta została owca od id: ", nearest_sheep.id)
            logging.info("Pożarta została owca od id: " + str(nearest_sheep.id))
        logging.debug('wolf move():' + str(sheeps) + str(wolf_move_distance))
        logging.info('pozycja wilka: ' + 'x: ' + str(self.x) + 'y: ' + str(self.y))
