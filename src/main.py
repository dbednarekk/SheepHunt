import logging
import os
import random
from zad2.lib.Logs import *
from zad2.lib.Sheep import Sheep
from zad2.lib.Wolf import Wolf

arguments = python_Arg()
if arguments.log:
    if arguments.log == "DEBUG":
        lvl = logging.DEBUG
    if arguments.log == "INFO":
        lvl = logging.INFO
    if arguments.log == "WARNING":
        lvl = logging.WARNING
    if arguments.log == "ERROR":
        lvl = logging.ERROR
    if arguments.log == "CRITICAL":
        lvl = logging.CRITICAL
    logging.basicConfig(filename='chase.log', level=lvl)
    logging.debug("start")
if arguments.rounds:
    runds = arguments.rounds
else:
    runds = 50
if arguments.sheeps:
    sheeps_number = arguments.sheeps
else:
    sheeps_number = 15
if arguments.dir:
    if not os.path.exists(os.getcwd() + "\\" + arguments.dir):
        os.makedirs(os.getcwd() + "\\" + arguments.dir)
if arguments.config:
    init_pos_limit, sheep_move_dist, wolf_move_dist = config(arguments.config)
else:
    init_pos_limit = 10.0
    sheep_move_dist = 0.5
    wolf_move_dist = 1.0

sheeps = []
for i in range(sheeps_number):
    sheeps.append(
        Sheep(random.uniform(-init_pos_limit, init_pos_limit), random.uniform(-init_pos_limit, init_pos_limit), i))
wolf = Wolf(0.0, 0.0)
for rund in range(1, runds + 1):
    if len(sheeps) == 0:
        break
    for sheep in sheeps:
        sheep.move(sheep_move_dist)
    wolf.move(sheeps, wolf_move_dist)
    print('Tura:', rund, 'Pozycja Wilka: %.3f %.3f' % (wolf.x, wolf.y), 'Liczba żywych owiec:', len(sheeps))
    if arguments.wait:
        input('Wciśnij dowolny przycisk aby kontynuować')
    if arguments.dir:
        positions_json(sheeps, wolf, rund, os.getcwd() + "\\" + arguments.dir + "\\" + "pos.json")
        alive_csv(rund, len(sheeps), os.getcwd() + "\\" + arguments.dir + "\\" + "alive.csv")
    else:
        positions_json(sheeps, wolf, rund)
        alive_csv(rund, len(sheeps))
