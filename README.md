# multiplayer-pixel-painter
A web-based multiplayer pixel painter application.

### Dependencies
 - Python, flask and flask_socketio for backend
 - Svelte for frontend
 - Two.js for 2D vector graphics

### Installation
Install Python and npm package manager

clone the repo
`git clone https://github.com/ch-iv/multiplayer-pixel-painter`

make a virtual environment
`python -m venv env`

activate the evniroment. For Windows:
`env\Scripts\activate.bat`

install python libraries
`pip install -r requirements.txt`

build the frontend
`cd clinet`
`npm install`
`npm run build`
`cd ..`

start the app
`python main.py`

