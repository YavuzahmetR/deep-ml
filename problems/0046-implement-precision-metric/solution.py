import numpy as np
def precision(y_true, y_pred):
	# Your code here
	# Precision is defined as the ratio of true positives to the sum of true positives and false positives. TP / TP + FP
	true_positives = (y_true == y_pred) & (y_true == 1) & (y_pred == 1)

	false_positives = (np.subtract(y_pred, y_true) == 1)

	total_positives = np.sum(true_positives) + np.sum(false_positives)

	if total_positives == 0:
		return 0.0
	return np.sum(true_positives) / total_positives



