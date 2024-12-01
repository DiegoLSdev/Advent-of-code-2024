
def part1(input_data):

    # Initialize variables for the left and right columns
    left_col = []
    right_col = []

    # Split the input data by new lines to create pairs
    pairs = input_data.split("\n")


    # Iterate over each pair and split it into left and right values
    for i in pairs:
        right_col.append(i.split("   ")[1])
        left_col.append(i.split("   ")[0])

    # Turn each item of the column into a Integer
    right_col_int = [int(x) for x in right_col] # Left column: first part of the pair
    left_col_int = [int(x) for x in left_col] # Right column: second part of the pair


    # Sort both columns and pair the corresponding items together using zip
    list_of_pairs = list(zip( sorted(left_col_int) ,sorted(right_col_int) ))

    # Calculate the absolute distances between the items in the sorted pairs
    distances=[]
    for index, item in list_of_pairs:
        # Calculate the distance between the sorted left value and the corresponding right value
        distance = item-index
        distances.append(abs(distance)) # Store the absolute distance

    # Sum all the distances to get the total
    total_distances = sum(distances)
    
    return total_distances 

def part2(input_data):
    return ""
 