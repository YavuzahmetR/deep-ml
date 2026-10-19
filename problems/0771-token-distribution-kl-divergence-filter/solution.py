import math

def kl_divergence_filter(reference_freq: dict, documents: list, threshold: float) -> dict:
    """Filter documents by KL divergence from a reference token distribution."""

    kl_divergences = []
    flagged = []
    kept = []

    for doc in documents:

        if not doc:
            kl_divergences.append(0.0)
            flagged.append(False)
            kept.append(doc)
            continue
        N = len(doc)
        V = set(doc)   
        payda_toplami = 0
        for token in V:
            payda_toplami += reference_freq.get(token, 0) + 1

        kl_toplami = 0.0
        for token in V:
            token_count = doc.count(token)
            P_t = token_count / N
            
            Q_t = (reference_freq.get(token, 0) + 1) / payda_toplami
            
            kl_toplami += P_t * math.log(P_t / Q_t)

        kl_divergences.append(round(kl_toplami, 4))
        
        is_flagged = kl_toplami > threshold
        flagged.append(is_flagged)
        
        if not is_flagged:
            kept.append(doc)

    return {
        'kl_divergences': kl_divergences,
        'flagged': flagged,
        'kept': kept
    }
