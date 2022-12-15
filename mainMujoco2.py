import gym

env = gym.make("HalfCheetah-v4", render_mode="human")
observation, info = env.reset()

for _ in range(10000):
    action = env.action_space.sample()  # agent policy that uses the observation and info
    observation, reward, terminated, truncated, info = env.step(action)

    print(reward)
    
    if terminated or truncated:
        observation, info = env.reset()

env.close()