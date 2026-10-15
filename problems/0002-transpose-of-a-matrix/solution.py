def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    transpozed_matrix = []

    for i in range(len(a[0])):
        list_transpoze = []
        for j in range(len(a)):
            list_transpoze.append(a[j][i])
        transpozed_matrix.append(list_transpoze)
    
    return transpozed_matrix