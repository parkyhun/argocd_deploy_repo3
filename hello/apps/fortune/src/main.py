from fastapi import FastAPI

app = FastAPI()

@app.get("/fortune")
def get_fortune():
    return {
        "service": "fortune", 
        #"message": "동쪽으로 가명 귀인을 만나요"
        "message": "하이닉스 300만원 다시 갈거야!삼성전자는 40만원, 두산에너빌 20만원, 현대차는 70만원 갈거라면서 하"
    }