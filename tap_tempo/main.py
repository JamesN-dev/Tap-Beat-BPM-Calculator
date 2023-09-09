from fastapi import FastAPI
import time
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.responses import HTMLResponse

templates = Jinja2Templates(directory="templates")

app = FastAPI()

# Initialize variables to keep track of tap times and tap count
first_tap_time = None
last_tap_time = None
tap_count = 0
TIMEOUT = 3.0  # 3-second timeout

@app.get("/", response_class=HTMLResponse)
async def get_html(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
def read_root():
    return {"message": "Hello, world!"}

@app.get("/tap/", response_class=HTMLResponse)
def tap():
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
            <p><strong></strong> First Tap</p>
            <p><strong>Number of Taps:</strong> 1</p>
            <p><strong>Average BPM:</strong> - </p>
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
        <p><strong></strong> Tap registered</p>
        <p><strong>Number of Taps:</strong> {tap_count}</p>
        <p><strong>Average BPM:</strong> {bpm}</p>
    </div>
    '''

@app.get("/tempo/")
def calculate_tempo():
    global first_tap_time, last_tap_time, tap_count
    
    if tap_count < 2:
        return {"message": "Keep tapping..."}
    
    # Calculate the time interval between the first and last tap
    time_interval = last_tap_time - first_tap_time
    
    # Calculate the tempo (Beats Per Minute)
    tempo = (tap_count - 1) * 60 / time_interval
    
    return {"message": "Tempo calculated", "tempo": tempo}
