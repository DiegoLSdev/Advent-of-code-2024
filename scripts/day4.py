def part1(input_data):
    # Convert the input data into a grid
    grid = input_data.split("\n")
    rows = len(grid)
    cols = len(grid[0])
    target = "XMAS"
    target_len = len(target)
    directions = [
        (0, 1),   # Horizontal: left-to-right
        (0, -1),  # Horizontal: right-to-left
        (1, 0),   # Vertical: top-to-bottom
        (-1, 0),  # Vertical: bottom-to-top
        (1, 1),   # Diagonal: top-left to bottom-right
        (-1, -1), # Diagonal: bottom-right to top-left
        (1, -1),  # Diagonal: top-right to bottom-left
        (-1, 1),  # Diagonal: bottom-left to top-right
    ]
    count = 0

    def is_valid(x, y):
        # Check if (x, y) is within grid boundaries
        return 0 <= x < rows and 0 <= y < cols

    # Traverse the grid
    for row in range(rows):
        for col in range(cols):
            # Check each direction from the current cell
            for dr, dc in directions:
                match = True
                for k in range(target_len):
                    new_row = row + dr * k
                    new_col = col + dc * k
                    if not is_valid(new_row, new_col) or grid[new_row][new_col] != target[k]:
                        match = False
                        break
                if match:
                    count += 1

    return count