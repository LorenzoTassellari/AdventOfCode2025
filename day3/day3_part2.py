def get_max_voltage(line : str) -> int:
    """This one feels like a sliding window would be good for. If each line is of length x, then we should probably find
    the biggest number withing the first x - 12 numbers in the line. Then just find the biggest number between the 
    biggest number and the last 11 numbers and so on.
    After I pick the first number I still need at least 11 numbers to the right of it, so pick from the first 
    len of line - 11 numbers in the line
    """
    len_of_line = len(line)
    maximums = ""
    maximum_position = -1
    for numbers_left_to_pick in range(12, 0, -1): # 12 is for the amount of numbers we need to pick from each line.
        search_start_position = maximum_position + 1 # First time around this is 0
        previous_maximum_position = maximum_position + 1
        search_end_position = len_of_line - (numbers_left_to_pick - 1) 
        subline = line[search_start_position : search_end_position]
        maximum, maximum_position = find_max_value_and_position(subline)
        maximum_position += previous_maximum_position
        if maximum_position == -1:
            print("error, previous max not found")
        maximums += maximum
    return int(maximums)

def find_max_value_and_position(_string : str) -> [str, int]:
    max_value = "0"
    max_value_position = -1
    for i, char in enumerate(_string):
        if char > max_value:
            max_value = char
            max_value_position = i
    return [max_value, max_value_position]

def main():
    with open("day3/input.txt", 'r') as f:
        exercise_input = f.read().splitlines()
    total_max_voltage = 0
    for line in exercise_input:
        line_max_voltage = get_max_voltage(line)
        total_max_voltage += line_max_voltage
    print(total_max_voltage)
if __name__ == "__main__":
    main()