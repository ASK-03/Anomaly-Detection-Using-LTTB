### IMPORTS 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

## LTTB
import anomaly_lttb

## PLOTLY
import plotly.express as px
import plotly.graph_objects as go

### DATASET
df=pd.read_csv('./EEG_dataset.csv')
idx=df.pop('Unnamed: 0')

### FUNCTIONS
def find_null(df, col):
    return df[col].isnull().sum()

def make_plot(data, col):
    from plotly.subplots import make_subplots
    x=[data[i][0] for i in range(len(data))]
    y=[data[i][1] for i in range(len(data))]

    fig=make_subplots(rows=1, cols=2)
    fig.add_trace(go.Scatter(x=x, y=y), row=1, col=1)

    sample_data, anomaly_points=anomaly_lttb.largest_triangle_three_buckets(data=data, threshold=100)

    x=[sample_data[i][0] for i in range(len(sample_data))]
    y=[sample_data[i][1] for i in range(len(sample_data))]

    fig.add_trace(go.Scatter(x=x, y=y), row=1, col=2)

    x=[anomaly_points[i][0] for i in range(len(anomaly_points))]
    y=[anomaly_points[i][1] for i in range(len(anomaly_points))]
    print(len(anomaly_points))
    
    fig.add_trace(go.Scatter(x=x, y=y, mode="markers", marker=dict(size=20)), row=1, col=2)
    
    fig.show()
    

def make_data(df, col, to_idx):
    if len(df)<to_idx:
        raise("error")
    data=[]
    for idx, i in enumerate(df[col][:to_idx]):
        data.append([idx, i])
    return data
    


def pipeline(data, column, to_idx):
    data=make_data(data, column, to_idx)
    make_plot(data, column)


#### Data generation
pipeline(df, "FP2", len(df))