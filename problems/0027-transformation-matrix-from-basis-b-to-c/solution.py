import numpy as np

def transform_basis(B: list[list[int]], C: list[list[int]]) -> list[list[float]]:
    # Convert the input Python lists into NumPy arrays for matrix operations
    npB = np.array(B) 
    npC = np.array(C)

    # Compute the transformation matrix P using the formula: P = C^-1 * B
    # np.linalg.inv() finds the inverse, and '@' performs matrix multiplication
    p = np.linalg.inv(npC) @ npB

    # Convert the resulting NumPy array back to a standard Python list and return
    return p.tolist()