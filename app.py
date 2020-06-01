from flask import Flask, render_template, url_for, request, session, redirect, g, jsonify
from random import sample
import pandas as pd

dataframe=pd.read_csv("dataset.csv")
dataframe=dataframe.sort_values(by='Confirmed')
for _ in range(6):
    dataframe.drop(dataframe.index[-1], inplace= True)


dataframe2=pd.read_csv("dataset2.csv")


app = Flask(__name__)
app.secret_key='d7afcbc8d55d6266483a4d1f2b6ee8599e2543b45f3c4c2d'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return url_for('static', filename='favicon.ico')

@app.route('/district',methods=['GET','POST'])
def district():
    return render_template('district.html')
a=[]
@app.route('/dis',methods=['GET','POST'])
def dis(df=dataframe2):
    if request.method == 'POST':
        district= request.form['district']
        d=df.loc[df['District'] == district]
        global a
        a.clear()
        for index, rows in d.iterrows():
            a+=[rows.Density,rows.Workplaces,rows.Residential,rows.Retail,rows.Grocery,rows.Parks,rows.Stations,rows['Air quality'],rows['Water accessibility'],rows['Thermal anomalies'],rows.Confirmed,rows.Active]
        return render_template('dis.html')
    else:
        return 'error'
@app.route('/disj')
def disj(di=a):
    return jsonify({'a' : di})


@app.route('/df2')
def df2(df=dataframe2):
    districts=list(df['District'])
    return jsonify({'district' : districts})

@app.route('/graph')
def graph():
    return render_template('graph.html')

@app.route('/popvsconf')
def popvsconf(df=dataframe):
    df=df.sort_values(by='Population')
    confirmed=list(df['Confirmed'])
    population=list(df['Population'])
    return jsonify({'confirmed' : confirmed,'population' : population})


@app.route('/areavsconf')
def areavsconf(df=dataframe):
    df=df.sort_values(by='Area')
    confirmed=list(df['Confirmed'])
    area=list(map(int,(df['Area'])))
    return jsonify({'confirmed' : confirmed,'area' : area})

@app.route('/denvsconf')
def denvsconf(df=dataframe):
    df=df.sort_values(by='Density')
    confirmed=list(df['Confirmed'])
    density=list(map(int,(df['Density'])))
    return jsonify({'confirmed' : confirmed,'density' : density})

@app.route('/actvsconf')
def actvsconf(df=dataframe):
    df=df.sort_values(by='Active')
    confirmed=list(df['Confirmed'])
    active=list(df['Active'])
    return jsonify({'confirmed' : confirmed,'active' : active})

@app.route('/retvsconf')
def retvsconf(df=dataframe):
    df=df.sort_values(by='Retail')
    confirmed=list(df['Confirmed'])
    retail=list(df['Retail'])
    return jsonify({'confirmed' : confirmed,'retail' : retail})

@app.route('/grovsconf')
def grovsconf(df=dataframe):
    df=df.sort_values(by='Grocery')
    confirmed=list(df['Confirmed'])
    grocery=list(df['Grocery'])
    return jsonify({'confirmed' : confirmed,'grocery' : grocery})

@app.route('/parvsconf')
def parvsconf(df=dataframe):
    df=df.sort_values(by='Parks')
    confirmed=list(df['Confirmed'])
    parks=list(df['Parks'])
    return jsonify({'confirmed' : confirmed,'parks' : parks})

@app.route('/stavsconf')
def stavsconf(df=dataframe):
    df=df.sort_values(by='Stations')
    confirmed=list(df['Confirmed'])
    stations=list(df['Stations'])
    return jsonify({'confirmed' : confirmed,'stations' : stations})

@app.route('/worvsconf')
def worvsconf(df=dataframe):
    df=df.sort_values(by='Workplaces')
    confirmed=list(df['Confirmed'])
    workplaces=list(df['Workplaces'])
    return jsonify({'confirmed' : confirmed,'workplaces' : workplaces})

@app.route('/resvsconf')
def resvsconf(df=dataframe):
    df=df.sort_values(by='Residential')
    confirmed=list(df['Confirmed'])
    residential=list(df['Residential'])
    return jsonify({'confirmed' : confirmed,'residential' : residential})

if __name__ == '__main__':
    app.run(debug=False)