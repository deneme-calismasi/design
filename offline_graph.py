import plotly
import plotly.graph_objs as go
import numpy as np  # So we can use random numbers in examples

# Must enable in order to use plotly off-line (vs. in the cloud... hate cloud)


N = 1000
random_x = np.random.randn(N)
random_y = np.random.randn(N)

# Create a trace
trace = go.Scatter(
    x=random_x,
    y=random_y,
    mode='markers'
)

data = [trace]

# Plot and embed in ipython notebook!
plotly.offline.iplot(data, filename='basic-scatter')
