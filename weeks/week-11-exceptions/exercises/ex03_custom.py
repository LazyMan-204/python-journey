"""Exercise 03: reproduce and fix a defect."""


def distance(position: int, goal: int) -> int:
    """Return the absolute distance from position to goal."""
    return abs(position - goal)


if __name__ == "__main__":
    # Regression check for the original failing input (1, 4).
    assert distance(1, 4) == 3
    assert distance(4, 1) == 3
    assert distance(3, 3) == 0
    print("Distance regression checks: PASS")
