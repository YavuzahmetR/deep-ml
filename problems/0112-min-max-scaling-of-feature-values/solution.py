
def min_max(x: list[float]) -> list[float]:
    """
    Perform Min-Max normalization to scale values to [0, 1].
    
    Args:
        x: A list of numerical values
    
    Returns:
        A new list with values normalized to [0, 1]
    """
    # Your code here
    #optimized
    x_min, x_max = min(x), max(x)
    if x_min == x_max:
        return [0.0] * len(x)
    return [(element - x_min) / (x_max - x_min) for element in x]



    #manuel
    # normalized_list = []
    # min_val = min(x)
    # max_val = max(x)

    # if min_val == max_val:
    #     return [0.0] * len(x)

    # for element in x:
    #     normalized_list.append((element - min_val) / (max_val - min_val))
    # return  normalized_list