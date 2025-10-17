import gym
import numpy as np
import yaml
from argparse import Namespace
from policy.policy import policy
#import sys
#import os
#sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..', 'main'))) 
#from policy.policy import policy

env=gym.make("drp_env:drp-2agent_map_3x3-v2", state_repre_flag = "onehot_fov", task_flag = True)

n_obs=env.reset()
#print("action_space", env.action_space)
#print("observation_space", env.observation_space)

#print("obs", env.start_ori_array, env.goal_array)

for _ in range(50):
    env.render()
    input()

    #actions=tuple(map(int, input().split()))
    #task = tuple(map(int, input().split()))
    actions, task = policy(n_obs, env)
    joint_action = {"pass": actions, "task": task}
    n_obs, reward, done, info = env.step(joint_action)

#"""