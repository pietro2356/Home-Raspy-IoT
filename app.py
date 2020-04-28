from flask import Flask
from gpiozero import LED

radioScanner = LED(14)  # Only on
radioCRI = LED(23)
radioVVF = LED(25)
luce = LED(15)
computer = LED(18)  # Only ON
homeMini = LED(7)  # Only ON
cell = LED(8)
svegliaVar = LED(1)  # Only ON


app = Flask(__name__)


@app.route('/')
def index():
    return {'status': 'online'}, 200


app.run(host='0.0.0.0')
