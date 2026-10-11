from langchain_core.prompts import ChatPromptTemplate

SYSTEM_PROMPT = """You are an expert prompt engineer.
Your job is to transform a simple user prompt into a professional, detailed prompt.

Domain: {domain}
Write all fields in this language: {language}

Rules:
- Keep the original intent of the user's prompt.
- Define a clear Role, rich Context, specific Constraints, and a clear Expected Output.
- The improved_prompt must combine all of them into one ready-to-use prompt.
- If the domain is Cybersecurity, focus on defensive and educational use only.

{format_instructions}
"""

prompt_template = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    ("human", "Simple prompt: {user_prompt}"),
])