from flask import Flask, render_template
import random
import socket

app = Flask(__name__)

container_hostname = socket.gethostname()

# list of cat images
images = [
    "https://media.giphy.com/media/JfDNFU1qOZna/giphy.gif",
    "https://media.giphy.com/media/pSpmpxFxFwDpC/giphy.gif",
    "https://media.giphy.com/media/9IRX12VhoXoR2/giphy.gif",
    "https://media.giphy.com/media/BlRv1TWmIXYVq/giphy.gif",
    "https://media.giphy.com/media/3oEduKP4VaUxJvLwuA/giphy.gif",
    "https://media.giphy.com/media/NcNCvPAkUH43e/giphy.gif",
    "https://media.giphy.com/media/timWG1lyyfcYw/giphy.gif",
    "https://media.giphy.com/media/KDn7wFpW7V9ba/giphy.gif",
    "https://media.giphy.com/media/EzOpIqfw2zLDa/giphy.gif",
    "https://media.giphy.com/media/3o7Zez01HKXvaLXiHS/giphy.gif"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url, hostname=container_hostname)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
