# --- Day 13: Knights of the Dinner Table ---
#
#
# In years past, the holiday feast with your famil hasn't gone so well. Not
# everyone gets along! This year, you resolve, will be different. You're
# going to find the optimal seating arrangement and avoid all those awkward
# conversations.
#
# You start by writing up a list of everyone invited and the amount their
# happiness would increase or decrease if they were to find themselves
# sitting next to each other person. You have a circular table that will be
# just big enough to fit everyone comfortably, and so each person will have
# exactly two neighbors.
#
# For example, suppose you have only four attendees planned, and you
# calculate their potential happiness as follows:
#   Alice would gain 54 happiness units by sitting next to Bob.
#   Alice would lose 79 happiness units by sitting next to Carol.
#   Alice would lose 2 happiness units by sitting next to David.
#   Bob would gain 83 happiness units by sitting next to Alice.
#   Bob would lose 7 happiness units by sitting next to Carol.
#   Bob would lose 63 happiness units by sitting next to David.
#   Carol would lose 62 happiness units by sitting next to Alice.
#   Carol would gain 60 happiness units by sitting next to Bob.
#   Carol would gain 55 happiness units by sitting next to David.
#   David would gain 46 happiness units by sitting next to Alice.
#   David would lose 7 happiness units by sitting next to Bob.
#   David would gain 41 happiness units by sitting next to Carol.
#
# Then, if you seat Alice next to David, Alice would lose 2 happiness units
# (because David talks too much), but David would gain 46 happiness units
# (because Alice is such a good listener), for a total change of 44.
#
# If you continue around the table, you could then seat Bob next to Alice
# (Bob gains 83, Alice gains 54). Finally, seat Carol, who sits next to Bob
# (Carol gains 60, Bob loses 7) and David (Carol gains 55, David gains 41).
# The arrangement looks like this:
#       +41 +46
#   +55   David    -2
#   Carol       Alice
#   +60    Bob    +54
#       -7  +83
#
# After trying every other seating arrangement in this hypothetical scenario,
# you find that this one is the most optimal, with a total change in
# happiness of 330.
#
# What is the total change in happiness for the optimal seating arrangement
# of the actual guest list?

from os import path
import sys
from itertools import permutations

guests = {}

with open(path.join(sys.path[0], "input\\13_Knights_of_the_Dinner_Table.txt")) as f:
  for line in f:
    line = line.strip()
    line = line.split(' ')
    guest1, happiness,  guest2 = line[0], "", line[-1][:-1]
    if (line[2] == "gain"): happiness = int(line[3])
    else: happiness = int('-' + line[3])
    # {'Alice' : {'Bob' : 54, 'Carol' : -81}, 'Bob' : {}}
    if (guests.get(guest1) == None): guests.update({guest1 : {guest2 : happiness}})
    else: guests.get(guest1).update({guest2 : happiness})

def partOne(guests: dict) -> int:
  happiestTable = 0
  for table in permutations(guests.keys()):
    happiness = 0
    for i in range(0, len(table)):
      if (i == 0): happiness += guests[table[i]][table[-1]] + guests[table[i]][table[1]]
      elif (i == len(table) - 1): happiness += guests[table[i]][table[i - 1]] + guests[table[i]][table[0]]
      else: happiness += guests[table[i]][table[i - 1]] + guests[table[i]][table[i + 1]]
    if happiness > happiestTable: happiestTable = happiness
  return happiestTable

print("Part One: " + str(partOne(guests))) # 709


# --- Part Two ---
#
#
# In all the commotion, you realize that you forgot to seat yourself. At this
# point, you're pretty apathetic toward the whole thing, and your happiness
# wouldn't really go up or down regardless of who you sit next to. You assume
# everyone else would be just as ambivalent about sitting next to you, too.
#
# So, add yourself to the list, and give all the happiness relationships that
# involve you a score of 0.
#
# What is the total change in happiness for the optimal seating arrangement
# that actually includes yourself?

def partTwo(guests: dict) -> int:
  for key in guests.keys():
    guests.get(key).update({"Me" : 0})
  guests.update({"Me" : None})
  for key in guests.keys():
    if (key != "Me"):
      if (guests.get("Me") == None): guests.update({"Me" : {key : 0}})
      else: guests.get("Me").update({key : 0})

  return partOne(guests)

print("Part Two: " + str(partTwo(guests))) # 668