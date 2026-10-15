import numpy as np

def make_diagonal(x):
	# Your code here
	matrix_shape = (len(x),len(x))
	diagonal_matrix = np.zeros(matrix_shape)
	for i in range(len(x)):
		diagonal_matrix[i][i] = x[i]
	return  diagonal_matrix
