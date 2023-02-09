from gym.envs.registration import register

register(
    id='reacher-hwkoffrl-v0',
    entry_point='hwkoffrl.envs.reacher:Reacher7DOFEnv',
    max_episode_steps=500,
)
from hwkoffrl.envs.reacher.reacher_env import Reacher7DOFEnv
