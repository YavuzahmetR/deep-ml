def fim_transform(tokens: list, i: int, j: int) -> list:
    """
    Apply Fill-in-the-Middle (PSM) transformation to a token sequence.
    
    Args:
        tokens: list of token strings representing the document
        i: index where prefix ends / middle begins
        j: index where middle ends / suffix begins
    
    Returns:
        Transformed list of tokens in PSM format with special tokens.
    """
    # Your code here
    return ['<PRE>'] + tokens[0:i] + ['<SUF>'] + tokens[j:] + ['<MID>'] +  tokens[i:j] + ['<EOT>']
    

    

    