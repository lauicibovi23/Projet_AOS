import random
from flask import Flask, request

from qlearning import QLearningAgent

# app = Flask(__name__)

# @app.route("/", methods=["POST"])
def next_move():
    """
    Retourne le prochain déplacement du fantôme en fonction de la position du Pac-Man.

    Args:
        data: Un dictionnaire contenant les informations suivantes :
            * "grid": Le tableau de jeu
            * "ghost_position": La position du fantôme
            * "pacman_position": La position de Pac-Man

    Returns:
        La prochaine position du fantôme.
    """
    # data = request.get_json()
    # grid = data["grid"]
    # ghost_position = data["ghost_position"]
    # pacman_position = data["pacman_position"]
    
    b = {(0, 0): 0, (0, 1): 0, (0, 2): 0, (0, 3): 0, (0, 4): 0, (0, 5): 0, (1, 0): 0, (1, 1): 3, (1, 2): 0, (1, 3): 0, (1, 4): 0, (1, 5): 0, (2, 0): 0, (2, 1): 0, (2, 2): 0, (2, 3): 0, (2, 4): 0, (2, 5): 0, (3, 0): 0, (3, 1): 0, (3, 2): 0, (3, 3): 0, (3, 4): 3, (3, 5): 0, (4, 0): 0, (4, 1): 0, (4, 2): 0, (4, 3): 0, (4, 4): 0, (4, 5): 0, (5, 0): 0, (5, 1): 0, (5, 2): 0, (5, 3): 0, (5, 4): 0, (5, 5): 0}
    a =(3,4)
    c =(1,1)
        
    agent = QLearningAgent(
        ghost_position= c,
        pacman_position = a,
        board = b,
    )
    
    q_table = agent.train()
    
    next_action = max(q_table)
    print(next_action)
    
next_move()