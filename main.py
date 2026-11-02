from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.post("/", response_class=PlainTextResponse)
async def hello(request: Request):
    try:
        # Отримуємо JSON з POST-запиту
        data = await request.json()
        name = data.get("name", "World")
    except:
        name = "World"
    
    return f"Hello, {name}!"