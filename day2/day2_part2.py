
def check_invalid_id(_id : int) -> bool:
    '''
    This check is now a bit harder, invalid ids can now be of any length and be repeated any number of times.
    We still only need to keep the partial array up to the midpoint, as that's the last time the sequence could be
    repeated.
    Either way the whole sequence needs to be a repeat so 22224 still wouldn't work.
    A sliding window solution sounds good here.
    If the first number repeates then try keep going with a window of size 1. 
    If that doesn't work, then go to a window of size 2 check for repeats.
    Continue up to window of size len(id) // 2 - 1.
    '''
    len_of_sliding_window = 1
    id_str = str(_id)
    id_len = len(id_str)
    id_midpoint = id_len // 2 - 1
    id_is_invalid = False
    # Each time we increase the size of the window I'd like to restart from the beginning of the sequence.
    # If the length of the window is larger than the midpoint of the id then we've gone too far and the
    # sequence is valid.
    while len_of_sliding_window <= id_midpoint + 1: 
        skip_this_window = False
        # If the length of the id is not divisible by the length of the window there's no point checking it.
        if id_len % len_of_sliding_window != 0: 
            len_of_sliding_window += 1
            continue
        # I'll create an array with all the characters of the string, each string in the array will be the
        # length of the window.
        _array = []
        for i in range(0, id_len, len_of_sliding_window):
            _array.append(id_str[i : i + len_of_sliding_window])
        first_item = _array[0]
        for item in _array:
            # Check that all the sections of the array are the same, this ensures the pattern is repeated.
            # If at any point the pattern doens't work, then the ID is valid and check the next window.
            if item != first_item:
                len_of_sliding_window += 1
                skip_this_window = True
                break
        if skip_this_window:
            continue

        # If we got here, that means that the patter was repeated, no need to check for other patterns just return True.
        id_is_invalid = True
        return id_is_invalid
    # If we got here, that means there was no repeated pattern and the ID is valid. id_is_invalid should be False here.
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


