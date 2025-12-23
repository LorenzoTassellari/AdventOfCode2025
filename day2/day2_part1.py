with open("day2/input.txt", 'r') as f:
    exercise_input = f.read()
ranges_ids = [ranges.split('-') for ranges in exercise_input.split(',')]
all_ids = []
for _range in ranges_ids:
    print("ranges: ", _range)
    for _id in range(int(_range[0]), int(_range[1]) + 1): 
        print(_id)
        all_ids.append(_id)

output = 0
for _id in all_ids:
    str_id = str(_id)
    length_of_id = len(str_id)
    if length_of_id % 2 == 1: # Get rid of all odd numbers as they can't have a repeated pattern in them.
        continue
    first_half_id_index = length_of_id // 2 - 1 # -1 for the first half of the number.
    id_is_invalid = False
    for i in range(first_half_id_index + 1):
        if str_id[i] == str_id[i + first_half_id_index + 1]:
            id_is_invalid = True
        else:
            id_is_invalid = False
            break
    if id_is_invalid == True:
        output += _id
print(output)