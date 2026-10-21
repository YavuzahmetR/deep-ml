import numpy as np

def impute_missing_data(data: np.ndarray, strategy: str = 'mean') -> np.ndarray:
    """
    Impute missing values in a 2D array using the specified strategy.
    Args:
        data: 2D numpy array with missing values represented as np.nan
        strategy: Imputation strategy - 'mean', 'median', or 'mode'
    Returns:
        2D numpy array with missing values imputed
    """
    imputed_data = data.copy()
    
    if strategy == 'mean':
        for col_idx in range(imputed_data.shape[1]):
            col_nan_check = np.isnan(imputed_data[:, col_idx])
            if np.any(col_nan_check):
                col_mean = np.nanmean(imputed_data[:, col_idx])
                imputed_data[col_nan_check, col_idx] = col_mean
                
    elif strategy == 'median':  
        for col_idx in range(imputed_data.shape[1]):
            col_nan_check = np.isnan(imputed_data[:, col_idx])
            if np.any(col_nan_check):
                col_median = np.nanmedian(imputed_data[:, col_idx])
                imputed_data[col_nan_check, col_idx] = col_median
                
    elif strategy == 'mode':
        for col_idx in range(imputed_data.shape[1]):
            col_nan_check = np.isnan(imputed_data[:, col_idx])
            if np.any(col_nan_check):
                clean_values = imputed_data[~col_nan_check, col_idx]
                if len(clean_values) > 0:
                    values, counts = np.unique(clean_values, return_counts=True)
                    col_mode = values[np.argmax(counts)]
                    imputed_data[col_nan_check, col_idx] = col_mode
                    
    return imputed_data
