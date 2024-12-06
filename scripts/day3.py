import re

def part1(input_data):

    # Storage of pairs to multiply
    multiplied_pairs = []
    
    # Pattern that will extract the first and second number
    pattern_to_match = r"mul\((\d{1,3}),(\d{1,3})\)"
    
    # Find & Store chunks matching pattern
    correct_chunks = re.findall(pattern_to_match,input_data)

    # Loop over the chunks
    for n1, n2 in correct_chunks:   
        # Add to multiplied_pairs first and second number multitplied
        multiplied_pairs.append(int(n1)*int(n2))

    return sum(multiplied_pairs) # Sum of pairs multiplied


def part2(input_data):
    # Storage of pairs to multiply
    multiplied_pairs = []
    
    # Patterns
    pattern_do = r"do\(\)"
    pattern_dont = r"don't\(\)"
    pattern_mul = r"mul\((\d{1,3}),(\d{1,3})\)"
    
    # Divide input_data into chunks that starts with "do()" and ends with "don't()""
    valid_sections = re.split(f"({pattern_do}|{pattern_dont})", input_data)
    
    # Variable for controlling if we are inside "do()" loop 
    enabled = True
    
    # Loop over valid_sections
    for section in valid_sections:
        section = section.strip()

        if section == "do()":
            enabled = True  # Initial process turned on (code will go on with this section)
        elif section == "don't()":
            enabled = False  # Initial process turned off (code will not go on with this section)
        elif enabled:  
            # # Find & Store chunks matching pattern
            correct_chunks = re.findall(pattern_mul, section)
            for n1, n2 in correct_chunks:
                multiplied_pairs.append(int(n1) * int(n2))
    
    return sum(multiplied_pairs) # Sum of pairs multiplied