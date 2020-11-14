board = [
    [0, 0, 6, 0, 0, 3, 4, 0, 10, 0 ],
    [2, 6, 4, 0, 0, 0, 0, 0, 9, 0 ],
    [0, 2, 10, 0, 0, 0, 0, 0, 5, 9 ],
    [10, 1, 5, 4, 2, 0, 0, 0, 0, 0 ],
    [0, 0, 0, 0, 1, 9, 8, 4, 0, 0 ],
    [0, 0, 3, 2, 9, 0, 0, 1, 0, 0 ],
    [6, 0, 0, 0, 0, 7, 0, 10, 0, 5 ],
    [0, 0, 0, 0, 0, 8, 6, 5, 0, 7 ],
    [1, 3, 0, 6, 0, 0, 5, 0, 0, 2 ],
    [0, 5, 0, 9, 6, 2, 0, 0, 8, 0]
]


def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,11):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        p=pos[0]
        if bo[p][i] == num :
            return False

    # Check column
    for i in range(len(bo)):
        q=pos[1]
        if bo[i][q] == num :
            return False

    return True


def print_board(bo):
    for i in range(len(bo)):

        for j in range(len(bo[0])):

            if j == len(bo)-1:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None

print_board(board)
solve(board)
print("___________________")
print_board(board)