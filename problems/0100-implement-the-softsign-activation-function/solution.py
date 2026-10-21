def softsign(x: float) -> float:
	"""
	Implements the Softsign activation function.

	Args:
		x (float): Input value

	Returns:
		float: The Softsign of the input
	"""
	# Your code here
	if x < 0:
		abs_x = x * -1
	else:
		abs_x = x
	result = x / (1 + abs_x)

	return round(result, 4)