def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means = []
	if mode == "column":
		for i in range(len(matrix[0])):
			column_total = []
			for j in range(len(matrix)):
				column_total.append(matrix[j][i])
			means.append(sum(column_total) / len(column_total))
	
	elif mode == "row":
		for i in range(len(matrix)):
			means.append(sum(matrix[i]) / len(matrix[i]))

	return means
