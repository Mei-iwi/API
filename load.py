import os
import pyodbc
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
CORS(app)
Server = "MEI\\SQLEXPRESS"
database = "LOGIN"
# Server = os.getenv("DB_SERVER", "MEI\\SQLEXPRESS")  # Tên server của bạn
# database = os.getenv("DB_DATABASE", "LOGIN")  
def getDataBase():
   return pyodbc.connect(f'DRIVER={{SQL Server}};'f'SERVER={Server};'f'DATABASE={database};''Trusted_Connection=yes;''PORT = 1433')

@app.route("/", methods=['GET'])
def getData():
    conn = getDataBase()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM ACCOUNT')
    rows = cursor.fetchall()
    data = [{'ACC': row[0], 'PASS':row[1]} for row in rows]
    response = jsonify(data)
    response.headers.add("Access-Control-Allow-Origin", "*")
    cursor.close()
    conn.close()
    return response
@app.route("/", methods=['POST'])
def addData():
    data = request.get_json()
    ACC = data.get('ACC')
    PASS = data.get('PASS')
    # if not ACC or not PASS:
    #     return 
    conn = getDataBase()
    cursor = conn.cursor()
    cursor.execute("SELECT ACC FROM ACCOUNT WHERE ACC = ?",(ACC,))
    if cursor.fetchone():
        return jsonify({"error": "Fail"}), 400
    cursor.execute("INSERT INTO ACCOUNT (ACC, PASS) VALUES(?,?)",(ACC, PASS))
    conn.commit()
    conn.close()
    return jsonify({"message":"Congratulation"}), 201
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
