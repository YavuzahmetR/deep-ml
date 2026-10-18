import copy

def inject_reasoning_effort(messages, effort_level):
    effort_levels = {
        'low' : "Reasoning effort: low. Provide concise answers with minimal deliberation.",
        'medium' : "Reasoning effort: medium. Think step by step before answering.",
        'high' : "Reasoning effort: high. Carefully decompose the problem and verify each step.",
        'max' : "Reasoning effort: max. Exhaustively decompose the problem, stress-test all edge cases, and document every intermediate step."
       }

    if effort_level not in effort_levels.keys():
         raise ValueError("What The Hell?")
    
    output_message = copy.deepcopy(messages)

    if not output_message or output_message[0]['role'] != "system":
        output_message.insert(0, {'role':'system', 'content': effort_levels[effort_level]})
        return output_message 

    elif output_message[0]['role'] == "system":
        output_message[0]['content'] = effort_levels[effort_level] + "\n" + output_message[0]['content']
        return output_message