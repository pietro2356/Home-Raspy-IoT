# GUIDA AL CODICE

Ecco cosa serve per far funzionare il codice

> PREMESSA: L'ambiente utilizzato e **Unix Based**.

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
