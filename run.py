# -*- coding:utf-8 -*-
# author :wangxiao
# CREATETIME :2021/3/7 下午4:12

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash_core_components import Input
from dash_html_components import Output

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
        dcc.Dropdown(
            id='my-dropdown',
            options=[
                {'label': 'cpu', 'value': cpu},
                {'label': 'memory', 'value': memory},
                {'label': 'karst', 'value': karst},
                {'label': 'python', 'value': python},
                {'label': 'database', 'value': database},
                {'label': 'hplc', 'value': hplc},

            ],
            value='python'
        ),
        dcc.Graph(id='my-graph')
])

# @app.callback(Output('my-graph', 'figure'), [Input("my-dropdown", "value")])
# def update_graph(select_data):
#     if select_data == 'python':
#         data =
#     trace = go.Bar(
#         x=df_date_month.index,
#         y=df_date_month['date_month'],
#         text=df_date_month['date_month'],
#         textposition='auto',
#         marker=dict(color=color_scale[:len(df_date_month)])
#     )
#     layout = go.Layout(
#         margin=dict(l=40, r=40, t=10, b=50)
#     )
#     return go.Figure(data=[trace], layout=layout)
# if __name__ == '__main__':
#     app.run_server(debug=True)
