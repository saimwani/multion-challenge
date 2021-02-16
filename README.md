# MultiON Challenge 2021

This repository contains submission guidelines and starter code for the MultiON Challenge 2021. For challenge overview, check [challenge webpage](http://aspis.cmpt.sfu.ca/projects/multion/). To participate, visit EvalAI challenge page.

## Task

In MultiON, an agent is tasked with navigating to a sequence of objects inserted into a realistic 3D environment. The challenge uses [AI Habitat](https://aihabitat.org/) for simulation and uses scenes from Matterport3D dataset. The target objects are randomly sampled from a set of 8 cylinders with identical shapes but different colors. 

In each episode, the agent is initialized at a random starting position and orientation in an unseen environment and provided a 
list of target objects randomly sampled (without replacement) from the set of 8 objects. The agent must navigate to each object in the list, in order, and call a FOUND action to indicate its discovery. The agent has access to an RGB-D camera and a (noiseless) GPS+Compass sensor. GPS+Compass sensor provides the agent's current location and orientation information relative to the start of the episode.

## Dataset

We use [Matterport3D scenes](https://niessner.github.io/Matterport/) for the challenge with the standard train/val/test splits. MultiON dataset `train` split contains 50,000 episodes per scene for the 3-ON task. The `mini-val` split consists of 25 episodes. Both `train` and `mini-val` splits are publicly available. `test-standard` and `test-challenge` splits are not made public, and consist of 1000 episodes each. 

For each m-ON dataset the train split consists of 50,000 episodes per scene, and 223 the validation and test splits each contain 12,500 episodes per scene.

## Evaluation

We extend the evaluation protocol of [ObjectNav](https://arxiv.org/abs/2006.13171). We use two metrics to evaluate agent performance:  
**Progress**: Fraction of object goals that are successfully FOUND. This effectively measures if the agent was able to navigate to goals.  
**PPL**: Overall path length weighted by progress. This effectively measures the path efficiency of the agent. Formally, 
**Formula image here**

## Participation Instructions

Register your team on the EvalAI challenge page. For participating in the challenge, you would upload docker containers with your agent (see details above). Before submission, please evaluate you model locally on the `mini-val` split and make sure you get the same performance metrics in remote evaluation. 




## Citation

>Saim Wani*, Shivansh Patel*, Unnat Jain*, Angel X. Chang, Manolis Savva, 2020. MultiON: Benchmarking Semantic Map Memory using Multi-Object Navigation in Neural Information Processing Systems (NeurIPS). [PDF](https://shivanshpatel35.github.io/multi-ON/resources/MultiON.pdf)

## Bibtex
```
  @inproceedings{wani2020multion,
  title={Multi-ON: Benchmarking Semantic Map Memory using Multi-Object Navigation},
  author={Saim Wani and Shivansh Patel and Unnat Jain and Angel X. Chang and Manolis Savva},
  booktitle={Neural Information Processing Systems (NeurIPS)},
  year={2020},
}
```

## Acknowledgements

We thank the habitat team for building the habitat framework. We also thank [EvalAI](https://eval.ai/) team who helped us host the challenge. This work would not be possible without the [Matterport3D dataset](https://niessner.github.io/Matterport/).



