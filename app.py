from flask import Flask, render_template, request, jsonify
from nltk.chat.util import Chat, reflections

app = Flask(__name__)

# Definir las reglas de chat
pares = [
    [
        r"mi nombre es (.*)",
        ["Hola %1, ¿en qué puedo ayudarte hoy?"]
    ],
    [
        r"¿cómo estás?",
        ["Estoy bien, gracias. ¿Y tú?"]
    ],
    [
        r"¿quien eres?",
        ["Soy un bot de chat y mi nombre es Bot. ¿Cómo puedo ayudarte?"]
    ],
    [
        r"adiós",
        ["¡Adiós! Espero haberte ayudado."]
    ],
    [
        r"(.*) (cumpleaños|cumple)",
        ["Feliz cumpleaños. ¡Que tengas un gran día!"]
    ],
    [
        r"hola",
        ["hola mucho gusto soy una inteligencia artificial"]
    ],
    [
        r"como te llamas",
        ["soy juancito creado en python 3.11.9 xDDDDDD"]
    ],
    [
        r"¿(.*) consejo",
        ["No te preocupes por las cosas que no puedes controlar.", "Mantén la calma y sigue adelante."]
    ]
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_message = request.args.get("msg")
    chat = Chat(pares, reflections)
    bot_response = chat.respond(user_message)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run()
