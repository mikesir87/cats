from flask import Flask, render_template
import random
import socket

app = Flask(__name__)

container_hostname = socket.gethostname()

# list of cat images
images = [
   "https://media.giphy.com/media/NlhFkubROc8VO/giphy.gif",
   "https://media.giphy.com/media/i9LSCNABlPkBy/giphy.gif",
   "https://media.giphy.com/media/FaKV1cVKlVRxC/giphy.gif",
   "https://media.giphy.com/media/1fVxVX43xs7eM/giphy.gif",
   "https://media.giphy.com/media/qhhamrBnxSKNG/giphy.gif",
   "https://media.giphy.com/media/k440hwq05EgBW/giphy.gif",
   "https://media.giphy.com/media/1fjC4zSQTiRkAfnQAj/giphy.gif"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url, hostname=container_hostname)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
