# --- Day 10: Elves Look, Elves Say ---
#
#
# Today, the Elves are playing a game called look-and-say (https://en.wikipedia.org/wiki/Look-and-say_sequence). They take turns
# making sequences by reading aloud the previous sequence and using that
# reading as the next sentence. For example, 211 is read as "one two, two
# ones", which becomes 1221 (1 2, 2 1s).
#
# Look-and-say sequences are generated iteratively, using the previous value
# as input for the next step. For each step, take the previous value, and
# replace each run of digits (like 111) with the number of digits (3)
# followed by the digit itself (1).
#
# For example:
#  - 1 becomes 11 (1 copy of digit 1).
#  - 11 becomes 21 (2 copies of digit 1).
#  - 21 becomes 1211 (one 2 followed by one 1).
#  - 1211 becomes 111221 (one 1, one 2, and two 1s).
#  - 111221 becomes 312211 (three 1s, two 2s, and one 1).
#
# Starting with the digits in your puzzle input, apply this process 40 times.
# What is the length of the result?
#
# Your puzzle input is 1113122113.

input = "1113122113"

def partOne(input: str, steps: int) -> str:
  res = input
  for i in range(0, steps):
    newRes = ""
    counter, j = 1, 1
    lastC = res[0]
    if (len(res) == 1): return "1" + lastC
    while (j < len(res)):
      c = res[j]
      if (c == lastC): counter += 1
      else:
        newRes += str(counter) + lastC
        lastC = c
        counter = 1
      j += 1
    newRes += str(counter) + lastC
    res = newRes
  return len(res)

print("Part One: " + str(partOne(input, 40))) # 360154


# --- Part Two ---
#
#
# Neat, right? You might also enjoy hearing
# John Conway talking about this sequence (https://www.youtube.com/watch?v=ea7lJkEhytA) (that's Conway Game of
# Life fame)
#
# Now, starting again with the digits in your puzzle input, apply this
# process 50 times. What is the length of the new result?

print("Part Two: " + str(partOne(input, 50))) # 5103798