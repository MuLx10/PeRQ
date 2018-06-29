import urllib, json
from copy import copy
from pyhoroscope import fetch_horoscope
url = 'http://horoscope-api.herokuapp.com/horoscope'

fulfillmentMessages = {"fulfillmentMessages":[{"text":{"text":["here is your horoscope"]}},{"card":{"buttons":[{"postback":"http://sandipbgt.com/api/horoscope/Leo/todayleo/todayleo/todayleo/todayleo/today","text":"(c) Kelli Fox, The Astrologer"}],"imageUri":"https://assistant.google.com/static/images/molecule/Molecule-Formation-stop.png","subtitle":"text","title":"LEO"}}],"outputContexts":[{"lifespanCount":2,"name":"projects/tarrot-99e8d/agent/sessions/fef2289f-7493-f0c5-765a-9e34e3bdffa2/contexts/HoroScope","parameters":{"astroSign":"Leo"}}]}

sample_resp = {"payload":{"google":{"expectUserResponse":"true","richResponse":{"items":[{"simpleResponse":{"textToSpeech":"This is a Basic Card:"}},{"basicCard":{"title":"Card Title","image":{"url":"https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png","accessibilityText":"Google Logo"},"subtitle":"dfgh","formattedText":"body","buttons":[{"title":"horoscope-api","openUrlAction":{"url":"http://horoscope-api.herokuapp.com/horoscope/"}}],"imageDisplayOptions":"WHITE"}}]}}}}



def get_json_resp_aog(sunsign,day):
  resp = copy(sample_resp)
  dicti,image = fetch_horoscope(sunsign,day)
  horoscope = dicti['horoscope'].replace('\\u','').replace('[u','')
  url = dicti['url']
  try:
    date = 'Horoscope-API  '+str(dicti['date'])
  except:
    date = 'Horoscope-API'
  resp['payload']['google']['richResponse']['items'][0]['simpleResponse']['textToSpeech'] = "Here's your Horoscope for "+day.upper()
  resp['payload']['google']['richResponse']['items'][1]['basicCard']['title'] = sunsign.upper()
  resp['payload']['google']['richResponse']['items'][1]['basicCard']['image']['url'] = image
  resp['payload']['google']['richResponse']['items'][1]['basicCard']['subtitle'] = horoscope.split('.')[0]+'.'
  resp['payload']['google']['richResponse']['items'][1]['basicCard']['formattedText'] = '.'.join(horoscope.split('.')[1:])
  resp['payload']['google']['richResponse']['items'][1]['basicCard']['buttons'][0]['openUrlAction']['url'] = url
  resp['payload']['google']['richResponse']['items'][1]['basicCard']['buttons'][0]['title'] = date
  return resp

def get_json_resp_df(sunsign,day):
  resp = copy(fulfillmentMessages)
  dicti,image = fetch_horoscope(sunsign,day)
  horoscope = dicti['horoscope'].replace('\\u','').replace('[u','')
  url = dicti['url']
  resp['fulfillmentMessages'][1]['card']['title'] = sunsign.upper()
  resp['fulfillmentMessages'][1]['card']['subtitle'] = horoscope
  resp['fulfillmentMessages'][1]['card']['buttons'][0]['postback'] = url
  return resp