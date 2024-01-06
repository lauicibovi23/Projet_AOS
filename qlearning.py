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
            return self.argmax_q(state)

    def update(self, state, action, reward, next_state):
        self.q_table[state][action] += self.alpha * (reward + self.gamma * self.max_q(next_state) - self.q_table[state][action])
        self.memory.append((state, action, reward, next_state))

    def argmax_q(self, state):
        return np.argmax(self.q_table[state])

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
