import numpy as np

def residual_block(x: np.ndarray, w1: np.ndarray, w2: np.ndarray) -> np.ndarray:
	# Your code here
	out = w1 @ x
	out = np.maximum(0, out)
	out = w2 @ out
	out = out + x
	final_out= np.maximum(0, out)
	return final_out