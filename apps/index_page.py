import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import os

from app import navbar as navbar
from app import arrow as arrow

directories = [a for a in os.listdir('./monthly_data/')]

column_style = {'height': '45%', 'flexDirection': 'column',
                'display': 'flex', 'alignItems': 'center',
                'justifyContent': 'center',
                'boxShadow': '2px 2px 50px -3px grey',
                'borderRadius': '10px',
                'margin': 0,
                'overflow': 'hidden'}

arrow_style = {'height': '45%', 'flexDirection': 'column',
               'display': 'flex', 'alignItems': 'center',
               'justifyContent': 'center',
               'margin': 0}

button_style = {'width': '100%', 'whiteSpace': 'normal',
                'textDecoration': 'overline'}

layout = html.Div([
    navbar,
    dbc.Row([
        dbc.Col(dbc.Button('New Calculation', href='/apps/app1',
                           size="lg", style=button_style),
                style=column_style),

        dbc.Col(html.Img(src=arrow,
                         style={'height': '6vh'}),
                style=arrow_style),

        dbc.Col(dbc.Button('Adjust', href='/apps/adjust115',
                           size="lg", style=button_style),
                style=column_style),

        dbc.Col(html.Img(src=arrow,
                         style={'height': '6vh'}),
                style=arrow_style),

        dbc.Col(dbc.Button('Results', href='/apps/results',
                           size="lg", style=button_style),
                style=column_style)
    ],
        style={'alignItems': 'center',
               'justifyContent': 'center',
               'flex': 'auto',
               'margin': '15vh 5vw',
               },
        no_gutters=True)
], style={'height': '100vh',
          'display': 'flex',
          'flexDirection': 'column',
          })
