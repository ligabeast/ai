import gym
import fh_ac_ai_gym

wumpus_env = gym.make('Wumpus-v0',disable_env_checker=True)
wumpus_env.reset()
wumpus_env.render()

while True:
    action = int(input("Action: "))
    wumpus_env.step(action)
    wumpus_env.render()