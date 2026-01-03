from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()

# 🔥 CORS (HER ŞEYE İZİN – DEBUG İÇİN)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # prod'da domain yazılır
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Echo(BaseModel):
    text: str

@app.get("/", response_class=HTMLResponse)
def index():
    return """
    <html>
    <body>
        <input id="txt" />
        <button onclick="send()">Send</button>
        <pre id="out"></pre>

        <script>
        async function send() {
            const res = await fetch("/echo", {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({text: document.getElementById("txt").value})
            });
            document.getElementById("out").innerText = await res.text();
        }
        </script>
    </body>
    </html>
    """

@app.post("/echo")
def echo(data: Echo):
    return {"received": data.text}
