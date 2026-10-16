import numpy as np

def accuracy_score(y_true, y_pred):
	# Your code here
	bool_mask = (y_true == y_pred)
	return sum(bool_mask) / y_pred.shape[0]