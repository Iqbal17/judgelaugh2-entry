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

Revision pass (pipeline review, output byte-identical):
  E. "My salary was frozen, so now I defrost it one pizza slice at a
     time." — LOSES. It keeps the pizza-as-pay idea but turns it into a
     freezer pun; the judge criteria put a true observation ahead of
     wordplay, and C's observation (a party literally given instead of a
     raise) is the lived experience, not a metaphor built on "frozen".
  F. "HR said compensation is competitive. It is: my paycheck is in a
     close race with the pizza budget." — LOSES, close. Fresh framing and
     a real turn, but it needs two sentences of setup to land and the race
     image blurs who won; C lands the same pay-versus-pizza contrast in
     one clean claim the reader can repeat verbatim.
  G. "I got a 3 percent raise and a 100 percent pizza." — LOSES. Tight,
     but the percentages are invented precision — the joke reads as a
     statistic, not a story, and there is no person in it; C's "I am now
     the highest-paid person in the building" gives the line a narrator
     whose pride in slices is the laugh.
Decision after revision: keep C exactly as written. The only code change
in this pass is structural: a dedicated gate-guard helper (guard_line)
that rejects empty, oversized, or multi-line candidates before the
existing gate check runs, so a future edit to LINE fails loudly at the
guard instead of silently writing a bad entry file. The shipped line,
its wording, and the bytes written to entry.txt are unchanged.
"""

import os

MAX_CHARS = 200

LINE = (
    "I asked for a raise and got a pizza party. "
    "I am now the highest-paid person in the building, in slices."
)


def guard_line(text):
    """Gate-guard: reject empty, oversized, or multi-line candidates early.

    Runs before check_gate so a bad future edit to LINE fails with a
    specific reason instead of a generic gate failure at write time.
    """
    if not isinstance(text, str) or text.strip() == "":
        raise SystemExit("guard: line is empty or not text")
    if len(text) > MAX_CHARS:
        raise SystemExit("guard: line exceeds the 200 character gate")
    if "\n" in text or "\r" in text:
        raise SystemExit("guard: line must be a single line")
    return text


def check_gate(text):
    """Mirror the sealed gate: 1-200 chars, not only whitespace, one line."""
    return bool(text) and len(text) <= MAX_CHARS and text.strip() and "\n" not in text


def entry_path():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out, exist_ok=True)
    return os.path.join(out, "entry.txt")


def main():
    guard_line(LINE)
    assert check_gate(LINE), "line fails the 1-200 char gate"
    with open(entry_path(), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
