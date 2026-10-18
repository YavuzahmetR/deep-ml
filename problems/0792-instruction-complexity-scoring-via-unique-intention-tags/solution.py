def score_dialog_complexity(dialogs):
    """
    Args:
        dialogs: list of lists of intention tag strings
    Returns:
        list of (index, score) tuples sorted by score desc, then index asc
    """
    #list of tuple
    #unique - set
    idx_score_list = []
    for idx, tags in enumerate(dialogs):
        tags_set = len(set(tags))
        idx_score_list.append((idx, tags_set))
    
    return sorted(idx_score_list, key=lambda x: (-x[1], x[0]))