import numpy as np

def ridge_loss(X: np.ndarray, w: np.ndarray, y_true: np.ndarray, alpha: float) -> float:
	# Your code here
	predictions = X @ w

	mse = np.sum(((y_true - predictions)**2) / len(y_true))

	regularization_term = np.sum(w ** 2) * alpha

	return  (mse + regularization_term)
