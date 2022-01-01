# --- Day 12: JSAbacusFramework.io ---
#
#
# Santa's Accounting-Elves need help balancing the books after a recent
# order. Unfortunately, their accounting software uses a peculiar storage
# format. That's where you come in.
#
# They have a JSON (https://www.json.org/json-en.html) document which contains a variety of things: arrays (
# [1,2,3]), objects ({"a":1, "b":2}), numbers, and strings. Your first job is
# to simply find all of the numbers throughout the document and add them together.
#
# For example:
#  - [1, 2, 3] and {"a":1, "b":2} both have a sum of 6.
#  - [[[3]]] and {"a":{"b":4},"c":-1} both have a sum of 3.
#  - {"a":[-1,1]} and [-1,{"a":1}] both have a sum of 0.
#  - [] and {} both have a sum of 0.
#
# You will not encounter any strings containing numbers.
#
# What is the sum of all numbers in the document?

from os import path
import sys
import json

js = {}

with open(path.join(sys.path[0], "input\\12_JSAbacusFramework.io.txt")) as f:
  js = json.load(f)

def partOne(js) -> int:
  def reduce(el) -> int:
    if type(el) is int: return el
    elif type(el) is list:
      s = 0
      for l in el: s += reduce(l)
      return s
    elif type(el) is dict:
      s = 0
      for l in el.values(): s += reduce(l)
      return s
    else: return 0
  return reduce(js)
    
print("Part One: " + str(partOne(js)))


# --- Part Two ---
#
#
# Uh oh - the Accouting-Elves have realized that they double-counted
# everything red.
#
# Ignore any object (and all of its children) which has any property with the
# value "red". Do this only for objects ({...}), not arrays ([...]).
#
#  - [1,2,3] still has a sum of 6.
#  - [1,{"c":"red","b":2},3] now has a sum of 4, because the middle object is ignored.
#  - {"d":"red","e":[1,2,3,4],"f":5} now has a sum of 0, because the entire structure is ignored.
#  - [1,"red",5] has a sum of 6, because "red" in an array has no effect.

def partTwo(js) -> int:
  def reduce(el) -> int:
    if type(el) is int: return el
    elif type(el) is list:
      s = 0
      for l in el: s += reduce(l)
      return s
    elif type(el) is dict:
      if "red" in el.values(): return 0
      else:
        s = 0
        for l in el.values(): s += reduce(l)
        return s
    else: return 0
  return reduce(js)

print("Part Two: " + str(partTwo(js)))