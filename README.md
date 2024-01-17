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
{
  "grid":{(0, 0): 0, (0, 1): 0, (0, 2): 0, (0, 3): 0, (0, 4): 0, (0, 5): 0, (1, 0): 0, (1, 1): 0, (1, 2): 0, (1, 3): 0, (1, 4): 0, (1, 5): 0, (2, 0): 0, (2, 1): 0, (2, 2): 0, (2, 3): 0, (2, 4): 0, (2, 5): 0, (3, 0): 0, (3, 1): 0, (3, 2): 0, (3, 3): 0, (3, 4): 0, (3, 5): 0, (4, 0): 0, (4, 1): 0, (4, 2): 0, (4, 3): 0, (4, 4): 0, (4, 5): 0, (5, 0): 0, (5, 1): 0, (5, 2): 0, (5, 3): 0, (5, 4): 0, (5, 5): 0},
  "ghost_position": (1,1),
  "pacman_position": (3,4)
}

******* IMPOTRTANT *****
pour tester il suffit de faire en ligne de commande python main.py et vous aurez le résultat en ligne de commande, car pour la récupération des data on a un problème
