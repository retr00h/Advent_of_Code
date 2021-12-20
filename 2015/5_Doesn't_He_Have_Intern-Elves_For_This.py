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


# --- Part Two ---
#
#
# Realizing the error of his ways, Santa has switched to a better model of
# determining whether a string is naughty or nice. None of the old rules
# apply, as they are all clearly ridiculous.
#
# Now, a nice string is one with all of the following properties:
#  - It contains a pair of any two letters that appears at least twice in
#  the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but
#  not like aaa (aa, but it overlaps).
#  - It contains at least one letter which repeats with exactly one letter
#  between them, like xyx, abcdefeghi (efe), or even aaa.
#
# For example:
#  - qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj)
#  and a letter that repeats with exactly one letter between them (zxz).
#  - xxyxx is nice because it has a pair that appears twice and a letter
#  that repeats with one between, even though the letters used by each
#  rule overlap.
#  - uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat
#  with a single letter between them.
#  - ieodomkazucvgmuy is naughty because it has a repeating letter with one
#  between (odo), but no pair that appears twice.
#
# How many strings are nice under these new rules?

from itertools import count

def partTwo(input: list[str]) -> int:
  nice = 0

  for string in input:
    twice: list[chr] = []
    for c in "abcdefghijklmnopqrstuvwxyz":
      if (string.count(c) >= 2): twice.append(c)
      
    pairs = list[str]()
    for ch1 in twice:
      for ch2 in twice:
        pairs.append(ch1 + ch2)

    containsPair = False
    for pair in pairs:
      firstIndex = string.find(pair)
      if (firstIndex != -1):
        secondIndex = string[firstIndex + 1 : ].find(pair)
        if (secondIndex != -1 and secondIndex - firstIndex >= 2):
          containsPair = True
          break
    
    if (containsPair):
      containsTriple = False
      for i in range(1, len(string) - 1):
        if (string[i - 1] == string[i + 1]):
          containsTriple = True
          break
      
      if (containsTriple): nice += 1
  
  return nice

print("Part Two: " + str(partTwo(inputList))) # 25 INCORRECT

# print(partTwo(["qjhvhtzxzqqjkmpb"]) == 1)
# print(partTwo(["xxyxx"]) == 1)
# print(partTwo(["uurcxstgmygtbstg"]) == 1)
# print(partTwo(["ieodomkazucvgmuy"]) == 1)