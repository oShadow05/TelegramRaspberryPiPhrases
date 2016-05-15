import botogram
import random
from config import *


# Prepara il bot
bot = botogram.create(TELEGRAM_TOKEN)
# Lista dei messaggi
messages = (
    "Compra un raspberry pi!",
    "Ti sei ricordato di comparare un raspberry pi?",
    "Compralo!",
    "Anche Pelloni ne dovrebbe compare uno!",
    "Costa solo 45€!",
    "Se vuoi c'è anche quello da 5€!"
)


# Il messaggio in chat contiene 'raspberry'
@bot.message_contains("raspberry")
def raspberry_message(chat, message):
    """Invia un messaggio a random dalla lista messages"""
    send_raspberry_message(chat, message)


# Comando /raspberry
@bot.command("raspberry")
def raspberry_commad(chat, message):
    """Invia un messaggio a random dalla lista messages"""
    send_raspberry_message(chat, message)


# Comando /raspberrypi
@bot.command("raspberrypi")
def raspberrypi_commad(chat, message):
    """Invia un messaggio a random dalla lista messages"""
    send_raspberry_message(chat, message)


def send_raspberry_message(chat, message):
    """Funziona per inviare un messaggio a random dalla lista messages"""
    msg_n = random.randint(0, len(messages) - 1)
    msg = messages[msg_n]
    chat.send(msg)

    log_request(chat, message)


# Logga in console che qualcuno ha fatto una richiesta
def log_request(chat, message):
    # Un utente potrebbe non avere un nome utente
    if message.from_.username is None:
        # Se non hanno un username logghiamo il nome
        print("Ricevuto messaggio da chatid: " + message.from_.name)
    else:
        # Se hanno un username logghiamo l'username
        print("Ricevuto messaggio da: " + message.from_.username)


if __name__ == '__main__':
    # Avvia il bot
    bot.run()
