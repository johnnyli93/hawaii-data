
# coding: utf-8

# In[287]:

import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import Column, Integer, String, Numeric, Text, Float, DateTime
import numpy as np
import matplotlib.pyplot as plt
from sqlalchemy.orm import Session
import matplotlib.ticker as ticker
import matplotlib.dates as mdates
import datetime as dt


# In[288]:

prev_year = dt.date.today() - dt.timedelta(days=365)
prev_year


# In[289]:

#connecting to the sqlite table hawaii_hw that was created in data_engineering notebook, then connecting to it
engine = create_engine("sqlite:///hawaii_hw.sqlite")
conn = engine.connect()


# In[290]:

#creating a session, i think??
session = Session(engine)


# In[291]:

Base = automap_base()
Base.prepare(engine, reflect = True)
Base.classes.keys()


# In[292]:

measurements = Base.classes.hawaii_measurement
stations = Base.classes.hawaii_station


# In[293]:

everything_tuples = session.query(measurements.station, measurements.date, measurements.rainfall, measurements.temp).all()
everything_tuples[30]


# In[294]:

station = [x[0] for x in everything_tuples]
dates = pd.to_datetime([x[1] for x in everything_tuples])
rainfall = [x[2] for x in everything_tuples]
temp = [x[3] for x in everything_tuples]
df = pd.DataFrame(station)
df[1] = dates
df[2] = rainfall
df[3] = temp

df.rename(columns = {0: 'station',  1: 'date', 2: 'rainfall', 3: 'temp'})


# In[295]:

rainfall_tuples = session.query(measurements.date,measurements.station, measurements.rainfall).all()


# In[296]:

rainfall_df = pd.DataFrame(dates)
rainfall_df[1] = station
rainfall_df[2] = rainfall
rainfall_df[3] = temp
rainfall_df.columns = ['date', 'station', 'rainfall', 'temp']


# In[297]:

one_year = rainfall_df[rainfall_df['date'] > prev_year]
waikiki_station = one_year[one_year['station'] == 'USC00519397']
waikiki_rainfall = waikiki_station['rainfall']
waikiki_date = waikiki_station['date']
yearsFmt = mdates.DateFormatter('%m-%d-%y')
one_year


# In[298]:

#hawaii precip
one_year = rainfall_df[rainfall_df['date'] > prev_year]
yearsFmt = mdates.DateFormatter('%m-%d-%y')

ax = plt.axes()

plt.plot(one_year['date'], one_year['rainfall'])
ax.xaxis.set_major_locator(ticker.MultipleLocator(30))
ax.xaxis.set_major_formatter(yearsFmt)
ax.xaxis.set_minor_locator(ticker.MultipleLocator(12))
plt.xticks(rotation=45)
plt.xlabel('dates')
plt.ylabel('precipitation')
plt.title("Hawaii rainfall for past year")
plt.tight_layout()


plt.show()


# In[299]:


#waikiki rainfall
ax = plt.axes()

plt.plot(waikiki_date, waikiki_rainfall)
ax.xaxis.set_major_locator(ticker.MultipleLocator(30))
ax.xaxis.set_major_formatter(yearsFmt)
ax.xaxis.set_minor_locator(ticker.MultipleLocator(12))
plt.xticks(rotation=45)
plt.xlabel('dates')
plt.ylabel('precipitation')
plt.title("Waikiki rainfall for past year")
plt.tight_layout()


plt.show()


# #I misread the question and ended up doing a precipitation 
# graph for each station

# In[300]:

#kaneohe precip
kaneohe_station = one_year[one_year['station'] == 'USC00513117']
kaneohe_rainfall = kaneohe_station['rainfall']
kaneohe_date = kaneohe_station['date']

ax = plt.axes()

plt.plot(kaneohe_date, kaneohe_rainfall)
ax.xaxis.set_major_locator(ticker.MultipleLocator(30))
ax.xaxis.set_major_formatter(yearsFmt)
ax.xaxis.set_minor_locator(ticker.MultipleLocator(12))
plt.xticks(rotation=45)
plt.xlabel('dates')
plt.ylabel('precipitation')
plt.title("Kaneohe rainfall for past year")
plt.tight_layout()
plt.show()


# In[301]:


kualoa_station = one_year[one_year['station'] == 'USC00514830']
kualoa_rainfall = kaneohe_station['rainfall']
kualoa_date = kaneohe_station['date']

ax = plt.axes()

plt.plot(kualoa_date, kualoa_rainfall)
ax.xaxis.set_major_locator(ticker.MultipleLocator(30))
ax.xaxis.set_major_formatter(yearsFmt)
ax.xaxis.set_minor_locator(ticker.MultipleLocator(12))
plt.xticks(rotation=45)
plt.xlabel('dates')
plt.ylabel('precipitation')
plt.title("Kualoa rainfall for past year")
plt.tight_layout()
plt.show()


# In[302]:

#pearl city precip
pearl_station = one_year[one_year['station'] == 'USC00517948']
pearl_rainfall = pearl_station['rainfall']
pearl_date = pearl_station['date']
ax = plt.axes()

plt.plot(pearl_date, pearl_rainfall)
ax.xaxis.set_major_locator(ticker.MultipleLocator(30))
ax.xaxis.set_major_formatter(yearsFmt)
ax.xaxis.set_minor_locator(ticker.MultipleLocator(12))
plt.xticks(rotation=45)
plt.xlabel('dates')
plt.ylabel('precipitation')
plt.title("Pearl City rainfall for past year")
plt.tight_layout()
plt.show()


# In[303]:

#upper wahiawa precip doesn't have data for the past year so we skip


# In[304]:

#waimanalo experimental farm precip
waimanalo_station = one_year[one_year['station'] == 'USC00519523']
waimanalo_rainfall = waimanalo_station['rainfall']
waimanalo_date = waimanalo_station['date']
ax = plt.axes()

plt.plot(waimanalo_date, waimanalo_rainfall)
ax.xaxis.set_major_locator(ticker.MultipleLocator(30))
ax.xaxis.set_major_formatter(yearsFmt)
ax.xaxis.set_minor_locator(ticker.MultipleLocator(12))
plt.xticks(rotation=45)
plt.xlabel('dates')
plt.ylabel('precipitation')
plt.title("Waimanalo Experimental Farm rainfall for past year")
plt.tight_layout()
plt.show()


# In[305]:

#waihee precip 
waihee_station = one_year[one_year['station'] == 'USC00519281']
waihee_rainfall = waihee_station['rainfall']
waihee_date = waihee_station['date']
ax = plt.axes()

plt.plot(waimanalo_date, waimanalo_rainfall)
ax.xaxis.set_major_locator(ticker.MultipleLocator(30))
ax.xaxis.set_major_formatter(yearsFmt)
ax.xaxis.set_minor_locator(ticker.MultipleLocator(12))
plt.xticks(rotation=45)
plt.xlabel('dates')
plt.ylabel('precipitation')
plt.title("Waihee rainfall for past year")
plt.tight_layout()
plt.show()


# In[306]:

#honolulu observatory precip
honolulu_station = one_year[one_year['station'] == 'USC00519281']
honolulu_rainfall = honolulu_station['rainfall']
honolulu_date = honolulu_station['date']
ax = plt.axes()

plt.plot(honolulu_date, honolulu_rainfall)
ax.xaxis.set_major_locator(ticker.MultipleLocator(30))
ax.xaxis.set_major_formatter(yearsFmt)
ax.xaxis.set_minor_locator(ticker.MultipleLocator(12))
plt.xticks(rotation=45)
plt.xlabel('dates')
plt.ylabel('precipitation')
plt.title("Honolulu Observatory rainfall for past year")
plt.tight_layout()
plt.show()


# In[307]:

#manoa lyon arboretum precip

manoa_station = one_year[one_year['station'] == 'USC00516128']
manoa_rainfall = manoa_station['rainfall']
manoa_date = manoa_station['date']
ax = plt.axes()

plt.plot(manoa_date, manoa_rainfall)
ax.xaxis.set_major_locator(ticker.MultipleLocator(30))
ax.xaxis.set_major_formatter(yearsFmt)
ax.xaxis.set_minor_locator(ticker.MultipleLocator(12))
plt.xticks(rotation=45)
plt.xlabel('dates')
plt.ylabel('precipitation')
plt.title("Manoa Lyon Arbo rainfall for past year")
plt.tight_layout()
plt.show()


# In[ ]:




# In[308]:

#now we graph the bar plot temp for waihee because it has the most tobs

#grab the 


# In[309]:


waihee_temp = waihee_station['temp']


# In[ ]:



