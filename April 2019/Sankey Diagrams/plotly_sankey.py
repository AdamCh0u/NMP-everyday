#%%
import json, urllib
import plotly.plotly as py
import plotly
import pandas as pd
import numpy as np
plotly.tools.set_credentials_file(username='AdamCh0u',
                                  api_key='9O4XaWfHmGzHUwXdB2ly')

#%%
url = r'https://rawgit.com/monfera/plotly-webgl-parcoords/sankey-example-01/drones.json'
response = urllib.request.urlopen(url)
data = json.loads(response.read())

#%%
label = []
for x in data['data'][0]['nodes']:
    label.append(x['label'])

linkSource = []
linkValue = []
linkTarget = []
linkLabel = []
for x in data['data'][0]['links']:
    linkLabel.append(x['label'])
    linkSource.append(x['source'])
    linkValue.append(x['value'])
    linkTarget.append(x['target'])

#%%
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
      label =  label
    ),
    link = dict(
      source = linkSource,
      target = linkTarget,
      value = linkValue,
      label =  linkLabel
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