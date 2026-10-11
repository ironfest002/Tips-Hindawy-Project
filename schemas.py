from typing import List
from pydantic import BaseModel, Field


class OptimizedPrompt(BaseModel):
    improved_prompt: str = Field(description="The final professional prompt, ready to copy and use")
    role: str = Field(description="The role the AI should act as")
    context: str = Field(description="Background and context for the task")
    constraints: List[str] = Field(description="Rules and limits the AI must follow")
    expected_output: str = Field(description="Description of the expected output format")