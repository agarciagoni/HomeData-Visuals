# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 17:35:50 2019

@author: Alejandro Garcia
Script to create the dashboard about actual status of the kitchen user
"""

import dash
import dash_table
from statistics import mean
import dash_core_components as dcc
import dash_html_components as html
import plotly.subplots as subplots
import pandas as pd
import plotly.graph_objs as go

#data=pd.read_csv('PositionFile')


Current_layout=html.Div([
                        html.H5(className='tab-title',
                                children=['Current Kitchen Status']),
                        html.Div(className='row',children=[
                            html.Div(className='five columns',children=[
    
                                    dcc.Interval(id='intervals-pos',
    #                                             interval=0.1*1000, # in milliseconds USEFULL FOR REAL
                                                 interval=1*1000,
                                                 n_intervals=0),
                                    html.Div(className='', children=[
                                            html.H5('User Position'),
                                            dcc.Slider(
                                                       id='pos-slider',
                                                       min=0,max=400,
                                                       step=1,
                                                       value=0),
                                            dcc.Graph(id='user-pos')
                                    ]),
                                    html.Br(),
                                    html.Div(className='row', children=[
                                        html.Div(className='',children=[
                                                html.H5(className='six columns',children=[
                                                        'Front Cabinet']),
                                                html.H5(className='six columns ',children=
                                                         "Up")       
                                            ]),
                                        html.Div(className='',children=[
                                                html.H5(className='six columns',children=[
                                                        'Back Cabinet']),
                                                html.H5(className='six columns',children=
                                                         "High")       
                                           ])
                                    ])
                            ]),
                            html.Div(className='seven columns',children=[
    
                                    dcc.Interval(id='intervals-ter',
    #                                             interval=0.1*1000, # in milliseconds USEFULL FOR REAL
                                                 interval=1*1000,
                                                 n_intervals=0),
                                    html.Div(className='', children=[
                                            html.H5('Enviroment Data'),
                                            dcc.Graph(id='real-ter')
                                    ]),
    
                                ]),
                        ]),
                        html.Div(className='row', children=[
                        html.Div(className='six columns row pretty-container',children=[
                                html.H5(className='six columns',children=[
                                        'Front Cabinet']),
                                html.H5(className='six columns ',children=
                                         "Up")       
                            ]),
                        html.Div(className='six columns row pretty-container',children=[
                                html.H5(className='six columns',children=[
                                        'Back Cabinet']),
                                html.H5(className='six columns',children=
                                         "High")       
                            ])
                        ]),
                        ])