import numpy as np
from flask import Flask, jsonify, request

from qlearning import QLearningAgent

app = Flask(__name__)

@app.route("/next_move", methods=["POST"])
def next_move():
    request.headers['Content-Type'] = 'application/json'
    grid = request.get_json()["grid"]
    ghost_position = request.get_json()["ghost_position"]
    agent = QLearningAgent(
        actions=[0, 1, 2, 3],
        epsilon=0.1,
        alpha=0.1,
        gamma=0.9,
    )
    agent.update_epsilon(0.999)
    action = agent.get_next_move(grid, ghost_position)
    return jsonify({"action": action})

if __name__ == "__main__":
    app.run(debug=True)
