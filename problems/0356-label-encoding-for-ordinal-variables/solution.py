def label_encode_ordinal(values: list, order: list) -> list:
    """
    Encode ordinal categorical values to integers based on specified order.
    
    Args:
        values: List of categorical values to encode
        order: List specifying the order of categories from lowest (0) to highest
    
    Returns:
        List of integers representing the encoded values
    """
    #constraints
    if not values:
        return []

    for element in order:
        if order.count(element) > 1:
            raise ValueError("WTF")
    
    #problem
    order_dict = {}
    order_idx = 0
    for element in order:
        order_dict[element] = order_idx
        order_idx += 1
    
    return [order_dict.get(value, -1) for value in values]


    


    
