# Tap Beat BPM Calculator

## Python - FastAPI - HTMX - TailewindCSS

## Overview
This is a simple web app that calculates Beats Per Minute (BPM) by tapping a button or key.

## Features
- Real-time BPM calculation(Average and Nearest Whole BPM).
- Enter timeout - seconds until BPM calculations reset to zero.
- Use any key to tap or click the tap button with your mouse.


## If you want to use this code for some reason:

### Prerequisites
- Coded in Python 3.11.5 but may work in other versions.
- Poetry (for package management)
- Other required packages are listed in the `pyproject.toml` file.

### Setup
1. Clone this repository: `git clone <THIS_REPOSITORY_URL>`
2. Navigate to the project folder: `cd Tap_tempo`
3. Install dependencies: `poetry install`
4. Run the project: `poetry run uvicorn tap_tempo.main:app --reload`

## Usage
Open your web browser and navigate to your localhost to use the application.

## Disclaimer ##
 This project is currently in active development and may not be suitable for production use. It is intended for testing, learning, and experimentation purposes.

## License
MIT License. See `LICENSE` for more information.
