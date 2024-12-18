def part1(input_data):
    # Split input data into rows
    reports = input_data.split("\n")
    
    # Convert each row of numbers into a list of integers
    array_of_nums = []
    for item in reports:
        if item.strip():  # Skip empty lines
            array_of_nums.append([int(x) for x in item.split()])
    
    # Check if a row is ascending
    def is_ascending(row):
        return row == sorted(row)
    
    # Check if a row is descending
    def is_descending(row):
        return row == sorted(row, reverse=True)
    
    # Check if adjacent levels differ by at least 1 and at most 3
    def has_valid_difference(row):
        for i in range(len(row) - 1):
            difference = abs(row[i + 1] - row[i])
            if difference < 1 or difference > 3:
                return False
        return True
    
    # Count safe reports
    safe_count = 0
    for row in array_of_nums:
        if (is_ascending(row) or is_descending(row)) and has_valid_difference(row):
            safe_count += 1
    
    print(safe_count)

def part2(input_data):
    # Split input data into rows
    reports = input_data.split("\n")
    
    # Convert each row of numbers into a list of integers
    array_of_nums = []
    for item in reports:
        if item.strip():  # Skip empty lines
            array_of_nums.append([int(x) for x in item.split()])
    
    # Check if a row is ascending
    def is_ascending(row):
        return row == sorted(row)
    
    # Check if a row is descending
    def is_descending(row):
        return row == sorted(row, reverse=True)
    
    # Check if adjacent levels differ by at least 1 and at most 3
    def has_valid_difference(row):
        for i in range(len(row) - 1):
            difference = abs(row[i + 1] - row[i])
            if difference < 1 or difference > 3:
                return False
        return True
    
    # Check if a row is safe
    def is_safe(row):
        return (is_ascending(row) or is_descending(row)) and has_valid_difference(row)
    
    # Check if a row can be made safe by removing one level
    def can_be_made_safe(row):
        for i in range(len(row)):
            # Create a new row with the i-th level removed
            new_row = row[:i] + row[i+1:]
            if is_safe(new_row):
                return True
        return False

    # Count safe reports
    safe_count = 0
    for row in array_of_nums:
        if is_safe(row) or can_be_made_safe(row):
            safe_count += 1
    
    print(safe_count)