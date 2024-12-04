import os
import re

class Day3:
    def inputPasser(self, raw_data):
        pattern = r'mul\s*\(\s*(\d+)\s*,\s*(\d+)\s*\)'
        do = r'do\s*\(\s*\)'
        dont = r"don't\s*\(\s*\)"

        instructions = re.findall(r'do\s*\(\s*\)|don\'t\s*\(\s*\)|mul\s*\(\s*\d+\s*,\s*\d+\s*\)', raw_data)

        mul_enabled = True  
        results = []

        for instr in instructions:
            if re.fullmatch(do, instr):
                mul_enabled = True
            elif re.fullmatch(dont, instr):
                mul_enabled = False
            elif re.fullmatch(pattern, instr):
                if mul_enabled:
                    num1, num2 = map(int, re.findall(r'\d+', instr))
                    results.append(self.mul(num1, num2))

        return sum(results)

    @staticmethod
    def mul(int1, int2):
        return int1*int2

with open('rawDataDayThree.txt', 'r', encoding='utf-8') as f:
    raw_data = f.read()

day3 = Day3()

results = day3.inputPasser(raw_data)
print("Raw data:", repr(raw_data))
print("Results:", results)