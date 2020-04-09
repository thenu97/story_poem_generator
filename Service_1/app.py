from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import os, random, requests
import json


app = Flask(__name__)
mysql = MySQL(app)


app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB')


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        theme = request.form['theme']
        char_1 = request.form['char']
        char_2 = request.form['anchar']
        them = requests.get('http://service_3:5002?theme='+theme)
        characters = requests.get('http://service_2:5001?char='+char_1+char_2)
        dec = requests.get('http://service_4:5003?story='+theme+char_1+char_2)
        story = []
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO story (theme, chars, decide) VALUES (%s, %s, %s)", (str(them.text), str(characters.text), str(dec.text)))
        mysql.connection.commit()
        cur.close()
        if dec.text == "poem":
            if them.text == "tragic":
                with open("/SFIA2/Service_1/doc/poem/sad/tragic") as trag:
                    tragic = trag.read()
                    story.append(tragic)
                    mit = story[0]
            if them.text == "sorrow":
                with open("/SFIA2/Service_1/doc/poem/sad/sorrow") as sorrow:
                    sor = sorrow.read()
                    story.append(sor)
                    mit = story[0]
            if them.text == "dark humour":
                with open("/SFIA2/Service_1/doc/poem/comedy/dark") as dark:
                    dark_humour = dark.read()
                    story.append(dark_humour)
                    mit = story[0]
            if them.text == "light humour":
                with open("/SFIA2/Service_1/doc/poem/comedy/light") as light:
                    light_humour = light.read()
                    story.append(light_humour)
                    mit = story[0]
            if them.text == "fluff":
                with open("/SFIA2/Service_1/doc/poem/romance/fluff") as fluff:
                    flu = fluff.read()
                    story.append(flu)
                    mit = story[0]
            if them.text == "intense":
                with open("/SFIA2/Service_1/doc/poem/romance/intense") as intense:
                    inten = intense.read()
                    story.append(inten)
                    mit = story[0]
        else:
            if them.text == "fluff":
                with open("/SFIA2/Service_1/doc/story/romance/fluff") as fluff:
                    flu = fluff.read()
                    story.append(flu)
                    lit = story[0].replace("___", characters.text.split(' ')[1])
                    mit = lit.replace("///", characters.text.split(' ')[0])
            if them.text == "intense":
                with open("/SFIA2/Service_1/doc/story/romance/intense") as inten:
                    intense = inten.read()
                    story.append(intense)
                    lit = story[0].replace("___", characters.text.split(' ')[1])
                    mit = lit.replace("///", characters.text.split(' ')[0])
        mit = ("<br>").join(mit.split("\n"))
        return render_template("index.html", sentence = mit, title="read")
    return render_template("index.html", sentence = "Hello, Welcome to the site!! Choose your theme and be surprised", title="read")

if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')