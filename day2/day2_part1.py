
def check_invalid_id(_id : int) -> bool:

    str_id = str(_id)
    length_of_id = len(str_id)
    id_is_invalid = False

    if length_of_id % 2 == 1: # Get rid of all odd numbers as they can't have a repeated pattern in them.
        return id_is_invalid

    first_half_id_index = length_of_id // 2 - 1 # -1 for the first half of the number.

    for i in range(first_half_id_index + 1):
        if str_id[i] == str_id[i + first_half_id_index + 1]:
            id_is_invalid = True
        else:
            id_is_invalid = False
            return id_is_invalid

    return id_is_invalid

def main():
    with open("day2/input.txt", 'r') as f:
        exercise_input = f.read()

    ranges_ids = [ranges.split('-') for ranges in exercise_input.split(',')]
    all_ids = []

    sum_of_invalid_ids = 0
    for _range in ranges_ids:
        for _id in range(int(_range[0]), int(_range[1]) + 1): 
            if check_invalid_id(_id):
                sum_of_invalid_ids += _id

    print(sum_of_invalid_ids)
    
if __name__ =="__main__":
    main()


