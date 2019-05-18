import loader
import numpy as np
import plotly
import plotly.graph_objs as go

data = loader.load_data()

(x, y) = data['United States']

traces = []
for c, (years,pops) in data.items():
    traces.append(go.Scatter(
        x = years,
        y = pops,
        mode = 'lines+markers',
        name = c
    ))

plotly.offline.plot(traces)