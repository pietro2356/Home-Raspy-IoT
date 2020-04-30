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
# TELEGRAM FUNCTION
def botToken():
    return "<<Telegram bot token>>"     # Lo fornisce BotFather alla creazione del bot telegram.


def myId():
    return -1   # ChatID del proprietario.

# ~~UNICODE PER EMOJI~~
def greenSquare():
    return u'\U00002705'


def redSquare():
    return u'\U0000274C'


def casaEM():
    return u'\U0001F3E0'


def radioEM():
    return u'\U0001F4FB'


def faceEM():
    return u'\U0001F917'


def teschioEM():
    return u'\U00002620'


def boomEM():
    return u'\U0001F4A5'


def goEM():
    return u'\U00002733'
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


keyboard = ReplyKeyboardMarkup(keyboard=[
    ['/START', '/STATUS'],
    ['RADIO ON' + radioEM() + greenSquare(), 'RADIO OFF' + radioEM() + redSquare()],
    ['CASA ON' + casaEM() + greenSquare(), 'CASA OFF' + casaEM() + redSquare()],
    ['ALL ON' + greenSquare(), 'ALL OFF' + redSquare()],
    ['/ADV']])


def isOnline():
    bot.sendMessage(myId(), "Bot online", reply_markup=keyboard)


def handle(msg):
    contentType, chatType, chatId = telepot.glance(msg)
    text = msg['text'].upper()

    if not (chatId == myId()):
        bot.sendMessage(chatId, "Non sei autorizzato ad utilizzare questo bot!" + teschioEM())

    # RADIO
    elif text == "RADIO ON" + radioEM() + greenSquare():
        radio("1")
        bot.sendMessage(myId(), "Radio accese" + greenSquare())
    elif text == "RADIO OFF" + radioEM() + redSquare():
        radio("0")
        bot.sendMessage(myId(), "Radio spente" + redSquare())

    # CASA
    elif text == "CASA ON" + casaEM() + greenSquare():
        casa("1")
        bot.sendMessage(myId(), "Casa accesa" + greenSquare())
    elif text == "CASA OFF" + casaEM() + redSquare():
        casa("0")
        bot.sendMessage(myId(), "Casa spenta" + redSquare())

    # TUTTO
    elif text == "ALL ON" + greenSquare():
        all("1")
        bot.sendMessage(myId(), "Tutto acceso" + greenSquare())
    elif text == "ALL OFF" + redSquare():
        all("0")
        bot.sendMessage(myId(), "Tutto spento" + redSquare())

    # START
    elif text == '/START':
        bot.sendMessage(myId(), "Benvenuto!" + faceEM(), reply_markup=keyboard)

    # BACK
    elif text == '/BACK':
        bot.sendMessage(myId(), 'Sessione avanzata disabilitata.', reply_markup=keyboard)

    # COMANDI AVANZATI
    elif text == 'RADIO SCANNER ON':
        radSc("1")
        bot.sendMessage(myId(), "Radio scanner acceso" + greenSquare())
    elif text == 'RADIO SCANNER OFF':
        radSc("0")
        bot.sendMessage(myId(), "Radio scanner spento" + redSquare())

    elif text == '118 ON':
        cri("1")
        bot.sendMessage(myId(), "Radio 118 accesa" + greenSquare())
    elif text == '118 OFF':
        cri("0")
        bot.sendMessage(myId(), "Radio 118 spenta" + redSquare())

    elif text == 'VVF ON':
        vvf("1")
        bot.sendMessage(myId(), "Radio VVF accesa" + greenSquare())
    elif text == 'VVF OFF':
        vvf("0")
        bot.sendMessage(myId(), "Radio VVF spenta" + redSquare())

    elif text == 'LUCE ON':
        light("1")
        bot.sendMessage(myId(), "Luce accesa" + greenSquare())
    elif text == 'LUCE OFF':
        light("0")
        bot.sendMessage(myId(), "Luce spenta" + redSquare())

    elif text == 'COMPUTER ON':
        pc("1")
        bot.sendMessage(myId(), "Computer acceso" + greenSquare())
    elif text == 'COMPUTER OFF':
        pc("0")
        bot.sendMessage(myId(), "Computer spento" + redSquare())

    elif text == 'CARICATORE ON':
        charger("1")
        bot.sendMessage(myId(), "Carica cell acceso" + greenSquare())
    elif text == 'CARICATORE OFF':
        charger("0")
        bot.sendMessage(myId(), "Carica cell spento" + redSquare())

    else:
        bot.sendMessage(myId(), "Comando non valido!" + redSquare() + redSquare())


isOnline()
MessageLoop(bot, handle).run_as_thread()


app.run(host='0.0.0.0')
