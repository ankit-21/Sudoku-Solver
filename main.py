# A Backtracking program in Python to solve Sudoku problem

# Recursive function to find an empty box in the Grid

def find_empty(arr, l):
    for row in range(len(arr)):
        for col in range(len(arr)):
            if arr[row][col] == 0:
                l[0] = row
                l[1] = col
                return True
    return False


# Checks if any assigned entry in the specified row matches the given number

def if_in_row(arr, row, num):
    for i in range(len(arr)):
        if arr[row][i] == num:
            return True
    return False


# Checks if any assigned entry in the specified column matches the given number

def if_in_col(arr, col, num):
    for i in range(len(arr)):
        if arr[i][col] == num:
            return True
    return False


# Checks if any assigned entry in the specified 3x3 box matches the given number

def if_in_box(arr, row, col, num):
    for i in range(3):
        for j in range(3):
            if arr[i + row][j + col] == num:
                return True
    return False


# Checks if the current number in the grid are valid

def check_location_is_safe(arr, row, col, num):
    return not if_in_row(arr, row, num) and not if_in_col(arr, col, num) and not if_in_box(arr, row - row % 3,
                                                                                                 col - col % 3, num)


# The main solver function

def solve_sudoku(arr):
    # Uncomment to check what happens at every step of the back-tracking process (interesting!!)
    # print(arr)

    # 'l' is a list variable that keeps the record of row and col in the find_empty function
    l = [0, 0]

    # If there is no unassigned location, we are done
    if not find_empty(arr, l):
        return True

    # Assigning the list values to row and col that we got from the above Function
    row = l[0]
    col = l[1]

    # consider digits 1 to 9
    for num in range(1, 10):

        # if looks good
        if (check_location_is_safe(arr,
                                   row, col, num)):

            # make tentative assignment
            arr[row][col] = num

            # return if success
            if solve_sudoku(arr):
                return True

            # else, unmake & try again
            arr[row][col] = 0

    # this triggers backtracking
    return False

def print_board(arr):
    """
    prints the board
    :param arr: 2d List of ints
    :return: None
    """
    for i in range(len(arr)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - -")
        for j in range(len(arr[0])):
            if j % 3 == 0 and j != 0:
                print(" | ",end="")

            if j == 8:
                print(arr[i][j], end="\n")
            else:
                print(str(arr[i][j]) + " ", end="")


# Driver main function to test above functions
if __name__ == "__main__":

    # assigning values to the grid
    grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0],
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    # if success print the grid
    print("Before:")
    print_board(grid)
    print("***************************")
    print("After:")
    if (solve_sudoku(grid)):
        print_board(grid)
    else:
        print("No solution exists")