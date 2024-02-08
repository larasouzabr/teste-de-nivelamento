from collections import defaultdict
from operator import itemgetter
from flask import Flask, jsonify
import psycopg2
import os
from dotenv import load_dotenv
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app)

load_dotenv()


def get_db_connection():
    try:
       conn = psycopg2.connect(
            dbname=os.getenv('DB_NAME'), 
            user=os.getenv('DB_USER'), 
            password=os.getenv('DB_PASSWORD'), 
            host=os.getenv('DB_HOST')
    ); return conn   
    except psycopg2.Error as e:
        print("Erro ao conectar ao banco de dados:", e)
        return None


@app.route('/api/dados', methods=['GET'])
def get_data_from_db():
    conn = get_db_connection()
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM operadorasativas")
        column_names = [desc[0] for desc in cursor.description]
        data = cursor.fetchall()
        conn.close()
        response = []
        for row in data:
            row_data = {}
            for idx, col in enumerate(column_names):
                row_data[col] = row[idx]
            response.append(row_data)
        return jsonify(response), 200, {'Content-Type': 'application/json; charset=utf-8'}
    else:
        return jsonify({'message': 'Erro ao conectar ao banco de dados'}), 500

@app.route('/api/busca/<query>', methods=['GET'])
def search_data_from_db(query):
    if not query:
        return jsonify({'message': 'Informe um parâmetro de consulta'}), 400
    
    conn = get_db_connection()
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM operadorasativas")
        column_names = [desc[0] for desc in cursor.description]
        data = cursor.fetchall()
        conn.close()

    #ANALISA QUANTAS VEZES O TERMO APARECEU NA LINHA DO OBJETO
        relevance_scores = defaultdict(int)
        for row in data:
            for col in row:
                if col and isinstance(col, str):
                    relevance_scores[row] += col.lower().count(query.lower())
        
        sorted_records = sorted(relevance_scores.items(), key=itemgetter(1), reverse=True)
        
        relevant_data = []
        for record, relevance_score in sorted_records:
            record_dict = {'relevance_score': relevance_score}
            for col_index, col_value in enumerate(record):
                col_name = column_names[col_index]
                record_dict[col_name] = col_value
            relevant_data.append(record_dict)

        return jsonify(relevant_data), 200
    else:
        return jsonify({'message': 'Erro ao conectar ao banco de dados'}), 500

if __name__ == '__main__':
    app.run(debug=True)

