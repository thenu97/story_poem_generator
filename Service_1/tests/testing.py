import urllib3, flask, pytest, requests, os
from flask_mysqldb import MySQL
from flask import Flask
from app import home

app = Flask(__name__)

app.config['MYSQL_HOST'] = os.environ['MYSQLHOST']
app.config['MYSQL_USER'] = os.environ['MYSQLUSER']
app.config['MYSQL_PASSWORD'] = os.environ['MYSQLPASSWORD']
app.config['MYSQL_DB'] = os.environ['MYSQLDB']

mysql = MySQL(app)

url = "http://35.214.24.78/"
url2 = "http://35.214.24.78:5000/"
url3 = "http://35.246.33.39/"
url4 = "http://35.246.33.39:5000/"

############################################################### testing url ###############################################################
def test_urlmanager_home():
    r = requests.get(url)
    assert r.status_code == 200

def test_manager_home2():
    r = requests.get(url2)
    assert r.status_code == 200

def test_worker_home():
    r = requests.get(url3)
    assert r.status_code == 200

def test_worker_home2():
    r = requests.get(url4)
    assert r.status_code == 200

def test_nonexist():
    r = requests.get("http://35.214.24.78/nonexist")
    assert r.status_code == 404

def test_getresponse():
    r = requests.get(url)
    assert isinstance(r.text, str)

def test_getresponse1():
    r = requests.get(url3)
    assert isinstance(r.text, str)



############################################################### testing db ###############################################################

def test_insert():
    with app.app_context():
        m = []
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO story (theme, chars, decide) VALUES ('Testing', 'Testing', 'Testing')")
        mysql.connection.commit()
        cur.execute("SELECT * FROM story") #this gets record after update
        record_after = cur.fetchall()
        print(record_after)
        for i in record_after:
            for j in i:
                m.append(j)
        cur.close()
    lena = len(record_after)
    assert('Testing') == m[-3]
    assert('Testing') == m[-2]
    assert('Testing') == m[-1]

def test_delete():
    with app.app_context():
        cur = mysql.connection.cursor()
        records_before = cur.execute("SELECT * FROM story")
        print(records_before)
        mysql.connection.commit()
        cur.execute("DELETE FROM story WHERE theme = 'Testing'")
        mysql.connection.commit()
        records_after = cur.execute("SELECT * FROM story")
        print(records_after)
        mysql.connection.commit()
        cur.close()
    assert records_before - 1 == records_after