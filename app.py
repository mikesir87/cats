from flask import Flask, render_template
import random
import socket

app = Flask(__name__)

container_hostname = socket.gethostname()

# list of cat images
images = [
    "https://media.giphy.com/media/cfuL5gqFDreXxkWQ4o/giphy.gif",
    "https://media.giphy.com/media/W8krmZSDxPIfm/giphy.gif",
    "https://media.giphy.com/media/UxGNvgpU1hoAw/giphy.gif",
    "https://media.giphy.com/media/UxGNvgpU1hoAw/giphy.gif",
    "https://media.giphy.com/media/WLNASdXoq0ZtC/giphy.gif",
    "https://media.giphy.com/media/HYpZKsyLOn1ks/giphy.gif",
    "https://media.giphy.com/media/l8px6snusvpII/giphy.gif",
    "https://media.giphy.com/media/l0Iy9Kry5yhBSwQSs/giphy.gif",
    "https://media.giphy.com/media/7SfAXqgRgh0li/giphy.gif",
    "https://media.giphy.com/media/W80Y9y1XwiL84/giphy.gif"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url, hostname=container_hostname)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
