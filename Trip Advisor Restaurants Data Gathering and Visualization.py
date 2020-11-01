#!/usr/bin/env python
# coding: utf-8

# ### Import Libraries

# In[66]:


from bs4 import BeautifulSoup
from requests import get
import pandas as pd
import re
import requests
from selenium import webdriver
import shutil
import time
import os
import glob
import pandas as pd 
import googlemaps
import urllib
import requests
import geocoder
from pprint import pprint
import json
import gmaps
import getpass
headers = ({'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})


# ### Intiating the driver , declaring variables , defining the search page

# In[10]:


search_page='https://www.tripadvisor.com/Restaurants-g295424-Dubai_Emirate_of_Dubai.html'
chromedriver = "chromedriver.exe"
driver=webdriver.Chrome(chromedriver)
driver.get(search_page)
response = get(search_page,headers=headers)
time.sleep(2)
df=pd.DataFrame()
links=[]
titles=[]
y=0


# ### Making a list of URLS of the search results , only define the number of pages you want

# In[11]:


for i in range (1):
    page_soup = BeautifulSoup(driver.page_source, 'html.parser')
    for i in range (len(page_soup.findAll('div', class_="_1llCuDZj"))):
        rest = page_soup.findAll('div', class_="_1llCuDZj")[i]
        title=page_soup.findAll('div', class_="_2kbTRHSI")[i].getText()
        print(title)
        titles.append(title)
        for url in rest.findAll('a'):
                link="https://www.tripadvisor.com/"+url.get('href')
                print(link)
                links.append(link)
                break
    for x in driver.find_elements_by_link_text('Next'):
        driver.execute_script("arguments[0].click();", x)
        time.sleep(3)
    time.sleep(3)
    y=y+1
    print(y)


# ### assigning the dataframe columns to the list of restaurant

# In[12]:


df['Title']=titles
df['Link']=links
df


# ### Declaring the columns of the selected fields to be scraped

# In[16]:


location_column=[]
telephone_column=[]
website_column=[]
menu_url_column=[]
cost_column=[]
description_column=[]
rating_column=[]
reviews_no_column=[]
features_column=[]
order_of_restaurant_column=[]


# ### Iterating through the links and scrape those fields 

# In[17]:


x=0
number_of_scrapped_search_pages=1
for i in range(len(df)):
    place_url=df.iloc[i,number_of_scrapped_search_pages] 
    driver.get(place_url)
    place_response=get(place_url,headers=headers)
    soup = BeautifulSoup(place_response.text, 'html.parser')

    try:
        location_class = "_15QfMZ2L"
        location_list=soup.findAll('a', class_=location_class)
        
        location=location_list[1].text
    except: 
        location="Error in Location"
        
    location_column.append(location)
    
    
    
    
    try:
        order_of_restaurant=location_list[0].text.split(' ')[0]
    except:
        order_of_restaurant="Error in Order"
        
    order_of_restaurant_column.append(order_of_restaurant)
        
        
    try:
        telephone_class= "_3S6pHEQs"
        telephone_list=soup.findAll('a', class_=telephone_class)
        telephone=telephone_list[1].text
    except:
        telephone="Error in Telephone"
        
    telephone_column.append(telephone)
        
        
        
        
    try:
        website_list=driver.find_elements_by_link_text('Website')
        website=website_list[0].get_attribute("href")
    except:
        website="Error in website"
        
    website_column.append(website)
        
        

        
        
    try:
        description_class="_2mn01bsa"
        description_list=soup.findAll('a', class_=description_class)
        description_str= [x.text for x in description_list]
        description=' '.join(description_str[1:])
    except:
        description="Error in Description"
        
    description_column.append(description)
        
    try:
        menu_list=driver.find_elements_by_link_text('Menu')
        menu_url=menu_list[0].get_attribute("href")
    except:
        menu_url="Error in Menu Url"
        
    menu_url_column.append(menu_url)
        
    
        
    try:
        cost=description_list[0].text
    except:
        cost="Error in Cost"
        
    cost_column.append(cost)
        
        
    
        
    try:
        rating_class= "r2Cf69qf"
        rating_list=soup.findAll('span', class_=rating_class)
        rating=float(rating_list[0].text[:3])
    except:
        rating="Error in rating"
        
    rating_column.append(rating)
        
    
    try:
        reviews_class="_10Iv7dOs"
        reviews_list=soup.findAll('a', class_=reviews_class)
        reviews_no=int(reviews_list[0].text.split(" ")[0].replace(",",""))
    except:
        reviews_no="Error in reviews_no"
        
    reviews_no_column.append(reviews_no)
        
        
        
    try:
        features_class="_2170bBgV"
        features_list=soup.findAll('div', class_=features_class)
        features=features_list[-1].text
    except:
        features="No Features"
        
    features_column.append(features)
    
    x=x+1
    print(website)
    


# ### Assign the lists to dataframe columns

# In[18]:


df['Location']=location_column
df['Telephone']=telephone_column
df['Website']=website_column
df['Menu Url']=menu_url_column
df['Cost']=cost_column
df['Description']=description_column
df['Rating']=rating_column
df['Reviews']=reviews_no_column
df['Features']=features_column
df['Order']=order_of_restaurant_column


# In[23]:


df


# In[68]:


api_key=getpass.getpass(prompt='API Key: ', stream=None) 
gmaps_key=googlemaps.Client(key=api_key)

df['lat']=None
df['lng']=None


# In[28]:


for i in range(len(df)):
    geocode_result=gmaps_key.geocode(df.loc[i,'Location'])
    try:
        lat=geocode_result[0]['geometry']['location']['lat']
        lng=geocode_result[0]['geometry']['location']['lng']
        df.loc[i,'lat']=lat
        df.loc[i,'lng']=lng
    except:
        lat=None
        lng=None
print(df)


# In[29]:


df


# In[51]:


dubai_lat=25.2048
dubai_lng=55.2708


# In[56]:


restaurant_map = folium.Map(location=[dubai_lat, dubai_lng], zoom_start=15)
restaurant_map


# In[62]:


for title, telephone , url , lat, lon,Rating in zip(df["Title"],df["Telephone"],df["Website"],df['lat'], df['lng'],df["Rating"]):
    folium.CircleMarker(
        [lat, lon],
        radius=5,
        popup = ('Title: ' + str(title).capitalize() + '<br>'
                 'Telephone: ' + str(telephone) + '<br>'
                 'url: ' + str(url)
                ),
        color='red',
        threshold_scale=[0,1,2,3],
        fill=True,
        #fill_color=colordict[df['']],
        fill_opacity=0.7
        ).add_to(restaurant_map)
restaurant_map


# In[ ]:





# In[ ]:




