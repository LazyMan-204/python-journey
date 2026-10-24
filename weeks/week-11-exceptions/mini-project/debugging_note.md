# Week 11 Mini-project — Robust Bot Debugging Note

## Minimal failing input

The distance helper received `position=1` and `goal=4`. The original expression `position - goal` returned `-3`, which violates the distance function's non-negative contract.

## Failure and root cause

- **Failure type:** incorrect result / invariant violation (not an input parsing exception).
- **Observed result:** `distance(1, 4) == -3`.
- **Expected result:** `3`.
- **Root cause:** subtraction order was treated as if it always produced a non-negative distance.

## Fix

Use `abs(position - goal)` so the result is non-negative regardless of argument order.

## Regression checks

The solution checks `distance(1, 4) == 3`, `distance(4, 1) == 3`, and `distance(3, 3) == 0`.

## Strategy weakness vs. software defect

A strategy loss occurs when the bot follows its contract but makes a poor decision. A software defect includes a crash, malformed replay, illegal local action, or a broken invariant such as a negative distance. Exceptions should be handled at a meaningful boundary and logged visibly; they should not be silently swallowed.

## Debugging loop

Reproduce → read traceback or failure reason → isolate → apply the smallest fix → re-test.
