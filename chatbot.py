import aiml
import os
import requests
import json
import datetime
from time import sleep
import gc
import pandas as pd
# from dbconnect import connection



class Chatbot(object):
    """docstring for Chatbot"""
    def __init__(self):
        super(Chatbot, self).__init__()
        self.arg = 0
        
        self.atomic_kernel = self.spin_kernel('atomic')
        self.cities = pd.read_csv(r'chatbot/weather/city.csv')
        self.cities.drop(
            ['locId', 'country', 'region', 'postalCode', 'metroCode', 'areaCode'],
            inplace=True, axis=1)
    def saveBrain(self):
        self.atomic_kernel.saveBrain('bot_brain.brn')

    def weather_parser(self,response, place):
        """
        """
        if response is None:
            resp = json.load(open("templates/weath.er"))
        else:
            resp = json.loads(response)
        # print(resp)
        current = resp['currently']
        summary = resp['hourly']['summary']
        statement = 'It is going to be ' + str(summary.lower()) + ' The temperature is ' + str(current['temperature']) + ' degrees F, humidity ' + str(
            current['humidity']) + ', wind speed is ' + str(current['windSpeed']) + ' kmph with a visibility of ' + str(current['visibility']) + ' kilometres.'
        return statement


    def weather(self,place):
        # set your API key from api.darksky.net as environment variable 
        API_KEY = os.environ['API_KEY']
        url = "https://api.darksky.net/forecast/" + API_KEY + '/' + \
            place
        forecast = requests.get(url)
        return self.weather_parser(forecast.text, place)


        # print(self.cities)
        # self.cities.sort_values(by='city', ascending=False).groupby(level=0).first()
        # return "Hi, this is AI Bot. Make a request to /<message> to get started."


    def atomic_router(self,user_text):
        lower_text = user_text.lower()

        if lower_text.find('weather') > -1 or lower_text.find('temperature') > -1:
            words = lower_text.split()
            for word in words:
                print(word)
                word = word.title()
                row = self.cities.loc[self.cities['city'] == word]
                if(row.size > 0):
                    place = str(row['latitude'].values[0]) + ',' + str(row['longitude'].values[0])
                    response = self.weather(place)
                else:
                    response = "Did you forget to tell me the city?"
        else:
            response = self.atomic_kernel.respond(user_text.upper())
        sleep(len(response) * 0.01 + 1)

        # c, conn = connection()
        # c.execute("INSERT INTO chat_logs (msg_user,msg_bot,timestramp) VALUES(%s,%s,%s);",
        #         ((user_text),(response), str(datetime.datetime.now())))
        # conn.commit()
        # c.close()
        # conn.close()
        gc.collect()
        print(user_text,'-->',response)
        return response




    def spin_kernel(self,knowledge_file):
        """
        method to spin an AIML Kernel from knowledge file
        args: knowledge_file, placed inside 'knowledge/' folder
                  file name only required, path and extension is self appended
                  argument 'computers' will be read as => 'knowledge/computers.aiml'
        returns: kernel, learned from knowledge_file
        """
        kernel = aiml.Kernel()
        green_aimls = self.get_all_files('green')
        orange_aimls = self.get_all_files('orange')
        yellow_aimls = self.get_all_files('yellow')
        yellow_aimls = self.get_all_files('aiml')
        aimls = green_aimls+orange_aimls+yellow_aimls
        print('kernel',aimls)
        for aiml_file in aimls:
            if '.aiml' in aiml_file:
                kernel.learn(aiml_file)
        return kernel


    def get_all_files(self,color):
        """
        List all files recursively in the root specified by root
        """
        files_list = []
        root = 'knowledge/' + color
        for path, subdirs, files in os.walk(root):
            for name in files:
                files_list.append(os.path.join(root, name))
        print(files_list)
        return files_list[0:-1]

