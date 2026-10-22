
import numpy as np

def gini_impurity(y):
	"""
	Calculate Gini Impurity for a list of class labels.

	:param y: List of class labels
	:return: Gini Impurity rounded to three decimal places
	"""

	values, counts  = np.unique(np.array(y), return_counts = True)
	fractions = counts / np.array(y).size

	impurity = 1 - (np.sum(fractions ** 2))
	return round(impurity,3)