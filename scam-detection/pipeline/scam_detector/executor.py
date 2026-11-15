# pipeline/scam_detector/executor.py

from typing import Optional
from xml.parsers.expat import model
from llm.client import LLMClient
from utils import get_logger

logger = get_logger(__name__)

class LLMExecutor:
    
    """Executor for running scam detection using LLMClient."""
    
    def __init__(self, model: Optional[str] = None) -> None:
        """
    
        Initialize the LLMExecutor with an optional model name.
        
        Args:
            model (Optional[str]): The name of the LLM model to use. If None, defaults to the model specified in LLMClient.
        """
        self.llm : LLMClient = LLMClient(model) if model else LLMClient()
        
        logger.info(f"LLMExecutor initialized")
    
    def execute(self, prompt: str) -> str:
        """Execute the prompt using the LLM client and return the response.
        
            Args:
                prompt (str): The prompt to send to the LLM for execution.  
                
            Returns:
                str: The response from the LLM.       
        """
        try:
            response = self.llm.call(prompt)
            logger.info(f"Prompt executed successfully , response Length:  {len(response)}")
            return response
        except Exception as e:
            logger.error(f"LLM Execution Error: {str(e)}")
            
            raise