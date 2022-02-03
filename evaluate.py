import sys
sys.path.insert(0, "")
import argparse
import os
import random
import numpy as np
import habitat
from habitat.core.challenge import Challenge

class RandomWalker(habitat.Agent):
    def __init__(self, task_config: habitat.Config):
        self._POSSIBLE_ACTIONS = task_config.TASK.POSSIBLE_ACTIONS

    def reset(self):
        pass

    def act(self, observations):
        return {"action": np.random.choice(self._POSSIBLE_ACTIONS)}

def main():
    
    evaluation = os.environ["AGENT_EVALUATION_TYPE"]
    config_paths = os.environ["CHALLENGE_CONFIG_FILE"]
    config = habitat.get_config(config_paths)
    agent = RandomWalker(task_config=config)
    
    if evaluation == "local":
        challenge = habitat.Challenge(eval_remote=False)
    else:
        challenge = habitat.Challenge(eval_remote=True)

    challenge.submit(agent)
    
if __name__ == "__main__":
    main()
