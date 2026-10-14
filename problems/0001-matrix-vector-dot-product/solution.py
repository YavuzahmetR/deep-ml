def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	
	outside_total = []
	
	for i in range(len(a)):
		inside_total = []
		if len(a[i]) == len(b):
			for j in range(len(a[i])):
				inside_total.append(a[i][j] * b[j])
			outside_total.append(sum(inside_total))
		else:
			return -1

	return outside_total

	








		
		