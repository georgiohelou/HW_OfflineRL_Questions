from gym.envs.registration import register

register(
    id='cheetah-hwkoffrl-v0',
    entry_point='hwkoffrl.envs.cheetah:HalfCheetahEnv',
    max_episode_steps=1000,
)
from hwkoffrl.envs.cheetah.cheetah import HalfCheetahEnv
