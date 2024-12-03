import os
import re

class Day3:
    def inputPasser(self, raw_data):
        pattern = r'mul\s*\(\s*(\d+)\s*,\s*(\d+)\s*\)'
        matches = re.findall(pattern, raw_data)
        results = []
        for match in matches:
            try:
                num1 = int(match[0])
                num2 = int(match[1])
                result = self.mul(num1, num2)
                results.append(result)
            except ValueError:
                continue
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