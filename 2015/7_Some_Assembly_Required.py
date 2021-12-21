# --- Day 7: Some Assembly Required ---
#
#
# This year, Santa brought little Bobby Tables a set of wires and
# bitwise logic gates (https://en.wikipedia.org/wiki/Bitwise_operation)! Unfortunately, little Bobby is a little under the
# recommended age range, and he needs help assembling the circuit.
#
# Each wire has an identifier (some lowercase letters) and carry a 16-bit (https://en.wikipedia.org/wiki/16-bit)
# signal (a number from 0 to 65535). A signal is probided to each wire by a
# gate, another wire, or some specific value. Each wire can only get a signal
# from one source, but can provide its signal to multiple destinations. A
# gate provides no signal until all of its inputs have a signal.
#
# The included instructions booklet describes how to connect the parts
# together: x AND y -> z means to connect wires x and y to an AND gate, and
# then connect its output to wire z.
#
# For example:
#  - 123 -> z means that the signal 123 is provided to wire x.
#  - x AND y -> z means that the bitwise AND (https://en.wikipedia.org/wiki/Bitwise_operation#AND) of wire x and wire y is
#  provided to wire z.
#  - p LSHIFT 2 -> q means that the value from wire p is left-shifted (https://en.wikipedia.org/wiki/Logical_shift) by 2
#  and then provided to wire q.
#  - NOT e -> f means that the bitwise complement (https://en.wikipedia.org/wiki/Bitwise_operation#NOT) of the value from wire e
#  is provided to wire f.
#
# Other possible gates include OR (bitwise OR (https://en.wikipedia.org/wiki/Bitwise_operation#OR)) and RSHIFT (right-shift (https://en.wikipedia.org/wiki/Logical_shift)). If,
# for some reason, you'd like to emulate the circuit instead, almost all
# programming languages (for example, C (https://en.wikipedia.org/wiki/Bitwise_operations_in_C), JavaScript (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators), or Python (https://wiki.python.org/moin/BitwiseOperators)) provide
# operators for these gates.
#
# For example, here is a simple circuit:
#   123 -> x
#   456 -> y
#   x AND y -> d
#   x OR y -> e
#   x LSHIFT 2 -> f
#   y RSHIFT 2 -> g
#   NOT x -> h
#   NOT y -> i
#
# After it is run, these are the signals on the wires:
#   d: 72
#   e: 507
#   f: 492
#   g: 114
#   h: 65412
#   i: 65079
#   x: 123
#   y: 456
#
# In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?

from os import access, path
import sys
from typing import Tuple

instructions = list[str]()

with open(path.join(sys.path[0], "input\\7_Some_Assembly_Required.txt")) as f:
  for line in f:
    line = line.strip()
    instructions.append(line)

def partOne(instructions: list[str]) -> int:

  # Extracts operands in an instructions
  def findOperands(instruction: str) -> Tuple[str, str]:
    if (instruction.startswith("NOT")): instruction = instruction[4:]
    operands = instruction.split(" -> ")
    return operands[0], operands[1]
  
  # If the operands are values, leaves them as is, else (they are registers), access them;
  # if they are in memory, leave them as is, else (they are not in memory) use the default value.
  def accessRegisters(firstOperand: str, secondOperand: str):
    if (firstOperand.isdigit()):
          if (not secondOperand.isdigit()):
            secondOperand = memory.get(secondOperand)
            if (secondOperand == None): secondOperand = defVal
    else:
      if (secondOperand.isdigit()):
        firstOperand = memory.get(firstOperand)
        if (firstOperand == None): firstOperand = defVal
      else:
        firstOperand = memory.get(firstOperand)
        secondOperand = memory.get(secondOperand)
        if (firstOperand == None): firstOperand = defVal
        if (secondOperand == None): secondOperand = defVal
  
    return firstOperand, secondOperand

  # Dictionary object used as memory
  memory = dict[str, int]()

  # Default value used for empty registers
  defVal = 0
  
  # Compute each instruction
  for instruction in instructions:
    if (instruction.startswith("NOT")):
      # If the instruction is a NOT instruction, find the operands, then if the left operand
      # is a digit, perform the NOT operation and save the result in the target register,
      # else (the left operand is a register) access the register; if they are in memory,
      # leave them as is, else (they are not in memory) use the default value.
      # Perform the NOT operation and save the result in the target register.
      leftOperand, targetRegister = findOperands(instruction)
      if (leftOperand.isdigit()): memory.update({targetRegister : 65535 - int(leftOperand)})
      else:
        operand = memory.get(leftOperand)
        if (operand == None): operand = defVal
        memory.update({targetRegister : 65535 - int(operand)})
    else:
      # If the instraction is not a NOT instruction, it is either an assignment or a binary
      # operation. Either way, find the operands
      leftOperand, targetRegister = findOperands(instruction)
      if ("AND" in leftOperand):
        # The instruction is an AND instruction, find the operands, perform the AND operation
        # and save the result in the target register.
        operands = leftOperand.split(" AND ")
        firstOperand, secondOperand = operands[0], operands[1]
        firstOperand, secondOperand = accessRegisters(firstOperand, secondOperand)
        memory.update({targetRegister : int(firstOperand) & int(secondOperand)})
      elif ("OR" in leftOperand):
        # The instruction is an OR instruction, find the operands, perform the OR operation
        # and save the result in the target register.
        operands = leftOperand.split(" OR ")
        firstOperand, secondOperand = operands[0], operands[1]
        firstOperand, secondOperand = accessRegisters(firstOperand, secondOperand)
        memory.update({targetRegister : int(firstOperand) | int(secondOperand)})
      elif ("LSHIFT" in leftOperand):
        # The instruction is a LEFT SHIFT instruction, find the operands, perform the LEFT SHIFT
        # operation and save the result in the target register
        operands = leftOperand.split(" LSHIFT ")
        firstOperand, secondOperand = operands[0], operands[1]
        firstOperand, secondOperand = accessRegisters(firstOperand, secondOperand)
        memory.update({targetRegister : int(firstOperand) << int(secondOperand)})
      elif ("RSHIFT" in leftOperand):
        # The instruction is a RIGHT SHIFT instruction, find the operands, perform the RIGHT SHIFT
        # operation and save the result in the target register
        operands = leftOperand.split(" RSHIFT ")
        firstOperand, secondOperand = operands[0], operands[1]
        firstOperand, secondOperand = accessRegisters(firstOperand, secondOperand)
        memory.update({targetRegister : int(firstOperand) >> int(secondOperand)})
      else:
        # The instruction is an assignment, either from a register or a direct assignment
        if (leftOperand.isdigit()): memory.update({targetRegister : int(leftOperand)})
        else:
          leftOperand = memory.get(leftOperand)
          if (leftOperand == None): leftOperand = defVal
          memory.update({targetRegister : leftOperand})
  
  return memory

print("Part One: " + str(partOne(instructions).get("a")))