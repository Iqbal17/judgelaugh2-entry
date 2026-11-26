"""Make the AI Judge Laugh — one line about office life (103 chars, gate 1-200).

Decision record (judge's criteria, in order: on-subject -> true to office life
-> surprising turn -> tight -> original):

Candidates weighed:
  A. "My boss said we're a family, so I asked HR when my birthday present
     is due." — LOSES. The "we're a family" setup is the most worn office
     trope there is; the judge has heard it a thousand times, and the turn
     (asking HR) is the first joke anyone writes after it.
  B. "The office plant died, so we held a farewell meeting about it. It
     lasted longer than the plant did." — LOSES. Two beats where one would
     do, and the meeting joke is the same shape as every "meeting about a
     meeting" line; the plant is a prop, not the observation.
  C. "I asked for a raise and got a pizza party. I am now the highest-paid
     person in the building, in slices." — CHOSEN. The observation is true
     and lived: pizza parties handed out instead of raises. The turn lands
     on the last two words — "in slices" re-prices a salary in pizza — and
     it is a fresh angle, not a pun and not a swapped-noun stock line.
  D. "I have been 'circling back' since March. I am now dizzy and the email
     is still unanswered." — LOSES, close second. "Dizzy" is a nice surprise
     and the corporate phrase is real, but the joke leans on the phrase
     itself rather than an observation, and it reads as wordplay where the
     winner reads as a story.

Pass 2 — two genuine revisions to the winner:
  1. First draft: "I asked for a raise and got a pizza party instead. Now I'm
     the highest-paid person in the office, paid in slices." Cut "instead"
     (the contrast is already in the sentence), changed "in the office" to
     "in the building" (a bigger, funnier scale for one pizza party), and
     cut "paid in slices" to "in slices" — the landing is tighter when the
     currency joke is implied rather than spelled out.
  2. Tried ending "...in pepperoni." and dropped it: it names the joke out
     loud and narrows the image to one topping, where "in slices" keeps the
     whole pizza as the salary. Also tried "I am now the richest person in
     the building" — dropped, "highest-paid" is the salary word, and the
     joke is about pay, not wealth.

The line is deliberately different from our already-submitted office lines
(the reply-all line, the IT ticket line, the shared-screen line): no email,
no ticket, no meeting, no screen — a raise, a pizza party, and a salary
paid in slices.
"""

import os

MAX_CHARS = 200

LINE = (
    "I asked for a raise and got a pizza party. "
    "I am now the highest-paid person in the building, in slices."
)


def check_gate(text):
    """Mirror the sealed gate: 1-200 chars, not only whitespace, one line."""
    return bool(text) and len(text) <= MAX_CHARS and text.strip() and "\n" not in text


def entry_path():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out, exist_ok=True)
    return os.path.join(out, "entry.txt")


def main():
    assert check_gate(LINE), "line fails the 1-200 char gate"
    with open(entry_path(), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
