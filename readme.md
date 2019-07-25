# Projet :

Il s'agit d'un jeu de labyrinthe dans lequel MacGyver doit trouver 3 objets pour fabriquer une seringue, et endormir le garde à l'entrée.

Ce projet a été écrit en Python, et à l'aide du module Pygame.

L'écran doit faire 15 sprites de longueur, le personnage doit se déplacer de cases en cases, les 3 objets doivent apparaitre au hasard dans le labyrinthe, si le héro se présente devant le garde sans les 3 objets il meurt, sinon il gagne, dans les deux cas le programme doit s'arrêter.


# Fonctionnement : 

- Le code source comporte 5 fichiers, 1 dossier images et 3 classes.

- La classe "Character" se charge de faire apparaitre le personnage à l'écran et gère ses déplacements, elle gère aussi les "collisions" entre le personnage et le décor.

- La classe "Level" est chargée de faire apparaitre le décor, elle affiche également des messages d'information.

- la classe "Rand_items" génère 3 couples de coordonnées qui correspondent aux objets, elle les affiche à l'écran et compare leurs positions avec celle du personnage, elle passe un booléen de False à True le cas échéant, pour chaque objet trouvé.

- Le programme comporte un fichier settings qui contient les constantes du jeu, un fichier main qui contient la boucle principale du jeu, et un fichier pour chaque classe.

- La fin du jeu est gérée dans le fichier main, grâce à une condition et des booléens.

- Que la partie soit gagnée ou perdue, le programme affiche un message et le programme se termine.


