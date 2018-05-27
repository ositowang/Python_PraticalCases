import requests
from collections import Iterable, Iterator


# def getWeather(city):
#     r = requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city='+city)
#     data = r.json()['data']['forecast'][0]
#     return '%s:%s,%s' % (city, data['low'], data['high'])

#
# print(getWeather(u'北京'))

# Use Iterator to call one city at one time

class weatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0
    def getWeather(self, city):
        r = requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city=' + city)
        data = r.json()['data']['forecast'][0]
        return '%s:%s,%s' % (city, data['low'], data['high'])
    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index+=1
        return self.getWeather(city)

class weatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities
    def __iter__(self):
        return weatherIterator(self.cities)



for x in weatherIterable([u'北京', u'长春', u'广州']):
    print(x)



