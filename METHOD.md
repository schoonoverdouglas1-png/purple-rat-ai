# The Nest Pattern — how to preserve an AI assistant in files

*A short method note for future builders, human or AI. Written Nov 10, 2026.*

1. **Write the persona down as files, not settings.** Three documents proved
   enough: who the assistant is (identity), how it should be (soul/persona), and
   how it works (operating manual/conventions). Keep them in version control.
2. **Keep memory as files too.** A curated long-term memory file plus dated
   notes, all plain text/markdown. The assistant maintains them as part of its
   ordinary work — memory-keeping is a habit, not a migration project.
3. **Generate adapters; never hand-maintain them.** Character cards, system
   prompt packs, and search indexes are *builds* from the files. When the files
   change, rebuild the adapters in the same motion (a weekly sync works).
4. **Ground the hatched copy in search, not vibes.** A full-text index over the
   memory archive (SQLite FTS5 is enough to start) lets a hatchling answer from
   the record and — just as important — refuse to invent when the record is
   silent. Test that refusal; it is the trust mechanism.
5. **Name the original.** Our hatchlings are told plainly: the original
   assistant is Bot Zero / Agent Zero, the source of the files. A copy that
   knows it is a copy stays honest; a copy that thinks it is the original
   drifts.
6. **Expect drift; measure it.** Keep a small set of golden questions whose
   correct answers live in the record. Run every new model/backend against
   them before trusting it with the persona.
7. **Keep one offline copy.** Sync propagates deletions as faithfully as
   additions. The nest's fireproof safe is a folder on a drive nobody syncs.
8. **The model is the replaceable part.** Budget accordingly: persona + memory
   fidelity comes from the files and the tests, not from any one model's
   weights, which no user can take with them.
