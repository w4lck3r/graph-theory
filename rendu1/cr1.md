# Compte rendu intermédiaire numéro 1 - modélisation

## Modélisation du sudoku

* On a une grille de sudoku composée de 9 x 9 casses qu'on remplit par des chifres (de 1 a 9) donc on peut mettre une graph de 81 sommets chaque sommet est une cell du sudoku , chaque sommet a un arret avec tous les autres sommets respectivement colonnes , lignes et 3 x 3 casses .
Pour choisir le nombre cromatique ; On a pour chaque petite grille chaque sommet a le meme nombre de degres donc a chaque fois on va choisir une nouveau couleur , enfin G = 3 x 3 = 9 . 
Donc on peut considéré le Sudoku comme une graphe et peut etre résolu par une coloration de graphe avec un chromatique nombre de 9 'deux sommets adjacents n'aient pas la meme couleurs' .
Pour bien comprendre la logique veuillez 
VOIR `sudoku-conn `.

## Modélisation du coloriage de cartes

* On represente les pays comme les sommets de notre graphe ,et les arrets sont les frontieres entre ces pays, alors on colorie ces sommets pour que les sommets voisines n'aurent pas la meme couleur . Commençons par colorer le graphique en commençant par le 4 et en contourant l'etérieur . on aurra 3 couleurs rouge , vert , bleu . On colorant le sommet 4 par rouge , le sommet 5 est adjacent a 4 dont doit avoir une couleur différente , On colorant par vert , le sommet 0 et adjacent a 4 mais pas a 5 donc on peut le colorer par le meme couleur de 5 qui est vert , le sommet 2 est adjacent avec 0 , 1 et 4 donc on doit colorer avec un autre couleur , 3 est adjacent avec 0 et 4 donc on peut pas faire le rouge et le vert on met le bleu , 1 est adjacent avec 0 ,5 ,4 et 2 donc on peut faire le couleur du sommet 3 . 
VOIR  ` ./images ` 

## Modélisation de l'attribution de fréquences

* On represente les antennes par les sommets et les voisines par les arrets et les fréquances par les couleurs , On distribuer avec la meme methode de la coloration des cartes geographique . 

## Problème commun

* On peut resolu tous ces problemes on utilisons les graphes avec les notions sommet , voisine et colorée .

## Citations
* discrete mathematics susanna S.epp
* https://imgur.com/gallery/uFq1lfg
