import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	# Implement your code here
	cos_score = 0
	v1_distance = 0
	v2_distance = 0
	if (np.array(v1).shape == np.array(v2).shape) and (np.array(v1).shape != (0,)) and (np.array(v2).shape != (0,)):
		for i in range(v1.size):
			cos_score += v1[i] * v2[i]
			v1_distance += v1[i] ** 2
			v2_distance += v2[i] ** 2
		dist = (v1_distance ** 0.5) * (v2_distance ** 0.5)

		return cos_score / dist
	else:
		return None
		
	# NP
	#cs = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
 