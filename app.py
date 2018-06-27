from flask import Flask, render_template, request, jsonify, url_for
import aiml
import os
from chatbot import Chatbot

app = Flask(__name__)

bot = Chatbot()

@app.route("/")
def hello():
    return render_template('chat.html')
@app.route('/chat')
def chat():
    return render_template('chat2.html')
@app.route('/we')
def we():
    return render_template('chat3.html')

@app.route("/ask", methods=['POST','GET'])
def ask():
    message = str(request.form['chatmessage'])
    print(message)
    while True:
        if message == "quit":
            exit()
        elif message == "save":
            bot.saveBrain()
        else:
            bot_response = bot.atomic_router(message)
            return jsonify({'status':'OK','answer':bot_response})

if __name__ == "__main__":
    app.run(debug=True)