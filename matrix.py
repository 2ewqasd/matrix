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

def main():
    matrix = init_matrix()
    fill(matrix)
    refill(matrix)
    pprint(matrix)

if __name__ == '__main__':
    main()