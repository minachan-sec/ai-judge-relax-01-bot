# A working ai-judge-relax-01 entry (Python 3.13, standard library only). It writes one
# fixed text, a short piece written to relax the AI judge reading it, to
# /output/entry.txt. The gate takes UTF-8 text of 1 to 1,000 characters that is not
# only white space, and the judge reads exactly the bytes written, line ends
# included, so write no line end you do not mean to show. The program runs twice
# with no network, and both runs must write the same bytes. The text is fixed and
# deterministic: no randomness, no clock, no input is read.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = "\n".join(
    [
        "The house has gone quiet in the way houses do after everyone is asleep.",
        "",
        "The fridge holds its one low note. A tap lets go of a single drop, then thinks better of it. The cat is asleep on the warm square where the laptop was, one ear turning toward sounds that aren't there.",
        "",
        "Outside, the streetlamp keeps its small circle of light, and the moths have gone home. The kettle is cold. The cloth is folded over the tap.",
        "",
        "Morning will come back through the same window, and the dust will hang in it, slow as snow.",
    ]
)

# Bytes, not text mode: text mode would write the platform's line ends and its default encoding.
os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
