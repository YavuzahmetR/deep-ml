import numpy as np

def kl_divergence_normal(mu_p, sigma_p, mu_q, sigma_q):

	log = np.log(sigma_q / sigma_p) 
	sigma_square = (sigma_p ** 2)
	mean = ((mu_p - mu_q) ** 2)
	sigma_two_square = (2 * (sigma_q ** 2)) 
	scaler = (1 / 2)


	return log + ((sigma_square + mean) / (sigma_two_square)) - scaler
	
