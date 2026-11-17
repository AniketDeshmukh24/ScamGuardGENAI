#main.py

from pathlib import Path
import sys
from pipeline.scam_detector.detector import ScamDetector
from utils import get_logger

#Add Project root to path
project_root = Path(__file__).parent
sys.path.append(str(project_root))


logger = get_logger(__name__)
logger.info("Starting Scam Detection Pipeline...")

def main():
    """Test the Scam Detection Pipeline with sample messages."""
    detector = ScamDetector()
    
    test_msg = str(input("Enter a message to analyze for scam detection: "))
    
    try:
        logger.info("Running scam detection...")
        result = detector.detect(test_msg)
        
        print("Test Message:", test_msg)
        print("Detection Result:", result)
        
    except Exception as e:
        logger.error(f"Error during scam detection: {str(e)}")
        print("An error occurred during scam detection. Please check the logs for details.")   
        print("Error:", str(e))

if __name__ == "__main__":
    main()
        