# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

# import dash
from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
# df = pd.DataFrame({
#     "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
#     "Amount": [4, 1, 2, 2, 4, 5],
#     "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
# })

df = pd.read_csv('output.csv')

app.layout = html.Div(children=[
    html.H1(children='Pink Morsel Sales'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    html.Div([
        html.Label('Regions'),
        dcc.RadioItems(
            df['region'].unique(),
            'north',
            id='region',
            inline=True
        )
    ], style={'width': '48%', 'float': 'right', 'display': 'inline-block', 'margin-top': '35%'}),

    dcc.Graph(
        id='result'
    )
])

@callback(
    Output('result', 'figure'),
    Input('region', 'value'))
def graph(region):
    fig = px.line(df[df['region'] == region], x="date", y="sales")
    return fig


if __name__ == '__main__':
    app.run(debug=True)
