# from https://dash.plot.ly/getting-started
import os
import dash
import pandas as pd
import plotly.graph_objs as go
from dash import dcc, html

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    requests_pathname_prefix=os.environ['SHINYPROXY_PUBLIC_PATH'],
    routes_pathname_prefix= os.environ['SHINYPROXY_PUBLIC_PATH']
)

df = pd.read_csv('gdp-life-exp-2007.csv')

app.layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure={
            'data': [
                go.Scatter(
                    x=df[df['continent'] == i]['gdp per capita'],
                    y=df[df['continent'] == i]['life expectancy'],
                    text=df[df['continent'] == i]['country'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.continent.unique()
            ],
            'layout': go.Layout(
                xaxis={'type': 'log', 'title': 'GDP Per Capita'},
                yaxis={'title': 'Life Expectancy'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
])


if __name__ == '__main__':
    app.run_server(debug=True, host = '0.0.0.0')
