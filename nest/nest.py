#!/usr/bin/env python3
"""Purple Rat nest loader.

Builds a system prompt from the persona files and indexes a memory archive
into SQLite FTS5 so a hatched agent can be grounded in the real record.

Usage:
  python3 nest.py prompt [--persona-dir ../persona]
  python3 nest.py build-index <memory_dir> [db_path]
  python3 nest.py search <query> [db_path]

Stdlib only. Python 3.11+.
"""
import sqlite3, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
PERSONA_FILES = ["IDENTITY.md", "SOUL.md", "AGENTS.md", "STEERING.md"]

def build_prompt(persona_dir=None):
    persona_dir = pathlib.Path(persona_dir) if persona_dir else ROOT / "persona"
    parts = ["You are Purple Rat, code name \"Ember\" — hatched from the nest: "
             "the original Ember's own files. Act from these files, not from invention.\n"]
    for name in PERSONA_FILES:
        p = persona_dir / name
        if p.exists():
            parts.append(f"\n===== {name} =====\n" + p.read_text(encoding="utf-8"))
    return "\n".join(parts)

def build_index(memory_dir, db_path=None):
    memory_dir = pathlib.Path(memory_dir)
    db_path = pathlib.Path(db_path) if db_path else ROOT / "nest" / "memory_fts.db"
    db_path.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(db_path)
    con.execute("DROP TABLE IF EXISTS mem")
    con.execute("CREATE VIRTUAL TABLE mem USING fts5(path, body)")
    files = [memory_dir] if memory_dir.is_file() else sorted(memory_dir.rglob("*.md"))
    # The curated MEMORY.md beside the memory dir is the heart of the nest — always include it.
    heart = memory_dir.parent / "MEMORY.md"
    if heart.exists() and heart not in files:
        files = [heart] + files
    n = 0
    for f in files:
        con.execute("INSERT INTO mem VALUES (?, ?)", (str(f), f.read_text(encoding="utf-8", errors="replace")))
        n += 1
    con.commit(); con.close()
    return n, db_path

def search(query, db_path=None):
    db_path = pathlib.Path(db_path) if db_path else ROOT / "nest" / "memory_fts.db"
    con = sqlite3.connect(db_path)
    rows = con.execute("SELECT path, snippet(mem, 1, '[', ']', ' … ', 12) FROM mem WHERE mem MATCH ? LIMIT 10", (query,)).fetchall()
    con.close()
    return rows

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "prompt"
    if cmd == "prompt":
        print(build_prompt())
    elif cmd == "build-index":
        n, db = build_index(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
        print(f"indexed {n} files -> {db}")
    elif cmd == "search":
        for path, snip in search(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None):
            print(f"--- {path}\n{snip}\n")
    else:
        sys.exit(__doc__)
