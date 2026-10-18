def check_contamination(benchmark_prompts, training_data):
    """
    Check whether each benchmark prompt exactly matches any training sample.

    Args:
        benchmark_prompts: list of strings
        training_data: list of strings

    Returns:
        list of booleans of length len(benchmark_prompts)
    """
    bool_list = []
    if not training_data:
        bool_list = [False for prompt in benchmark_prompts]
        return bool_list


    for i in range(len(benchmark_prompts)):
        if i < len(training_data):
            bool_list.append(benchmark_prompts[i] == training_data[i])
        else:
            bool_list.append(False) 
        

    return bool_list
