#!/usr/bin/python3
''' Module for N queens
'''
import sys


def print_board(board):
    '''Prints the chess board
    '''
    result = []
    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y] == 1:
                result.append([x, y])
    print(result)


def is_safe(board, row, column):
    '''Checks if it's safe to place a queen
    '''
    for x in range(column):
        if board[row][x] == 1:
            return False
    for x, y in zip(range(row, -1, -1),
                    range(column, -1, -1)):
        if board[x][y] == 1:
            return False
    for x, y in zip(range(row, len(board), 1),
                    range(column, -1, -1)):
        if board[x][y] == 1:
            return False
    return True


def solve(board, column):
    '''Solves the N Queen problem using Backtracking
    '''
    if column == len(board):
        print_board(board)
        return True
    res = False
    for x in range(len(board)):
        if is_safe(board, x, column):
            board[x][column] = 1
            res = solve(board, column + 1) or res
            board[x][column] = 0
    return res


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        sys.exit(1)
    if N < 4:
        print('N must be at least 4')
        sys.exit(1)
    board = [[0 for y in range(N)] for i in range(N)]
    solve(board, 0)
