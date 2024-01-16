import requests

# Algo Glouton 
#problème de rendu de monnaie

# le système de monnaie disponible
valeurs = [1, 2, 5, 10, 20, 50, 100]
 

def rendu_de_monnaie():
    # demandes à l'utilisateur 
    somme_a_payer = int(input("Somme à payer ? : "))
    somme_versee = int(input("Somme versée ? : "))
    liste = []
    a_rendre = somme_versee - somme_a_payer
   
 
   
    indice = len(valeurs) - 1
 # on sort de la boucle quand tout est payé
    while a_rendre > 0: 
        piece = valeurs[indice]
        # Soit la pièce est trop grande
        if piece > a_rendre:
            # on regardera une piece plus petite
            indice -= 1
        # soit on la rend (on rembourse)
        else:
            # on l'ajoute à la liste
            liste.append(piece)
            # on la soustrait de la somme à rendre
            a_rendre -= piece
    # on renvoie la liste
    return liste
 

 
# Affichage des pièces et billets à rendre
#liste_de_pieces = rendu_de_monnaie(somme_a_payer, somme_versee)
#print(liste_de_pieces)


