from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import random
import requests
import os
from pathlib import Path

app = FastAPI()

# Монтируем статику
app.mount("/static", StaticFiles(directory="static"), name="static")

BOT_TOKEN = os.getenv("BOT_TOKEN")
GROUP_ID = os.getenv("GROUP_ID")
MANAGER_USERNAME = os.getenv("MANAGER_USERNAME")

# Читаем HTML шаблон
BASE_DIR = Path(__file__).parent
TEMPLATE_PATH = BASE_DIR / "templates" / "index.html"

with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
    HTML_TEMPLATE = f.read()

@app.get("/", response_class=HTMLResponse)
async def home():
    return HTML_TEMPLATE

@app.post("/submit")
async def submit(request: Request):
    data = await request.json()
    track_code = random.randint(1000, 9999)
    
    text = f"""🆕 Новая заявка PRISM AGENCY

👤 ФИО: {data.get('fio')}
🎂 Дата рождения: {data.get('birth')}
📱 Телефон: {data.get('phone')}
✈️ Telegram: {data.get('telegram')}
💼 Опыт: {data.get('experience')}
⏰ Время: {data.get('time')}
📲 Смартфон: {data.get('device')}
🆔 HR-код: {track_code}"""
    
    try:
        requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            json={"chat_id": GROUP_ID, "text": text},
            timeout=10
        )
    except Exception as e:
        print(f"Error sending to Telegram: {e}")
    
    return JSONResponse(content={"success": True, "track_code": track_code})
