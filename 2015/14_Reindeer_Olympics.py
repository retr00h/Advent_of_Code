# --- Day 14: Reindeer Olympics ---
#
#
# This year is the Reindeer Olympics! Reindeer can fly at high speeds, but
# must rest occasionally to recover their energy. Santa would like to know
# which of his reindeer is fastest, and so he has them race.
#
# Reindeer can only either be flying (always at their top speed) or resting
# (not moving at all), and always spend whole seconds in either state.
#
# For example, suppose you have the following Reindeer:
#  - Comet can fly 14 km/s for 10 seconds, but then must rest for 127
#  seconds.
#  - Dancer can fly 16 mm/s for 11 seconds, but then must rest for 162 seconds.
#
# After one second, Comet has gone 14 km, while Dancer has gone 16 km. After
# ten seconds, Comet has gone 140 km, while Dancer has gone 160 km. On the
# eleventh second, Comet begins resting (staying at 140 km), and Dancer
# continues on for a total distance of 176 km. On the 12th second, both
# reindeer are resting. They continue to rest until the 138th second, when
# Comet flies for another ten seconds. On the 174th second, Dancer flies for another 11 seconds.
#
# In this example, after the 100th second, both reindeer are resting, and
# Comet is in the lead at 1120 km (poor Dancer has only gotten 1056 km by
# that point). So, in this situation, Comet would win (if the race ended at
# 1000 seconds).
#
# Given the descriptions of each reindeer (in your puzzle input), after
# exactly 2503 seconds, what distance has the winning reindeer traveled?

from os import path
import sys

reindeers = dict[str, dict[str, int]]()

with open(path.join(sys.path[0], "input\\14_Reindeer_Olympics.txt")) as f:
  for line in f:
    line = line.strip()
    parts = line.split(' ')
    name, speed, travelTime, restingTime = parts[0], parts[3], parts[6], parts[13]
    reindeers.update({name : {"speed" : int(speed), "travelTime" : int(travelTime), "restingTime" : int(restingTime)}})

def partOne(reindeers: dict, seconds: int) -> int:
  res = None
  for r in reindeers:
    counter, resting, distance = 0, False, 0
    travelTime = reindeers[r]["travelTime"]
    speed = reindeers[r]["speed"]
    restingTime = reindeers[r]["restingTime"]
    for i in range(0, seconds):
      if resting:
        if counter < restingTime:
          counter += 1
        else:
          counter = 0
          resting = False
      else:
        if counter < travelTime:
          counter += 1
          distance += speed
        else:
          counter = 0
          resting = True
      if i == seconds - 1:
        if res == None: res = distance
        elif distance > res: res = distance
    print(res)
  return res

testReindeers = {'Comet' : {'speed' : 14, 'travelTime' : 10, 'restingTime' : 127},
  'Dancer' : {'speed' : 16, 'travelTime' : 11, 'restingTime' : 162}}
print("Test: " + str(partOne(testReindeers, 1000)))

print("Part One: " + str(partOne(reindeers, 2503)))