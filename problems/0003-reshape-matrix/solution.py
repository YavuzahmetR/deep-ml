import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	
	matrix_length = len(a) * len(a[0])
	reshaped_length = new_shape[0] * new_shape[1]

	if matrix_length != reshaped_length:
		return []
	else:
		return np.array(a).reshape(new_shape)

	