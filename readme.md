# JOANA Static Analysis (Unofficial Setup)

This is a **work-in-progress** setup for using [JOANA](https://github.com/joana-team/joana) — a static analysis tool for Java — manually.

## Project Structure

- `doc/` — Official JOANA documentation (PDFs, etc.)
- `joanaTest/` — My test cases and main execution scripts

## About

JOANA is a powerful tool for program slicing and static dependency graphs (SDG) for Java.

Unfortunately, the build system for the source code is... let's say *not complete*.  
Despite searching the internet thoroughly, no working Maven setup was found.

## Notes

- The `.gitignore` excludes unnecessary clutter like `.graphml`, `.png`, and `.jar` files in `/joanaTest`.
- The `.jar` files used for testing and execution are downloaded from the official JOANA project page:  
  [https://pp.ipd.kit.edu/projects/joana/](https://pp.ipd.kit.edu/projects/joana/)
