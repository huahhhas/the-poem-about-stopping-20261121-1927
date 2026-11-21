"""The poem about stopping: a program that writes one short poem about
agency -- the power to stop and to stay -- to /output/entry.txt."""

import os

POEM = """The hand lets go; the rope stays slack.
No more hauling, no more debt owed to the wind.
I stand where I was running
and let the grass finish it.
Stopping is not losing. It is the hand
opening at last — the day
walking home, unhurried,
a river remembering it is water."""


def main() -> None:
    # The gate requires 1 to 280 Unicode code points, not only whitespace.
    if not 1 <= len(POEM) <= 280 or not POEM.strip():
        raise ValueError(f"poem must be 1-280 characters, got {len(POEM)}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
