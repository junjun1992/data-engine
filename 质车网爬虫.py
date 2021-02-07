# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 09:19:18 2021

@author: LiJunxia2
"""


import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_one_html(i):
    
    url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-{}.shtml'.format(i)
    #发送请求，接收响应
    
    resp = requests.get(url)
    
    html = print(resp.text)
    
    return html
    
def parse_one_page(html):
    
    # soup = BeautifulSoup(html,'lxml')
    
    # tr_list = soup.find_all('tbody')
    # print(tr_list)
    # for data in tr_list :
    #     sub_data = data.text
    #     print(sub_data)
    
    tb = pd.read_html(html,header=0)
    print(tb)
    
    return tb

def save_data(data):
    
    df = pd.concat(data)
    df.to_csv('车质网.csv',index=False)
    
data = []
    
    
for i in range(1,100)
    
    html = get_one_html(1)
    tb = parse_one_page(html)
    data.append(tb)
save_data(data)
    
