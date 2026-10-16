import math

def softmax(scores: list[float]) -> list[float]:

    overflow_guard = []

    for i in range(len(scores)):
       overflow_guard.append(math.e ** (scores[i] - max(scores)))
    
    total_guard = sum(overflow_guard)

    softmax_scores = [element / total_guard for element in overflow_guard]

    return softmax_scores