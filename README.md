# Tap Beat BPM Calculator

## Python - FastAPI - HTMX - TailewindCSS

## Overview
This web app aims to provide a simple and interactive way to calculate Beats Per Minute (BPM) by tapping a button. FastAPI for the backend and TailwindCSS for styling. The project also leverages htmx for efficient partial page updates without requiring a complete page reload.

## Features
- Real-time BPM calculation(Average and Nearest Whole BPM)
- Timeout for inactivity
- Responsive design

## Installation

### Prerequisites
- Coded in Python 3.11.5 but may work in other versions.
- Poetry - (https://python-poetry.org/docs/)
- htmx - (https://htmx.org/)
- Other required packages are listed in the `pyproject.toml` file.

### Setup
1. Clone this repository: `git clone <THIS_REPOSITORY_URL>`
2. Navigate to the project folder: `cd Tap_tempo`
3. Install dependencies: `poetry install`
4. Run the project: `poetry run uvicorn tap_tempo.main:app --reload`

## Usage
Open your web browser and navigate to `http://127.0.0.1:8000/` to use the application.

## License
MIT License. See `LICENSE` for more information.
