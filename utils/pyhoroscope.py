import requests
from lxml import html
img_url = "https://images.ganeshaspeaks.com/images_gsv7/"
astroSign = ['aquarius',
             'cancer',
             'leo',
             'sagittarius',
             'capricorn',
             'aries',
             'taurus',
             'scorpio',
             'pisces',
             'libra',
             'virgo',
             'gemini']

def get_monthly_horoscope(sunsign):
        
        return {
            'month': month,
            'horoscope': horoscope,
            'sunsign': sunsign
        }

def get_horoscope(sunsign,time):
    if 'today' in time:
        url = "http://www.ganeshaspeaks.com/horoscopes/daily-horoscope/" + sunsign
        response = requests.get(url)
        tree = html.fromstring(response.content)
        date = str(tree.xpath("//*[@id=\"daily\"]/div/div[1]/div[1]/div[2]/div/p/text()"))
        date = date.replace("']", "").replace("['", "")
        date_website = "-".join(date.split('-')[::-1])
        horoscope = str(tree.xpath(
        "//*[@id=\"daily\"]/div/div[1]/div[2]/p[1]/text()"))
        horoscope = horoscope.replace("\\n", "").replace("  ", "").replace("[\"", "").replace("\"]", "").replace("[\'", "").replace("\']", "")
        return {
            'date': date_website,
            'horoscope': horoscope,
            'sunsign': sunsign,
            'url': url
        }
    elif 'yesterday' in time:
        url = "https://www.ganeshaspeaks.com/horoscopes/yesterday-horoscope/" + sunsign
        response = requests.get(url)
        tree = html.fromstring(response.content)
        date = str(tree.xpath("//*[@id=\"daily\"]/div/div[1]/div[1]/div[2]/div/p/text()"))
        date = date.replace("']", "").replace("['", "")
        date_website = "-".join(date.split('-')[::-1])
        horoscope = str(tree.xpath(
            "//*[@id=\"daily\"]/div/div[1]/div[2]/p[1]/text()"))
        horoscope = horoscope.replace("\\n", "").replace("  ", "").replace("[\"", "").replace("\"]", "").replace("[\'", "").replace("\']", "")
        return {
            'date': date_website,
            'horoscope': horoscope,
            'sunsign': sunsign,
            'url': url
        }
    elif 'tomorrow' in time:
        url = "https://www.ganeshaspeaks.com/horoscopes/tomorrow-horoscope/" + sunsign
        response = requests.get(url)
        tree = html.fromstring(response.content)
        date = str(tree.xpath("//*[@id=\"daily\"]/div/div[1]/div[1]/div[2]/div/p/text()"))
        date = date.replace("']", "").replace("['", "")
        date_website = "-".join(date.split('-')[::-1])
        horoscope = str(tree.xpath(
            "//*[@id=\"daily\"]/div/div[1]/div[2]/p[1]/text()"))
        horoscope = horoscope.replace("\\n", "").replace("  ", "").replace("[\"", "").replace("\"]", "").replace("[\'", "").replace("\']", "")
        return {
            'date': date_website,
            'horoscope': horoscope,
            'sunsign': sunsign,
            'url': url
        }
    
    elif 'month' in time:
        url = "http://www.ganeshaspeaks.com/horoscopes/monthly-horoscope/" + sunsign
        response = requests.get(url)
        tree = html.fromstring(response.content)
        month = str(tree.xpath(
            "//*[@id=\"daily\"]/div/div[1]/div[1]/div[2]/div/p/text()"))
        month = month.replace("']", "").replace("['", "")
        horoscope = str(tree.xpath(
            "//*[@id=\"daily\"]/div/div[1]/div[2]/p[1]/text()[1]"))
        horoscope = horoscope.replace("\\n", "").replace("  ", "").replace("']", "").replace("['", "")
        return {
                'month': month,
                'horoscope': horoscope,
                'sunsign': sunsign,
                'url': url
        }
    
    elif 'week' in time:
        url = "http://www.ganeshaspeaks.com/horoscopes/weekly-horoscope/" + sunsign
        response = requests.get(url)
        tree = html.fromstring(response.content)
        week = str(tree.xpath(
            "//*[@id=\"daily\"]/div/div[1]/div[1]/div[2]/div/p/text()"))
        week = week.replace("']", "").replace("['", "")
        horoscope = str(tree.xpath(
            "//*[@id=\"daily\"]/div/div[1]/div[2]/p[1]/text()"))
        horoscope = horoscope.replace("\\n", "").replace("  ", "").replace("']", "").replace("['", "")
        return {
            'week': week,
            'horoscope': horoscope,
            'sunsign': sunsign,
            'url': url
        }




def fetch_horoscope(sunsign,time):
    return get_horoscope(sunsign,time),img_url+sunsign.lower()+'200.png'
