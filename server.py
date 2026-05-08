import random
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from aiogram import Bot

from config import (
    BOT_TOKEN,
    GROUP_ID
)

app = FastAPI()

bot = Bot(token=BOT_TOKEN)

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@app.post("/submit")
async def submit(request: Request):
    data = await request.json()

    track_code = random.randint(1000, 9999)

    text = f'''
🆕 Новая заявка Ozon

👤 Имя: {data['name']}
🎂 Возраст: {data['age']}
📱 Телефон: {data['phone']}
💬 Telegram: {data['telegram']}
🧠 Опыт: {data['experience']}
⏰ Готов уделять: {data['hours']}

🆔 HR-код: {track_code}
'''

    await bot.send_message(GROUP_ID, text)

    return JSONResponse({
        "success": True,
        "track_code": track_code
    })
