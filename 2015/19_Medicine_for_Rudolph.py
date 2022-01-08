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

def partOne(productions: dict, string: str) -> int:
  molecules, keys = set[str](), productions.keys()
  for k in keys:
    counter = 0
    index = string.find(k, counter)
    while index != -1:
      for p in productions[k]:
        newMolecule = string[:index] + string[index:].replace(k, p, 1)
        molecules.add(newMolecule)
      counter = index + len(k)
      index = string.find(k, counter)
  return len(molecules)
testProductions = {'H' : ["HO", "OH"], 'O' : ["HH"], 'e' : ['H', 'O']}
testString = "HOH"

# print("Test: " + str(partOne(testProductions, testString)))
print("Part One: " + str(partOne(productions, string))) # 509


# --- Part Two ---
#
#
# Now that the machine is calibrated, you're ready to begin molecule
# fabrication.
#
# Molecule fabrication always begins with just a single electron, e, and
# applying replacements one at a time, just like the ones during calibration.
#
# For example, suppose you have the following replacements:
#   e => H
#   e => O
#   H => HO
#   H => OH
#   O => HH
#
# If you'd like to make HOH, you start with e, and then make the following
# replacements:
#  - e => O to get O
#  - O => HH to get HH
#  H => OH (on the second H) to get HOH
#
# So, you could make HOH after 3 steps. Santa's favourite molecule, HOHOHO,
# can be made in 6 steps.
#
# How long will it take to make the medicine? Given the available
# replacements and the medicine molecule in your puzzle input, what is the
# fewest number of steps to go from e to the medicine molecule?

from time import sleep
from random import shuffle

def partTwo(productions: dict, originalString: str) -> int:
  sortedValues = list[str]()
  for l in productions.values(): sortedValues.extend(l)
  sortedValues = sorted(sortedValues, key = lambda x: len(x))
  sortedValues.reverse()
  steps, stepsToShuffle, oldString = 0, 5, originalString
  string = originalString
  while string != 'e':
    if stepsToShuffle == 0:
      string = oldString = originalString
      stepsToShuffle = 5
      shuffle(sortedValues)
    for v in sortedValues:
      if v in string:
        k = [key for key in productions.keys() if v in productions[key]]
        string = string.replace(v, k[0], 1)
        steps += 1
        break
    
    if string == oldString: stepsToShuffle -= 1
    else: stepsToShuffle == 5
    oldString = string
    # print("String: " + string)
    # print("Steps: " + str(steps))
    # print()
    # sleep(0.1)
  return steps

# print(str(partTwo(testProductions, testString)))
# print("Test: " + str(partTwo(testProductions, "HOH")))
# print()
# print("Test: " + str(partTwo(testProductions, "HOHOHO")))
print("Part Two: " + str(partTwo(productions, string)))