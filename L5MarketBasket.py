# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 16:21:08 2021

@author: LiJunxia2
"""


import pandas as pd
from nltk.tokenize import word_tokenize

data = pd.read_csv('./Market_Basket_Optimisation.csv', header = None)
print(data)
print(data.shape)

transactions = []

item_count ={}

for i in range(data.shape[0]):
    temp = []
    for j in range(data.shape[1]):
        item = str(data.values[i,j])
        if item!='nan':
            temp.append(item)
            if item not in item_count:
                item_count[item] = 1
            else:
                item_count[item]+=1
    transactions.append(temp)
print(transactions)

from wordcloud import WordCloud
def remove_stop_words(f):
    stop_words=[]
    for stop_word in stop_words:
        f = f.replace(stop_word,'')
        return f 
def create_word_cloud(f):
	f = remove_stop_words(f)
	cut_text = word_tokenize(f)
	cut_text = " ".join(cut_text)
	wc = WordCloud(
		max_words=100,
		width=2000,
		height=1200,
    )
	wordcloud = wc.generate(cut_text)
	wordcloud.to_file("wordcloud.jpg")

all_word =' '.join('%s'%item for item in transactions)
print(all_word)
                    