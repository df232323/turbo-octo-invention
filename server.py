from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import random
import requests
import os

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

BOT_TOKEN = os.getenv("BOT_TOKEN")
GROUP_ID = os.getenv("GROUP_ID")
MANAGER_USERNAME = os.getenv("MANAGER_USERNAME")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "manager_username": MANAGER_USERNAME
        }
    )

@app.post("/submit")
async def submit(request: Request):
    data = await request.json()
    
    track_code = random.randint(1000, 9999)
    
    text = f"""
🆕 Новая заявка PRISM AGENCY

👤 ФИО: {data.get('fio')}
🎂 Дата рождения: {data.get('birth')}
📱 Телефон: {data.get('phone')}
✈ Telegram: {data.get('telegram')}

💼 Опыт: {data.get('experience')}
⏰ Время: {data.get('time')}
📲 Смартфон: {data.get('device')}

🆔 HR-код: {track_code}
"""
    
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        json={
            "chat_id": GROUP_ID,
            "text": text
        }
    )
    
    return JSONResponse({
        "success": True,
        "track_code": track_code
    })
