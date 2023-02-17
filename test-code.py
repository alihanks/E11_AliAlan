#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time


itime = time.time()
print(itime)


# In[3]:


temp = 24.5
hum = 35.4
press = 1016.2
gas = 89450

data = [itime,temp,hum,press,gas]
print(itime,temp,hum,press,gas)


# In[4]:


meta_data = ["Time", "Temperature","Humidity","Pressure","Gas"]


# In[5]:


f = open("data.csv","w")


# In[6]:


for entry in meta_data:
    f.write(entry+',')

f.write('\n')


# In[8]:


for idata in data:
    f.write(str(idata)+',')
f.write("\n")


# In[9]:


f.close()


# In[10]:


import csv


# In[17]:


f = open("data.csv","w", newline='')
writer = csv.writer(f)


# In[18]:


writer.writerow(meta_data)


# In[19]:


writer.writerow(data)


# In[20]:


f.close()


# In[ ]:




while True:
    itime = time.time()
    temp = bme680.temperature
    hum = 35.4
    press = 1016.2
    gas = 89450

    data = [itime,temp,hum,press,gas]
    time.sleep(1)
    writer.writerow(data)

