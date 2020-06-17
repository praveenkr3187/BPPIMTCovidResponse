from flask import Flask, render_template, url_for, request, session, redirect, g, jsonify
from random import sample
import pandas as pd
import time

from createCSV import results
from createCSV2 import answer
from createCSV3 import solution
from graphs import sol

dataframe=pd.read_csv("dataset.csv")
dataframe=dataframe.sort_values(by='Confirmed')
for _ in range(6):
    dataframe.drop(dataframe.index[-1], inplace= True)


dataframe2=pd.read_csv("dataset2.csv")


app = Flask(__name__)
app.secret_key='d7afcbc8d55d6266483a4d1f2b6ee8599e2543b45f3c4c2d'

def stateCases(state):
    try:
        p = pd.read_csv('./Datasets/Confirmed.csv')
        x = p[p['Unnamed: 0']==state]
        p = list(x)[-1]
        r = list(x[p])
        confirmed = r[0]
        p = pd.read_csv('./Datasets/Recovered.csv')
        x = p[p['Unnamed: 0']==state.upper()]
        p = list(x)[-1]
        r = list(x[p])
        recovered = r[0]
        p = pd.read_csv('./Datasets/Deceased.csv')
        x = p[p['Unnamed: 0']==state.upper()]
        p = list(x)[-1]
        r = list(x[p])
        deaths = r[0]
    except:
        print("error",r)
        return 0,0,0
    return confirmed, deaths, recovered



@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/process/<name>')
def message(name):
    temp = name
    key = time.time()
    key = str(key)
    if temp == 'India':
        src1 = f'content/Images_India/india_confirm.png?{key}'
        src2 = f'content/Images_India/India_confirm_components.png?{key}'
        src3 = f'content/Images_India/india_deceased_seasonalities.png?{key}'
        src4 = f'content/Images_India/India_deceased_components.png?{time.time()}'
        src5 = f'content/Images_India/india_recovered_seasonalities.png?{key}'
        src6 = f'content/Images_India/India_recovered_components.png?{key}'
        src7 = f'content/Images_India/India_confirmed_trend.png?{key}'
        src8 = f'content/Images_India/India_deaths_trend.png?{key}'
        src9 = f'content/Images_India/India_recovered_trend.png?{key}'
    else:
        src1 = f'content/Images_Confirmed/{name}_seasonality.png?{key}'
        src2 = f'content/Images_Confirmed/{name}_components.png?{key}'
        src3 = f'content/Images_Death/{name.upper()}_seasonalities.png?{key}'
        src4 = f'content/Images_Death/{name.upper()}_components.png?{key}'
        src5 = f'content/Images_Recovered/{name.upper()}.png?{key}'
        src6 = f'content/Images_Recovered/{name.upper()}_components.png?{key}'
        src7 = f'content/Images_statewise_confirmed_plot/{name}_mean.png?{key}'
        src8 = f'content/Images_statewise_deaths_plot/{name.upper()}_deathtrend.png?{key}'
        src9 = f'content/Images_statewise_recovered_plot/{name.upper()}_normal.png?{key}'
    confirmed, deaths, recovered = stateCases(name)
    return render_template('newPlot.html',name=name,src1=src1,src2=src2,src3=src3,src4=src4,src5=src5,src6=src6,src7=src7,src8=src8,src9=src9,confirmed=confirmed,deaths=deaths,recovered=recovered,active=confirmed-recovered-deaths)
    
@app.route('/contact')
def contact():
    return render_template('contacts.html')

@app.route('/analysis')
def analysis():
    return render_template('analysis.html')

@app.route('/regression')
def regression():
    return "this page is coming soon"

@app.route('/redplots')
def red():
    return redirect('http://localhost:5000/process/India',code=301)

@app.route('/favicon.ico')
def favicon():
    return url_for('static', filename='favicon.ico')
a=[]
@app.route('/district',methods=['GET','POST'])
def district(df=dataframe2):
    if request.method == 'POST':
        district= request.form['district']
        d=df.loc[df['District'] == district]
        global a
        a.clear()
        for index, rows in d.iterrows():
            a+=[rows.Density,rows.Workplaces,rows.Residential,rows.Retail,rows.Grocery,rows.Parks,rows.Stations,rows['Air quality'],rows['Water accessibility'],rows['Thermal anomalies'],rows.Confirmed,rows.Active]
    return render_template('district.html')

@app.route('/state')
def state(df=dataframe2):
    states=list(df['State'])
    states = list(dict.fromkeys(states))
    return jsonify({'state' : states})

@app.route('/disj')
def disj(di=a):
    return jsonify({'a' : di})


@app.route('/df2',methods=['GET','POST'])
def df2(df=dataframe2):
    if request.method == 'POST':
        selstate= request.form['st']
        d=df.loc[df['State'] == selstate]
        print(d)
        districts=list(d['District'])
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


#adding the pie chart data 
@app.route('/getChartData')
def getChartData():
    #feature importance chart
    fIKeys = ['Density', 'Workplaces', 'Residential', 'Retail', 'Grocery', 'Parks','Stations', 'Air quality', 'Water accessibility', 'Thermal anomalies']
    fIvalues = [0.4618791598294936,0.06227403159833104,0.08207634908337734,0.03651755018792977,0.039347491857771026,0.09534702713361999,0.07274135115598075,0.05524684727075561,0.0688292487723259,0.025740943110414943]
    #feature importance for mobility factors 
    fIMKeys = ['Workplaces', 'Residential', 'Retail', 'Grocery', 'Parks', 'Stations']
    fIMValues = [0.1517348568781475,0.23008026816154137,0.1165129581412859,0.14357581125707372,0.17818569824981895,0.17991040731213265]
    
    #univariate selection
    uSKeys = ['Density', 'Workplaces', 'Residential', 'Retail', 'Grocery', 'Parks','Stations', 'Air quality', 'Water accessibility', 'Thermal anomalies']
    uSValues = [36.14733165859195,0.09273469257182483,23.506595629105053,1.2686150850584141,2.8919863541195197,0.1988008603787625,2.8880402443913873,0.22619739317656704,8.757174296933792,0.018634527564267676]
    
    #univariate selection for mobility factors 
    uSMKeys = ['Workplaces', 'Residential', 'Retail', 'Grocery', 'Parks', 'Stations']
    uSMValues = [0.09273469257182483,23.506595629105053,1.2686150850584141,2.8919863541195197,0.1988008603787625,2.8880402443913873]
    return jsonify({'fIKeys' : fIKeys,'fIvalues' : fIvalues,'fIMKeys' : fIMKeys,'fIMValues' : fIMValues,'uSKeys' : uSKeys,'uSValues' : uSValues,'uSMKeys' : uSMKeys,'uSMValues' : uSMValues})
    
#adding updation part
@app.route('/update')
def fetchDaily():
    print('genereating results')
    results()
    answer()
    solution()
    sol()
    return 'data updated'

if __name__ == '__main__':
    app.run(debug=True)
