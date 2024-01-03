import numpy as np

class QLearning:
    def __init__(self, state_space_size, action_space_size):
        self.q_table = np.zeros((state_space_size, action_space_size))

    def train(self, state, action, reward, next_state, learning_rate=0.1, discount_factor=0.9):
        # Mettre à jour le modèle Q
        current_q_value = self.q_table[state, action]
        best_future_q = np.max(self.q_table[next_state, :])
        new_q_value = (1 - learning_rate) * current_q_value + learning_rate * (reward + discount_factor * best_future_q)
        self.q_table[state, action] = new_q_value

    def act(self, state):
        # Prendre une décision basée sur le modèle Q
        return np.argmax(self.q_table[state, :])