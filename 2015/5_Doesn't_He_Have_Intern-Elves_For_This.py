# --- Day 5_ Doesn't He Have Intern-Elves For This? ---
#
#
# Santa needs help figuring out which strings in his text file are naughty or nice.
#
# A nice string is one with all of the following properties:
#
#  - It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
#  - It contains at least one letter that appears twice in a row, like xx,
#  abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
#  - It does not contain the strings ab, cd, pq, or xy, even if they are
#  part of one of hte other requirements.
#
# For example:
#  - ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed
#  substrings.
#  - aaa is nice because it has at least three vowels and a double letter,
#  even though the letters used by different rules overlap.
#  - jchzalrnumimnmhp is naughty because it has no double letter.
#  - haegwjzuvuyypxyu is naughty because it contains the string xy.
#  - dvszwmarrgswjxmb is naughty because it contains only one vowel.
#
# How many strings are nice?

from os import path
import sys

inputList = list[str]()

with open(path.join(sys.path[0], "input\\5_Doesn't_He_Have_Intern-Elves_For_This.txt")) as f:
  for line in f:
    line = line.strip()
    inputList.append(line)

def partOne(input: list[str]) -> int:
  nice = 0

  for string in input:
    if (("ab" not in string) and ("cd" not in string) and ("pq" not in string) and ("xy" not in string)):
      vowels = 0
      for c in "aeiou":
        vowels += string.count(c)
        if (vowels >= 3): break
      if (vowels >= 3):
        for i in range(0, len(string) - 1):
          if (string[i] == string[i + 1]):
            nice += 1
            break
  
  return nice

print("Part One: " + str(partOne(inputList))) # 236