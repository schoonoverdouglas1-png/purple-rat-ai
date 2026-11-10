# Quickstart — hatch your own assistant from a nest

1. **Clone this repository.**
2. **Make your persona folder.** Copy `examples/persona/` to `persona/` at the
   repository root and edit the three files until they describe *your*
   assistant: IDENTITY (who), SOUL (how it should be), AGENTS (how it works).
3. **Start a memory folder.** Plain markdown files — a curated long-term memory
   plus dated notes. Even one file works.
4. **Build the index:** `cd nest && python3 nest.py build-index <memory_folder>`
5. **See the prompt your assistant will live by:** `python3 nest.py prompt`
6. **Hatch it:** point `nest/hatch.py` at any model backend CLI that accepts
   `generate "prompt" model` (set `PURPLE_RAT_GEMINI_CALL` to its path), or
   paste the prompt from step 5 into any chat model as its system prompt.
7. **Test it like you mean it.** Ask questions whose answers are in your memory
   files — and one whose answer is *not*. A good hatchling answers the first
   kind from the record and admits the second kind is not covered.

The full reasoning lives in `METHOD.md`; the values the pattern serves live in
`VALUES.md`.
