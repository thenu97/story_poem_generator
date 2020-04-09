from flask import Flask, request
import requests, random


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def home():
    com = ['dark humour', 'light humour']
    rom = ['fluff', 'intense']
    blue = ['sorrow', 'tragic']
    theme = request.args.get("theme")
    if theme == '1':
        return blue[random.randrange(2)]
    elif theme == '2':
        return com[random.randrange(2)]
    else:
        return rom[random.randrange(2)]


if __name__ == "__main__":
    app.run(port=5002, host='0.0.0.0')