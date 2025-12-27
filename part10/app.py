#!/usr/bin/env python3
"""
Part 10 starter.

WHAT'S NEW IN PART 10
You will write two classes without detailed instructions! This is a refactoring, we are not adding new functionality 🙄.
"""

# ToDo 0: You will need to move and change some imports
from typing import List
import time

from .constants import BANNER, HELP
from .models import SearchResult, SearchEngine
from .file_utilities import load_sonnets, load_config, highlight_cmd, search_mode_cmd, hl_mode_cmd

def print_results(
    query: str,
    results: List[SearchResult],
    highlight: bool,
    query_time_ms: float | None = None,
    highlight_mode: str = "DEFAULT"
) -> None:
    total_docs = len(results)
    matched = [r for r in results if r.matches > 0]

    line = f'{len(matched)} out of {total_docs} sonnets contain "{query}".'
    if query_time_ms is not None:
        line += f" Your query took {query_time_ms:.2f}ms."
    print(line)

    for idx, r in enumerate(matched, start=1):
        r.print(idx, highlight, total_docs, highlight_mode)


# ---------- Paths & data loading ----------
# ToDo 0: Move to file_utilities.py

# ToDo 0: Move to file_utilities.py

# ToDo 0: Move to file_utilities.py

# ------------------------- Config handling ---------------------------------
# ToDo 0: Move to file_utilities.py

# ToDo 0: Move to file_utilities.py

# ToDo 0: Move to file_utilities.py

# ---------- CLI loop ----------

def main() -> None:
    print(BANNER)
    # ToDo 0: Depending on how your imports look, you may need to adapt the call to load_config()
    config = load_config()

    # Load sonnets (from cache or API)
    start = time.perf_counter()
    # ToDo 0: Depending on how your imports look, you may need to adapt the call to load_sonnets()
    sonnets = load_sonnets()
    search_engine = SearchEngine(sonnets)

    elapsed = (time.perf_counter() - start) * 1000
    print(f"Loading sonnets took: {elapsed:.3f} [ms]")

    print(f"Loaded {len(sonnets)} sonnets.")

    while True:
        try:
            raw = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBye.")
            break

        if not raw:
            continue

        # commands
        if raw.startswith(":"):
            if raw == ":quit":
                print("Bye.")
                break

            if raw == ":help":
                print(HELP)
                continue

            # ToDo 2: You realize that the three settings 'highlight', 'search-mode', and 'hl-mode' have a lot
            #  in common. Wrap the common behavior in a class and use this class three times.

            if highlight_cmd.get_mode(raw, config):
                continue

            if search_mode_cmd.get_mode(raw, config):
                continue

            if hl_mode_cmd.get_mode(raw, config):
                continue

            print("Unknown command. Type :help for commands.")
            continue

        # ---------- Query evaluation ----------
        words = raw.split()
        if not words:
            continue

        start = time.perf_counter()

        # ToDo 1: Extract the search - basically everything until the end of the time measurement in a new class.
        #  Find a good name for that class. Make this class encapsulate our list of sonnets!
        combined_results = search_engine.combine(raw, config.search_mode)

        # Initialize elapsed_ms to contain the number of milliseconds the query evaluation took
        elapsed_ms = (time.perf_counter() - start) * 1000

        # ToDo 0: You will need to pass the new setting, the highlight_mode to print_results and use it there
        print_results(raw, combined_results, config.highlight, elapsed_ms, config.highlight_mode)

if __name__ == "__main__":
    main()
