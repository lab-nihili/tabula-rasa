#!/usr/bin/env python3
"""Édition sûre des cartes Tabula Rasa (.tabula) depuis Claude.

Chaque commande lit le fichier, applique UNE modification, valide la cohérence, puis écrit de
façon atomique (fichier temporaire + remplacement) : l'app ne voit jamais un fichier à moitié écrit.

Usage : python tabula.py <commande> <fichier.tabula> [arguments]   (--help pour la liste)
Les nœuds se désignent par leur id numérique OU par leur titre exact (insensible à la casse).
Sortie : JSON sur stdout (ids créés, erreurs).
"""
import argparse
import json
import os
import sys
import tempfile

STRUCTURES = ["Radial", "LogicRight", "LogicLeft", "Timeline", "Fishbone", "Brace", "Org", "Tree", "Table"]


for _s in (sys.stdin, sys.stdout, sys.stderr):
    _s.reconfigure(encoding="utf-8")  # Windows : sinon cp1252 par défaut -> accents corrompus


def demojibake(s):
    """Répare un texte UTF-8 mal lu en cp1252 (« Ã© » -> « é »), éventuellement plusieurs fois."""
    for _ in range(3):
        try:
            fixed = s.encode("cp1252").decode("utf-8")
        except (UnicodeEncodeError, UnicodeDecodeError):
            break
        if fixed == s:
            break
        s = fixed
    return s


def die(msg):
    print(json.dumps({"ok": False, "error": msg}, ensure_ascii=False))
    sys.exit(1)


def load(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    if data.get("app") != "tabula-rasa":
        die("Pas un fichier Tabula Rasa (champ app)")
    return data


def save(path, data):
    validate(data["doc"])
    d = os.path.dirname(os.path.abspath(path))
    fd, tmp = tempfile.mkstemp(dir=d, suffix=".tmp")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    os.replace(tmp, path)


def new_node(nid, title, parent, note="", tags=None):
    return {"id": nid, "title": title, "note": note, "parent": parent, "children": [],
            "collapsed": False, "color": None, "side": 0, "tags": tags or []}


def new_file(title):
    doc = {"nodes": {"1": new_node(1, title, None)}, "root": 1, "relations": [],
           "structure": "Radial", "next_id": 2}
    return {"app": "tabula-rasa", "version": 1, "doc": doc}


def next_id(doc):
    return max(int(k) for k in doc["nodes"]) + 1


def find(doc, ref):
    """id numérique ou titre exact (insensible à la casse). Erreur si absent ou ambigu."""
    nodes = doc["nodes"]
    if str(ref) in nodes:
        return int(ref)
    hits = [int(k) for k, n in nodes.items() if n["title"].strip().lower() == str(ref).strip().lower()]
    if not hits:
        die(f"Idée introuvable : {ref!r}")
    if len(hits) > 1:
        die(f"Titre ambigu {ref!r} : ids {hits} — utiliser l'id")
    return hits[0]


def validate(doc):
    nodes = doc["nodes"]
    root = str(doc["root"])
    if root not in nodes:
        die("Racine absente")
    for k, n in nodes.items():
        if str(n["id"]) != k:
            die(f"Id incohérent pour le nœud {k}")
        if (n["parent"] is None) != (k == root):
            die(f"Parent invalide pour le nœud {k}")
        if n["parent"] is not None:
            p = nodes.get(str(n["parent"]))
            if p is None or n["id"] not in p["children"]:
                die(f"Le parent de {k} ne le liste pas comme enfant")
        for c in n["children"]:
            if str(c) not in nodes or nodes[str(c)]["parent"] != n["id"]:
                die(f"Enfant {c} de {k} incohérent")
        if len(set(n["children"])) != len(n["children"]):
            die(f"Enfants dupliqués dans {k}")
    seen, stack = set(), [doc["root"]]
    while stack:
        i = stack.pop()
        if i in seen:
            die("Cycle détecté")
        seen.add(i)
        stack.extend(nodes[str(i)]["children"])
    if len(seen) != len(nodes):
        die("Nœuds orphelins (non rattachés à la racine)")
    for r in doc["relations"]:
        if str(r["a"]) not in nodes or str(r["b"]) not in nodes:
            die(f"Relation vers une idée inexistante : {r}")
    if doc["structure"] not in STRUCTURES:
        die(f"Structure inconnue : {doc['structure']}")
    doc["next_id"] = next_id(doc)


def descendants(doc, i):
    out, stack = [], [i]
    while stack:
        x = stack.pop()
        out.append(x)
        stack.extend(doc["nodes"][str(x)]["children"])
    return out


def add(doc, parent, title, note="", tags=None, index=None):
    pid = find(doc, parent)
    nid = next_id(doc)
    doc["nodes"][str(nid)] = new_node(nid, title, pid, note, tags)
    kids = doc["nodes"][str(pid)]["children"]
    kids.insert(len(kids) if index is None else index, nid)
    return nid


def build_tree(doc, parent, spec):
    """spec = {"title":..., "note":..., "tags":[...], "children":[...]}; renvoie l'id créé."""
    nid = add(doc, parent, spec["title"], spec.get("note", ""), spec.get("tags"))
    for c in spec.get("children", []):
        build_tree(doc, nid, c)
    return nid


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    def cmd(name, *args, **kw):
        p = sub.add_parser(name, help=kw.get("help"))
        p.add_argument("file")
        for a in args:
            p.add_argument(a[0], **a[1])
        return p

    cmd("init", ("title", {}), help="Crée une carte (racine = title)")
    cmd("show", help="Affiche l'arbre avec les ids")
    cmd("add", ("parent", {}), ("title", {}), ("--note", {"default": ""}), ("--tags", {"default": ""}),
        help="Ajoute une idée sous parent (tags séparés par des virgules)")
    cmd("add-tree", ("parent", {}), ("json", {}), help='Ajoute un sous-arbre JSON {"title","note","tags","children":[...]} ("-" = stdin)')
    cmd("rename", ("node", {}), ("title", {}))
    cmd("note", ("node", {}), ("text", {}), help="Remplace la note d'une idée")
    cmd("move", ("node", {}), ("new_parent", {}), ("--index", {"type": int}), help="Re-parente une idée")
    cmd("delete", ("node", {}), help="Supprime l'idée et ses sous-idées")
    cmd("tag", ("node", {}), ("tags", {}), ("--remove", {"action": "store_true"}))
    cmd("link", ("a", {}), ("b", {}), ("--label", {"default": ""}), ("--remove", {"action": "store_true"}),
        help="Relation transverse entre deux idées")
    cmd("collapse", ("node", {}), ("--open", {"action": "store_true"}))
    cmd("structure", ("name", {"choices": STRUCTURES}))
    cmd("validate")
    cmd("repair", help="Répare les accents corrompus (Ã©, â€”…) dans titres, notes, tags, libellés")
    args = ap.parse_args()

    if args.cmd == "init":
        if os.path.exists(args.file):
            die("Le fichier existe déjà")
        data = new_file(args.title)
        save(args.file, data)
        print(json.dumps({"ok": True, "root": 1}))
        return

    data = load(args.file)
    doc = data["doc"]
    nodes = doc["nodes"]
    out = {"ok": True}

    if args.cmd == "show":
        def walk(i, d):
            n = nodes[str(i)]
            tags = f"  #{' #'.join(n['tags'])}" if n["tags"] else ""
            note = "  [note]" if n["note"] else ""
            print(f"{'  ' * d}[{i}] {n['title']}{tags}{note}")
            for c in n["children"]:
                walk(c, d + 1)
        walk(doc["root"], 0)
        for r in doc["relations"]:
            print(f"~ [{r['a']}] ↔ [{r['b']}] {r['label']}")
        return
    if args.cmd == "validate":
        validate(doc)
    elif args.cmd == "repair":
        n_fixed = 0
        for n in nodes.values():
            for key in ("title", "note"):
                new = demojibake(n[key])
                n_fixed += new != n[key]
                n[key] = new
            n["tags"] = [demojibake(t) for t in n["tags"]]
        for r in doc["relations"]:
            r["label"] = demojibake(r["label"])
        out["repaired_fields"] = n_fixed
    elif args.cmd == "add":
        tags = [t.strip() for t in args.tags.split(",") if t.strip()]
        out["id"] = add(doc, args.parent, args.title, args.note, tags)
    elif args.cmd == "add-tree":
        raw = sys.stdin.read() if args.json == "-" else args.json
        out["id"] = build_tree(doc, args.parent, json.loads(raw))
    elif args.cmd == "rename":
        nodes[str(find(doc, args.node))]["title"] = args.title
    elif args.cmd == "note":
        nodes[str(find(doc, args.node))]["note"] = args.text
    elif args.cmd == "move":
        i, np = find(doc, args.node), find(doc, args.new_parent)
        if i == doc["root"]:
            die("La racine ne se déplace pas")
        if np in descendants(doc, i):
            die("Impossible de déplacer une idée sous elle-même")
        n = nodes[str(i)]
        nodes[str(n["parent"])]["children"].remove(i)
        kids = nodes[str(np)]["children"]
        kids.insert(len(kids) if args.index is None else args.index, i)
        n["parent"] = np
    elif args.cmd == "delete":
        i = find(doc, args.node)
        if i == doc["root"]:
            die("La racine ne se supprime pas")
        gone = set(descendants(doc, i))
        nodes[str(nodes[str(i)]["parent"])]["children"].remove(i)
        for g in gone:
            del nodes[str(g)]
        doc["relations"] = [r for r in doc["relations"] if r["a"] not in gone and r["b"] not in gone]
        out["deleted"] = len(gone)
    elif args.cmd == "tag":
        n = nodes[str(find(doc, args.node))]
        for t in [t.strip() for t in args.tags.split(",") if t.strip()]:
            if args.remove and t in n["tags"]:
                n["tags"].remove(t)
            elif not args.remove and t not in n["tags"]:
                n["tags"].append(t)
    elif args.cmd == "link":
        a, b = find(doc, args.a), find(doc, args.b)
        same = lambda r: {r["a"], r["b"]} == {a, b}
        if args.remove:
            doc["relations"] = [r for r in doc["relations"] if not same(r)]
        elif a != b and not any(same(r) for r in doc["relations"]):
            doc["relations"].append({"a": a, "b": b, "label": args.label})
    elif args.cmd == "collapse":
        nodes[str(find(doc, args.node))]["collapsed"] = not args.open
    elif args.cmd == "structure":
        doc["structure"] = args.name

    save(args.file, data)
    print(json.dumps(out, ensure_ascii=False))


if __name__ == "__main__":
    main()
