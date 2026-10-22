import numpy as np

def global_avg_pool(x: np.ndarray) -> np.ndarray:
	# Your code here
	return np.mean(x, axis=(0,1))

	"""
	binary combination axis=(0,1)
	0 0 - 0	 	0 0 - 1  	0 0 - 2
	0 1 - 0  	0 1 - 1		0 1 - 2
	1 0 - 0  	1 0 - 1		1 0 - 2
	1 1 - 0  	1 1 - 1		1 1 - 2
	
	selection of first, mid and last indexes of any element column-based
	discoverd by myself.
	"""
