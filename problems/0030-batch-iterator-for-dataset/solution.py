import numpy as np

def batch_iterator(X, y=None, batch_size=64):
	#Your code here
    batches = []
    if y is not None and np.array(X).shape[0] != np.array(y).shape[0]:
        return None
    for i in range(0, np.array(X).shape[0], batch_size):
        X_batch = X[i: i + batch_size]
        if y is not None:
            y_batch = y[i: i + batch_size]
            batches.append([X_batch.tolist(), y_batch.tolist()])
        else:
            batches.append(X_batch.tolist())
    return batches
