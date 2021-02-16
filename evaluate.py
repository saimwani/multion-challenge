import argparse
import os
import random
# import sys
# sys.path.insert(0, "")
import numpy as np
import habitat
from habitat.core.challenge import Challenge

class RandomWalker(habitat.Agent):
    def __init__(self):
        self._POSSIBLE_ACTIONS = np.array([0,1,2,3])

    def reset(self):
        pass

    def act(self, observations):
        return {"action": np.random.choice(self._POSSIBLE_ACTIONS)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--phase", type=str, required=False, choices=["dev", "standard", "challenge"]
    )
    args = parser.parse_args()
    phase = args.phase
    agent = RandomWalker()
    challenge = Challenge(phase = phase)
    challenge.submit(agent)


if __name__ == "__main__":
    main()