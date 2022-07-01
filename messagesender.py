import requests
import json

def send_sms(number,message):
    url = 'https://www.fast2sms.com/dev/bulkV2'
    params = {
        'authorization':'MdxynU5pCSumDJhP1bv36kiFIqRf8z0VXZ4EONBW7Q2KjYlTaGDBGjrgiIHtCdsnof4wlL729Ne3XxOm',
        'sender_id':'FSTSMS',
        'message':message,
        'language':'english',
        'route':'p',
        'numbers':number
    }
    response = requests.get(url, params=params)
    dict=response.json()
    print(dict)


send_sms("8354985722","hello this is testing")   


