"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request   
from FPAI_EDA_GRP1 import app

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pygal
import warnings
warnings.filterwarnings('ignore')

df_wind=pd.read_csv('C:/Users/20193820/Documents/DatAfriS/Workshop/EDA/FPAI_EDA GRP1/FPAI_EDA_GRP1/static/data/windspeed.csv')
df_wind['date']=pd.to_datetime(df_wind['date'])
df_wind['year']=df_wind['date'].dt.year


@app.route('/')
@app.route('/home',methods=["get", "post"])
def home():
    graph = pygal.Line()
    #graph.x_labels = map(str, range(1, 12))
    graph.add('1998',df_wind[(df_wind['Year']==1998)&(df_wind['Month']==1)].speed.values)
    graph.add('2000',df_wind[(df_wind['Year']==2000)&(df_wind['Month']==1)].speed.values)
    graph.add('2002',df_wind[(df_wind['Year']==2002)&(df_wind['Month']==1)].speed.values)
    graph.add('2004',df_wind[(df_wind['Year']==2004)&(df_wind['Month']==1)].speed.values)
    graph_data = graph.render_data_uri()
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,graph_data=graph_data,month='January')

@app.route('/mJan')
def mJan():
    graph = pygal.Line()
    #graph.x_labels = map(str, range(1, 12))
    graph.add('1998',df_wind[(df_wind['Year']==1998)&(df_wind['Month']==1)].speed.values)
    graph.add('2000',df_wind[(df_wind['Year']==2000)&(df_wind['Month']==1)].speed.values)
    graph.add('2002',df_wind[(df_wind['Year']==2002)&(df_wind['Month']==1)].speed.values)
    graph.add('2004',df_wind[(df_wind['Year']==2004)&(df_wind['Month']==1)].speed.values)
    graph_data = graph.render_data_uri()
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,graph_data=graph_data,month='January')

@app.route('/mMar')
def mMar():
    graph = pygal.Line()
    #graph.x_labels = map(str, range(1, 12))
    graph.add('1998',df_wind[(df_wind['Year']==1998)&(df_wind['Month']==3)].speed.values)
    graph.add('2000',df_wind[(df_wind['Year']==2000)&(df_wind['Month']==3)].speed.values)
    graph.add('2002',df_wind[(df_wind['Year']==2002)&(df_wind['Month']==3)].speed.values)
    graph.add('2004',df_wind[(df_wind['Year']==2004)&(df_wind['Month']==3)].speed.values)
    graph_data = graph.render_data_uri()
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,graph_data=graph_data,month='March')

@app.route('/mAug')
def mAug():
    graph = pygal.Line()
    #graph.x_labels = map(str, range(1, 12))
    graph.add('1998',df_wind[(df_wind['Year']==1998)&(df_wind['Month']==8)].speed.values)
    graph.add('2000',df_wind[(df_wind['Year']==2000)&(df_wind['Month']==8)].speed.values)
    graph.add('2002',df_wind[(df_wind['Year']==2002)&(df_wind['Month']==8)].speed.values)
    graph.add('2004',df_wind[(df_wind['Year']==2004)&(df_wind['Month']==8)].speed.values)
    graph_data = graph.render_data_uri()
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,graph_data=graph_data,month='August')

@app.route('/mOct')
def mOct():
    graph = pygal.Line()
    #graph.x_labels = map(str, range(1, 12))
    graph.add('1998',df_wind[(df_wind['Year']==1998)&(df_wind['Month']==10)].speed.values)
    graph.add('2000',df_wind[(df_wind['Year']==2000)&(df_wind['Month']==10)].speed.values)
    graph.add('2002',df_wind[(df_wind['Year']==2002)&(df_wind['Month']==10)].speed.values)
    graph.add('2004',df_wind[(df_wind['Year']==2004)&(df_wind['Month']==10)].speed.values)
    graph_data = graph.render_data_uri()
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,graph_data=graph_data,month='October')
