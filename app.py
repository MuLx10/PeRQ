from flask import Flask, render_template, request, jsonify, url_for
import aiml
import os
from chatbot import Chatbot
from utils import get_json_resp
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
    data = json.loads(request.data)

    sunsign = str(data['queryResult']['parameters']['astroSign']).lower()
    day = str(data['queryResult']['parameters']['day']).lower()
    print(sunsign,day)
    resp = get_json_resp(sunsign,day)
    return jsonify(resp)

if __name__ == "__main__":
    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0', port=port, debug=True)




# {
#   "responseId": "a5b77534-10c6-467c-8ae6-5ee479dfce61",
#   "queryResult": {
#     "queryText": "What's today's horoscope for Leo?",
#     "parameters": {
#       "astroSign": "Leo",
#       "day": "today"
#     },
#     "allRequiredParamsPresent": true,
#     "fulfillmentText": "Hi Leo today",
#     "fulfillmentMessages": [{
#       "text": {
#         "text": ["Hi Leo today"]
#       }
#     }],
#     "intent": {
#       "name": "projects/tarrot-99e8d/agent/intents/428e1c41-0ab0-4242-8114-d7c7aa26c1b5",
#       "displayName": "actions.intent.GET_HOROSCOPE"
#     },
#     "intentDetectionConfidence": 1.0,
#     "diagnosticInfo": {
#     },
#     "languageCode": "en"
#   },
#   "originalDetectIntentRequest": {
#     "payload": {
#     }
#   },
#   "session": "projects/tarrot-99e8d/agent/sessions/fef2289f-7493-f0c5-765a-9e34e3bdffa2"
# }
