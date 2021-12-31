# --- Day 9: All in a Single Night ---
#
#
# Every year, Santa manages to deliver all of his presents in a single night.
#
# This year, however, he has some new locations to visit; his elves have provided him the distances between every pair of locations. He can start
# and end at any two (different) locations he wants, but he must visit each
# location exactly once. What is the shortest distance he can travel to
# achieve this?
#
# For example, given the following distances:
#  London to Dublin = 464
#  London to Belfast = 518
#  Dublin to Belfast = 141
#
# The possible routes are therefore:
#  Dublin -> London -> Belfast = 982
#  London -> Dublin -> Belfast = 605
#  London -> Belfast -> Dublin = 659
#  Dublin -> Belfast -> London = 659
#  Belfast -> Dublin -> London = 605
#  Belfast -> London -> Dublin = 982
#
# The shortest of these is London -> Dublin -> Belfast = 605, and so the
# answer is 605 in this example.
#
# What is the distance of the shortest route?

from os import path
import sys

nodes, links = set[str](), dict[str, dict[str, int]]()

with open(path.join(sys.path[0], "input\\9_All_in_a_Single_Night.txt")) as f:
  for line in f:
    line = line.strip()
    parts = line.split(" to ")
    source, destinationAndCost = parts[0], parts[1]
    destination, cost = parts[1].split(" = ")[0], parts[1].split(" = ")[1]
    nodes.add(source)
    nodes.add(destination)
    costs = links.get(source)
    if (costs == None): links.update({source : {destination : int(cost)}})
    else:
      costs.update({destination : int(cost)})
      links.update({source : costs})

def partOne(nodes: set[str], links: list[str]) -> int:
  