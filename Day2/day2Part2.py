import os

class Day2:
    """
    A class to process raw data representing sequences of numbers,
    check the safety of each sequence based on specific criteria,
    and count the number of safe sequences.
    """

    def input_formatter(self, raw_data):
        """
        Converts raw input data into a list of sequences of integers.
        Each sequence is extracted from a line of raw data, split by spaces.

        Args:
            raw_data (str): Multiline string containing raw numeric data.

        Returns:
            list: A list of lists where each inner list represents a sequence of integers.
        """
        sequences = [
            list(map(int, line.split())) 
            for line in raw_data.strip().split('\n') 
            if line.strip()  # Ignore empty lines
        ]
        return sequences

    def safety_check(self, lines):
        """
        Checks whether a given sequence of numbers is safe.
        A sequence is considered safe if:
        1. It is either strictly increasing or strictly decreasing.
        2. The absolute difference between consecutive numbers is between 1 and 3 (inclusive).
        Additionally, if the sequence is not safe, the method tries to make it safe
        by removing one element at a time.

        Args:
            lines (list): A list of integers representing a sequence.

        Returns:
            bool: True if the sequence is safe or can be made safe, otherwise False.
        """
        def is_safe(sequence):
            # Check if the sequence is strictly increasing
            is_increasing = all(sequence[i] < sequence[i+1] for i in range(len(sequence)-1))
            # Check if the sequence is strictly decreasing
            is_decreasing = all(sequence[i] > sequence[i+1] for i in range(len(sequence)-1))
            
            # The sequence must be either increasing or decreasing
            if not (is_increasing or is_decreasing):
                return False
            
            # Check the difference between consecutive numbers
            for i in range(len(sequence)-1):
                diff = abs(sequence[i+1] - sequence[i])
                if diff < 1 or diff > 3:
                    return False
            
            return True

        # Check if the sequence is safe as is
        if is_safe(lines):
            return True

        # Try removing one level at a time to see if it becomes safe
        for i in range(len(lines)):
            modified_sequence = lines[:i] + lines[i+1:]  # Remove the ith level
            if is_safe(modified_sequence):
                return True

        return False

    def count_safe_lines(self, raw_data):
        """
        Processes the raw data to count the number of safe sequences.

        Args:
            raw_data (str): Multiline string containing raw numeric data.

        Returns:
            int: The count of sequences that are safe or can be made safe.
        """
        # Convert raw data into formatted sequences
        sequences = self.input_formatter(raw_data)
        
        print("Sequences:", sequences)  # Debug: Print the processed sequences

        safe_count = 0
        # Iterate over each sequence and check its safety
        for seq in sequences:
            is_safe = self.safety_check(seq)
            print(f"Sequence: {seq}, Safe: {is_safe}")  # Debug: Log each sequence's safety status
            if is_safe:
                safe_count += 1
        
        return safe_count


# Read raw data from a file
with open('rawDataDayTwo.txt', 'r', encoding='utf-8') as f:
    raw_data = f.read()

# Debug: Print the raw data for verification
print("Raw data:")
print(repr(raw_data))  

# Instantiate the processor class
day2_processor = Day2()

# Calculate and print the number of safe sequences
safe_lines_count = day2_processor.count_safe_lines(raw_data)

print(f"Number of safe lines: {safe_lines_count}")
