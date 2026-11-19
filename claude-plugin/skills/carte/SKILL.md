---
name: carte
description: Crée et met à jour la carte mentale Tabula Rasa (.tabula) du projet ou de la discussion en cours. À utiliser quand l'utilisateur demande une carte, un mindmap, de « cartographier » ou « mettre à jour la carte », ou invoque /carte. / Creates and updates the Tabula Rasa mind map (.tabula) of the current project or conversation. Use when the user asks for a map, a mind map, to "map" or "update the map", or invokes /carte.
---

# Carte mentale Tabula Rasa

Tu maintiens une carte `.tabula` que l'utilisateur ouvre dans Tabula Rasa. L'app recharge le fichier
toute seule (≈1 s) tant qu'il n'a pas de modifications non enregistrées ; sinon elle l'avertit sans écraser.

## Où est la carte

1. Dans un projet (dossier de travail avec fichiers) : `<racine du projet>/carte.tabula`.
2. Sans projet (simple discussion) : `~/Documents/Tabula Rasa/<titre-court>.tabula` (crée le dossier).
3. Si une carte existe déjà (cherche `*.tabula` à la racine, ou celle que l'utilisateur nomme) : la réutiliser, jamais en créer une seconde.

## Outil : toujours passer par le script, jamais éditer le JSON à la main

`python "${CLAUDE_PLUGIN_ROOT}/scripts/tabula.py" <commande> <fichier> [args]`
(Si `CLAUDE_PLUGIN_ROOT` est vide, le script est dans `claude-plugin/scripts/` du dossier Tabula Rasa.)

| Commande | Effet |
|---|---|
| `show F` | affiche l'arbre avec les ids — **à lancer avant toute mise à jour** |
| `init F "Titre"` | nouvelle carte, racine = titre |
| `add F <parent> "Titre" [--note T] [--tags a,b]` | ajoute une idée |
| `add-tree F <parent> '<json>'` | sous-arbre entier : `{"title","note","tags","children":[…]}` (`-` = stdin) |
| `rename F <n> "Titre"` · `note F <n> "texte"` | renomme / remplace la note |
| `move F <n> <nouveau-parent> [--index i]` | re-parente |
| `delete F <n>` | supprime l'idée et ses sous-idées |
| `tag F <n> a,b [--remove]` | thèmes |
| `link F <a> <b> [--label L] [--remove]` | relation transverse |
| `repair F` | répare des accents corrompus (« Ã© », « â€” ») dans une carte existante |
| `collapse F <n> [--open]` · `structure F <Radial\|LogicRight\|…>` · `validate F` | |

`<n>`/`<parent>` = id numérique **ou** titre exact. En cas de titre ambigu, utiliser l'id. Le script valide
la cohérence avant d'écrire (écriture atomique) et renvoie une erreur plutôt que d'abîmer la carte.

Accents : le script lit et écrit en UTF-8. Après la première création, relis avec `show` et, si tu vois des
« Ã© » ou « â€” », lance `repair`.

## Méthode

- **Première fois** : `init`, puis construire d'un coup avec `add-tree`. Racine = le sujet du projet/de la discussion.
  Branches de 1er niveau = 4 à 8 grands axes (ex. Objectif, Décisions, Architecture, À faire, Questions ouvertes, Risques).
- **Mises à jour** : `show` d'abord, puis modifications ciblées. Ne reconstruis pas la carte. Ne renomme/supprime
  que ce qui est devenu faux. Ce que l'utilisateur a ajouté ou réorganisé dans l'app est à respecter.
- **Contenu** : titres courts (≤ 6 mots), le détail dans `--note`. Une idée = une chose. Profondeur ≤ 4.
  Utilise `tag` pour les thèmes qui traversent plusieurs branches, et `link` pour les liens de cause à effet
  ou de dépendance entre branches (avec un `--label` bref).
- **Quand** : à la demande, et proactivement en fin de session ou après une décision importante si une carte
  existe déjà pour ce projet (ne crée pas de carte non demandée).
- Termine en disant en une ligne ce qui a changé et le chemin du fichier.
