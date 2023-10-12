import random
from random import shuffle

from ruamel import yaml
from random import shuffle
from servant import Servant


class Deck:

    def __init__(self):
        self._deck = []

        with open("./servants.yml", "r") as file:
            servants = yaml.safe_load(file)

        for servant in servants:
            self._deck.append(Servant(name=servant["name"], short_desc=servant["short_desc"], long_desc=servant["long_desc"]))

    def shuffle(self):
        shuffle(self._deck)

    def random_card(self):
        return random.choice(self._deck)