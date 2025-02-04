def best_threshold(threshold_data):
    """
    Goal is to find the best confidence threshold that yields recall >= 0.9.
    
    :param threshold_data: expects a dictionary with keys as thresholds (0.1, 0.2, ... 0.9) 
                           and values as dictionaries {TP, TN, FP, FN}.
    :return: Best threshold or None if no threshold meets the criteria.
    """
    best_thresh = None
    
    for threshold, values in threshold_data.items():
        TP, FN = values["TP"], values["FN"]
        recall = TP / (TP + FN) if (TP + FN) > 0 else 0
        
        if recall >= 0.9:
            if best_thresh is None or threshold < best_thresh:
                best_thresh = threshold
                
    return best_thresh
