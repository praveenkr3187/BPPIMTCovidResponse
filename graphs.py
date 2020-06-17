# -*- coding: utf-8 -*-

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
#visualization libraries
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
from matplotlib import pyplot
#manipulating the default plot size
plt.rcParams['figure.figsize'] = 10,12
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
#disable warns
import warnings
warnings.filterwarnings('ignore')
#IMPORTANT PLEASE READ THE COMMENT BELOW BEFORE EXECUTING THE CODE
#create explicit folder of names Images_Confirmed , Images_Death , Images_India_ Confirmed ,Images_Recovered and Images_statewise_plot 
#EXPLICIT FOLDERS WITH THE COMNPULSORY NAMES ABOVE HAS TO BE CREATED INSIDE CONTENT FOLDER FOR GOOGLE.COLAB



#statewise
def sol():
  data = pd.read_csv('./Datasets/Confirmed.csv', header=0, index_col=0)
  data.head()

  rf = pd.read_csv('./Datasets/Deceased.csv',header=0, index_col=0)
  rf.head()

  jf = pd.read_csv('./Datasets/Recovered.csv',header=0, index_col=0)

  jf.head()



  tc = data.mean()
  plt.ylabel("Mean of Daily cases in India")
  plt.savefig('./static/content/Images_India/India_mean_daily_Confirm_cases.png')

  va = data.var()
  plt.ylabel("Variance of Daily cases")
  plt.savefig('./static/content/Images_India/India_variance_daily_Confirm_cases.png')

  sc = data.std()
  plt.ylabel("Standard Deviation Of daily cases")
  plt.savefig('./static/content/Images_India/India_standard_daily_Confirm_cases.png')

  data = data.T

  data.tail(10)

  a = np.array(data['India'])
  b = np.array(data.index)

  from datetime import datetime
  l = [i for i in range(len(a))]
  s = []
  for i in range(len(a)):
    x = datetime.strptime(b[i]+'20','%d-%b-%Y')
    s.append([x,float(str(a[i]).replace(',',''))])

  p = pd.DataFrame(data=s,index=l,columns=['ds','y'])
  p.plot('ds','y')
  plt.title("Trend in Increase of Confirmed Cases for India")
  plt.ylabel('Date')
  plt.xlabel('Number of Confirmed cases')
  plt.savefig('./static/content/Images_India/India_confirmed_trend.png')

  from fbprophet import Prophet
  m = Prophet()
  m.fit(p)
  future = m.make_future_dataframe(periods=30)
  forecast = m.predict(future)

  india_plot = m.plot(forecast)
  plt.ylabel("No. of Cases for India")
  india_plot.savefig('./static/content/Images_India/india_confirm.png');
  india_forecast_plot = m.plot_components(forecast)
  india_forecast_plot.savefig('./static/content/Images_India/India_confirm_components.png');

  forecast.tail(55)

  for j in ['Maharashtra','Delhi',	'Gujrat',	'Madhya Pradesh',	'Tamilnadu',	'Rajasthan',	'Uttar Pradesh',	'Telengana',	'Andhra Pradesh', 'Kerala',	'Karnataka',	'Jammu And Kashmir',	'West Bengal',	'Harayana',	'Punjab',	'Bihar',	'Orissa',	'Uttarakhand',	'Himachal Pradesh',	'Chattisgarh',	'Assam',	'Jharkhand',	'Chandigarh',	'Ladakh',	'Andaman And Nicobar',	'Meghalaya',	'Goa',	'Puducherry',	'Manipur',	'Tripura',	'Arunachal Pradesh',	'Mizoram','Nagaland','Dadra And Nagar Haveli','Daman And Deu','Lakshadweep']:
    a = np.array(data[j])
    b = np.array(data.index)
    from datetime import datetime
    l = [i for i in range(len(a))]
    s = []
    for i in range(len(a)):
        x = datetime.strptime(b[i]+'20','%d-%b-%Y')
        s.append([x,float(str(a[i]).replace(',',''))])
    p = pd.DataFrame(data=s,index=l,columns=['ds','y'])
    from fbprophet import Prophet
    m = Prophet()
    m.fit(p)
    future = m.make_future_dataframe(periods=30)
    forecast = m.predict(future)
    x = './static/content/Images_Confirmed/'
    state_plot = m.plot(forecast)
    plt.ylabel("No. of Confirmed Cases "+j)
    state_plot.savefig(x+j+'_seasonality.png');
    state_forecast_plot = m.plot_components(forecast)
    state_forecast_plot.savefig(x+j+'_components.png');

  for j in ['Maharashtra','Delhi',	'Gujrat',	'Madhya Pradesh',	'Tamilnadu',	'Rajasthan',	'Uttar Pradesh',	'Telengana',	'Andhra Pradesh', 'Kerala',	'Karnataka',	'Jammu And Kashmir',	'West Bengal',	'Harayana',	'Punjab',	'Bihar',	'Orissa',	'Uttarakhand',	'Himachal Pradesh',	'Chattisgarh',	'Assam',	'Jharkhand',	'Chandigarh',	'Ladakh',	'Andaman And Nicobar',	'Meghalaya',	'Goa',	'Puducherry',	'Manipur',	'Tripura',	'Arunachal Pradesh',	'Mizoram','Nagaland','Dadra And Nagar Haveli','Daman And Deu','Lakshadweep']:
    a = np.array(data[j])
    b = np.array(data.index)
    from datetime import datetime
    l = [i for i in range(len(a))]
    s = []
    for i in range(len(a)):
        x = datetime.strptime(b[i]+'20','%d-%b-%Y')
        s.append([x,float(str(a[i]).replace(',',''))])
    p = pd.DataFrame(data=s,index=l,columns=['ds','y'])
    pd.plotting.register_matplotlib_converters()
    x = p.plot('ds','y')
    plt.title("Cases for "+j)
    plt.savefig('./static/content/Images_statewise_confirmed_plot/'+j+'_mean.png')

  rf.head()

  rf = rf.T
  rf.tail()

  a = np.array(rf['INDIA'])
  b = np.array(rf.index)
  from datetime import datetime
  l = [i for i in range(len(a))]
  s = []
  for i in range(len(a)):
    x = datetime.strptime(b[i]+'20','%d-%b-%Y')
    s.append([x,float(str(a[i]).replace(',',''))])
  p = pd.DataFrame(data=s,index=l,columns=['ds','y'])
  pd.plotting.register_matplotlib_converters()
  p.plot('ds','y')
  plt.title("Trend in Increase of Deceased Cases for India")
  plt.ylabel('Date')
  plt.xlabel('Number of Deceased cases')
  plt.savefig('./static/content/Images_India/India_deaths_trend.png')

  from fbprophet import Prophet
  m = Prophet()
  m.fit(p)
  future = m.make_future_dataframe(periods=30)
  forecast = m.predict(future)
  india_plot = m.plot(forecast)
  plt.ylabel("No. of Cases for India")
  india_plot.savefig('./static/content/Images_India/india_deceased_seasonalities.png');
  india_forecast_plot = m.plot_components(forecast)
  india_forecast_plot.savefig('./static/content/Images_India/India_deceased_components.png');

  for j in ['MAHARASHTRA', 'DELHI',	'GUJRAT',	'MADHYA PRADESH',	'TAMILNADU',	'RAJASTHAN',	'UTTAR PRADESH',	'TELENGANA',	'ANDHRA PRADESH', 'KERALA',	'KARNATAKA',	'JAMMU AND KASHMIR',	'WEST BENGAL',	'HARAYANA',	'PUNJAB',	'BIHAR',	'ORISSA',	'UTTARAKHAND',	'HIMACHAL PRADESH',	'CHATTISGARH',	'ASSAM',	'JHARKHAND',	'CHANDIGARH',	'LADAKH',	'ANDAMAN AND NICOBAR',	'MEGHALAYA',	'GOA',	'PUDUCHERRY',	'MANIPUR',	'TRIPURA',	'ARUNACHAL PRADESH',	'MIZORAM','NAGALAND','DADRA AND NAGAR HAVELI','DAMAN AND DEU','LAKSHADWEEP']:
    a = np.array(rf[j])
    b = np.array(rf.index)
    from datetime import datetime
    l = [i for i in range(len(a))]
    s = []
    for i in range(len(a)):
      x = datetime.strptime(b[i]+'20','%d-%b-%Y')
      s.append([x,float(str(a[i]).replace(',',''))])
    p = pd.DataFrame(data=s,index=l,columns=['ds','y'])
    pd.plotting.register_matplotlib_converters()
    x = p.plot('ds','y')
    plt.title("Deaths for "+j)
    plt.savefig('./static/content/Images_statewise_deaths_plot/'+j+'_deathtrend.png')



  for j in ['MAHARASHTRA', 'DELHI',	'GUJRAT',	'MADHYA PRADESH',	'TAMILNADU',	'RAJASTHAN',	'UTTAR PRADESH',	'TELENGANA',	'ANDHRA PRADESH', 'KERALA',	'KARNATAKA',	'JAMMU AND KASHMIR',	'WEST BENGAL',	'HARAYANA',	'PUNJAB',	'BIHAR',	'ORISSA',	'UTTARAKHAND',	'HIMACHAL PRADESH',	'CHATTISGARH',	'ASSAM',	'JHARKHAND',	'CHANDIGARH',	'LADAKH',	'ANDAMAN AND NICOBAR',	'MEGHALAYA',	'GOA',	'PUDUCHERRY',	'MANIPUR',	'TRIPURA',	'ARUNACHAL PRADESH',	'MIZORAM','NAGALAND','DADRA AND NAGAR HAVELI','DAMAN AND DEU','LAKSHADWEEP']:
    a = np.array(rf[j])
    b = np.array(rf.index)
    from datetime import datetime
    l = [i for i in range(len(a))]
    s = []
    for i in range(len(a)):
      x = datetime.strptime(b[i]+'20','%d-%b-%Y')
      s.append([x,float(str(a[i]).replace(',',''))])
    p = pd.DataFrame(data=s,index=l,columns=['ds','y'])
    from fbprophet import Prophet
    m = Prophet(interval_width=0.95)
    m.fit(p)
    future = m.make_future_dataframe(periods=30)
    forecast = m.predict(future)
    x = './static/content/Images_Death/'
    state_plot = m.plot(forecast)
    plt.ylabel("No. of deaths for "+j)
    state_plot.savefig(x+j+'_seasonalities.png')
    state_forecast_plot = m.plot_components(forecast)
    state_forecast_plot.savefig(x+j+'_components.png')

  jf.head()

  jf = jf.T
  jf.tail(10)

  a = np.array(jf['INDIA'])
  b = np.array(jf.index)
  from datetime import datetime
  l = [i for i in range(len(a))]
  s = []
  for i in range(len(a)):
    x = datetime.strptime(b[i]+'20','%d-%b-%Y')
    s.append([x,float(str(a[i]).replace(',',''))])
  p = pd.DataFrame(data=s,index=l,columns=['ds','y'])
  pd.plotting.register_matplotlib_converters()
  p.plot('ds','y')
  plt.title("Trend in Increase of Recovered Cases for India")
  plt.ylabel('Date')
  plt.xlabel('Number of Recovered cases')
  plt.savefig('./static/content/Images_India/India_recovered_trend.png')

  from fbprophet import Prophet
  m = Prophet()
  m.fit(p)
  future = m.make_future_dataframe(periods=30)
  forecast = m.predict(future)
  india_plot = m.plot(forecast)
  plt.ylabel("No. of Cases for India")
  india_plot.savefig('./static/content/Images_India/india_recovered_seasonalities.png');
  india_forecast_plot = m.plot_components(forecast)
  india_forecast_plot.savefig('./static/content/Images_India/India_recovered_components.png');

  for j in ['MAHARASHTRA', 'DELHI',	'GUJRAT',	'MADHYA PRADESH',	'TAMILNADU',	'RAJASTHAN',	'UTTAR PRADESH',	'TELENGANA',	'ANDHRA PRADESH', 'KERALA',	'KARNATAKA',	'JAMMU AND KASHMIR',	'WEST BENGAL',	'HARAYANA',	'PUNJAB',	'BIHAR',	'ORISSA',	'UTTARAKHAND',	'HIMACHAL PRADESH',	'CHATTISGARH',	'ASSAM',	'JHARKHAND',	'CHANDIGARH',	'LADAKH',	'ANDAMAN AND NICOBAR',	'MEGHALAYA',	'GOA',	'PUDUCHERRY',	'MANIPUR',	'TRIPURA',	'ARUNACHAL PRADESH',	'MIZORAM','NAGALAND','DADRA AND NAGAR HAVELI','DAMAN AND DEU','LAKSHADWEEP']:
    a = np.array(jf[j])
    b = np.array(jf.index)
    from datetime import datetime
    l = [i for i in range(len(a))]
    s = []
    for i in range(len(a)):
      x = datetime.strptime(b[i]+'20','%d-%b-%Y')
      s.append([x,float(str(a[i]).replace(',',''))])
    p = pd.DataFrame(data=s,index=l,columns=['ds','y'])
    x = p.plot('ds','y')
    plt.title("Recovery Cases for "+j)
    plt.savefig('./static/content/Images_statewise_recovered_plot/'+j+'_normal.png')



  for j in ['MAHARASHTRA', 'DELHI',	'GUJRAT',	'MADHYA PRADESH',	'TAMILNADU',	'RAJASTHAN',	'UTTAR PRADESH',	'TELENGANA',	'ANDHRA PRADESH', 'KERALA',	'KARNATAKA',	'JAMMU AND KASHMIR',	'WEST BENGAL',	'HARAYANA',	'PUNJAB',	'BIHAR',	'ORISSA',	'UTTARAKHAND',	'HIMACHAL PRADESH',	'CHATTISGARH',	'ASSAM',	'JHARKHAND',	'CHANDIGARH',	'LADAKH',	'ANDAMAN AND NICOBAR',	'MEGHALAYA',	'GOA',	'PUDUCHERRY',	'MANIPUR',	'TRIPURA',	'ARUNACHAL PRADESH',	'MIZORAM','NAGALAND','DADRA AND NAGAR HAVELI','DAMAN AND DEU','LAKSHADWEEP']:
    a = np.array(jf[j])
    b = np.array(jf.index)
    from datetime import datetime
    l = [i for i in range(len(a))]
    s = []
    for i in range(len(a)):
      x = datetime.strptime(b[i]+'20','%d-%b-%Y')
      s.append([x,float(str(a[i]).replace(',',''))])
    p = pd.DataFrame(data=s,index=l,columns=['ds','y'])
    from fbprophet import Prophet
    m = Prophet(interval_width=0.95)
    m.fit(p)
    future = m.make_future_dataframe(periods=30)
    forecast = m.predict(future)
    x = './static/content/Images_Recovered/'
    state_plot = m.plot(forecast)
    plt.ylabel("No. of Recovered cases for "+j)
    state_plot.savefig(x+j+'.png')
    state_forecast_plot = m.plot_components(forecast)
    state_forecast_plot.savefig(x+j+'_components.png')




