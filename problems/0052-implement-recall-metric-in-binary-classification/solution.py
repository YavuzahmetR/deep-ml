import numpy as np

def recall(y_true, y_pred):
    """
    Calculate the recall metric for binary classification.
    
    Args:
        y_true: Array of true binary labels (0 or 1)
        y_pred: Array of predicted binary labels (0 or 1)
    
    Returns:
        Recall value as a float
    """
    # Your code here
    # TP / TP + FN (1 - 1) / (1-1) + (0 - 1)

    tp_mask = (y_pred == 1) & (y_true == 1)
    tp_value = np.sum(tp_mask)

    fn_mask = (y_pred == 0) & (y_true == 1)
    fn_value = np.sum(fn_mask)

    if tp_value + fn_value == 0:
        return 0.0
    else:
        return tp_value / (tp_value + fn_value)





