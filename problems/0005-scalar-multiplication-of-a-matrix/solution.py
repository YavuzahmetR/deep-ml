def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	return_matrix = []
	for i in range(len(matrix)):
		scalar_matrix = []
		for j in range(len(matrix[i])):
			scalar_matrix.append(matrix[i][j] * scalar)
		return_matrix.append(scalar_matrix)
	return return_matrix
		