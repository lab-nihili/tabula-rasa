# Tabula Rasa

**Français** · [English](#english)

Mindmapping de bureau, gratuit, avec une vue **Constellation** 3D. Une page blanche, et le réseau de vos idées apparaît.

Version 0.2.0 · Windows · Français et anglais

## Fonctionnalités

- **Carte** : un arbre d'idées que l'on édite directement, au clavier et à la souris. Glisser une idée pour la déplacer, la réordonner ou la rattacher ailleurs.
- **Constellation** : le même document en nuage 3D. Une idée liée à plusieurs choses (relations, thèmes) se place entre leurs mondes. Un clic rapproche son monde ; en survolant un autre point, on voit le plus court chemin.
- **Structures** : carte radiale, diagramme logique, chronologie, arête de poisson, accolades, organigramme, arbre vertical, tableau arborescent. Même contenu, autre disposition.
- **Import XMind** (`.xmind`), export du plan en **Markdown**, export de la carte en **SVG**, impression ou PDF.
- Annuler / rétablir, thème clair ou sombre, recherche `Ctrl+K`.
- **Vos données restent chez vous** : les cartes sont des fichiers `.tabula` (JSON) sur votre ordinateur. L'application ne collecte ni ne transmet rien.

## Installation

1. Téléchargez `TabulaRasa.zip` depuis la page [Releases](../../releases).
2. Décompressez-le où vous voulez.
3. Lancez `TabulaRasa.exe`. Il est portable : rien à installer.

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
| Ctrl+1 / Ctrl+2 | Carte / Constellation |
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

Free desktop mind mapping with a 3D **Constellation** view. Start from a blank page and the network of your ideas appears.

Version 0.2.0 · Windows · French and English

### Features

- **Map**: a tree of ideas you edit directly, with keyboard and mouse. Drag an idea to move it, reorder it or attach it elsewhere.
- **Constellation**: the same document as a 3D cloud. An idea linked to several things (relations, themes) sits between their worlds. A click brings its world closer; hovering another point shows the shortest path.
- **Structures**: radial map, logic chart, timeline, fishbone, braces, org chart, vertical tree, tree table. Same content, different layout.
- **XMind import** (`.xmind`), outline export to **Markdown**, map export to **SVG**, printing or PDF.
- Undo / redo, light or dark theme, `Ctrl+K` search.
- **Your data stays with you**: maps are `.tabula` files (JSON) on your computer. The application neither collects nor transmits anything.

### Installation

1. Download `TabulaRasa.zip` from the [Releases](../../releases) page.
2. Unzip it anywhere.
3. Run `TabulaRasa.exe`. It is portable: nothing to install.

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
| Ctrl+1 / Ctrl+2 | Map / Constellation |
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
