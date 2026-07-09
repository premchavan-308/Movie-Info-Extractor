from dotenv import load_dotenv
from typing import List, Optional

from pydantic import BaseModel
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_mistralai import ChatMistralAI


load_dotenv()

model = ChatMistralAI(model="mistral-small-2506",temperature=0)

class Movie(BaseModel):
    title: str
    release_year: Optional[int] = None
    genre: List[str]
    director: Optional[str] = None
    cast: List[str]
    rating: Optional[float] = None
    summary: str


parser = PydanticOutputParser(pydantic_object=Movie)

# Prompt
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
Extract movie information from the given paragraph.

{format_instructions}

Only return the JSON.
""",
        ),
        ("human", "{paragraph}"),
    ]
)

# User Input
paragraph = input("Enter movie description:\n")

# Create Prompt
final_prompt = prompt.invoke(
    {
        "paragraph": paragraph,
        "format_instructions": parser.get_format_instructions(),
    }
)


response = model.invoke(final_prompt)

movie = parser.parse(response.content)

print("\nExtracted Movie:\n")
print(movie)

print("\nAs Dictionary:\n")
print(movie.model_dump())