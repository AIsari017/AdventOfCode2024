import os

class Day2:
    def input_formatter(self, raw_data):
        sequences = [
            list(map(int, line.split())) 
            for line in raw_data.strip().split('\n') 
            if line.strip()
        ]
        return sequences

    def safety_check(self, lines):
        def is_safe(sequence):
            is_increasing = all(sequence[i] < sequence[i+1] for i in range(len(sequence)-1))
            is_decreasing = all(sequence[i] > sequence[i+1] for i in range(len(sequence)-1))
            
            if not (is_increasing or is_decreasing):
                return False
            
            for i in range(len(sequence)-1):
                diff = abs(sequence[i+1] - sequence[i])
                if diff < 1 or diff > 3:
                    return False
            
            return True

        if is_safe(lines):
            return True

        # Try removing one level at a time to see if it becomes safe
        for i in range(len(lines)):
            modified_sequence = lines[:i] + lines[i+1:]  # Remove the ith level
            if is_safe(modified_sequence):
                return True

        return False

    def count_safe_lines(self, raw_data):
        sequences = self.input_formatter(raw_data)
        
        print("Sequences:", sequences)

        safe_count = 0
        for seq in sequences:
            is_safe = self.safety_check(seq)
            print(f"Sequence: {seq}, Safe: {is_safe}")
            if is_safe:
                safe_count += 1
        
        return safe_count



with open('rawDataDayTwo.txt', 'r', encoding='utf-8') as f:
    raw_data = f.read()

print("Raw data:")
print(repr(raw_data))  

day2_processor = Day2()

safe_lines_count = day2_processor.count_safe_lines(raw_data)

print(f"Number of safe lines: {safe_lines_count}")
