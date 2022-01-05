# --- Day 19: Medicine for Rudolph ---
#
#
# Rudolph the Red-Nosed Reindeer is sick! His nose isn't shining very
# brightly, and he needs medicine.
#
# Red-Nosed Reindeer biology isn't similar to regular reindeer biology;
# Rudolph is going to need custom-made medicine. Unfortunately, Red-Nosed
# Reindeer chemistry isn't similar to regular reindeer chemistry, either.
#
# The North Pole is equipped with a Red-Nosed Reindeer nuclear fusion/fission
# plant, capable of constructing any Red-Nosed Reindeer molecule you need. It
# works by starting with some input molecule and then doing a series of
# replacements, one per step, until it has the right molecule.
#
# However, the machine has to be calibrated before it can be used.
# Calibration involves determining the number of molecules that can be
# generated in one step from a given starting point.
#
# For example, imagine a simpler machine that supports only the following
# replacements:
#   H => HO
#   H => OH
#   O => HH
#
# Given the replacements above and starting with HOH, the following molecules
# could be generated:
#  - HOOH (via H => HO on the first H).
#  - HOHO (via H => HO on the second H).
#  - OHOH (via H => OH on the first H).
#  - HOOH (via H => OH on the second H).
#  - HHHH (via O => HH).
#
# So, in the example above, there are 4 distinct molecules (not five, because
# HOOH appears twice) after one replacement from HOH. Santa's favorite
# molecule, HOHOHO, can become 7 distinct molecules (over nine replacements:
# six from H and three from O).
#
# The machine replaces without regard for the surrounding characters. For
# example, given the string H2O, the transition H => OO would result in OO2O.
#
# Your puzzle input describes all of the possible replacements and, at the
# bottom, the medicine molecule for which you need to calibrate the machine.
# How many distinct molecules can be created after all the different ways you
# can do one replacement on the medicine molecule?

from os import path
import sys

productions = dict[str, list[str]]()
string: str

with open(path.join(sys.path[0], "input\\19_Medicine_for_Rudolph.txt")) as f:
  for line in f:
    line = line.strip()
    if line != "":
      if " => " in line:
        parts = line.split(" => ")
        alfa, beta = parts[0], parts[1]
        if alfa in productions.keys(): productions[alfa].append(beta)
        else: productions.update({alfa : [beta]})
      else: string = line

def partOne(productions: dict, string: str):

  def prepareString(string: str) -> list[str]:
    tokens = list[str]()
    token = ""
    i = 0
    while (i < len(string)):
      c = string[i]
      token += c
      if not c.isupper():
        print(c)
        tokens.append(token)
        token = ""
      i += 1
    return tokens

  molecules = set[str]()
  tokens = prepareString(string)
  print(tokens)
  counter = 0

print("Part One: " + str(partOne(productions, string)))