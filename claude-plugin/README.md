# Plugin Claude « tabula-rasa »

Permet à Claude de créer et tenir à jour une carte `.tabula` pour n'importe quel projet ou discussion.

- `skills/carte/SKILL.md` : méthode et règles (invoquée par `/tabula-rasa:carte` ou en parlant de carte/mindmap).
- `scripts/tabula.py` : édition sûre et validée des fichiers (Python 3, sans dépendance).

## Installer

Essai : `claude --plugin-dir "D:\Dev\Apps\Tabula Rasa\claude-plugin"`.
Permanent : déclarer ce dossier dans une marketplace locale, ou le copier dans `~/.claude/plugins/`.

## Côté app

Tabula Rasa recharge le fichier ouvert quand il change sur le disque (Ctrl+Z annule le rechargement).
Il faut recompiler l'app une fois : `cd Windows && cargo build --profile portable`.
