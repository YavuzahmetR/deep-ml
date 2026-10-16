import math

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	probabilities = []
	loss = 0
	mse = 0
	for rows in features:
		total = []
		for row , weight in zip(rows , weights):
			total.append(row * weight)
		probabilities.append(sum(total) + bias)
	
	probabilities = [round(1 / (1 + (math.e ** -(element))), 4)  for element in probabilities]

	for probability , label in zip(probabilities, labels):
		loss += (label - probability) ** 2
		
	mse = round( loss / len(labels), 4)
	return probabilities, mse