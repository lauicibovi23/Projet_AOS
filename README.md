# Projet_AOS
Ce projet a pour but de Construire l'algo de PACMAN en se servant de L'I.A pour l'apprentissage et de l'API REST pour faire appel à notre service
pour Tester:

*******
## installer flask 
avec : pip install flask

# Tester flask avec l'algo Glouton
Il faut récupérer les fichiers mainOld.py, algo_glouton.py et lancer le mainOld.py 
## Executer 
python main.py

# postman
avec la méthode POST
url: http://127.0.0.1:5000/next_move
data: {
  "grid": [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 2, 0, 0, 0, 0, 0, 0, 0, 0]
  ],
  "ghost_position": 9
}
