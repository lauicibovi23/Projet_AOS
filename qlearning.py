import numpy as np

class QLearningAgent:

    def __init__(self, actions, epsilon, alpha, gamma):
        if not isinstance(actions, list):
            raise TypeError("actions must be a list")

        self.actions = actions
        self.epsilon = epsilon
        self.alpha = alpha
        self.gamma = gamma
        self.q_table = np.zeros((len(actions), len(actions)))
        self.memory = []

    def get_action(self, state):
        if np.random.random() < self.epsilon:
            return np.random.choice(self.actions)
        else:
            return self.max_q(state)

    def update(self, state, action, reward, next_state):
        self.q_table[state][action] += self.alpha * (reward + self.gamma * self.max_q(next_state) - self.q_table[state][action])
        self.memory.append((state, action, reward, next_state))

    def max_q(self, state):
        return np.max(self.q_table[state])

    def get_next_move(self, grid, ghost_position):
        state = self.get_state(grid, ghost_position)
        action = self.get_action(state)
        return action

    def get_state(self, grid, ghost_position):
        state = np.zeros(len(grid))
        state[ghost_position] = 1
        return state

    def update_epsilon(self, decay):
        self.epsilon *= decay

    def explore_randomly(self, probability):
        if np.random.random() < probability:
            return True
        else:
            return False

    def remember(self, state, action, reward, next_state):
        self.memory.append((state, action, reward, next_state))

    def replay(self):
        for state, action, reward, next_state in self.memory:
            self.update(state, action, reward, next_state)

def main():
    # Test d'initialisation de l'agent
    actions = [0, 1, 2]
    epsilon = 0.1
    alpha = 0.2
    gamma = 0.9
    agent = QLearningAgent(actions, epsilon, alpha, gamma)
    

    # Test de la fonction get_action
    state = 1
    action = agent.get_action(state)
    print("Selected action:", action)

    # Test de la fonction update
    state = 1
    action = 0
    reward = 1.0
    next_state = 2
    agent.update(state, action, reward, next_state)

    print(q_table) 

    # Test de la fonction get_next_move
    grid = [0, 0, 0, 1, 0]
    ghost_position = 3
    next_move = agent.get_next_move(grid, ghost_position)
    print("Next move:", next_move)

    # Test de la fonction get_state
    grid = [0, 0, 0, 1, 0]
    ghost_position = 3
    state = agent.get_state(grid, ghost_position)
    print("State:", state)

    # Test de la fonction update_epsilon
    decay = 0.9
    agent.update_epsilon(decay)
    print("Updated epsilon:", agent.epsilon)

    # Test de la fonction explore_randomly
    probability = 0.1
    exploration_result = agent.explore_randomly(probability)
    print("Explore randomly:", exploration_result)

    # Test de la fonction remember
    state = 1
    action = 0
    reward = 1.0
    next_state = 2
    agent.remember(state, action, reward, next_state)
    print("Memory:", agent.memory)

    # Test de la fonction replay
    agent.replay()

if __name__ == "__main__":
    main()
    