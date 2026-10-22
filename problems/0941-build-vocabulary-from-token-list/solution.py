def build_vocab(tokens):
    """
    Build a vocabulary dictionary from a list of tokens.

    Args:
        tokens: list of string tokens

    Returns:
        Dict mapping each unique token (sorted) to a unique integer ID starting from 0.
    """
    if not tokens:
        return {}
    unique_tokens = set(tokens)
    sorted_set = sorted(unique_tokens)
    output_dict = {f"{token}" : index for index, token in enumerate(sorted_set)}
    return output_dict
