import numpy as np

def detect_outliers_iqr(data: list[float], k: float = 1.5) -> dict:
	"""
	Detect and remove outliers using the IQR method.
	
	Args:
		data: List of numerical values
		k: IQR multiplier for determining outlier bounds (default 1.5)
	
	Returns:
		Dictionary with 'cleaned_data', 'outlier_indices', 'lower_bound', 'upper_bound'
	"""
	# Your code here
	
	#Q2
	median = 0 
	copy_data = np.copy(data)
	outliers = []
	cleaned_data = []

	copy_data = np.sort(copy_data)

	if len(copy_data) % 2 != 0:
		idx = len(copy_data) // 2 
		median = copy_data[idx]
	else:
		idx = len(copy_data) // 2 
		median = (copy_data[idx] + copy_data[idx - 1]) / 2
	
	#Q1
	q1 = np.percentile(data, 25)
	#Q3
	q3 = np.percentile(data, 75)
	#IQR	
	iqr = q3 - q1

	min_iqr, max_iqr = q1 - (iqr * k), q3 + (iqr * k)

	#outliers
	for original_idx, element in enumerate(data):
		if element > max_iqr or element < min_iqr:
			outliers.append(original_idx)
		else:
			cleaned_data.append(element)
	
	package = {
    'cleaned_data': cleaned_data,
    'outlier_indices': outliers,
    'lower_bound': float(min_iqr),
    'upper_bound': float(max_iqr)
	}

	return package


	""" Standart Math
	#Q2
	median = 0 
	copy_data = np.copy(data)
	outliers = []
	cleaned_data = []

	copy_data = np.sort(copy_data)

	if len(copy_data) % 2 != 0:
		idx = len(copy_data) // 2 
		median = copy_data[idx]

	else:
		idx = len(copy_data) // 2 
		median = (copy_data[idx] + copy_data[idx - 1]) / 2

	#Q1
	q1_elements = copy_data[0:idx]
	idx_q1 = len(q1_elements) // 2

	if len(q1_elements) % 2 != 0:
		q1 = q1_elements[idx_q1]
	else:
		q1 = (q1_elements[idx_q1] + q1_elements[idx_q1 - 1]) / 2	
	

	#Q3
	if len(copy_data) % 2 != 0:
		q3_elements = copy_data[idx+1:]
	else:
		q3_elements = copy_data[idx:]

	idx_q3 = len(q3_elements) // 2

	if len(q3_elements) % 2 != 0:
		q3 = q3_elements[idx_q3]
	else:
		q3 = (q3_elements[idx_q3] + q3_elements[idx_q3 - 1]) / 2
	
	#IQR
	iqr = q3 - q1

	min_iqr, max_iqr = q1 - (iqr * k), q3 + (iqr * k)

	#outliers
	for original_idx, element in enumerate(data):
		if element > max_iqr or element < min_iqr:
			outliers.append(original_idx)
		else:
			cleaned_data.append(element)
	
	package = {
    'cleaned_data': cleaned_data,
    'outlier_indices': outliers,
    'lower_bound': min_iqr,
    'upper_bound': max_iqr
	}

	return package
	"""
