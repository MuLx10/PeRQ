from flask import Flask, render_template, request, jsonify, url_for
from flask import stream_with_context, Response
import aiml
import os
from chatbot import Chatbot
from utils.utils import get_json_resp_aog,get_json_resp_df
import json

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

@app.route("/horro", methods=['POST','GET'])
def horo():
    data = json.loads(request.data.decode('utf-8'))
    # print(data)
    sunsign = str(data['queryResult']['parameters']['astroSign']).lower()
    try:
        time = str(data['queryResult']['parameters']['time']).lower()
    except:
        time ='today'
        # print(time)
    print(sunsign,time)
    resp = get_json_resp_aog(sunsign,time)
    # ans = [resp,resp]
    # resp = get_json_resp_df(sunsign,time)
    return jsonify(resp)
    def generate():
        for resp in ans:
            yield jsonify(resp)
    return Response(generate(), mimetype='text/json')

if __name__ == "__main__":
    port = int(os.environ.get('PORT',8080))
    app.run(host='0.0.0.0', port=port, debug=not True)



