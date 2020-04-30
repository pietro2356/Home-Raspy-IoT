from flask import Flask, request
from gpiozero import LED
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup

radioScanner = LED(14)  # Only on
radioCRI = LED(23)
radioVVF = LED(25)
luce = LED(15)
computer = LED(18)  # Only ON
homeMini = LED(7)  # Only ON
cell = LED(8)
svegliaVar = LED(1)  # Only ON


# ---------------------------------
def botToken():
    return "<<Telegram bot token>>"     # Lo fornisce BotFather alla creazione del bot telegram.


def myId():
    return -1   # ChatID del proprietario.
# ---------------------------------


app = Flask(__name__)
bot = telepot.Bot(botToken())




@app.route('/status')
def index():
    return {'status': 'online'}, 200


@app.route('/relay/', methods=['POST'])
def relay():
    tmp = request.get_json()
    print("Request JSON: ", tmp)
    rel = tmp['rel'].lower()
    val = tmp['val']

    try:
        # comparto radio
        if rel == "radio scanner":
            radSc(val)
        elif rel == "118":
            cri(val)
        elif rel == "vvf":
            vvf(val)

        # comparto casalingo
        elif rel == "luce":
            light(val)
        elif rel == "computer":
            pc(val)
        elif rel == "carica" or rel == "caricatore":
            charger(val)
        elif rel == "home mini":
            mini(val)
        elif rel == "sveglia":
            sveglia(val)

        # categorie
        elif rel == "tutto":
            all(val)
        elif rel == "radio":
            radio(val)
        elif rel == "casa":
            casa(val)
        else:
            return {"Invalid": "value"}, 500
    except Exception as e:
        return {"Exception": e}, 200


# Funzioni principali
# TODO: Da sistemare.
def all(val):
    radSc(val)
    light(val)
    pc(val)
    cri(val)
    vvf(val)
    charger(val)
    mini(val)
    sveglia(val)


def radio(val):
    cri(val)
    vvf(val)
    radSc(val)


def casa(val):
    light(val)
    pc(val)
    charger(val)
    mini(val)
    sveglia(val)


def radSc(val):
    if val == "1":
        radioScanner.on()
        return "OK", 200
    elif val == "0":
        radioScanner.off()
        return "OK", 200
    else:
        return "Error", 500


def light(val):
    if val == "1":
        luce.on()
        return "OK", 200
    elif val == "0":
        luce.off()
        return "OK", 200
    else:
        return "Error", 500


def pc(val):
    if val == "1":
        computer.on()
        return "OK", 200
    elif val == "0":
        computer.off()
        return "OK", 200
    else:
        return "Error", 500


def cri(val):
    if val == "1":
        radioCRI.on()
        return "OK", 200
    elif val == "0":
        radioCRI.off()
        return "OK", 200
    else:
        return "Error", 500


def vvf(val):
    if val == "1":
        radioVVF.on()
        return "OK", 200
    elif val == "0":
        radioVVF.off()
        return "OK", 200
    else:
        return "Error", 500


def charger(val):
    if val == "1":
        cell.on()
        return "OK", 200
    elif val == "0":
        cell.off()
        return "OK", 200
    else:
        return "Error", 500


def mini(val):
    if val == "1":
        homeMini.on()
        return "OK", 200
    elif val == "0":
        homeMini.off()
        return "OK", 200
    else:
        return "Error", 500


def sveglia(val):
    if val == "1":
        svegliaVar.on()
        return "OK", 200
    elif val == "0":
        svegliaVar.off()
        return "OK", 200
    else:
        return "Error", 500


app.run(host='0.0.0.0')
