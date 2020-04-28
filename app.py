from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return {'status': 'online'}, 200


app.run(host='0.0.0.0')
