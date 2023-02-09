from gym.envs.registration import register

register(
    id='obstacles-hwkoffrl-v0',
    entry_point='hwkoffrl.envs.obstacles:Obstacles',
    max_episode_steps=500,
)
from hwkoffrl.envs.obstacles.obstacles_env import Obstacles
