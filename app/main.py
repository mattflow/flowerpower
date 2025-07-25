from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from enum import Enum
from pydantic import BaseModel
from core.greeting import get_greeting

app = FastAPI(title="flowerpower")


@app.get("/", include_in_schema=False)
async def redirect_to_docs() -> RedirectResponse:
    return RedirectResponse(url="/docs")


class Status(str, Enum):
    ok = "ok"


class HealthResponse(BaseModel):
    status: Status


@app.get("/health")
async def health_check() -> HealthResponse:
    return HealthResponse(status=Status.ok)

class GreetingResponse(BaseModel):
    greeting: str

@app.get("/greeting")
async def greeting(name: str = "world") -> GreetingResponse:
    return GreetingResponse(greeting=get_greeting(name))