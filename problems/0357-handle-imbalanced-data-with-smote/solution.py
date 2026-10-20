import numpy as np

def smote(X_minority: np.ndarray, n_synthetic: int, k: int = 5) -> np.ndarray:
    """
    Generate synthetic samples using SMOTE algorithm.

    Note: the random seed is set by the grader before your function runs,
    so you do NOT need to set it. Just use numpy's global RNG directly
    (np.random.randint, np.random.random, ...).

    Args:
        X_minority: 2D array of minority class samples (n_samples, n_features)
        n_synthetic: Number of synthetic samples to generate
        k: Number of nearest neighbors to consider

    Returns:
        2D array of synthetic samples (n_synthetic, n_features)
    """
    # Your code here
    n_samples = len(X_minority)
    k_actual = min(k, n_samples - 1)

    if k_actual == 0 or n_synthetic == 0:
        return  np.empty((0, X_minority.shape[1]))

    synthetic_samples = []

    for _ in range(n_synthetic):
    
        i = np.random.randint(0, n_samples)
        j = np.random.randint(0, k_actual)
        gap = np.random.random()

        start_point = X_minority[i]
        neigbohr_distances = []
        for data_points in X_minority:
            neigbohr_distances.append(np.linalg.norm(start_point - data_points))
    
        idx_sorted_neighbor_distances = np.argsort(neigbohr_distances)

        #Exclude [0] (start_point itself as neighbor)

        neigbor_pool = idx_sorted_neighbor_distances[1:k_actual + 1]
        neigbor_point = X_minority[neigbor_pool[j]]


        new_sample = start_point + (gap * (neigbor_point - start_point))
        synthetic_samples.append(new_sample)

    return  np.array(synthetic_samples)
