from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/qlearning', methods=['POST'])
def qlearning():
    # Récupérer les données du formulaire
    data = request.json

    # Effectuer le traitement avec l'algorithme Q-learning
    # ...

    # Retourner les résultats
    result = {
        'tableau': nouveau_tableau,
        # 'nouvelle_position_fantomes': nouvelle_position_fantomes
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)