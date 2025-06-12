from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)
DB = 'sensors.db'

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS sensor_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            gsr INTEGER,
            heart INTEGER,
            ecg INTEGER
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.get_json()
    gsr = data['gsr']
    heart = data['heart']
    ecg = data['ecg']
    timestamp = datetime.now().isoformat()

    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('INSERT INTO sensor_data (timestamp, gsr, heart, ecg) VALUES (?, ?, ?, ?)',
              (timestamp, gsr, heart, ecg))
    conn.commit()
    conn.close()
    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
