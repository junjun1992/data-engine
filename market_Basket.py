# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 10:34:09 2021

@author: LiJunxia2
"""


import pandas as pd


pd.set_option('max_columns',None)
data = pd.read_csv('./Market_Basket_Optimisation.csv',header = None)
print(data)
print(data.shape)

transaction = []

for i in range (0,data.shape[0]):
    temp=[]
    for j in range(0,data.shape[1]):
        if str(data.values[i,j])!= 'nan':
         temp.append(data.values[i,j])
   # print(temp)
    
    transaction.append(temp)
    
from efficient_apriori import apriori
itemsets, rules = apriori(transactions, min_support=0.02,  min_confidence=0.3)
print('频繁项集：', itemsets)
print('关联规则：', rules)
        