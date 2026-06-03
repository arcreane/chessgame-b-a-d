[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/NhlhWyZq)



# Chessgame-b-a-d

Un jeu d'echecs developpe en **Python** avec la bibliotheque **Pygame**. Le projet affiche un plateau 8x8, permet de deplacer les pieces a la souris (drag & drop), met en evidence les coups possibles et le dernier coup joue.

Projet realise dans le cadre d'un travail de groupe via GitHub Classroom.

## Fonctionnalites

- Plateau d'echecs 8x8 avec theme de couleurs personnalisable.
- Deplacement des pieces par glisser-deposer (drag & drop) a la souris.
- Affichage des coups valides pour la piece selectionnee.
- Mise en evidence du dernier coup joue et de la case survolee.
- Pieces aux formats 80px et 128px.

## Prerequis

- Python 3.x
- Pygame

Installation de la dependance :

```bash
pip install pygame
```

## Lancer le jeu

Depuis la racine du projet :

```bash
python main.py
```

Une fenetre de 800x800 pixels intitulee "Chess" s'ouvre. Cliquez sur une piece et faites-la glisser vers la case souhaitee pour jouer.

## Structure du projet

| Fichier | Role |
|---------|------|
| `main.py` | Point d'entree : boucle de jeu et gestion des evenements. |
| `game.py` | Logique d'affichage (fond, pieces, coups, survol). |
| `board.py` | Representation du plateau et des cases. |
| `square.py` | Representation d'une case du plateau. |
| `piece.py` | Definition des pieces et de leurs deplacements. |
| `move.py` | Representation d'un coup. |
| `dragger.py` | Gestion du glisser-deposer des pieces. |
| `color.py` / `theme.py` | Couleurs et themes du plateau. |
| `const.py` | Constantes (dimensions du plateau, nombre de cases). |
| `config.py` | Configuration generale du jeu. |
| `assets/images/` | Sprites des pieces (80px et 128px). |

## Auteurs

Projet de groupe -- voir l'historique des commits et les contributeurs sur GitHub.

              
