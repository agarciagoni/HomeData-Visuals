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
                                            dcc.Graph(id='light-graph',className='',
                                                      figure=px.line(data,x='Time',y='Temperature',title='Temperature (ºC)',range_x=[0,100],range_y=[15,33],color_discrete_sequence=['rgb(248, 160, 126)',''],height=graph_height))
                                                                               
                                        ]),
                                html.Div(className='four columns',children=[      
                                            dcc.Graph(id='temperature-graph',
                                                      figure=px.line(data,x='Time',y='Light',title='Light Levels (Lux)',range_x=[0,100],range_y=[0,600],color_discrete_sequence=['rgb(254, 252, 205)',''],height=graph_height))
                                                                               
                                        ]),                               
                                html.Div(className='four columns',children=[      
                                            dcc.Graph(id='humidity-graph',
                                                      figure=px.line(data,x='Time',y='Humidity',title='Humidity (%)',range_x=[0,100],range_y=[20,55],color_discrete_sequence=['rgb(133, 196, 201)',''],height=graph_height))
                                                                               
                                        ]), 
                               ]),
                        html.Br(),
                        html.Div(className='row eleven columns',children=[
                            html.Div(className='six columns',children=[
                                            dcc.Graph(id='humidity-graph',
                                                      figure=px.line(data,x='Time',y='Sound 1',title='Sound Right',range_y=[0,30],color_discrete_sequence=['rgb(76, 200, 163)',''],height=graph_height))
                                ]),
                                                                        html.Div(className='six columns',children=[
                                            dcc.Graph(id='humidity-graph',
                                                      figure=px.line(data,x='Time',y='Sound 2',title='Sound Left',range_y=[0,30],color_discrete_sequence=['rgb(56, 178, 163)',''],height=graph_height))
                                ]),
                        ]),
])