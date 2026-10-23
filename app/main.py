from fastapi import FastAPI
from app.routes import file 

app = FastAPI()

@app.get("/")
def landing_page():
    return {
        "message": "Hi, DK ,Welcome"
        }


@app.get("/health") 
def health():
    return{
        "message" : "your health is good"
    }

app.include_router(file.router)

