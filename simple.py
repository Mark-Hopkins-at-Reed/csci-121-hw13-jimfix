from config import GameConfiguration
from breakout import BreakoutGame
from json import load

config = GameConfiguration()
breakout = BreakoutGame(config)
breakout.start()