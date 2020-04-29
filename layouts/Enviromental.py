# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 17:35:50 2019

@author: Alejandro Garcia

Script to create the dashboard about actual status of the kitchen user. Here it is 
designed the page structure, all callback functions are defined in the main script.


"""

import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.io as pio

file_name='C:/Users/Alejandro/Desktop/MIT Media Lab/PiccoloKitchen/codes/Git/HomeData-Visuals/Data/kitchen_status.csv'
pio.templates.default = "plotly_dark"
colors=px.colors.diverging.Tealrose
data=pd.read_csv(file_name)
graph_height=520
Enviromental_layout=html.Div([
                        html.H5(className='tab-title',
                                children=['Room Environment']),
                        html.Div(className='row',children=[
                                html.Div(className='four columns',children=[      
                                            dcc.Graph(id='light-graph',
                                                      figure=px.line(data,x='Time',y='Light',title='Light Level',range_y=[0,550],color_discrete_sequence=['rgb(209, 238, 234)',''],height=graph_height))
                                                                               
                                        ]),
                                html.Div(className='four columns',children=[      
                                            dcc.Graph(id='temperature-graph',
                                                      figure=px.line(data,x='Time',y='Temperature',title='Temperature',range_y=[0,33],color_discrete_sequence=['rgb(168, 219, 217)',''],height=graph_height))
                                                                               
                                        ]),                               
                                html.Div(className='four columns',children=[      
                                            dcc.Graph(id='humidity-graph',
                                                      figure=px.line(data,x='Time',y='Humidity',title='Humidity',range_y=[0,50],color_discrete_sequence=['rgb(133, 196, 201)',''],height=graph_height))
                                                                               
                                        ]), 
                               ]),
                        html.Br(),
                        html.Div(className='row eleven columns',children=[
                            html.Div(className='six columns',children=[
                                            dcc.Graph(id='humidity-graph',
                                                      figure=px.line(data,x='Time',y='Humidity',title='Sound Right',range_y=[20,60],color_discrete_sequence=['rgb(76, 200, 163)',''],height=graph_height))
                                ]),
                                                                        html.Div(className='six columns',children=[
                                            dcc.Graph(id='humidity-graph',
                                                      figure=px.line(data,x='Time',y='Temperature',title='Sound Left',range_y=[20,40],color_discrete_sequence=['rgb(56, 178, 163)',''],height=graph_height))
                                ]),
                        ]),
])