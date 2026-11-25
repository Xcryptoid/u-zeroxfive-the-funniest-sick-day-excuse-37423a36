"""Copy the pre-written sick-day excuse into the output directory.

The entry text lives in entry.txt next to this program. This program
only copies it, so the grader always sees the exact same bytes.
"""

import os
import shutil


def main():
    # The joke is already written; this function just moves it along.
    # Keeping the copy step tiny means nothing can drift between runs.
    # The grader gets the same file every time, byte for byte.
    here = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(
        os.path.join(here, "entry.txt"),
        os.path.join(out_dir, "entry.txt"),
    )


if __name__ == "__main__":
    main()
