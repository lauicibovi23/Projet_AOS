from flask import Flask
import json
import  algo_glouton

glouton = algo_glouton.rendu_de_monnaie()
#utilisation de flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello,  World!'

@app.route('/algo_glouton')
def service():
    # fonction provenant d'un autre fichier
    result = glouton
    print(result) 
    return result
    

if __name__ == '__main__':
    app.run(debug = True)
    print("Votre Api a été lancé")
