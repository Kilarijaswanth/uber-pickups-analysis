import pandas as pd
from matplotlib import pyplot as plt
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
print(data.info())
# monthly analysis
data_month = data.groupby(['Month'], sort=False).count()
d_month = pd.DataFrame({'Number_of_trips':data_month.values[:,0]}, index = data_month.index) 
d_month.plot(kind='bar',color="green")
plt.ylabel('No of trips(in lakhs)')
plt.title('monthly analysis of trips')
plt.show()
number_trips_apr= d_month.loc['April'].values
number_trips_sep = d_month.loc['September'].values
r_month = (((number_trips_sep - number_trips_apr) / number_trips_apr) * 100)[0]
r_month = round(r_month)
print('The ratio of the increase from April to September is {} %.'.format(r_month))

#day wise analysis
d_day = data.groupby(['Day']).count()
dj_day = pd.DataFrame({'Number_of_trips':d_day.values[:,0]}, index = d_day.index) 
plt.plot(dj_day, color = 'g', linestyle = 'dashed',marker = 'o')
plt.ylabel('No of Trips')
plt.xlabel('days')
plt.grid(color='black')
plt.title('Day wise analysis', fontsize = 20)
plt.show()
print("The overall observation of the graph depicts that the highest no of trips was observed in day 30 however, day by day no of trips differ marginally.")
print("the lowest no of trips is on 31st day because  April, June and September have 30 days.")

