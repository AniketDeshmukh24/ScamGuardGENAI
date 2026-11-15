from llm.prompts import generate_prompt

def build_prompt(message: str, strategy: str ="react") -> str:
    
    """
    Build a prompt for scam detection based on the provided message and strategy.
   
    Args:

        message (str): The user message to analyze.
        strategy (str): The strategy to use for prompt generation. Default is "react".  
    
    Returns:
        str: The generated prompt for scam detection.
    """
    
    if strategy == "react":
        return generate_prompt(message)
    else:
        raise NotImplementedError(f"Strategy '{strategy}' is not implemented. Please choose a valid strategy.")