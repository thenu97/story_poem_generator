from flask import Flask, request
import requests

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    story = request.args.get("story")
    if story == '312' or story == '321':
        return "story"
    else:
        return "poem"

if __name__ == "__main__":
    app.run(port=5003, host='0.0.0.0')