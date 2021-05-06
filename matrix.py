#matrix 
import random

from pprint import pprint

def init_matrix():
    n = random.randint(4, 11)
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(n):
            matrix[i].append(random.randint(0, 100))
    return matrix

def fill(matrix):
    for i in range(len(matrix)):
        matrix[i][i] = 1

def refill(matrix):
    for i in range(len(matrix)):
        matrix[i][-i - 1] = 2

def upper_null(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if (j >= i):
                matrix[i][j] = 3

def low_null(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if (j <= i):
                matrix[i][j] = 4

def main():
    matrix = init_matrix()
    fill(matrix)
    refill(matrix)
    pprint(matrix)
    upper_null(matrix)
    pprint(matrix)
    low_null(matrix)
    pprint(matrix)

if __name__ == '__main__':
    main()