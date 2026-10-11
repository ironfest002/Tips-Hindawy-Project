import os
from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

from schemas import OptimizedPrompt
from prompts import prompt_template

load_dotenv()

parser = PydanticOutputParser(pydantic_object=OptimizedPrompt)


def build_chain():
    llm = ChatGoogleGenerativeAI(
        model="gemini-3.1-flash-lite",
        temperature=0.4,
        timeout=60,
        max_retries=2,
        google_api_key=os.getenv("GOOGLE_API_KEY"),
    )
    prompt = prompt_template.partial(
        format_instructions=parser.get_format_instructions()
    )
    return prompt | llm | parser


def optimize(user_prompt: str, domain: str, language: str) -> OptimizedPrompt:
    chain = build_chain()
    return chain.invoke({
        "user_prompt": user_prompt,
        "domain": domain,
        "language": language,

    })