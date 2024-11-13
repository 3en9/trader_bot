from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Request, HTTPException, Body
import datetime
text = ''
app = FastAPI()
ALLOWED_IPS = {"127.0.0.1", "192.168.1.100", '52.89.214.238', '34.212.75.30', '54.218.53.128', '52.32.178.7'}
@app.middleware("http")
async def ip_filter_middleware(request: Request, call_next):
    client_ip = request.client.host
    if client_ip not in ALLOWED_IPS:
        raise HTTPException(status_code=403, detail="Access forbidden")
    response = await call_next(request)
    return response

@app.post("/")
async def read_root(data=Body()):
    global text
    try:
        data = data.decode('utf-8')
        text += f'{datetime.datetime.today().hour}:{datetime.datetime.today().minute} {data}\n'
    except:
        pass

@app.get("/")
async def root():
    return HTMLResponse(text.replace('\n', '<br>'))

# curl -H "Content-Type: text / plain; charset = utf-8" -d "BTCUSD Больше 9000" -X POST http://127.0.0.1:8000


