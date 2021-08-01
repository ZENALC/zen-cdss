"""
Main file for FastAPI.
"""
from typing import Dict

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root() -> Dict[str, str]:
    """
    Main root function endpoint.
    :return: JSON dictionary.
    """
    return {"message": "Hello World"}
