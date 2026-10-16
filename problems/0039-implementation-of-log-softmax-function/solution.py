import numpy as np

def log_softmax(scores: list) -> np.ndarray:
	# Your code here
	x = np.array(scores)
	c = np.max(x, axis=0)
	return np.round((x - c) - (np.log(np.sum(np.exp(x - c)))), 4)


 #log_softmax(xi) = (xi - c) - ln(sum((e ** (xi - c))))