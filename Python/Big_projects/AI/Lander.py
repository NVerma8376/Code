import gymnasium as gym
import threading

env = gym.make("LunarLander-v2", render_mode="human")
observation, info = env.reset(seed=42)
def env1():
    for _ in range(1000):
        action = env.action_space.sample()  # this is where you would insert your policy
        observation, reward, terminated, truncated, info = env.step(action)
        if terminated or truncated:
            observation, info = env.reset()
            
def env2():
    for _ in range(1000):
        action = env.action_space.sample()  # this is where you would insert your policy
        observation, reward, terminated, truncated, info = env.step(action)
        if terminated or truncated:
            observation, info = env.reset()

env1thread = threading.Thread(target=env1())
env2thread = threading.Thread(target=env2())

env1thread.start()
env2thread.start()

env.close()