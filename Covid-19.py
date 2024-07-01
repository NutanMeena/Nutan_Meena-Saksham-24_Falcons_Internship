import pandas as pd
import datetime as dt
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
#df=pd.read_excel('DataD.xlsx')
df = pd.read_excel('DataD.xlsx', parse_dates=['Date'])
df = df[['Date', 'State/UnionTerritory', 'Cured', 'Confirmed', 'Deaths']]
df.head()
print(df['Date'])
df.columns=['date','state','cured','confirmed','deaths' ]
df.tail()
#Top State in Today-
today = df[df['date'] == '2020-07-17']
print(today.head)

#Top State Confirmed-
sns.set(rc={'figure.figsize':(15,10)})
sns.barplot(x='state',y='confirmed', data=today , hue='state')
plt.show()
#Top State Death-
sns.set(rc={'figure.figsize':(15,10)})
sns.barplot(x='state',y='deaths', data=today, hue='state')
plt.show()
#Top State Cured-
sns.set(rc={'figure.figsize':(15,10)})
sns.barplot(x='state',y='cured', data=today , hue='state')
plt.show()
#State Mha-
maha=df[df.state=='Maharashtra']
print(maha.head)
sns.set(rc={'figure.figsize':(15,10)})
sns.lineplot(x='date',y='confirmed', data=maha , hue='state')
plt.show()
sns.set(rc={'figure.figsize':(15,10)})
sns.lineplot(x='date',y='deaths', data=maha , hue='state')  
plt.show()
#State Dehli-
delhi=df[df.state=='Delhi']
print(delhi.head)
sns.set(rc={'figure.figsize':(15,10)})
sns.lineplot(x='date',y='confirmed', data=delhi , hue='state')
plt.show()
sns.set(rc={'figure.figsize':(15,10)})
sns.lineplot(x='date',y='deaths', data=delhi , hue='state' )
plt.show()
#State Kerla-
Kerala=df[df.state=='Kerala']
print(Kerala.head)
sns.set(rc={'figure.figsize':(15,10)})
sns.lineplot(x='date',y='confirmed', data=Kerala , hue='state')
plt.show()
sns.set(rc={'figure.figsize':(15,10)})
sns.lineplot(x='date',y='deaths', data=Kerala , hue='state' )
plt.show()
x = maha['date'].values.astype(np.int64).reshape(-1, 1)  # independent variable as numeric date
y = maha['confirmed'].values  # dependent variable
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
# Create Linear Regression model
lr = LinearRegression()
# Fit the model using training data
lr.fit(x_train, y_train)
prediction_date = pd.Timestamp('2020-07-19').value  # get timestamp value for the date
prediction = lr.predict([[prediction_date]])  # predict for the specified date
print("Prediction for 2020-07-19 in Maharashtra:", prediction)




#print(df)
