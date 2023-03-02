# This file is for strategy

from util.objects import *
from util.routines import *


class Bot(GoslingAgent):
    # This function runs every in-game tick (every time the game updates anything)
    def run(self):
        # the line below tells the bot what it's trying to do
        speed = 1000
        self.set_intent(drive(speed))
        self.set_intent(jumper())
