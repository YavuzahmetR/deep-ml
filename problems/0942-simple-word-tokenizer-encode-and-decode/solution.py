import re

def encode(text, vocab):
    pattern = r'[,.:;?_!"()\']|--|\s'
    punct_text = re.sub(pattern, r" \g<0> ", text).split()
    ids = []
    for token in punct_text:
        token.strip()
        if token:
            ids.append(vocab[token])
    return ids
    

def decode(ids, vocab):
    inverse_vocab = {v : k for k, v in vocab.items()}
    tokens = [inverse_vocab[idx] for idx in ids]
    token_string = " ".join(tokens)
    cleaned_string = re.sub(r'\s+([,.?!"()\'])', r'\1', token_string)
    return cleaned_string
