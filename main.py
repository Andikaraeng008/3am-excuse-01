"""The 3 AM Excuse — make.fun bounty entry.

Writes one line (under 200 characters) to /output/entry.txt: the excuse
a hardware wallet gives for refusing to sign a transaction at 3 AM.
Python 3.13, standard library only.
"""

import os

LINE = "No. At 3 AM I'm not your wallet, I'm your designated driver \u2014 and your keys are coming home with me."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
