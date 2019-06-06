# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import json
from urllib.request import quote
import requests
#import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def getlnglat(address):
    """
    获取一个中文地址的经纬度(lat:纬度值,lng:经度值)
    """
    url_base = "http://api.map.baidu.com/geocoder/v2/"
    output = "json"
    ak = "nSxiPohfziUaCuONe4ViUP2N" # 浏览器端密钥
    address = quote(address) # 由于本文地址变量为中文，为防止乱码，先用quote进行编码
    url = url_base + '?' + 'address=' + address  + '&output=' + output + '&ak=' + ak 
    lat = 0.0
    lng = 0.0
    res = requests.get(url)
    temp = json.loads(res.text)
    if temp["status"] == 0:
        lat = temp['result']['location']['lat']
        lng = temp['result']['location']['lng']
    return lat,lng

#用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
#用来正常显示负号
plt.rcParams['axes.unicode_minus'] = False

"""数据加载"""
house = pd.read_excel('house.xls', index_col=None)

"""生成经纬度信息"""
idint = []
names = []
lats = []
lngs = []
lat_lng_data = {"id":idint,"communityName":names,"lat":lats,"lng":lngs}

#flag = 0
for idi,name,city in zip(list(range(10106)),list(house["position"]),list(house['city'])):
    try:
        name = str(name)
        city = str(city)
        lat,lng = getlnglat("深圳市"+city+name)
        if lat != 0 or lng !=0:
            idint.append(idi)
            names.append(name)
            lats.append(lat)
            lngs.append(lng)
            print(idi)
    except json.JSONDecodeError:
        idint.append(idi)
        names.append(name)
        lats.append(None)
        lngs.append(None)
        print(idi)
        continue
    
frame_test = pd.DataFrame(lat_lng_data)
frame_test.to_csv("latlng.csv")