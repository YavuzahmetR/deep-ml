def dup_ngram_ratio(text: str, n: int) -> float:
    # Your code here
    clean_text = text.split()
    n_grams = []
    duplicate = []
    total = 0
    if len(clean_text) < n:
        return 0.0

    for i in range(len(clean_text) - n + 1):
        n_grams.append(tuple(clean_text[i:i+n]))

    for element in n_grams:
        if n_grams.count(element) > 1:
            duplicate.append(1)
        else:
            duplicate.append(0)
    
    total = sum(duplicate)
    
    return round(total / len(n_grams), 4)

