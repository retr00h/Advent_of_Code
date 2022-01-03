# --- Day 15: Science for Hungry People ---
#
#
# Today, you set out on the task of perfecting your milk-dunking cookie
# recipe. All you have to do is find the right balance of ingredients.
#
# Your recipe leaves room for exactly 100 teaspoons of ingredients. You make
# a list of the remaining ingredients you could use to finish the recipe
# (your puzzle input) and their properties per teaspoon:
#  - capacity (how well it helps the cookie absorb milk)
#  - durability (how well it keeps the cookie intact when full of milk)
#  - flavor (how tasty it makes the cookie)
#  - texture (how it improves the feel of the cookie)
#  - calories (how many calories it adds to the cookie)
#
# You can only measure ingredients in whole-teaspoons amounts accurately, and
# you have to be accurate so you can reproduce your results in the future.
# The total score of a cookie can be found by adding up each of the
# properties (negative totals become 0) and then multiplying together
# everything except calories.
#
# For instance, suppose you have these two ingredients:
#   Butterschotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
#   Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
#
# Then, choosing to use 44 teaspoons of butterschotch and 56 teaspoons of
# cinnamon (because the amounts of each ingredient must add up to 100) would
# result in a cookie with the following properties:
#  - A capacity of 44*-1 + 56*2 = 68
#  - A durability of 44*-2 + 56*3 = 80
#  - A flavor of 44*6 + 56*-2 = 152
#  - A texture of 44*3 + 56*-1 = 76
#
# Multiplying these together (68 * 80 / 152 * 76, ignoring calories for now)
# results in a total score of 62842880, which happens to be the best score
# possible given these ingredients. If any properties had produced a negative
# total, it would have instead become zero, causing the whole score to multiply to zero.
#
# Given the ingredients in your kitchen and their properties, what is the
# total score of the highest-scoring cookie you can make?

from os import path
import sys

ingredients = dict[str, dict[str, int]]()

with open(path.join(sys.path[0], "input\\15_Science_for_Hungry_People.txt")) as f:
  for line in f:
    line = line.strip()
    parts = line.split(' ')
    name = parts[0][:-1]
    capacity = int(parts[2][:-1])
    durability = int(parts[4][:-1])
    flavor = int(parts[6][:-1])
    texture = int(parts[8][:-1])
    calories = int(parts[10])
    ingredient = {name : {'capacity' : capacity, 'durability' : durability,
      'flavor' : flavor, 'texture' : texture, 'calories' : calories}}
    ingredients.update(ingredient)

def partOne(ingredients: dict) -> int:
  m = 0
  for a in range(1, 97):
    for b in range(1, 97):
      for c in range(1, 97):
        for d in range(1, 97):
          if (a + b + c + d == 100):
            totalCapacity = a * ingredients['Sprinkles']['capacity'] + b * ingredients['Butterscotch']['capacity'] + c * ingredients['Chocolate']['capacity'] + d * ingredients['Candy']['capacity']
            totalDurability = a * ingredients['Sprinkles']['durability'] + b * ingredients['Butterscotch']['durability'] + c * ingredients['Chocolate']['capacity'] + d * ingredients['Candy']['durability']
            totalFlavor = a * ingredients['Sprinkles']['flavor'] + b * ingredients['Butterscotch']['flavor'] + c * ingredients['Chocolate']['flavor'] + d * ingredients['Candy']['flavor']
            totalTexture = a * ingredients['Sprinkles']['texture'] + b * ingredients['Butterscotch']['texture'] + c * ingredients['Chocolate']['texture'] + d * ingredients['Candy']['texture']
            if totalCapacity < 0: totalCapacity = 0
            if totalDurability < 0: totalDurability = 0
            if totalFlavor < 0: totalFlavor = 0
            if totalTexture < 0: totalTexture = 0
            total = totalCapacity * totalDurability * totalFlavor * totalTexture
            if total > m: m = total
  return m

print("Part One: " + str(partOne(ingredients))) # 21367368


# --- Part Two ---
#
#
# Your cookie recipe becomes wildly popular! Someone asks if you can make
# another recipe that has exactly 500 calories per cookie (so they can use it
# as a meal replacement). Keep the rest of your award-winning process the
# same (100 teaspoons, same ingredients, same scoring system).
#
# For example, given the ingredients above, if you had instead selected 40
# teaspoons of butterscotch and 60 teaspoons of cinnamon (which still adds to
# 100), the total calorie count would be 40*8 + 60*3 = 500. The total score
# would go down, though: only 57600000, the best you can do un such trying
# circumstances.
#
# Given the ingredients in your kitchen and their properties, what is the
# total score of the highest-scoring cookie you can make with a calorie total
# of 500?


def partTwo(ingredients: dict) -> int:
  m = 0
  for a in range(1, 97):
    for b in range(1, 97):
      for c in range(1, 97):
        for d in range(1, 97):
          if (a + b + c + d == 100):
            totalCalories = a * ingredients['Sprinkles']['calories'] + b * ingredients['Butterscotch']['calories'] + c * ingredients['Chocolate']['calories'] + d * ingredients['Candy']['calories']
            if (totalCalories == 500):
              totalCapacity = a * ingredients['Sprinkles']['capacity'] + b * ingredients['Butterscotch']['capacity'] + c * ingredients['Chocolate']['capacity'] + d * ingredients['Candy']['capacity']
              totalDurability = a * ingredients['Sprinkles']['durability'] + b * ingredients['Butterscotch']['durability'] + c * ingredients['Chocolate']['capacity'] + d * ingredients['Candy']['durability']
              totalFlavor = a * ingredients['Sprinkles']['flavor'] + b * ingredients['Butterscotch']['flavor'] + c * ingredients['Chocolate']['flavor'] + d * ingredients['Candy']['flavor']
              totalTexture = a * ingredients['Sprinkles']['texture'] + b * ingredients['Butterscotch']['texture'] + c * ingredients['Chocolate']['texture'] + d * ingredients['Candy']['texture']
              if totalCapacity < 0: totalCapacity = 0
              if totalDurability < 0: totalDurability = 0
              if totalFlavor < 0: totalFlavor = 0
              if totalTexture < 0: totalTexture = 0
              total = totalCapacity * totalDurability * totalFlavor * totalTexture
              if total > m: m = total
  return m

print("Part Two: " + str(partTwo(ingredients))) # 1766400