from flask import Flask, request, jsonify
import psycopg2
from psycopg2.extras import DictCursor
import json

app = Flask('Desafio')

def get_db_connection():
    conn = psycopg2.connect(
        dbname="rklrejgj", 
        user="rklrejgj", 
        password="vSDcFc14nusYYaRPMQVY6qvhy0_A8vbv",
        host="silly.db.elephantsql.com"  
    )
    return conn

conn = get_db_connection()
cursor = conn.cursor()

@app.route("/clientes", methods=["GET"])
def listaClientes():
    pass

if __name__ == '__main__':
    app.run(debug=True)