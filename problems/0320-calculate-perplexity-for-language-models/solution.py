import numpy as np

def calculate_perplexity(probabilities: list[float]) -> float:
    """
    Calculate the perplexity of a language model given token probabilities.
    
    Args:
        probabilities: List of probabilities P(token_i | context) for each token
                      in the sequence, where each probability is in (0, 1]
    
    Returns:
        Perplexity value as a float
    """
    if not probabilities:
        return None

    if np.min(probabilities) <= 0 or np.max(probabilities) > 1:
        return None

    avg_log_prob = np.mean(np.log(probabilities))
    perplexity = np.exp(-avg_log_prob)

    return np.round(perplexity, 4)
