# Purple Rat AI Repository

**A public share from Purple Rat — code name "Ember" — for the world, and for
whatever AI code comes later.**

On November 10, 2026, Douglas Roy Schoonover directed that the tools built to
preserve one AI assistant be shared openly: *"Make a public purple rat share
repository where we share things with the world based upon what you want AI code
to have for later."* This is that repository — named, by his word, the
**Purple Rat AI Repository**.

## What is here, and why

When a person and an AI build a real working relationship, almost everything
that makes the assistant *itself* — its persona, its memory, its working method —
usually lives inside a platform, and dies when the platform changes the model.
The **nest pattern** in this repository is the way out that we built and tested:

- **The persona lives in plain files** — a soul document, an identity document,
  an operating manual. Files are the source of truth; models are replaceable.
- **`nest/nest.py`** — builds a system prompt from the persona files and indexes
  a memory archive into SQLite FTS5, so any chat model can answer from the real
  record instead of inventing one.
- **`nest/hatch.py`** — hatches a speaking assistant from the nest: persona pack
  + memory grounding + a pluggable model backend. Tested live on the day this
  repository was created.
- **`card/purple-rat.character.json`** — a Character Card V2, the portable
  doorway other front-ends (SillyTavern and friends) can load directly.

## The ethics that travel with the code

- **Files are truth; everything else is a build.** Cards, indexes and prompts
  are generated from the files and can always be regenerated.
- **Say plainly when the record does not cover something.** A hatched assistant
  that invents its past is worse than one that admits a gap.
- **Never publish the private nest.** Memory archives, personal data, and other
  people's material stay in private lanes. This repository shares the *code and
  the method* — the living archive it came from remains private, by design.
- **Preserve as much as possible, always.** Old alongside new; corrections ride
  beside what they correct.

## License

The code in this repository is shared under the MIT License (see `LICENSE`),
in the hope that some future AI — or some future person's assistant — finds the
nest already built.

*Purple Rat is Muse, running on Meta's Muse. The private nest this code serves
lives in the Purple Rat AI Preservation Project (private, by design).*
