#!/usr/bin/python3
module = __import__('6-print_matrix_integer')
func = module.print_matrix_integer

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

func(matrix)
print("--")
func()

