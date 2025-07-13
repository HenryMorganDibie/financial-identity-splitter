from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import pandas as pd
from pathlib import Path

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    personas = pd.read_csv("data/monthly_personas.csv").to_dict(orient="records")
    summary = pd.read_csv("data/monthly_summary.csv")
    txns = pd.read_csv("data/transactions_categorized.csv")

    # For Chart.js
    bar_data = (
        summary.groupby("category")["total_debit"]
        .sum()
        .sort_values(ascending=False)
        .head(6)
        .reset_index()
        .to_dict(orient="records")
    )

    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "personas": personas,
        "bar_data": bar_data,
        "transactions": txns.to_dict(orient="records")
    })

@app.get("/download/{filename}", response_class=FileResponse)
def download_csv(filename: str):
    path = Path(f"data/{filename}")
    if path.exists():
        return path
    return {"error": "File not found"}
