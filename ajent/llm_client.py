from abc import ABC, abstractmethod
from typing import Any, Dict, List

class LLMClient(ABC):    
    @abstractmethod
    def send(self, messages: List[Dict], tools: List[Dict], model: str = "gpt-4o-mini") -> Any:
        pass

    @abstractmethod
    def serialize_response(self, response: Any) -> Dict:
        pass