def score_prompt_complexity(prompts):
    """
    prompts: list of {'text': str, 'tags': list[str]}
    Returns: list of {'text': str, 'complexity': int} sorted by complexity desc (stable).
    """
    sorted_prompt = []
    for prompt in prompts:
        new_dict = {'text': prompt['text'], 'complexity': len(set(prompt['tags']))}
        sorted_prompt.append(new_dict)
    return sorted(sorted_prompt, key=lambda x: x['complexity'], reverse=True)
    
    
    
    