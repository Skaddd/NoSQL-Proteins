# -*- coding: utf-8 -*-

from flask import Flask, Blueprint, render_template, request

import pandas as pd
import numpy as np
import os
import re
from neo4j_connection import *
from preprocessing_human import *
from create_request import *
from create_links import *
from preprocessing_human import counter 

hello = Blueprint('hello', __name__)
humans=pd.read_csv("./data/humans.csv")# 1
humans_cleared=preprocessing(humans[['protein_id','domains']],'domains') 


@hello.route("/", methods=['GET', 'POST'])
def hello_world():

    if request.method == 'POST':
        pid = request.form['inputprotid']
        pname = request.form['inputprotpws']
        doLink = True if request.form.get('idlink') is not None else False
        jaccardTreshold = request.form['jaccardtreshold']
        create_req(humans_cleared,pid,pname,session)
        return graph()
    
    
    return render_template('form.html')


def graph():
    print("changement de page")
    return render_template('graph.html')



if __name__ == '__main__':
    session=connection_dbms() #1
    app = Flask(__name__)
    app.register_blueprint(hello, url_prefix='/')
    app.run(host='0.0.0.0', port='8000')

    
    
