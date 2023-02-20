#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf


# In[2]:


stock_list = ["XLE", "XLB", "XLI","XLY", "XLP", "XLV", "XLF", "SMH", "XTL", "XLU", "IYR"]
print("stock_list:", stock_list)
data = yf.download(stock_list, start="2020-01-01", end="2021-12-31")['Adj Close']
data.head()


# In[3]:


data.plot()
plt.legend()
plt.title("Returns", fontsize=16)
plt.ylabel('Cumulative Returns', fontsize=14)
plt.xlabel('Year', fontsize=14)
plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
plt.show()


# In[4]:


percent_changes = {}
for stock in stock_list:
    percent_change = (data[stock][-1] - data[stock][0]) / data[stock][0] * 100
    percent_changes[stock] = round(percent_change, 2)
print(percent_changes)
print('The highest performing sector is SMH with a percentage increase of ', percent_changes['SMH'])


# In[ ]:




