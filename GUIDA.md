# GUIDA AL CODICE

Ecco cosa serve per far funzionare il codice

> **PREMESSA: L'ambiente utilizzato e Unix Based.**

## 1. Ambiente virtuale:

Questa operazione è alquanto delicata. Si consiglia di effettuarla in un ambiente pulito.

Operazioni:

1. Installare Python3 e pip3.

2. Creare una nuova cartella per il progetto.

3. Installare l'ambiente virtuale.

4. Installare Flask.

5. Creazione file `app.py`

6. Primo avvio e prova.

Comandi:

```bash
#Passo 1:
sudo apt install python3 python3-pip

#Passo 2:
mkdir pippo
cd pippo

#Passo 3:
# In questo modo il pacchetto pipenv viene 
# inserito automaticamente nel PATH di sistema.
# Ed è richiamabile subito dopo l'installazione.
sudo -H pip3 install -U pipenv


#Passo 4:
sudo pipenv install flask
```

Adeso creiamo il file `app.py`:

```python
# Passo 5
#~ pippo/app.py

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return {"Hello": "World!"}

app.run(host='0.0.0.0')
```

Adesso non rimane altro che avviare la nostra API.

```bash
#Passo 6
pipenv shell
python app.py
```

Una volta avviato verrà generato un'output di questo tipo:

```
* Serving Flask app "app" (lazy loading)
* Environment: production
  WARNING: This is a development server. Do not use it in a production deployment.
  Use a production WSGI server instead.
* Debug mode: off
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

---

### 2. Uso GPIO del RaspberryPi

Adesso andiamo ad analizzre come utilizzre le GPIO del nostro RaspberryPi.

#### Installiamo le librerie per le GPIO

Nell ultime versioni i pin sono pressocché indentici, ma per sicurezza volgiamo visualizzare la pinnatura del nostro Raspberry. 

Per fare questo ci servirà un pacchetto python chiamato gpiozero:

```shell
# Aggiorniamo il raspberry
sudo apt update && sudo apt upgrade

# Installiamo il paccheto con:
sudo apt install python3-gpiozero
```

Una volta fatto ciò, basterà lanciare il comando:

```shell
pinout
```

---

#### 3. Implementazione bot Telegram

> **Per prima cosa bisogna creare un bot telegram tramite botFather.**

Adesso vi sono un paio di operazioni da fare:

1. installare telepot.

2. implementare telepot tramite python.

```shell
# Passo 1
sudo pip3 install telepot
```

```python
# Passo 2

import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup
```

Per comodità andiamo a definire due funzioni che ci restituiranno il nostro ChatID ed il tag del bot telegram fornito da botFather.

```python
def botToken():
    return "Bot token"


def myId():
    return -1 # Sostituire col proprio chatID.
```
