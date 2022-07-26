import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import csv

df =pd.read_csv("data.csv")

fig = go.Figure(go.Scatter(
    x = df.groupby("level")["attempt"].mean(),
    y = ["Level 1" , "Level 2" , "Level 3" , "Level 4"]
))

fig.show()


