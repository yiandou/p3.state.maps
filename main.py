import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('./visited_states.csv')

fig = go.Figure(data=go.Choropleth(
    locations = df['code'],
    z = df['number students'].astype(float),
    locationmode = 'USA-states',
    colorscale = 'plasma',
    colorbar_title = 'Number of students that have visited a state'
    
))

fig.update_layout(
        geo_scope='usa',
        title_text="Map of visited states"
)

fig.show()
