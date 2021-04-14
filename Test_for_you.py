#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import matplotlib as pl
import matplotlib.pyplot as plt
# pyplot is a subpackage of matplotlib.


# In[4]:


years=[1960,1970,1980,1990,2000,2010,2020]
pop=[22,29,39,57,66,75,80]


# In[5]:


#LinePlot
#plt.plot(x,y)
#plt.show()
plt.plot(years,pop)
plt.show()


# In[6]:


#ScatterPlot
#plt.scatter(x,y)
#plt.show()
plt.scatter(years,pop)
plt.show()


# In[7]:


#HistogramPlot
#plt.hist(y)
#plt.show()
plt.hist(pop)
plt.show()


# In[15]:


#HistogramPlot with specific bin
#plt.hist(y ,bins=n)
#plt.show()
plt.hist(pop, bins=4)
plt.show()


# In[16]:


#Which bin is  best one? the best one is \sqrt(n) with lower approximation.
#For this example n=7, then bins=2 is best bin.
plt.hist(pop, bins=2)
plt.show()


# In[17]:


#Which bin is  best one by matplotlib? bins="auto"
plt.hist(pop, bins="auto")
plt.show()


# In[19]:


#PieChartPlot
#plt.pie(y, labels="x")
#plt.show()
plt.pie(pop, labels=years)
plt.show()


# In[20]:


#PieChartPlot
#plt.pie(y, labels="x")
#plt.show()
plt.pie(pop, labels=pop)
plt.show()


# In[25]:


city=["Tehran","Kermanshah", "Fars", "Ardabil", "Arak"]
pop=[20,2,4,0.5,1]


# In[26]:


plt.pie(pop, labels=city)
plt.show()


# In[30]:


plt.hist(pop, bins="auto")
plt.show()


# In[40]:


#Costomization of Plots: such as title, legend, axies name and so on
#plt.figure(figsize=(length,width), dpi=resolution)
#plt.xlabel("")
#plt.ylabel("")
plt.figure(figsize=(8,4), dpi=100)
years=[1960,1970,1980,1990,2000,2010,2020]
pop=[22,29,39,57,66,75,80]
plt.plot(years,pop)
plt.xlabel("Years")
plt.ylabel("Populations(million)")
plt.show()


# In[49]:


plt.figure(figsize=(8,4), dpi=100)
years=[1960,1970,1980,1990,2000,2010,2020]
pop=[22,29,39,57,66,75,80]
plt.plot(years,pop)
plt.xlabel("Years")
plt.ylabel("Populations")
plt.xticks([1960,1965,1970,1975,1980,1985,1990,1995,2000,2005,2010,2015,2020])
plt.yticks([22,29,39,57,66,75,80], ["22M","29M","39M","57M","66M","75M","80M"])
plt.show()


# In[45]:


plt.figure(figsize=(5,10), dpi=100)
years=[1960,1970,1980,1990,2000,2010,2020]
pop=[22,29,39,57,66,75,80]
plt.plot(years,pop)
plt.xlabel("Years")
plt.ylabel("Populations(million)")
plt.yticks([22,25,29,30,35,39,40,50,55,57,60,65,66,70,75,80])
plt.show()


# In[51]:


#Title of Table:
plt.figure(figsize=(8,4), dpi=100)
plt.title("Trend of Iran Populations")
years=[1960,1970,1980,1990,2000,2010,2020]
pop=[22,29,39,57,66,75,80]
plt.plot(years,pop)
plt.xlabel("Years")
plt.ylabel("Populations")
plt.xticks([1960,1965,1970,1975,1980,1985,1990,1995,2000,2005,2010,2015,2020])
plt.yticks([22,29,39,57,66,75,80], ["22M","29M","39M","57M","66M","75M","80M"])
plt.show()


# In[73]:


plt.figure(figsize=(10,4), dpi=100)
pop_size=np.array([1000,750,180,170,100,80,20,10])
colors=("red","yellow","green","blue","tomato","black","pink","orange")
course=["Art", "History","Mathematics","Statistics", "Computer", "Physics", "Chemistry","Literature"]
score=[1000,750,180,170,100,80,20,10]
#plt.titel("course Scores")
plt.scatter(course,score,s=pop_size, c=colors)
plt.margins(0.2)
plt.show()


# In[19]:


# we can add Line style as ls="line between of nodes-" , marker="* sign of grade" , mew="size of grade"
plt.figure(figsize=(8,4), dpi=100)
plt.title("Trend of Iran Populations")
years=[1960,1970,1980,1990,2000,2010,2020]
pop=[22,29,39,57,66,75,80]
plt.plot(years,pop, ls="-" , marker="+" , mew="10")
plt.xlabel("Years")
plt.ylabel("Populations")
plt.xticks([1960,1965,1970,1975,1980,1985,1990,1995,2000,2005,2010,2015,2020])
plt.yticks([22,29,39,57,66,75,80], ["22M","29M","39M","57M","66M","75M","80M"])
plt.show()


# In[32]:


#Add another graph for example population of korea is popkor=[12,13,17,40,48,73,88]  and we can line wideth as lw=number
#Add legend to the graph for example plt.legend(["Iran", "Korea"], loc="location")
plt.figure(figsize=(8,4), dpi=100)
plt.title("Trend of Iran Populations")
years=[1960,1970,1980,1990,2000,2010,2020]
pop=[22,29,39,57,66,75,80]
popkor=[12,13,17,40,48,73,88]
plt.plot(years,pop, ls="-" , marker="+" , mew="10")
plt.plot(years,popkor, ls="--" , marker="*" , lw=1, mew="10")
plt.legend(["Iran", "Korea"], loc="right")
plt.xlabel("Years")
plt.ylabel("Populations")
plt.xticks([1960,1965,1970,1975,1980,1985,1990,1995,2000,2005,2010,2015,2020])
plt.yticks([22,29,39,57,66,75,80], ["22M","29M","39M","57M","66M","75M","80M"])
plt.show()


# In[36]:


#Let to the python to select location as best such as loc="best"
plt.figure(figsize=(8,4), dpi=100)
plt.title("Trend of Iran Populations")
years=[1960,1970,1980,1990,2000,2010,2020]
pop=[22,29,39,57,66,75,80]
popkor=[12,13,17,40,48,73,88]
plt.plot(years,pop, ls="-" , marker="+" , mew="10")
plt.plot(years,popkor, ls="--" , marker="*" , lw=1, mew="10")
plt.legend(["Iran", "Korea"], loc="best")
plt.xlabel("Years")
plt.ylabel("Populations")
plt.xticks([1960,1965,1970,1975,1980,1985,1990,1995,2000,2005,2010,2015,2020])
plt.yticks([22,29,39,57,66,75,80], ["22M","29M","39M","57M","66M","75M","80M"])
plt.show()


# In[4]:


#Add grid (net) to the graph for comparison:
#Add a notation to the graph: plt.annotate("Text", xytext=(location of text), fontsize=number, xy=(Start point of arrow), arrowprops=dict(facecolor="",width=number))
plt.figure(figsize=(8,4), dpi=100)
plt.title("Trend of Iran Populations")
years=[1960,1970,1980,1990,2000,2010,2020]
pop=[22,29,39,57,66,75,80]
popkor=[12,13,17,40,48,73,88]
plt.plot(years,pop, ls="-" , marker="+" , mew="10")
plt.plot(years,popkor, ls="--" , marker="*" , lw=1, mew="10")
plt.legend(["Iran", "Korea"], loc="best")
plt.xlabel("Years")
plt.ylabel("Populations")
plt.xticks([1960,1965,1970,1975,1980,1985,1990,1995,2000,2005,2010,2015,2020])
plt.yticks([22,29,39,57,66,75,80], ["22M","29M","39M","57M","66M","75M","80M"])
plt.grid()
plt.annotate("5th President of Iran: Khatami", xytext=(2005,58), fontsize=8, xy=(1997,63.5),  arrowprops=dict(facecolor="silver",width=4))
plt.show()


# In[52]:


pip install seaborn


# In[2]:


import numpy as np
import matplotlib as pl
import matplotlib.pyplot as plt
# pyplot is a subpackage of matplotlib.


# In[5]:


#plt.subplot(n,m,id)  n=Row m=Column  id from 1 to mn for example:
plt.subplot(1,2,1)
plt.plot(years,pop)
plt.title("Iran")

plt.subplot(1,2,2)
plt.plot(years,popkor)
plt.title("Korea")

plt.show()


# In[12]:


#plt.subplot(2,3,id)  n=Row m=Column  id from 1 to 6 for example:
plt.subplot(2,3,1)
plt.plot(years,pop)
plt.title("Iran1")

plt.subplot(2,3,2)
plt.plot(years,pop)
plt.title("Iran2")

plt.subplot(2,3,3)
plt.plot(years,pop)
plt.title("Iran3")

plt.subplot(2,3,4)
plt.plot(years,popkor)
plt.title("Korea1")

plt.subplot(2,3,5)
plt.plot(years,popkor)
plt.title("Korea2")

plt.subplot(2,3,6)
plt.plot(years,popkor)
plt.title("Korea3")

plt.show()


# In[10]:


#seaborn is very important for statistical graphs (statistical data visualization)
import pandas as pd
import seaborn as sb
import matplotlib as pl
import matplotlib.pyplot as plt


# In[16]:


Labourforce97=pd.read_excel("G:\RawData\Labour95-96-97\LFS-Hamed\lfs97.xlsx")


# In[17]:


Labourforce97.head()


# #Strip plot:
# sb.stripplot(y="W2", data=Labourforce97, size=5)
# plt.show()

# #Strip plot:
# sb.stripplot(x="W3", y="W2", data=Labourforce97, size=5)
# plt.show()

# titanic=pd.read_csv("G:\Machine_Learning\titanic.csv")

# In[11]:


2+2


# In[13]:


#seaborn is very important for statistical graphs (statistical data visualization)
import pandas as pd
import seaborn as sb
import matplotlib as pl
import matplotlib.pyplot as plt


# In[18]:


titanic=pd.read_excel(r"G:\MachineLearning\titanic.xls")


# In[19]:


titanic


# In[21]:


titanic.tail


# In[24]:


titanic.head


# In[ ]:


get_ipython().run_line_magic('pinfo', 'read')

