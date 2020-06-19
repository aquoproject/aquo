from flask import Flask
import pymysql.cursors
import json
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/get/<string:userid>')
def sendData(userid):
    connection = pymysql.connect(host='89.46.111.208',
                                user='Sql1448166',
                                password='4m3x452151',
                                db='Sql1448166_2',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

    sql = "SELECT * FROM `dati` WHERE userid = '" + userid + "';"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return json.dumps(result)
    connection.commit()
    cursor.close()
    connection.close()

@app.route('/send/<string:raw_data>')
def getData(raw_data):
    data = raw_data.split(',')
    
    tz = pytz.timezone('Europe/Rome')
    rome = datetime.now(tz)
    currentDate = rome.strftime('%Y/%m/%d')
    currentTime = rome.strftime('%H:%M:%S')

    connection = pymysql.connect(host='localhost',
                                user='aquo',
                                password='ilovewater2020',
                                db='aquo',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

    sql = "INSERT INTO dati (nome, cognome, userid, ph, temperatura, data, ora) VALUES ('" + data[0] + "', '" + data[1] + "', '" + data[2] + "', '" + data[3] + "', '" + data[4] + "', '" + currentDate + "', '" + currentTime + "');"
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    return "fatto"
    cursor.close()
    connection.close()