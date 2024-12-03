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

    return "Not done yet"