import numpy as np

def shuffle_data(X, y, seed=None):
	# Your code here
	
	np.random.seed(seed)
	X = np.array(X)
	y = np.array(y)

	shuffled_index = np.random.permutation(y.shape[0])

	X_shuffle = X[shuffled_index]
	y_shuffle = y[shuffled_index]

	return X_shuffle, y_shuffle

	# np.random.seed(seed)
	# X = np.array(X)
	# y = np.array(y)

	# combine_list = []

	# if X.shape[0] != y.shape[0]:
	# 	return None	
	# for i in range(y.shape[0]):
	# 	combine_list.append((X[i],y[i]))
	# np.random.shuffle(combine_list)
	
	# shuffled_X = []
	# shuffled_Y = []

	# for item in combine_list:
	# 	shuffled_X.append(item[0])
	# 	shuffled_Y.append(item[1])
	
	# return np.array(shuffled_X), np.array(shuffled_Y)

