from typing import Dict, Any
from utils import get_logger,extract_json_from_text

logger = get_logger(__name__)

class OutputParser:
    """Parser for processing LLM output."""
    
    def parse_llm_output(self, llm_output: str) -> Dict[str, Any]:
        """Parse the output from the LLM and extract relevant information.
        
        Args:
            llm_output (str): The raw output string from the LLM.
            
        Returns:
            Dict[str, Any]: A dictionary containing the parsed information.
        """
        try:
            parsed_json = extract_json_from_text(llm_output)
            
            if parsed_json:
                logger.info(f"LLM output parsed successfully, Length: {len(parsed_json)}")
                return parsed_json
            else:
                logger.warning("No valid JSON found in LLM output.")
                fallback_result = {
                    "label": "Uncertain",
                    "reasoning": "No valid JSON found in LLM output.",
                    "intent": "Could not determine intent",
                    "risk_factors": []
                }
                return fallback_result
        except Exception as e:
            logger.error(f"Error parsing LLM output: {str(e)}")
            raise