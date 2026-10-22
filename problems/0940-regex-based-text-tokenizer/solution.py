import re

def tokenize_text(text: str) -> list:
    """
    Split raw text into tokens using regex-based splitting on whitespace
    and punctuation. Returns a list of non-empty stripped tokens.
    """
    pattern = r'--|[,.:;?_!"()\']'
    clean_text = re.sub(pattern, r" \g<0> ", text) #space left and right after cac
    return clean_text.split()
    





            
