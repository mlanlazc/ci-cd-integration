from fastapi import FastAPI, status, Query
from fastapi.openapi.utils import get_openapi
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from enum import Enum

class Language(str, Enum):
    ENGLISH = "en"
    SERBIAN = "sr"
    SPANISH = "es"
    FRENCH = "fr"
    GERMAN = "de"
    DUTCH = "nl"
    JAPANESE = "ja"

class HelloResponse(BaseModel):
    message: str = Field(..., description="The greeting message")
    timestamp: datetime = Field(default_factory=datetime.now, description="When the greeting was generated")
    language: Language = Field(default=Language.ENGLISH, description="The language of the greeting")

# Language mappings for greetings
GREETINGS: dict[str, str] = {
    Language.ENGLISH: "Hello World",
    Language.SERBIAN: "Zdravo Svete",
    Language.SPANISH: "Hola Mundo",
    Language.FRENCH: "Bonjour le Monde",
    Language.GERMAN: "Hallo Welt",
    Language.DUTCH: "Hallo Wereld",
    Language.JAPANESE: "こんにちは世界",
}

app = FastAPI(
    title="Example API",
    description="A simple FastAPI example with OpenAPI specification",
    version="1.0.0"
)

@app.get(
    "/",
    response_model=HelloResponse,
    status_code=status.HTTP_200_OK,
    summary="Get a hello world greeting",
    operation_id="hello_world",
    description="Returns a greeting message with timestamp and optional language specification.",
    response_description="A greeting message with metadata"
)
async def hello_world(
    language: Language = Query(default=Language.ENGLISH)
) -> HelloResponse:
    """
    Get a hello world greeting.
    
    Args:
        language: Optional language code for the greeting
    
    Returns:
        HelloResponse: A response containing the greeting message and metadata
    """
    greeting = GREETINGS.get(language or Language.ENGLISH)
    return HelloResponse(
        message=greeting,
        language=language or Language.ENGLISH
    )

@app.get("/openapi-json")
async def get_openapi_json():
    return get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 