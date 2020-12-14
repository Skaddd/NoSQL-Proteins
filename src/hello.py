# -*- coding: utf-8 -*-

from flask import Flask, Blueprint, render_template, request




hello = Blueprint('hello', __name__)



@hello.route("/", methods=['GET', 'POST'])
def hello_world():

    if request.method == 'POST':
        pid = request.form['inputprotid']
        pname = request.form['inputprotpws']
        doEc = True if request.form.get('idec') is not None else False
        doGo = True if request.form.get('idgoterm') is not None else False
        jaccardTreshold = request.form['jaccardtreshold']
        print(pid, pname, doEc, doGo, jaccardTreshold)
        return graph(pid, pname, doEc, doGo, jaccardTreshold)
    
    
    return render_template('form.html')


def graph(pid, pname, doEc, doGo, jaccardTreshold):
    print("changement de page")
    return render_template('graph.html')



if __name__ == '__main__':
    
    app = Flask(__name__)
    app.register_blueprint(hello, url_prefix='/')
    app.run(debug=True)

    
    
