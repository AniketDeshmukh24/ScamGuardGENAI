import os

from pathlib import Path

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).parent

print(PROJECT_ROOT)

load_dotenv(dotenv_path=PROJECT_ROOT / ".env")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

DEFAULT_MODEL = 'gemini-3.8-flash'

MAX_RETRIES = 3

RETRY_DELAY = 2  

DEFAULT_DATASET_PATH = PROJECT_ROOT / "scam_detection_dataset.csv"

TEST_DATASET_PATH = PROJECT_ROOT / "test_scam_dataset.csv"

TEXT_COLUMNS = ["text", "message_text", "message"]

LABEL_COLUMN = "label"

OUTPUTS_DIR = PROJECT_ROOT / "outputs"

LOGS_DIR = PROJECT_ROOT / "logs"

OUTPUTS_DIR.mkdir(exist_ok=True)

LOGS_DIR.mkdir(exist_ok=True)

def get_dataSet_path(filename :str) -> Path:
    
    '''

    Get the absolute path of the dataset file.

    Args:

        filename (str): The name of the dataset file.

    Returns:    

        Path: The absolute path of the dataset file.

    Raises:

        FileNotFoundError: If the dataset file is not found in the current directory or the

    '''
    if Path(filename).exists():
        return Path(filename)
    
    project_path = PROJECT_ROOT / filename
    if project_path.exists():
        return project_path
    
    raise FileNotFoundError (f"File not found: {filename}")
