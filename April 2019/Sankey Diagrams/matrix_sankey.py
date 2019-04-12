#%%
import json, urllib
import plotly.plotly as py
import plotly
import pandas as pd
import numpy as np
# github 登陆plot
plotly.tools.set_credentials_file(username='AdamCh0u',
                                  api_key='jo3suMDHBGUGmBVYEvz7')

df= pd.read_csv("I:\Project\BHLU\Tabulate\ma_92-02.csv",index_col="OID")

#from operator import methodcaller
#map(methodcaller("split", "_"),list(df.columns)):

linkSource = []
linkValue = []
linkTarget = []
#len(df)
for i in range(9):
    for j in range(1,9+1):
        linkSource.append(df.iloc[i,0])
        linkValue.append(df.iloc[i,j])
        linkTarget.append(list(df.columns)[j].split("_")[1])

label = []
for x in range(9):
    label.append(df.iloc[x,0])

data_trace = dict(
    type='sankey',
    domain = dict(
      x =  [0,1],
      y =  [0,1]
    ),
    orientation = "h",
    valueformat = ".0f",
    node = dict(
      pad = 5,
      thickness = 30,
      line = dict(
        color = "black",
        width = 0.5
      ),
      label = label
    ),
    link = dict(
      source = linkSource,
      target = linkTarget,
      value = linkValue,
  )
)

layout =  dict(
    title = "Wapo example",
    height = 1250,
    width = 1000,
    font = dict(
    size = 10
    ),
)
fig = dict(data=[data_trace], layout=layout)
py.iplot(fig)

