# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 17:32:10 2019

@author: Alejandro
"""
import dash
import dash_table
from statistics import mean
import dash_core_components as dcc
import dash_html_components as html
import plotly.subplots as subplots
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import plotly.io as pio
file_name='C:/Users/Alejandro/Desktop/MIT Media Lab/codes/full_kitchen_sensor/Data/kitchen_status.csv'
data=pd.read_csv(file_name)
variables=data.columns
data_tras=data.T
data_table=data_tras.iloc[:,10:15]
data_table.insert(0,'Variables',variables,True)
data_tras.insert(0,'Variables',variables,True)
variables_table=['Position','Position Back','Position Front','Temperature','Humidity','Light']
def generate_table(dataframe, max_rows=10, max_columns=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(className=col,children=[col]) for col in dataframe.columns[0:max_columns]])] +
        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns[0:max_columns]
        ]) for i in range(min(len(dataframe), max_rows))]
    )

def generate_table_user(dataframe,variables):
    return html.Table(
        # Header
      
        [html.Tr([html.Th(col) for col in dataframe.columns])] + 
        # Body  
        [html.Tr([html.Td(dataframe.loc[i][col]) for col in dataframe.columns]) for i in variables]
    )

pio.templates.default = "plotly_white"

Sensors_layout=html.Div([
      
        html.Div(className='row four columns',children=[
                html.Div(className='row dropdown-container',children=[
                    html.Label('Variables: '),
                    dcc.Dropdown(className='eight columns',id='var-dropdown',options=[{'label':x, 'value':x} for x in variables],
                                value='Position')
                ]),
                dcc.Graph(id='main-graph'                                  
                          ),
                dcc.RangeSlider(id='first-slider',
                                min=0,max=900, step=1, value=[0,900])]), 
        html.Div(className='row four columns',children=[
            html.Div(className='row dropdown-container', children=[
                    html.Div(className='six columns', children=[
                        html.Label('Variable X:'),
                        dcc.Dropdown(className='',id='bar-sensor-x',options=[{'label':x, 'value':x} for x in variables],
                                                        value='Position Back')
                        ]),   
                    html.Div(className='six columns', children=[              
                        html.Label('Variable Comp:'),
                        dcc.Dropdown(id='bar-sensor-compare',options=[{'label':x, 'value':x} for x in variables],
                                                        value='Position')]),
    #                    html.Br()
#                    dcc.RangeSlider(id='second-slider',
#                                min=0,max=900, step=1, value=[0,900])]), 
                    
            ]),
            html.Div(className='', children=[
                    dcc.Graph(id='bar-sensor')])
            ]),
     
#        html.Br(),
        html.Div(className='row four columns',children=[
#            html.Div(className='graph-title', children=[
#                    "Sound Graph"]),
            html.Div(className='row dropdown-container', children=[
                    html.Div(className='six columns', children=[
                        html.Label('Variable X:'),
                        dcc.Dropdown(className='',id='pie-sensor-x',options=[{'label':'Sound 1', 'value':'Sound 1'},
                                                                             {'label':'Sound 2', 'value':'Sound 2'}],#for x in variables, ##Make it General
                                                        value='Sound 1')]),
    
                    html.Div(className='six columns', children=[              
                        html.Label('Variable Comp:'),
                        dcc.Dropdown(id='pie-sensor-compare',options=[{'label':x, 'value':x} for x in variables],
                                                        value='Position')]),

    #                    html.Br()
                    ]),
            html.Div(className='row', children=[
                    dcc.Graph(id='pie-sensor'),
                    dcc.RangeSlider(id='third-slider',
                                min=0,max=900, step=1, value=[0,900], 
                             )])
            ]),
        html.Div(className='eleven columns',style={'overflow-x':'scroll'}, children=[
            html.H3('User data table'),
            dcc.Slider(id='table-slider',
                       min=0, max=800,step=1,value=0),
            html.Div(id='hist-table'),
#            dash_table.DataTable(
#            id='status-table',
#            columns=[{"name":i,"id":i} for i in variables],
#            data=data,
#            ),              
        ])                                 

            
   ])