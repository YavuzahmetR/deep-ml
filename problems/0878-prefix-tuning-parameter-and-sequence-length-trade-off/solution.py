def prefix_tuning_tradeoff(d_model: int, max_sequence_length: int, l_p: int, l_i: int) -> dict:
    """Compute prefix-tuning parameter count and sequence-length trade-off.

    Args:
        d_model: hidden size of the transformer.
        max_sequence_length: model's maximum context length.
        l_p: number of prefix tokens (prepended).
        l_i: number of infix tokens (inserted).

    Returns:
        dict with keys 'trainable_params', 'effective_seq_len', 'prefix_fraction'.
    """
    
    prefix_tokens = l_p
    infix_tokens = l_i

    if prefix_tokens + infix_tokens >= max_sequence_length:
        effective_seq_len = 0
        prefix_fraction = 1.0
    else:
        effective_seq_len = max_sequence_length - (prefix_tokens + infix_tokens)
        prefix_fraction = (prefix_tokens + infix_tokens) / max_sequence_length

    trainable_params = d_model * (prefix_tokens + infix_tokens)

    trade_off_dict = {
        'trainable_params' : trainable_params,
        'effective_seq_len': effective_seq_len,
        'prefix_fraction' : prefix_fraction
    }

    return trade_off_dict
