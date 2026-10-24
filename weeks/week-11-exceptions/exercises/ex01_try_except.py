"""Exercise 01: expected bad input."""

raw_turn = "not-a-number"

try:
    turn = int(raw_turn)
except ValueError:
    print(f"Turn must be an integer; received {raw_turn!r}.")
else:
    print(f"Turn: {turn}")
