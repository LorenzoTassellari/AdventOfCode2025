def get_max_voltage(line : str) -> int:
    """I'd like to find the maximum number in the string up to the previous to last digit.
    That will ensure we have the biggest 10's digit in the number, which in turn will give us the biggest total
    number.
    """
    max_value = max(line[:-1])
    position_max_value = line.find(max_value)
    max_value_after_max_value = max(line[position_max_value + 1:])
    return int(max_value + max_value_after_max_value)
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