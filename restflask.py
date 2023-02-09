
from flask import Flask,request,Response
import json
import sqlite3
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('input.html')

@app.route('/date',methods = ['GET','POST'])
def Input():
    Date = request.form['Date']
    
    connection = sqlite3.connect(r"C:\\Users\\HP\Documents\\dB browser\\assignment.sqlite3")
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM MSFT WHERE DATE = {Date}")
    cursor.close()
    
    json_output = json.dumps(cursor)    
    return Response.json(json_output)

if __name__ == '__main__':
   app.run(debug = True,use_reloader=False)