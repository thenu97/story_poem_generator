from flask import Flask, request
import random, requests

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def home():
    female = ['Taylor', 'Casey', 'Sarah', 'Felicia', 'Sage', 'Hope', 'Julia', 'Grace', 'Aria', 'Joy', 'Megan', 'Hannah', 'Gillian', 'Eden']
    male = ['Mund', 'Ash', 'Gordon', 'Aaron', 'Adam', 'Axel', 'Art', 'Eli', 'Evan', 'Jose', 'Kero', 'Noah', 'Trent', 'Zac']
    character = request.args.get("char")
    if character == '11':
        return female[random.randrange(14)] + " " + female[random.randrange(14)]
    elif character == '21' or character == '12':
        return male[random.randrange(14)] + " " + female[random.randrange(14)]
    else:
        return male[random.randrange(14)] + " " + male[random.randrange(14)]


if __name__ == "__main__":
    app.run(port=5001, host='0.0.0.0')