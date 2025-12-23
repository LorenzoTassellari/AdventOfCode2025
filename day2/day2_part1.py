with open("day2/test.txt", 'r') as f:
    exercise_input = f.read()
print(exercise_input)
ranges_ids = [ranges.split('-') for ranges in exercise_input.split(',')]
print(ranges_ids)