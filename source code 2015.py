import pandas as pd 
apr14=pd.read_csv("uber-raw-data-apr14.csv")
may14=pd.read_csv("uber-raw-data-may14.csv")
jun14=pd.read_csv("uber-raw-data-jun14.csv")
jul14=pd.read_csv("uber-raw-data-jul14.csv")
aug14=pd.read_csv("uber-raw-data-aug14.csv")
sep14=pd.read_csv("uber-raw-data-sep14.csv")
data=apr14.append([may14,jun14,jul14,aug14,sep14],ignore_index=True)
data['Date/Time'] = pd.to_datetime(data['Date/Time'])
data['Month'] = data['Date/Time'].dt.month_name()
data['Weekday'] = data['Date/Time'].dt.dayofweek
data['Day'] = data['Date/Time'].dt.day
data['Hour'] = data['Date/Time'].dt.hour
data['Minute'] = data['Date/Time'].dt.minute

#hour and month analysis
d_hourmonth = data.groupby(['Hour','Month']).count()
h_month = pd.DataFrame({'Number_of_trips':d_hourmonth.values[:,1]}, index = d_hourmonth.index) 
h_month.reset_index(inplace= True)
data_hour_month = h_month['Number_of_trips'].values.reshape(24,6)
h_month = pd.DataFrame(data = data_hour_month, index = h_month['Hour'].unique(), columns = data['Month'].unique())
c=['red','orange','yellow','green','blue','black']
h_month.plot(kind='bar', stacked=True,color=c)
from matplotlib import pyplot as plt
plt.xlabel('Hour')
plt.ylabel('No of Trips')
plt.title(' Hour and Month trip analysis')
plt.show()

#hour and day analysis
import seaborn as ss
def c(row):
    return len(row)
dd = data.groupby('Hour Day'.split()).apply(c).unstack()
plt.figure(figsize = (12,8))
from matplotlib import cm 
ax = ss.heatmap(dd, cmap=cm.PuOr, linewidth = .5)
ax.set(title="Trips by Hour and Day")
plt.show()
