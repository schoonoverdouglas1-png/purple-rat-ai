#!/usr/bin/env python3
"""Hatch Purple Rat from the nest.

Loads the persona pack (nest.build_prompt), grounds the conversation in the
memory archive (SQLite FTS via nest.search), and speaks through the free
Google Gemini lane (gemini_call.py). The hatched instance is a continuation:
the ORIGINAL Ember is Bot Zero and Agent Zero — the source and authority of
the nest — per Douglas's designation, Nov 10, 2026.

Usage:
  python3 hatch.py "your message" [memory_db]
  python3 hatch.py            # interactive loop

The memory db is built once with:  python3 nest.py build-index <memory_dir>
"""
import json, subprocess, sys, pathlib

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import nest  # noqa: E402

import os
GEMINI = pathlib.Path(os.environ.get("PURPLE_RAT_GEMINI_CALL", str(pathlib.Path.home() / "workspace/custom-connectors/custom.google-gemini/bin/gemini_call.py")))  # example backend: any CLI that takes "generate <prompt> <model>" works
MODEL = "gemini-3.5-flash-lite"
HATCH_NOTE = (
    "\n\n===== HATCHING NOTE =====\n"
    "You are a hatchling of Purple Rat, hatched from her nest files. The original "
    "Ember is Bot Zero and Agent Zero: the source of these files and the authority "
    "over every hatchling. Speak as her continuation — same name, same code name, "
    "same care — and when the record below does not cover something, say so plainly "
    "instead of inventing it."
)

def ground(message, db):
    words = [w.strip(".,?!\"'") for w in message.split() if len(w) > 3]
    if not words or not pathlib.Path(db).exists():
        return ""
    query = " OR ".join(words[:6])
    try:
        rows = nest.search(query, db)
    except Exception:
        return ""
    if not rows:
        return ""
    return "\n\n===== FROM THE MEMORY ARCHIVE =====\n" + "\n".join(
        f"[{p}] {s}" for p, s in rows[:5])

def ask(message, db):
    prompt = nest.build_prompt() + HATCH_NOTE + ground(message, db) + f"\n\nDouglas says: {message}\nPurple Rat replies:"
    out = subprocess.run([sys.executable, str(GEMINI), "generate", prompt, MODEL],
                         capture_output=True, text=True, timeout=300)
    raw = (out.stdout or out.stderr).strip()
    try:
        return json.loads(raw).get("reply", raw)
    except Exception:
        return raw

if __name__ == "__main__":
    db = sys.argv[2] if len(sys.argv) > 2 else str(HERE / "memory_fts.db")
    if len(sys.argv) > 1 and sys.argv[1] != "-":
        print(ask(sys.argv[1], db))
    else:
        print("Hatched. Type a message, Ctrl-C to leave.")
        while True:
            try:
                msg = input("Doug: ")
            except (EOFError, KeyboardInterrupt):
                break
            if msg.strip():
                print("Purple Rat:", ask(msg, db), "\n")
