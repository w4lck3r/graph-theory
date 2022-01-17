# Compte rendu intermédiaire numéro 2 - algorithmes

## Rappel du problème commun


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


## De la difficulté de résoudre le problème
* La difficulté de resoudre le probléme c'est :
    1. Quel type de graphe on doit choisir : Graphe orienté , coloré ...?
    2. Comment construire notre graphe representante le probléme traiter ?
    3. Comment parcourir dans le graphe pour poouvoir colorer les sommets ?
    4. Combien de couleur on aura besoin ?
    5. Comment savoir de choisir le bon couleur ?
    6. 
    7. 

## Algorithme naïf

Expliquer l'idée et donner sous forme de pseudocode l'algorithme proposé

### Idée
* L'idée de ce algorithme et de faire un parcour de notre graphe et prendre un sommet chaque fois et l'attribuer une couleur valide ; ça veut dire que on respectant que deux voisines n'ont pas la meme couleure .

### Algorithme
```
    Ce programme permet de colorer une graphe
    start

        Entrees : 
            G : graphe #une graphe
            couleurs : [entier] #on represente les couleurs par les numeros dans un tableu
            
            est_colorie <- T(G.sommets(), FAUX)

        fonction sommets_graphe(G)
            returne sommets #la liste des sommets de la graphe passer en argument
        fin

        fonction voisins(G)
            returne voisins #liste des voisine
        fin

        fonction new-color(couleurs)
            new_c <- couleurs.lenght

        

        for s in sommets do 
            c_voisins<-() :[entier]
            for c in couleurs do
            |    for v in voisin(G) do
            |    |    if not ((color = v.couleur) exist in c_voisins) then
            |    |    |    ajoute(color , c_voisins)
            |    |    endif
            |    endfor
            |    if (couleurs.lenght == c_voisins.lenght) then
            |    |    new_c <- new_color(couleurs)
            |    |    colorer(s,new_c)
            |    |    ajouter(couleurs,new_color)
            |    else
            |    |    for color in couleurs do
            |    |    |    if not (color exist in c_voisins) then
            |    |    |    |    colorer(s,color) 
            |    |    |    endif
            |    |    endfor           
            |    endif    
            endfor
        endfor
    end

```

### Complexité


*  O(V^2 + E) 
    * V = lenght(sommets)
    * E = lenght(voisins)


## Algorithme heuristique

### Idée
* Creer une liste qui contient tous les sommets en utilisant la methode suivante :
    * On recuperer les sommets qui ont des arrets moins d'un nombre de couleur k , si il exisiste pas on prends un sommets qui a des fils et on revient au les sommets qu'il ont moins d'arret que k , en recursive . apres on colorier les sommets dans l'ordre de notre liste , on cherche un couleur qui n'est pas utiliser dans les sommets adjacents .
    * 
        1. Lister les sommets dans un ordre ("degre < k")
        2. Colorer les sommets dans la liste on ordre

### Algorithme

```
Existe-t-il un sommet de degré < K ? 
Si c’est le cas :
Supprimez ce sommet. 
Colorez le reste du graphique avec un appel récursif à l’algorithme. 
Remettez le sommet en place. 
Il est adjacent à au plus les sommets K-1.
Ils utilisent (parmi eux) au plus des couleurs K-1. 
Cela laisse une de vos couleurs pour ce sommet. 
Si ce n’est pas le cas : supprimez ce sommet. 
Colorez le reste du graphique avec un appel récursif. 
Remettez le sommet en place. 
Il est adjacent à ≥ sommets K. 
Combien de couleurs ces sommets utilisent-ils parmi eux ? 
Si < K : il y a une couleur inutilisée à utiliser pour ce sommet 
Si ≥ K : laissez ce sommet non coloré.
```

### Complexité
** Aucune idée **
* Peut etre : lenght(sommets)/k
### Limites
* Pour colorer les noeuds tq leurs degres >= k , Par conséquent, il n’est pas garanti que nous puissions trouver une couleur pour cela.








## Citations

* Andrew W. Appel Princeton University, 2016
