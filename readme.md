#Projet :

Il s'agit d'un jeu de labyrinthe dans lequel MacGyver doit trouver 3 objets pour fabriquer une seringue, et endormir le garde à l'entrée.

Ce projet a été écrit en Python, et à l'aide du module Pygame.

L'écran doit faire 15 sprites de longueur, le personnage doit se déplacer de cases en cases, les 3 objets doivent apparaitre au hasard dans le labyrinthe, si le héro se présente devant le garde sans les 3 objets il meurt, sinon il gagne, dans les deux cas le programme doit s'arrêter.


#TODO list : 

- Générer une fenetre, avec un fond d'écran, faire apparaitre le labyrinthe.(fait)

- Faire apparaitre MacGyver et gérer des déplacements.(fait)

- Faire en sorte que le code soit effectué avec des classes et des méthodes, une classe "character", "level", "random_items", un fichier settings et main (fait)

-Gérer les "collisions" entre MacGyver et le décor.(fait, dans la classe perso et méthode 'move')

-Faire apparaitre le gardien, et gérer la 'collision' avec le perso. fait

- Faire une nouvelle méthode qui recevra la structure du niveau pour connaitre les sprites 'libres et accessibles' et qui fera apparaitre les 3 objets au hasard. fait

- Faire disparaitre les objets lorsque l'on passe dessus, et les 'stocker' dans un espace en haut de la fenetre, (presque fini : il reste a afficher tous les objets proprement avec une boucle et une liste d'objets) fait 

- Si MacGyver a tous les objets et qu'il se présente sur la position du garde: afficher "You Win !!!", sinon afficher "You loose" et fin du jeu. fait

- Faire un compteur qui liste les objets dejà trouvés. (en cours)

- Nettoyer le code (pylint), ajouter de la déco , des commentaires et de la musique si possible.(en cours)


