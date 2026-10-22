
import numpy as np

def rmse(y_true, y_pred):
	# Write your code here

	if y_true.shape != y_pred.shape or not y_true.size or not y_pred.size:
		raise ValueError()

	rmse_res = np.sqrt(np.sum((y_true - y_pred)**2) / y_true.size)
	return round(rmse_res,3)
