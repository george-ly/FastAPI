import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()

class CallRequest(BaseModel):
    phone_number: str

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html>
      <head>
        <meta charset="utf-8" />
        <title>AI Resume Interviewer</title>
      </head>
      <body>
        <h1>AI Resume Interviewer</h1>
        <input id="phone" placeholder="+44..." />
        <button onclick="startCall()">Start Call</button>
        <pre id="output"></pre>

        <script>
          async function startCall() {
            const phone = document.getElementById("phone").value;
            const res = await fetch("/start-call", {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify({ phone_number: phone })
            });
            const data = await res.json();
            document.getElementById("output").textContent =
              JSON.stringify(data, null, 2);
          }
        </script>
      </body>
    </html>
    """

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/start-call")
def start_call(req: CallRequest):
    # replace this with your Retell/Vapi outbound-call API request
    return {
        "status": "ok",
        "message": f"Would place outbound call to {req.phone_number}"
    }



if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)