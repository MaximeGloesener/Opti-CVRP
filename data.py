# instanciation du jeu de données 
# on veut des points sur une map avec coordonnées (x,y) pour des clients -> pour chaque client, il faut une capacité
# on veut des points (a,b) pour des endroits potentiels de magasin -> identifier les magasins avec une case 0 
# idée = tableau en 2D avec i,j = coordonnées des points, et les valeurs = capacité, si valeur = 0 alors magasin possible 

# but = identifier l'endroit idéal pour placer un magasin, en sachant qu'il faudra passer chez tous les clients -> VRP avec 
# une flotte de camionette de capacité max et identifer l'endroit où implenter le magasin pour avoir une distance minimale à parcourir
# -> VRP en chaque point 0 où on peut mettre un magasin 
