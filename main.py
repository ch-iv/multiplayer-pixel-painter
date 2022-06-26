from flask import Flask, send_from_directory
from flask_socketio import SocketIO
import os
from board import Board
import time


_board = Board(100, 50, (255, 255, 255))
board_save_interval = 5
app = Flask(__name__, static_folder=os.path.join("client", "public"))
socketio = SocketIO(app)


@app.route("/")
def board():
    return send_from_directory(app.static_folder, "index.html")


@app.route("/<path:path>")
def static_files(path):
    """This function is used to serve static files"""
    return send_from_directory(app.static_folder, path)


@socketio.on("set_pixel")
def set_pixel_event(data):
    assert "x" in data
    assert "y" in data
    assert "color" in data
    assert len(data["color"]) == 3
    assert data["color"][0] < 256 and data["color"][1] < 256 and data["color"][2] < 256

    _board.set(data["x"], data["y"], data["color"])

    socketio.emit("pixel_change", data)


@socketio.on("connection_event")
def connection_event():
    socketio.emit("board_full", {"pixels": _board.pixels})


def save_board():
    while 1:
        _board.dump()
        time.sleep(board_save_interval)


if __name__ == "__main__":
    socketio.start_background_task(save_board)
    socketio.run(app)
