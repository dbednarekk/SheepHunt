import argparse
import configparser
import csv
import json
import logging


def positions_json(sheep, wolf, runds, dir='pos.json'):
    x = {
        "round_no": runds,
        "wolf_pos": str(wolf.x) + ", " + str(wolf.y)
    }
    pos = []
    for i in sheep:
        pos.append(str(i.x) + ", " + str(i.y))

    x['sheep_pos'] = pos
    if runds == 1:
        f = open(dir, "w")
    else:
        f = open(dir, "a")
    f.write(json.dumps(x, indent=4, sort_keys=True))
    f.close()
    logging.debug('positions_json()' + str(sheep) + str(wolf) + str(runds) + str(dir))


def alive_csv(runds, sheep_count, dir='alive.csv'):
    if runds == 1:
        with open(dir, mode='w', newline='') as csv_file:
            fieldnames = ['round', 'alive']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'round': runds, 'alive': sheep_count})
    else:
        with open(dir, mode='a', newline='') as csv_file:
            fieldnames = ['round', 'alive']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writerow({'round': runds, 'alive': sheep_count})
    logging.debug('alive_csv()' + str(sheep_count) + str(runds) + str(dir))


def python_Arg():
    parser = argparse.ArgumentParser('Simulation of sheeps beeing chased by wolf in a field ')
    parser.add_argument('-c', '--config', metavar='FILE', help='additional config file', dest='config')
    parser.add_argument('-d', '--dir', metavar='DIR', help='subcatalog, where the logs file are to be stored',
                        dest='dir')
    parser.add_argument('-l', '--log', metavar='LEVEL', help='choose the level of writing events', dest='log')
    parser.add_argument('-r', '--rounds', metavar='NUM', type=int, choices=range(0, 1000), help='Number of rounds',
                        dest='rounds')
    parser.add_argument('-s', '--sheep', metavar='NUM', type=int, choices=range(0, 1000), help='Number of sheeps',
                        dest='sheeps')
    parser.add_argument('-w', '--wait', help="wait for input after each round", action='store_true')
    return parser.parse_args()


def config(file):
    config = configparser.ConfigParser()
    config.read(file)
    pos_limit = config.get('Terrain', 'InitPosLimit')
    sheep_move = config.get('Movement', 'SheepMoveDist')
    wolf_move = config.get('Movement', 'WolfMoveDist')
    if float(pos_limit) <= 0 or float(sheep_move) <= 0 or float(wolf_move) <= 0:
        raise ValueError("Wartości w pliku muszą być większe od zera")
    logging.error('Wartości w pliku muszą być większe od zera')
    logging.debug('config()' + str(file) + 'return: ' + pos_limit + sheep_move + wolf_move)
    return float(pos_limit), float(sheep_move), float(wolf_move)
