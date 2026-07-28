from fastapi import FastAPI

app = FastAPI()

@app.get("/greet")
def get_fortune():
    return {
        "service": "greet", 
        "message": "안녕하세요, 즐거운 하루, 즐거운 한 주, 즐거운 한 달"
    }