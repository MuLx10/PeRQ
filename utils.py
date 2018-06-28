import urllib, json
from copy import copy
fulfillmentMessages = {
                        "fulfillmentMessages": [
                          {
                            "card": {
                              "title": "Leo",
                              "subtitle": "Life could get really interesting today. At the very least, you're likely to read or hear something that captures your attention and fascinates you. An interesting article could kick off a whole new hobby or course of study! Who knows? As long as you're brave enough to chase down the people, places and subjects that intrigue you, you're taking advantage of today's influence in exactly the right way",
                              "imageUri": "https://assistant.google.com/static/images/molecule/Molecule-Formation-stop.png",
                              "buttons": [
                                {
                                  "text": "(c) Kelli Fox, The Astrologer",
                                  "postback": "http://sandipbgt.com/api/horoscope/Leo/today"
                                }
                              ]
                            }
                          }
                        ],
                        "outputContexts": [
                          {
                            "name": "projects/tarrot-99e8d/agent/sessions/fef2289f-7493-f0c5-765a-9e34e3bdffa2/contexts/HoroScope",
                            "lifespanCount": 2,
                            "parameters": {
                              "astroSign": "Leo"
                            }
                          }
                        ]
                      }

url = 'http://sandipbgt.com/theastrologer/api/horoscope/'

def fetch_horoscope(sunsign,day):
  try:
    response = urllib.urlopen(url+'/'+sunsign+'/'+day)
    data = json.loads(response.read())
  except:
    response = urllib.request.urlopen(url+'/'+sunsign+'/'+day)
    data = json.loads(response.read().decode())
  return str(data['horoscope']), str(data['meta']['mood'])


def get_json_resp(sunsign,day):
  resp = copy(fulfillmentMessages)
  horoscope, mood = fetch_horoscope(sunsign,day)
  resp['fulfillmentMessages'][0]['card']['title'] = sunsign.upper()
  resp['fulfillmentMessages'][0]['card']['subtitle'] = horoscope
  resp['fulfillmentMessages'][0]['card']['buttons'][0]['postback']+=sunsign+'/'+day
  return resp