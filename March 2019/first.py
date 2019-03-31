#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

#%%
print(os.getcwd())## 获取当前路径
os.chdir("i:/Project/NMP-everyday/March 2019")# 改变当前工作路径


#%%
train = pd.read_csv("./Data/train.csv")
test = pd.read_csv("./Data/test.csv")

#%%
test.describe()
train
#%% [markdown]
## 合并数据集

#%%
print("trainlines:" , train.shape[0]," test.lines:",test.shape[0])
full = train.append(test,sort = True)
full.head()

#%%
full.info()#计算空数据


#%%
