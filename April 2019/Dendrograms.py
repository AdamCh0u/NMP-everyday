#%%
import plotly
import plotly.plotly as py
import plotly.figure_factory as ff
import numpy as np
import pandas as pd
plotly.tools.set_credentials_file(username='AdamCh0u',
                                  api_key='jo3suMDHBGUGmBVYEvz7')

#%%
df = pd.read_csv("I:\Project\BHLU\Tabulate\ma_92-02.csv",encoding="utf-8")
df
#%%
dendro = ff.create_dendrogram(df)

#%%
dendro['layout'].update({'width':800, 'height':500})
py.iplot(dendro, filename='simple_dendrogram')

#%%
