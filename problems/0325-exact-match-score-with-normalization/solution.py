import string

def exact_match_score(predictions: list[str], references: list[str]) -> float:
    """
    Calculate the exact match score between predictions and references.
    
    Args:
        predictions: List of predicted strings
        references: List of reference (ground truth) strings
    
    Returns:
        Exact match score as a float between 0 and 1
    """
    # Your code here
    if not predictions or not references:
         return  0.0

    predictions_clean = []
    references_clean = []
    counter = 0

    for pred in predictions:
        clean_pred = "".join(filter(lambda x: x not in string.punctuation, pred))
        predictions_clean.append(" ".join(clean_pred.lower().split()))
    for ref in references:
        clean_ref = "".join(filter(lambda x: x not in string.punctuation, ref))
        references_clean.append(" ".join(clean_ref.lower().split()))
    
    for clean_p, clean_r in zip(predictions_clean, references_clean):
        if clean_p == clean_r:
            counter += 1
    
    return counter / len(references_clean)


    
    