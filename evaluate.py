import sys
sys.path.insert(0, "")
import argparse
import os
import random
import numpy as np
import habitat
from habitat.core.challenge import Challenge

class RandomWalker(habitat.Agent):
    def __init__(self):
        self._POSSIBLE_ACTIONS = np.array([0,1,2,3])

    def reset(self):
        pass

    def act(self, observations, not_done_masks):
        return [np.random.choice(self._POSSIBLE_ACTIONS) for i in range(len(observations))]

def main():
    agent = RandomWalker()
    challenge = Challenge()
    challenge.submit(agent)
if __name__ == "__main__":
    main()
