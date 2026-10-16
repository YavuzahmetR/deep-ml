import numpy as np

def to_categorical(x, n_col=None):
	# Your code here
	if n_col == None:
		one_hot_encoder_matrix = np.zeros((np.array(x).shape[0], np.max(x) + 1))
	else:
		one_hot_encoder_matrix = np.zeros((np.array(x).shape[0], n_col))
	
	for index, value in enumerate(x):
		 one_hot_encoder_matrix[index][value] = 1.0
	return one_hot_encoder_matrix


		
