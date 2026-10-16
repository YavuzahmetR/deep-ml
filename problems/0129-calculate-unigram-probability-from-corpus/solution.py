def unigram_probability(corpus: str, word: str) -> float:
    # Your code here
    
    corpus_list = corpus.split(" ")
    token_counter = len(corpus_list)
    word_counter = sum([True if element == word else False for element in corpus_list])


    return word_counter / token_counter


