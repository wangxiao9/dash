# -*- coding:utf-8 -*-
# author :wangxiao
# CREATETIME :2021/3/7 下午4:12

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from sql import SQL

# data = pd.read_csv('avocado.csv')
# data = data.query('type == 'conventional' and region == 'Albany'')
# data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m-%d')
# data.sort_values('Date', inplace=True)

python = SQL().python()
karst = SQL().karst()
hplc = SQL().hplc()
database = SQL().data()
cpu = SQL().cpu()
memory = SQL().memory()

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(children='Karst', ),
        html.P(
            children='python service',
        ),
        dcc.Graph(
            figure={
                'data': [
                    {
                        'x': python[0],
                        'y': python[1],
                        'type': 'lines',
                    },
                ],
                'layout': {'title': 'python cpu'},
            },
        ),
        dcc.Graph(
            figure={
                'data': [
                    {
                        'x': python[0],
                        'y': python[2],
                        'type': 'lines',
                    },
                ],
                'layout': {'title': 'python memory'},
            },
        ),
        html.P(
            children='KarstServic+',
        ),
        dcc.Graph(
            figure={
                'data': [
                    {
                        'x': karst[0],
                        'y': karst[1],
                        'type': 'lines',
                    },
                ],
                'layout': {'title': 'karst cpu'},
            },
        ),
        dcc.Graph(
            figure={
                'data': [
                    {
                        'x': karst[0],
                        'y': karst[2],
                        'type': 'lines',
                    },
                ],
                'layout': {'title': 'karst memory'},
            },
        ),
        html.P(
            children='hplc service',
        ),
        dcc.Graph(
            figure={
                'data': [
                    {
                        'x': hplc[0],
                        'y': hplc[1],
                        'type': 'lines',
                    },
                ],
                'layout': {'title': 'hplc cpu'},
            },
        ),
        dcc.Graph(
            figure={
                'data': [
                    {
                        'x': hplc[0],
                        'y': hplc[2],
                        'type': 'lines',
                    },
                ],
                'layout': {'title': 'hplc memory'},
            },
        ),
        html.P(
            children='database service',
        ),
        dcc.Graph(
            figure={
                'data': [
                    {
                        'x': database[0],
                        'y': database[1],
                        'type': 'lines',
                    },
                ],
                'layout': {'title': 'database cpu'},
            },
        ),
        dcc.Graph(
            figure={
                'data': [
                    {
                        'x': database[0],
                        'y': database[2],
                        'type': 'lines',
                    },
                ],
                'layout': {'title': 'database memory'},
            },
        ),
        html.P(
            children='cpu',
        ),
        dcc.Graph(
            figure={
                'data': [
                    {
                        'x': cpu[0],
                        'y': cpu[1],
                        'type': 'bar',
                        'name': 'user'
                    },
                    {
                        'x': cpu[0],
                        'y': cpu[2],
                        'name': 'system',
                        'type': 'bar',
                    },
                ],
                'layout': {'title': 'cpu', 'width': 0.5, 'barmode': "stack"},
            },
            # style={"height": "60%", "width": "80%"}
        ),
        html.P(
            children='memory',
        ),
        dcc.Graph(
            figure={
                'data': [
                    {
                        'x': memory[0],
                        'y': memory[1],
                        'type': 'lines',
                        'name': 'used'
                    },
                    {
                        'x': memory[0],
                        'y': memory[2],
                        'name': 'free',
                        'type': 'lines',
                    },
                ],
                'layout': {'title': 'memory', 'width': 10, 'barmode': "stack"},
            },
            # style={"height": "60%", "width": "80%"}
        ),
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
