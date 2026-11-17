from typing import List, Dict,Any
from utils import get_logger
from .builder import build_prompt
from .parser import OutputParser
from .executor import LLMExecutor

logger = get_logger(__name__)

class ScamDetector:
    """Orchestrator for scam detection using LLM."""
    
    def __init__(self, strategy: str = "react") -> None:
        """
        Initialize the ScamDetector with an optional model name.
        
        Args:
            strategy (str): The detection strategy to use. Defaults to "react".
        """
        self.executor = LLMExecutor()
        self.parser = OutputParser()
        self.strategy = strategy
        logger.info(f"ScamDetector initialized with strategy: {self.strategy}")
    
    def detect(self, message: str) -> Dict[str, Any]:
        """
        Runs Scam Detection on a single message.
        
        Args:
            message (str): The message to analyze for scam detection.
        Returns:
            Dict[str, Any]: A dictionary containing the detection results.
        """
        try:
            # The 3-step process: Build prompt, Execute LLM, Parse output
            prompt = build_prompt(message, self.strategy)
            raw_response = self.executor.execute(prompt)
            parsed_result = self.parser.parse_llm_output(raw_response)
            
            logger.info(f"Scam detection completed successfully. Result : {parsed_result.get('label', 'Unknown')}")
            return parsed_result
        
        except Exception as e:
            logger.error(f"Scam detection failed: {str(e)}")
            # Reaise the exception to be handled by the caller (UI layer)
            raise
        
    def detect_batch(self, messages: List[str]) -> List[Dict[str, Any]]:
        """
        Runs Scam Detection on a batch of messages.
        
        Args:
            messages (List[str]): A list of messages to analyze for scam detection.
        Returns:
            List[Dict[str, Any]]: A list of dictionaries containing the detection results for each message.
        """
        total_messages = len(messages)
        logger.info(f"Starting batch scam detection for {total_messages} messages.")
     
        results = List[Dict[str, Any]] = []
        
        for i, message in enumerate(messages):
            try:
                result = self.detect(message)
                results.append(result)
            except Exception as e:
                logger.error(f"Scam detection failed for message: {message}. Error: {str(e)}")
                
                logger.error(f"Failed to process message {i + 1}/{total_messages}: {message}. Error: {str(e)}")
                # Append a fallback result for this message
                results.append({
                    "label": "Uncertain",
                    "reasoning": f"Error Processing Message: {str(e)}",
                    "intent": "Could not determine intent",
                    "risk_factors": ["processing error"]
                })
        successful = sum(1 for r in results if r.get("label") != "Uncertain" and "processing_error" not in r.get("risk_factors", []))
        logger.info(f"Batch processing complete. {successful}/{total_messages} succeeded.")
        return results