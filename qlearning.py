import numpy as np
import random

ACTIONS = ['left', 'right', 'up', 'down']
class QLearningAgent:
    epsilon=2
    alpha=0.1
    gamma=0.9
    qTable = {} # Maps cell to possible actions. Actions then map to reward
    
    def __init__(self,ghost_position, pacman_position, board):
        self.ghost_position = ghost_position
        self.pacman_position = pacman_position
        self.board = board
        self.initQTable()

    def initQTable(self):
        for state in self.board.keys():
            for action in ["up", "down", "left", "right"]:
                self.qTable[state, action] = 0

    def choose_action(self, state):
        randInt = random.randint(1,11)
        if randInt <= 3:

            validActions = list(filter(lambda action: self.isValidCell(state), ACTIONS))
            return random.choice(validActions)
        else:
            # Gets all qValues for specified state for all q values
            # for key, val in self.qTable.items():
            arr = {key: val for key, val in self.qTable.items() if key[0] == state}
            
            # Choisissez l'action avec la plus grande valeur Q (exploitation)
            var = max(arr)
            return var[1]
        
    def evalQFunction(self,coord, action):
        new_ghost_position=coord
        if action == "up":
            new_ghost_position = (coord[0], int(coord[1]) - 1)
        elif action == "down":
            new_ghost_position = (coord[0], coord[1]  + 1)
        elif action == "left":
            new_ghost_position = (coord[0] - 1, coord[1] )
        elif action == "right":
            new_ghost_position = (coord[0] + 1, coord[1] )
            
        reward = self.board[new_ghost_position]
        maxQSPrime = max([self.qTable[new_ghost_position, action] for action2 in ACTIONS if self.isValidCell(new_ghost_position)])
        self.qTable[new_ghost_position, action] += (self.alpha * (reward + self.gamma * maxQSPrime - self.qTable[new_ghost_position, action]))
        
    def isValidCell(self, coord):
        xCoord, yCoord = coord[0], coord[1]
        return (0 <= xCoord < 6  and 0 <= yCoord < 6) 
    
    def max_V(dictionary):
        # Recherche de la clé avec la valeur maximale
        max_key = None
        max_value = 0
        for key, value in dictionary.items():
            if value > max_value:
                max_key = key
                max_value = value

        # Retour de la clé et de la valeur maximale
        return max_key, max_value
    
    def train(self):
        for i in range(1000):
            # Génération d'une action aléatoire
            action = self.choose_action(self.ghost_position)

            # Mise à jour de la fonction Q
            self.evalQFunction(self.ghost_position, action)

        return self.qTable
       