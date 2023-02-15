#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time


# In[2]:


itime = time.time()
print(itime)


# In[9]:


temp = 24.5
hum = 35.4
press = 1016.2
gas = 89450

print(itime,temp,hum,press,gas)

meta_data = ["Time","Temp","Humidity","Pressure","Gas"]

data = [itime,temp,hum,press,gas]


# In[8]:


f = open("data.csv","w")


# In[10]:


for entry in meta_data:
    f.write(entry+',')
f.write('\n')

for idata in data:
    f.write(str(idata)+',')
f.write('\n')


# In[11]:


f.close()


# In[12]:


import csv


# In[19]:


f = open("data.csv","w", newline = '')


# In[20]:


writer = csv.writer(f)


# In[21]:


writer.writerow(meta_data)


# In[22]:


writer.writerow(data)


# In[23]:


f.close()


# In[ ]:




