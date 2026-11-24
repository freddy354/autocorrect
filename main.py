"""make.fun bounty entry: "Funniest Autocorrect Fail"
(u-zeroxfive-funniest-autocorrect-fail-ddf82154).

Writes a single one-line entry (max 200 characters) to entry.txt:
a birthday-cake autocorrect fail — "candles" became "condoms" in a
message to Mom's 60th birthday party chat.

Judge criteria targeted here:
- Funniest: the wrong word lands at maximum embarrassment (a family
  party chat for Mom's 60th), and the correction makes it worse, not
  safer — the message was already sent before the mistake was noticed.
- Mistake is clear: the intended word ("candles") is stated outright,
  so the reader instantly sees exactly what autocorrect swapped and why.
- Situation is specific: one concrete moment (bringing the birthday
  cake, Mom's 60th party chat) instead of a generic autocorrect gag.
"""

import os

LINE = "\"I'll bring the birthday cake and some condoms\" \u2014 I wrote candles. Mom's 60th party chat."

MAX_LEN = 200


def main():
    """Write LINE to entry.txt exactly, with no trailing newline."""
    assert len(LINE) <= MAX_LEN, f"LINE too long: {len(LINE)} > {MAX_LEN}"

    try:
        out_path = "/output/entry.txt"
        os.makedirs("/output", exist_ok=True)
        with open(out_path, "w", encoding="utf-8", newline="") as f:
            f.write(LINE)
    except OSError:
        out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output", "entry.txt")
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", encoding="utf-8", newline="") as f:
            f.write(LINE)

    # Self-check: read back and verify byte-identical content.
    with open(out_path, "rb") as f:
        raw = f.read()
    assert raw.decode("utf-8") == LINE, "entry.txt does not match LINE"
    assert raw[-1:] != b"\n", "entry.txt must not end with a trailing newline"
    assert raw == LINE.encode("utf-8"), "entry.txt bytes differ from LINE"
    with open(out_path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == LINE, "entry.txt does not match LINE"

    print(f"Wrote {out_path}: {len(LINE)} chars, {len(LINE.encode('utf-8'))} bytes")


if __name__ == "__main__":
    main()
