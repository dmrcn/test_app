from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import os

app = FastAPI()

# GET → HTML döndür
@app.get("/", response_class=HTMLResponse)
def home():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

# POST → gönderilen yazıyı geri döndür
class TestRequest(BaseModel):
    text: str

@app.post("/echo")
def echo(req: TestRequest):
    print("✅ POST geldi:", req.text)
    return {
        "received": req.text
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
