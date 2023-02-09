from gym.envs.registration import register

register(
    id='ant-hwkoffrl-v0',
    entry_point='hwkoffrl.envs.ant:AntEnv',
    max_episode_steps=1000,
)
from hwkoffrl.envs.ant.ant import AntEnv
