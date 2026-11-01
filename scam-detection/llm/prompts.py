from pathlib import Path
from utils import load_file

PROMPTS_DIR = Path(__file__).parent / "prompts"
print(f"PROMPTS_DIR : {PROMPTS_DIR}")

#Load prompt template from external files
def load_prompt(filename: str) -> str:
    """ Load a prompt template from file """
    
    return load_file(PROMPTS_DIR/ filename)


PROMPT = load_prompt("react.md")

def generate_prompt(user_input : str) -> str:
    "Generate a prompt for scam detetction - choose your strategy here !"    
    template = PROMPT
    return f"{template}\n\n User Message : \n"