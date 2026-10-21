def swish(x: float) -> float:
	"""
	Implements the Swish activation function.

	Args:
		x: Input value

	Returns:
		The Swish activation value
	"""
	# Your code here
	e = 2.7182818284

	result = x * (1 / (1 + e**-x))
	return round(result, 4)