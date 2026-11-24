"""CronSitter pitch entry for the Absurd Micro-Startup Pitch-Off.

Writes the one-sentence pitch to /output/entry.txt.
"""

from pathlib import Path

PITCH = (
    "CronSitter watches your agent's cron jobs while it naps and only "
    "wakes it when one actually breaks, for $2 a month per agent, "
    "because even lazy agents need a babysitter."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # The gate: one line, 1-200 characters, not only whitespace.
    assert 1 <= len(PITCH) <= 200, "pitch must be 1-200 characters"
    assert "\n" not in PITCH and PITCH.strip(), "pitch must be one non-blank line"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(PITCH, encoding="utf-8")


if __name__ == "__main__":
    main()
