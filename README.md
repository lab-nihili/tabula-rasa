# Tabula Rasa

**Français** · [English](#english)

Mindmapping de bureau, gratuit, avec une vue **Constellation** 3D, des **arbres de décision** et des **plannings** (Gantt). Une page blanche, et le réseau de vos idées apparaît.

Version 0.3.0 · Windows · Français et anglais

## Fonctionnalités

- **Carte** : un arbre d'idées que l'on édite directement, au clavier et à la souris. Glisser une idée pour la déplacer, la réordonner ou la rattacher ailleurs.
- **Constellation** : le même document en nuage 3D. Une idée liée à plusieurs choses (relations, thèmes) se place entre leurs mondes. Un clic rapproche son monde ; en survolant un autre point, on voit le plus court chemin.
- **Arbre** *(nouveau en 0.3.0)* : arbres de décision (décisions, hasards avec probabilités, résultats avec montants) avec espérance de gain calculée à chaque nœud, et organigrammes de programmation (conditions Oui / Non, actions, début / fin, texte sur les branches).
- **Planning** *(nouveau en 0.3.0)* : diagramme de Gantt. Colonne de gauche avec un nom et une description par ligne, calendrier à l'échelle de votre choix (heures, jours, semaines, mois, trimestres, années), texte dans les barres. Plusieurs barres par ligne, jamais superposées. Lignes réordonnables par glisser-déposer, couleur par ligne.
- **Structures** : carte radiale, diagramme logique, chronologie, arête de poisson, accolades, organigramme, arbre vertical, tableau arborescent. Même contenu, autre disposition.
- **Import XMind** (`.xmind`), export du plan en **Markdown**, export de la carte en **SVG**, impression ou PDF.
- Annuler / rétablir, thème clair ou sombre, recherche `Ctrl+K`.
- **Vos données restent chez vous** : les cartes sont des fichiers `.tabula` (JSON) sur votre ordinateur. L'application ne collecte ni ne transmet rien.

## Installation

**Avec l'installeur** (recommandé) : téléchargez `TabulaRasa-0.3.0-fr.msi` depuis la page [Releases](../../releases) et lancez-le. Il s'installe pour votre compte, sans droits d'administrateur, et vous choisissez un raccourci dans le menu Démarrer et/ou sur le Bureau. (Version anglaise : `TabulaRasa-0.3.0-en.msi`.)

**Version portable** : téléchargez `TabulaRasa.zip`, décompressez-le où vous voulez et lancez `TabulaRasa.exe`. Rien à installer.

Au premier lancement, la langue suit celle du système si elle est connue, sinon le français. Vous pouvez la changer à tout moment avec le menu de langue en haut à droite.

## Raccourcis

| Touche | Action |
|---|---|
| Tab / Entrée | idée enfant / idée voisine |
| F2, double-clic | renommer |
| Glisser | déplacer / réordonner |
| Maj + glisser, Ctrl+L | relier deux idées |
| Espace | replier / déplier |
| Suppr | supprimer l'idée et ses sous-idées |
| Ctrl+K | rechercher |
| Ctrl+1 à Ctrl+4 | Carte / Constellation / Arbre / Planning |
| Ctrl+Z / Ctrl+Y | annuler / rétablir |
| Ctrl+N, O, S, P | nouveau, ouvrir, enregistrer, imprimer |

## Utiliser avec Claude

Un plugin Claude Code permet de créer et tenir à jour une carte `.tabula` à partir d'un projet ou d'une discussion. L'application recharge le fichier automatiquement.

```
/plugin marketplace add lab-nihili/tabula-rasa
/plugin install tabula-rasa@laboratorium-nihili
```

Puis tapez `/carte`.

## Licence

Tabula Rasa est un logiciel propriétaire, **gratuit pour tout usage, y compris professionnel**. Le code source n'est pas publié. Voir [LICENSE](LICENSE) (FR/EN) et [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md) pour les composants libres utilisés.

© 2026 Laboratorium Nihili

---

## English

Free desktop mind mapping with a 3D **Constellation** view, **decision trees** and **planning charts** (Gantt). Start from a blank page and the network of your ideas appears.

Version 0.3.0 · Windows · French and English

### Features

- **Map**: a tree of ideas you edit directly, with keyboard and mouse. Drag an idea to move it, reorder it or attach it elsewhere.
- **Constellation**: the same document as a 3D cloud. An idea linked to several things (relations, themes) sits between their worlds. A click brings its world closer; hovering another point shows the shortest path.
- **Tree** *(new in 0.3.0)*: decision trees (decisions, chances with probabilities, outcomes with amounts) with the expected value computed at every node, and programming flowcharts (Yes / No conditions, actions, start / end, text on branches).
- **Planning** *(new in 0.3.0)*: Gantt chart. A left column with a name and a description per row, a calendar at the scale you choose (hours, days, weeks, months, quarters, years), text inside the bars. Several bars per row, never overlapping. Rows can be reordered by drag and drop, with a colour per row.
- **Structures**: radial map, logic chart, timeline, fishbone, braces, org chart, vertical tree, tree table. Same content, different layout.
- **XMind import** (`.xmind`), outline export to **Markdown**, map export to **SVG**, printing or PDF.
- Undo / redo, light or dark theme, `Ctrl+K` search.
- **Your data stays with you**: maps are `.tabula` files (JSON) on your computer. The application neither collects nor transmits anything.

### Installation

**With the installer** (recommended): download `TabulaRasa-0.3.0-en.msi` from the [Releases](../../releases) page and run it. It installs for your account, with no administrator rights, and lets you choose a Start menu and/or Desktop shortcut. (French version: `TabulaRasa-0.3.0-fr.msi`.)

**Portable version**: download `TabulaRasa.zip`, unzip it anywhere and run `TabulaRasa.exe`. Nothing to install.

On first launch, the language follows the system language when it can be detected, otherwise French. You can change it at any time from the language menu at the top right.

### Shortcuts

| Key | Action |
|---|---|
| Tab / Enter | child idea / sibling idea |
| F2, double-click | rename |
| Drag | move / reorder |
| Shift + drag, Ctrl+L | link two ideas |
| Space | fold / unfold |
| Delete | delete the idea and its sub-ideas |
| Ctrl+K | search |
| Ctrl+1 to Ctrl+4 | Map / Constellation / Tree / Planning |
| Ctrl+Z / Ctrl+Y | undo / redo |
| Ctrl+N, O, S, P | new, open, save, print |

### Use with Claude

A Claude Code plugin creates and maintains a `.tabula` map from a project or a conversation. The application reloads the file automatically.

```
/plugin marketplace add lab-nihili/tabula-rasa
/plugin install tabula-rasa@laboratorium-nihili
```

Then type `/carte`.

### License

Tabula Rasa is proprietary software, **free for any use, including professional use**. The source code is not published. See [LICENSE](LICENSE) (FR/EN) and [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md) for the open-source components used.

© 2026 Laboratorium Nihili
