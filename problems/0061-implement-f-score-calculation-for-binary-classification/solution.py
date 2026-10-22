import numpy as np

def f_score(y_true, y_pred, beta):
	"""
	Calculate F-Score for a binary classification task.

	:param y_true: Numpy array of true labels
	:param y_pred: Numpy array of predicted labels
	:param beta: The weight of precision in the harmonic mean
	:return: F-Score rounded to three decimal places
	"""
	true_positive = (y_pred == 1) & (y_true == 1)
	false_positive = (y_pred == 1) & (y_true == 0)
	false_negative = (y_pred == 0) & (y_true == 1)

	tp_value = np.sum(true_positive)
	fp_value = np.sum(false_positive)
	fn_value = np.sum(false_negative)

	presicion = tp_value / (tp_value + fp_value)
	recall = tp_value / (tp_value + fn_value) 

	return round((1 + beta**2) * (presicion * recall) / ((beta**2 * presicion) + recall), 4)
