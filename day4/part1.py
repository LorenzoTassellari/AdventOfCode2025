import numpy as np
def count_at_signs(subgrid: list) -> int:
    count = 0
    subgrid = subgrid.flatten()
    for char in subgrid:
        if char == '@':
            count += 1
    return count
def search_grid(grid : list[list]) -> list:
    '''Double for loop, if we're at the edge don't check past it.
    If we find less than 4 around it then count +1. To replace the grid with asterisks I'd like to create a copy
    of the grid, otherwise checking becomes more complicated.
    '''
    asterisks_grid = grid.copy()
    asterisks_count = 0
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char != '@': # Skip the character each time there's a '.'
                continue
            if i == 0 and j == 0:
                at_sings_counted = count_at_signs([grid[i][j + 1], grid[i + 1][j + 1], grid[i + 1][j]])
            elif i == 0 and j == len(row) - 1:
                at_sings_counted = count_at_signs([grid[i][j - 1], grid[i + 1][j - 1], grid[i + 1][j]])
            elif i == 0:
                at_sings_counted = count_at_signs([grid[i][j - 1]]) 

            if at_sings_counted >= 3:
                asterisks_grid[i][j] = '*'
                asterisks_count += 1
    return asterisks_grid, asterisks_count
def main():
    '''Steps:
    - open the file
    - get the grid as a 2d array
    - search the grid to find the positions where an @ symbol only has up to 4 other @ simbols around it.
    - print the grid with a * instead of the @ symbol in that case
    - count the number of * in the grid and return it.
    '''
    with open("day4/test.txt", 'r') as f:
        exercise_input = f.read().splitlines()
    asterisks_grid, asterisks_count = search_grid(exercise_input)
    print(asterisks_grid, asterisks_count)
if __name__ == "__main__":
    #main()
    array = ['asd',['ad','as']]
    print(array.np.flatten())