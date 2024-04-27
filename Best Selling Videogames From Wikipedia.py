#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Importing Libraries to Scrape Website Data

from bs4 import BeautifulSoup
import requests


# In[4]:


# Connecting Website

url = 'https://en.wikipedia.org/wiki/List_of_best-selling_video_games'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')

print(soup)


# In[5]:


# Collecting Website Data

soup.find('table')


# In[7]:


soup.find_all('table')[1]


# In[30]:


soup.find('table', class_ = 'wikitable plainrowheaders')


# In[32]:


print(table)


# In[41]:


soup.find('table', class_ = "wikitable plainrowheaders sortable")


# In[66]:


game_titles = table.find_all('th')
game_titles


# In[67]:


game_table_titles = [title.text.strip() for title in game_titles]
print(game_table_titles)


# In[68]:


# Importing a new library

import pandas as pd


# In[91]:


# Creating a Table From Website Data for Analysis

df = pd.DataFrame(columns = game_table_titles)

df


# In[93]:


column_data = table.find_all('tr')


# In[96]:


for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]


# In[97]:


df


# In[102]:


# Convert to CSV
df.to_csv(r'C:\Users\davin\Downloads\BestSellingVideogames.csv', index = False)

