def part1(input_data):
    # Parse the input data
    lines = input_data.strip().split("\n")
    rules = [[int(num) for num in x.split("|")] for x in lines if "|" in x]
    updates = [[int(num) for num in x.split(",")] for x in lines if "," in x]

    def check_validity(page):
        """
        Check if the given page list adheres to the ordering rules.
        """
        for rule in rules:
            before, after = rule
            if before in page and after in page:
                # Ensure 'before' comes earlier than 'after' in the list
                if page.index(before) > page.index(after):
                    return False
        return True

    valid_updates = []
    
    for update in updates:
        if check_validity(update):
            valid_updates.append(update)

    # Find the middle page numbers for valid updates
    middle_pages = [update[len(update) // 2] for update in valid_updates]

    # Calculate the sum of middle page numbers
    result = sum(middle_pages)

    return result