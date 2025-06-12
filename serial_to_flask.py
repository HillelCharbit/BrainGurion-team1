import serial
import requests

SERIAL_PORT = 'COM3'  # or '/dev/ttyUSB0' on Linux
BAUD_RATE = 9600
FLASK_URL = 'http://localhost:5000/data'

ser = serial.Serial(SERIAL_PORT, BAUD_RATE)

while True:
    try:
        line = ser.readline().decode().strip()  # e.g., "512,480,623"
        gsr, heart, ecg = map(int, line.split(","))
        payload = {'gsr': gsr, 'heart': heart, 'ecg': ecg}
        requests.post(FLASK_URL, json=payload)
        print("Sent:", payload)
    except Exception as e:
        print("Error:", e)
