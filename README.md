# MultiON Challenge 2021

This repository contains submission guidelines and starter code for the MultiON Challenge 2021. For challenge overview, check [challenge webpage](http://aspis.cmpt.sfu.ca/projects/multion/). To participate, visit EvalAI challenge page.

## Task

In MultiON, an agent is tasked with navigating to a sequence of objects inserted into a realistic 3D environment. The challenge uses [AI Habitat](https://aihabitat.org/) for simulation and uses scenes from Matterport3D dataset. The target objects are randomly sampled from a set of 8 cylinders with identical shapes but different colors. 

In each episode, the agent is initialized at a random starting position and orientation in an unseen environment and provided a 
list of target objects randomly sampled (without replacement) from the set of 8 objects. The agent must navigate to each object in the list, in order, and call a FOUND action to indicate its discovery. The agent has access to an RGB-D camera and a (noiseless) GPS+Compass sensor. GPS+Compass sensor provides the agent's current location and orientation information relative to the start of the episode. The episode terminates when an agent finds all the objects in the current episode or when it calls an incorrect FOUND action or if the agent exhausts its given time budget.


## Dataset
We use [Matterport3D scenes](https://niessner.github.io/Matterport/) for the challenge. We follow the standard train/val/test split as recommended by [Anderson *et al.*](https://arxiv.org/abs/1807.06757) Each episode contains three sequential targets. For the challenge, we focus on the task of 3-ON or 3 object navigation.

## Evaluation
We extend the evaluation protocol of [ObjectNav](https://arxiv.org/abs/2006.13171). We use two metrics to evaluate agent performance:  
**Progress**: Fraction of object goals that are successfully FOUND. This effectively measures if the agent was able to navigate to goals.  
**PPL**: Overall path length weighted by progress. This effectively measures the path efficiency of the agent. Formally, 

![PPL Formula](imgs/PPL.png "PPL Formula")

## Submission Guidelines 

Participate in the contest by registering on the EvalAI challenge page and creating a team. Participants will upload docker containers with their agents that are evaluated on an AWS GPU-enabled instance. Before pushing the submissions for remote evaluation, participants should test the submission docker locally to ensure it is working. Instructions for training, local evaluation, and online submission are provided below.



To participate in the challenge, visit our [EvalAI](https://staging.eval.ai/web/challenges/challenge-page/474/overview) page. Participants need to upload docker containers with their agents using EvalAI. Before making your submission, you should run your container locally on the mini-val data split to ensure the performance metrics match with those of remote evaluation. We provide a base docker image and participants only need to edit `evaluate.py` file which implements the navigation agent. Instructions for building your docker container are provided below.


1. Install [nvidia-docker v2](https://github.com/NVIDIA/nvidia-docker) by following instructions given [here](https://github.com/nvidia/nvidia-docker/wiki/Installation-(version-2.0)).

2. Clone this repository: 
```
git clone https://github.com/saimwani/multion-challenge.git
cd multion-challenge
```
3. Edit `evaluate.py` to implement your agent. Currently, it uses an agent taking random actions.

4. Make changes in the the provided Dockerfile if your agent has additional dependencies. They should be installed inside a conda environment named `habitat` that already exists in our docker. 

5. Build the docker container (this may need `sudo` priviliges):
```
docker build -t multi_on .
```

6. Test the docker container locally. `${MULTION_DATA_PATH}` should contain the `data` folder such that `data/scene_datasets/mp3d` folder has the Matterport3D scenes and `data` contains the `3_ON_minival` folder provided in this repo.  
```
sudo docker run -v ${MULTION_DATA_PATH}/data:/multion-chal-starter/data --runtime=nvidia multi_on:latest
```

7. Install EvalAI and submit your docker image. See detailed instructions [here](https://cli.eval.ai/).

```
# Install EvalAI Command Line Interface
pip install "evalai>=1.3.5"

# Set EvalAI account token
evalai set_token <your EvalAI participant token>

# Push docker image to EvalAI docker registry
evalai push multi_on:latest --phase <phase-name>
```

## Citing MultiON Challenge 2021
If you use the multiON framework, please consider citing the following paper:
```
@inproceedings{wani2020multion,
    title       =   {Multi-ON: Benchmarking Semantic Map Memory using Multi-Object Navigation},
    author      =   {Saim Wani and Shivansh Patel and Unnat Jain and Angel X. Chang and Manolis Savva},
    booktitle   =   {Neural Information Processing Systems (NeurIPS)},
    year        =   {2020},
    }
```

## Acknowledgements
We thank the [habitat](https://aihabitat.org/) team for building the habitat framework. We also thank [EvalAI](https://eval.ai/) team who helped us host the challenge. This work would not be possible without the [Matterport3D dataset](https://niessner.github.io/Matterport/).

