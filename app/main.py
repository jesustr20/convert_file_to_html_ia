from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Document to HTML Converter API")

app.include_router(router)