import urllib3, flask, pytest, requests, os
from flask_mysqldb import MySQL
from flask import Flask
from app import home, crud, update, delete

app = Flask(__name__)

app.config['MYSQL_HOST'] = os.environ['MYSQLHOST']
app.config['MYSQL_USER'] = os.environ['MYSQLUSER']
app.config['MYSQL_PASSWORD'] = os.environ['MYSQLPASSWORD']
app.config['MYSQL_DB'] = os.environ['MYSQLDB']

mysql = MySQL(app)

url = 'http://35.214.21.98/'
url2 = 'http://35.214.21.98/crud'
url3 = 'http://35.189.121.149/'
url4 = 'http://35.189.121.149/crud'

############################################################### testing url ###############################################################
def test_urlmanager_home():
    r = requests.get(url)
    assert r.status_code == 200

def test_manager_crud():
    r = requests.get(url2)
    assert r.status_code == 200

def test_worker_home():
    r = requests.get(url3)
    assert r.status_code == 200

def test_worker_crud():
    r = requests.get(url4)
    assert r.status_code == 200

def test_nonexist():
    r = requests.get("http://35.214.21.98/nonexist")
    assert r.status_code == 404

def test_getresponse():
    r = requests.get(url)
    assert isinstance(r.text, str)

def test_getresponse1():
    r = requests.get(url3)
    assert isinstance(r.text, str)



############################################################### testing db ###############################################################
def test_select():
    with app.app_context():
        cur = mysql.connection.cursor()
        resultValue = cur.execute("SELECT * FROM lit")
        mysql.connection.commit()
        cur.close()
    print(resultValue)
    assert 5 == resultValue

def test_describe():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("DESCRIBE lit;")
        col = len(cur.fetchall())
        mysql.connection.commit()
        cur.close()
        assert col == 5

def test_insert():
    with app.app_context():
        m = []
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO lit (theme, chars, decide, up) VALUES ('Testing', 'Testing', 'Testing', 99)")
        mysql.connection.commit()
        cur.execute("SELECT * FROM lit") #this gets record after update
        record_after = cur.fetchall()
        for i in record_after:
            for j in i:
                m.append(j)
        cur.close()
    assert('Testing') == m[-4]
    assert('Testing') == m[-3]
    assert('Testing') == m[-2]
    assert 99 == m[-1]



def test_update():
    with app.app_context():
        m = []
        cur = mysql.connection.cursor()
        cur.execute("UPDATE lit SET theme = 'TESTING' WHERE up = 99")
        mysql.connection.commit()
        cur.execute("SELECT * FROM lit")
        records_after = cur.fetchall()
        for i in records_after:
            for j in i:
                m.append(j)
        cur.close()
    assert('TESTING') == m[-4]



def test_delete():
    with app.app_context():
        cur = mysql.connection.cursor()
        records_before = cur.execute("SELECT * FROM lit")
        mysql.connection.commit()
        cur.execute("DELETE FROM lit WHERE theme = 'TESTING'")
        mysql.connection.commit()
        records_after = cur.execute("SELECT * FROM lit")
        mysql.connection.commit()
        cur.close()
    assert records_before - 1 == records_after