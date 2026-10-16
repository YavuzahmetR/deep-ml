import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	npX = np.array(X)
	npY = np.array(y)
	theta = np.round(np.linalg.inv(npX.T @ npX) @ (npX.T @ npY), 4)
	return theta.tolist()