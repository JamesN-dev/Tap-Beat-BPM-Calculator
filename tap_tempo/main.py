from fastapi import FastAPI
import time
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

templates = Jinja2Templates(directory="templates")

app = FastAPI()

# Serve static files from the "static" directory
app.mount("/static/", StaticFiles(directory="static"), name="static")

# Initialize variables to keep track of tap times and tap count
first_tap_time = None
last_tap_time = None
tap_count = 0
TIMEOUT = 3.0  # 3-second timeout

@app.get("/", response_class=HTMLResponse)
async def get_html(request: Request):
    global TIMEOUT
    return templates.TemplateResponse("index.html", {"request": request, "TIMEOUT": TIMEOUT})

@app.get("/tap/", response_class=HTMLResponse)
async def tap():
    global first_tap_time, last_tap_time, tap_count
    
    # Capture the current time
    current_time = time.time()
    
    # If time between last tap and now exceeds timeout, reset
    if last_tap_time is not None and current_time - last_tap_time > TIMEOUT:
        first_tap_time = None
        last_tap_time = None
        tap_count = 0

    # If this is the first tap, set the first_tap_time
    if first_tap_time is None:
        first_tap_time = current_time
        last_tap_time = current_time
        tap_count = 1
        return '''
        <div id="result" class="mt-4">
            <p><strong>Average BPM:</strong> First Tap</p>
            <p><strong>Nearest Whole:</strong> - </p>
            <p><strong>Number of Taps:</strong> First Tap</p>
        </div>
        '''

    
    # Update the last_tap_time and increment the tap_count
    last_tap_time = current_time
    tap_count += 1
    
    # Calculate the tempo (Beats Per Minute)
    time_interval = last_tap_time - first_tap_time
    bpm = (tap_count - 1) * 60 / time_interval
    
    return f'''
    <div id="result" class="mt-4">
        <p><strong>Average BPM:</strong> {bpm:.2f}</p>
        <p><strong>Nearest Whole:</strong> {round(bpm)}</p>
        <p><strong>Number of Taps:</strong> {tap_count}</p>
    </div>
    '''

@app.get("/tempo/")
async def calculate_tempo():
    global first_tap_time, last_tap_time, tap_count
    
    # Calculate the time interval between the first and last tap
    time_interval = last_tap_time - first_tap_time
    
    # Calculate the tempo (Beats Per Minute)
    tempo = (tap_count - 1) * 60 / time_interval
    
    return {"message": "Tempo calculated", "tempo": tempo}

@app.get("/update_timeout/")
async def update_timeout(timeout: int):
    global TIMEOUT
    TIMEOUT = timeout
