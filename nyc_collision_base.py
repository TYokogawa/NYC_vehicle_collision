## NYC collision data

import pandas as pd
df = pd.read_csv('NYPD_Motor_Vehicle_Collisions.csv')


import matplotlib.pyplot as plt

## explore

df.shape
df.head()
df.tail()
df.describe()
df.columns


df['NUMBER OF PERSONS INJURED'].value_counts()
df['NUMBER OF PERSONS KILLED'].value_counts()
df['NUMBER OF PEDESTRIANS INJURED'].value_counts()
df['NUMBER OF PEDESTRIANS KILLED'].value_counts()
df['NUMBER OF CYCLIST INJURED'].value_counts()
df['NUMBER OF CYCLIST KILLED'].value_counts()
df['NUMBER OF MOTORIST INJURED'].value_counts()
df['NUMBER OF MOTORIST KILLED'].value_counts()
df['CONTRIBUTING FACTOR VEHICLE 1'].value_counts()
df['CONTRIBUTING FACTOR VEHICLE 2'].value_counts()
df['CONTRIBUTING FACTOR VEHICLE 3'].value_counts()
df['CONTRIBUTING FACTOR VEHICLE 4'].value_counts()
df['CONTRIBUTING FACTOR VEHICLE 5'].value_counts()
df['VEHICLE TYPE CODE 1'].value_counts()
df['VEHICLE TYPE CODE 2'].value_counts()
df['VEHICLE TYPE CODE 3'].value_counts()
df['VEHICLE TYPE CODE 4'].value_counts()
df['VEHICLE TYPE CODE 5'].value_counts()


## time of day analysis

from datetime import datetime
df['times'].groupby(df.times.dt.hour).count().plot(kind="bar")

dinj = df[df['NUMBER OF PERSONS INJURED'] >0]
dinj['times'].groupby(dinj.times.dt.hour).count().plot(kind="bar")
dkil = df[df['NUMBER OF PERSONS KILLED'] >0]
dkil['times'].groupby(dkil.times.dt.hour).count().plot(kind="bar")
dped = df[df['NUMBER OF PEDESTRIANS INJURED'] > 0]
dped['times'].groupby(dped.times.dt.hour).count().plot(kind="bar")
dpkl = df[df['NUMBER OF PEDESTRIANS KILLED'] > 0]
dpkl['times'].groupby(dpkl.times.dt.hour).count().plot(kind="bar")


dinj['VEHICLE TYPE CODE 1'].value_counts()
dkil['VEHICLE TYPE CODE 1'].value_counts()
dped['VEHICLE TYPE CODE 1'].value_counts()
dpkl['VEHICLE TYPE CODE 1'].value_counts()


## dates to datetime
df['dates']= pd.to_datetime(pd.Series(df['DATE']))

### year
df['dates'].groupby(df.dates.dt.year).count().plot(kind="bar")
df['dates'].groupby(df.dates.dt.year).count().plot(kind="bar")
### month
dinj['dates'].groupby(dinj.dates.dt.month).count().plot(kind="bar")
dkil['dates'].groupby(dkil.dates.dt.month).count().plot(kind="bar")
dped['dates'].groupby(dped.dates.dt.month).count().plot(kind="bar")
dpkl['dates'].groupby(dpkl.dates.dt.month).count().plot(kind="bar")
### day
df['dates'].groupby(df.dates.dt.day).count().plot(kind="bar")
dinj['dates'].groupby(dinj.dates.dt.day).count().plot(kind="bar")
dkil['dates'].groupby(dkil.dates.dt.day).count().plot(kind="bar")
dped['dates'].groupby(dped.dates.dt.day).count().plot(kind="bar")
dpkl['dates'].groupby(dpkl.dates.dt.day).count().plot(kind="bar")








