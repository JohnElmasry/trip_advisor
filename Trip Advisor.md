### Import Libraries


```python
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

```

### Intiating the driver , declaring variables , defining the search page


```python
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
```

### Making a list of URLS of the search results , only define the number of pages you want


```python
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
```

    SponsoredFolly by Nick & Scott
    https://www.tripadvisor.com//Restaurant_Review-g295424-d12187849-Reviews-Folly_by_Nick_Scott-Dubai_Emirate_of_Dubai.html
    1. Asil Restaurant
    https://www.tripadvisor.com//Restaurant_Review-g295424-d21035606-Reviews-Asil_Restaurant-Dubai_Emirate_of_Dubai.html
    2. MezzaLuna
    https://www.tripadvisor.com//Restaurant_Review-g295424-d3919907-Reviews-MezzaLuna-Dubai_Emirate_of_Dubai.html
    3. Cadiz - Ahlan Lounge @ Gate B26
    https://www.tripadvisor.com//Restaurant_Review-g295424-d16897846-Reviews-Cadiz_Ahlan_Lounge_Gate_B26-Dubai_Emirate_of_Dubai.html
    4. BLVD on One
    https://www.tripadvisor.com//Restaurant_Review-g295424-d12630110-Reviews-BLVD_on_One-Dubai_Emirate_of_Dubai.html
    5. Purani Dilli Dubai
    https://www.tripadvisor.com//Restaurant_Review-g295424-d16810811-Reviews-Purani_Dilli_Dubai-Dubai_Emirate_of_Dubai.html
    SponsoredGrapeskin Grape Bar and Kitchen
    https://www.tripadvisor.com//Restaurant_Review-g295424-d12632821-Reviews-Grapeskin_Grape_Bar_and_Kitchen-Dubai_Emirate_of_Dubai.html
    6. Trattoria By Cinque
    https://www.tripadvisor.com//Restaurant_Review-g295424-d18971372-Reviews-Trattoria_By_Cinque-Dubai_Emirate_of_Dubai.html
    7. Doors Freestyle Grill
    https://www.tripadvisor.com//Restaurant_Review-g295424-d15293945-Reviews-Doors_Freestyle_Grill-Dubai_Emirate_of_Dubai.html
    8. Urban Bar & Kitchen - ubk
    https://www.tripadvisor.com//Restaurant_Review-g295424-d6419196-Reviews-Urban_Bar_Kitchen_ubk-Dubai_Emirate_of_Dubai.html
    9. Barefoot Lounge
    https://www.tripadvisor.com//Restaurant_Review-g295424-d8470402-Reviews-Barefoot_Lounge-Dubai_Emirate_of_Dubai.html
    10. Mina Brasserie
    https://www.tripadvisor.com//Restaurant_Review-g295424-d13508198-Reviews-Mina_Brasserie-Dubai_Emirate_of_Dubai.html
    SponsoredGraze Gastro Grill
    https://www.tripadvisor.com//Restaurant_Review-g295424-d12365282-Reviews-Graze_Gastro_Grill-Dubai_Emirate_of_Dubai.html
    11. Al Sarab Rooftop Lounge
    https://www.tripadvisor.com//Restaurant_Review-g295424-d3918371-Reviews-Al_Sarab_Rooftop_Lounge-Dubai_Emirate_of_Dubai.html
    12. Soul Street
    https://www.tripadvisor.com//Restaurant_Review-g295424-d18344720-Reviews-Soul_Street-Dubai_Emirate_of_Dubai.html
    13. Bebemos
    https://www.tripadvisor.com//Restaurant_Review-g295424-d16884080-Reviews-Bebemos-Dubai_Emirate_of_Dubai.html
    14. Awtar
    https://www.tripadvisor.com//Restaurant_Review-g295424-d3918483-Reviews-Awtar-Dubai_Emirate_of_Dubai.html
    15. Tribes Carnivore
    https://www.tripadvisor.com//Restaurant_Review-g295424-d11948587-Reviews-Tribes_Carnivore-Dubai_Emirate_of_Dubai.html
    SponsoredSushi Nations
    https://www.tripadvisor.com//Restaurant_Review-g295424-d13162261-Reviews-Sushi_Nations-Dubai_Emirate_of_Dubai.html
    16. Al Dawaar Revolving Restaurant
    https://www.tripadvisor.com//Restaurant_Review-g295424-d814928-Reviews-Al_Dawaar_Revolving_Restaurant-Dubai_Emirate_of_Dubai.html
    17. Khyber
    https://www.tripadvisor.com//Restaurant_Review-g295424-d3919600-Reviews-Khyber-Dubai_Emirate_of_Dubai.html
    18. Danial Restaurant
    https://www.tripadvisor.com//Restaurant_Review-g295424-d3919038-Reviews-Danial_Restaurant-Dubai_Emirate_of_Dubai.html
    19. Eve Penthouse & Lounge
    https://www.tripadvisor.com//Restaurant_Review-g295424-d15106127-Reviews-Eve_Penthouse_Lounge-Dubai_Emirate_of_Dubai.html
    20. The Grill Shack
    https://www.tripadvisor.com//Restaurant_Review-g295424-d13455740-Reviews-The_Grill_Shack-Dubai_Emirate_of_Dubai.html
    SponsoredAmritsr Restaurant
    https://www.tripadvisor.com//Restaurant_Review-g295424-d17826458-Reviews-Amritsr_Restaurant-Dubai_Emirate_of_Dubai.html
    21. Maiden Shanghai
    https://www.tripadvisor.com//Restaurant_Review-g295424-d12399372-Reviews-Maiden_Shanghai-Dubai_Emirate_of_Dubai.html
    22. Purani Dilli Sheikh Zayed Road
    https://www.tripadvisor.com//Restaurant_Review-g295424-d18312975-Reviews-Purani_Dilli_Sheikh_Zayed_Road-Dubai_Emirate_of_Dubai.html
    23. Level 43 Sky Lounge
    https://www.tripadvisor.com//Restaurant_Review-g295424-d3403341-Reviews-Level_43_Sky_Lounge-Dubai_Emirate_of_Dubai.html
    24. Black Tap Craft Burgers & Shakes Dubai Mall
    https://www.tripadvisor.com//Restaurant_Review-g295424-d20912480-Reviews-Black_Tap_Craft_Burgers_Shakes_Dubai_Mall-Dubai_Emirate_of_Dubai.html
    25. Beef Bistro
    https://www.tripadvisor.com//Restaurant_Review-g295424-d2618147-Reviews-Beef_Bistro-Dubai_Emirate_of_Dubai.html
    SponsoredVerde Dubai
    https://www.tripadvisor.com//Restaurant_Review-g295424-d19685813-Reviews-Verde_Dubai-Dubai_Emirate_of_Dubai.html
    26. Nido Tapas Restaurant & Bar
    https://www.tripadvisor.com//Restaurant_Review-g295424-d19463460-Reviews-Nido_Tapas_Restaurant_Bar-Dubai_Emirate_of_Dubai.html
    27. Shamiana
    https://www.tripadvisor.com//Restaurant_Review-g295424-d19815899-Reviews-Shamiana-Dubai_Emirate_of_Dubai.html
    28. Kinara by Vikas Khanna
    https://www.tripadvisor.com//Restaurant_Review-g295424-d18856876-Reviews-Kinara_by_Vikas_Khanna-Dubai_Emirate_of_Dubai.html
    29. Little Miss India
    https://www.tripadvisor.com//Restaurant_Review-g295424-d13005029-Reviews-Little_Miss_India-Dubai_Emirate_of_Dubai.html
    30. Fish Hut Asmak Al Sultan Seafood Restaurant
    https://www.tripadvisor.com//Restaurant_Review-g295424-d11615000-Reviews-Fish_Hut_Asmak_Al_Sultan_Seafood_Restaurant-Dubai_Emirate_of_Dubai.html
    SponsoredChival
    https://www.tripadvisor.com//Restaurant_Review-g295424-d12597643-Reviews-Chival-Dubai_Emirate_of_Dubai.html
    1
    

### assigning the dataframe columns to the list of restaurant


```python
df['Title']=titles
df['Link']=links
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Title</th>
      <th>Link</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>SponsoredFolly by Nick &amp; Scott</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1. Asil Restaurant</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2. MezzaLuna</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3. Cadiz - Ahlan Lounge @ Gate B26</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4. BLVD on One</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5. Purani Dilli Dubai</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
    </tr>
    <tr>
      <th>6</th>
      <td>SponsoredGrapeskin Grape Bar and Kitchen</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
    </tr>
    <tr>
      <th>7</th>
      <td>6. Trattoria By Cinque</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
    </tr>
    <tr>
      <th>8</th>
      <td>7. Doors Freestyle Grill</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
    </tr>
    <tr>
      <th>9</th>
      <td>8. Urban Bar &amp; Kitchen - ubk</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
    </tr>
    <tr>
      <th>10</th>
      <td>9. Barefoot Lounge</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
    </tr>
    <tr>
      <th>11</th>
      <td>10. Mina Brasserie</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
    </tr>
    <tr>
      <th>12</th>
      <td>SponsoredGraze Gastro Grill</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
    </tr>
    <tr>
      <th>13</th>
      <td>11. Al Sarab Rooftop Lounge</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
    </tr>
    <tr>
      <th>14</th>
      <td>12. Soul Street</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
    </tr>
    <tr>
      <th>15</th>
      <td>13. Bebemos</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
    </tr>
    <tr>
      <th>16</th>
      <td>14. Awtar</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
    </tr>
    <tr>
      <th>17</th>
      <td>15. Tribes Carnivore</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
    </tr>
    <tr>
      <th>18</th>
      <td>SponsoredSushi Nations</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
    </tr>
    <tr>
      <th>19</th>
      <td>16. Al Dawaar Revolving Restaurant</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
    </tr>
    <tr>
      <th>20</th>
      <td>17. Khyber</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
    </tr>
    <tr>
      <th>21</th>
      <td>18. Danial Restaurant</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
    </tr>
    <tr>
      <th>22</th>
      <td>19. Eve Penthouse &amp; Lounge</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
    </tr>
    <tr>
      <th>23</th>
      <td>20. The Grill Shack</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
    </tr>
    <tr>
      <th>24</th>
      <td>SponsoredAmritsr Restaurant</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
    </tr>
    <tr>
      <th>25</th>
      <td>21. Maiden Shanghai</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
    </tr>
    <tr>
      <th>26</th>
      <td>22. Purani Dilli Sheikh Zayed Road</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
    </tr>
    <tr>
      <th>27</th>
      <td>23. Level 43 Sky Lounge</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
    </tr>
    <tr>
      <th>28</th>
      <td>24. Black Tap Craft Burgers &amp; Shakes Dubai Mall</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
    </tr>
    <tr>
      <th>29</th>
      <td>25. Beef Bistro</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
    </tr>
    <tr>
      <th>30</th>
      <td>SponsoredVerde Dubai</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
    </tr>
    <tr>
      <th>31</th>
      <td>26. Nido Tapas Restaurant &amp; Bar</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
    </tr>
    <tr>
      <th>32</th>
      <td>27. Shamiana</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
    </tr>
    <tr>
      <th>33</th>
      <td>28. Kinara by Vikas Khanna</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
    </tr>
    <tr>
      <th>34</th>
      <td>29. Little Miss India</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
    </tr>
    <tr>
      <th>35</th>
      <td>30. Fish Hut Asmak Al Sultan Seafood Restaurant</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
    </tr>
    <tr>
      <th>36</th>
      <td>SponsoredChival</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
    </tr>
  </tbody>
</table>
</div>



### Declaring the columns of the selected fields to be scraped


```python
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
```

### Iterating through the links and scrape those fields 


```python
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
    
```

    http://folly.ae/
    http://www.asilrestaurant.com/
    http://www.diningdfc.com/Restaurant-details/24/MezzaLuna
    http://www.dubaiintlhotels.com/dining/ahlan-lounge-b
    http://fivehotelsandresorts.com/dine-drink-dance/restaurants/blvd-on-one/
    http://www.puranidillidubai.com/
    http://www.livelaville.com/dining/Grapeskin/index.aspx
    http://jumeirahvillage.fivehotelsandresorts.com/meet-mingle/trattoria-by-cinque
    http://www.doorsdubai.com/en
    http://www.movenpick.com/en/middle-east/uae/dubai/dubai-jumeirah-lakes-towers/restaurants/restaurants/urban-bar-kitchen-ubk
    http://www.dxbmarine.com/
    http://www.minabrasserie.com/
    http://www.livelaville.com/dining/Graze/index.html
    http://www.meydanhotels.com/babalshams/dining.htm
    http://soul.st/
    http://www.bebemosdubai.com/
    https://www.hyattrestaurants.com/en/dining/uae/dubai/middle-eastern-restaurant-in-garhoud-awtar?utm_source=gmblisting_dxbgh&utm_medium=awtar&utm_campaign=GMB
    http://tribesrestaurant.com/
    https://sushinations.ae/
    http://www.hyattrestaurants.com/en/dining/uae/dubai/international-restaurant-in-deira-corniche-al-dawaar-revolving-restaurant
    https://www.dukesdubai.com/khyber/
    http://www.danialrestaurant.com/
    http://www.hyattrestaurants.com/en/dining/uae/dubai/international-restaurant-in-oud-metha-road-eve-penthouse-lounge?utm_source=Website_dxbhc&utm_medium=eve&utm_campaign=Hyatt
    http://www.thegrilllshack.com/
    http://amritsruae.com/
    http://fivehotelsandresorts.com/dine-drink-dance/restaurants/maiden-shanghai/
    http://www.puranidillidubai.com/sheikhzayedroad
    http://www.level43lounge.com/
    http://www.blacktapme.com/
    http://www.beefbistrodubai.com/
    http://www.verde-dubai.com/
    http://nidodxb.com/
    http://www.tajhotels.com/en-in/taj/taj-jumeirah-lakes-towers/restaurants/shamiana/
    http://www.kinaradubai.com/
    http://www.fairmont.com/palm-dubai/dining/little-miss-india/
    http://dubaifishhutrestaurant.com/index.php
    http://www.chivallaville.com/
    

### Assign the lists to dataframe columns


```python
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
```


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Title</th>
      <th>Link</th>
      <th>Location</th>
      <th>Telephone</th>
      <th>Website</th>
      <th>Menu Url</th>
      <th>Cost</th>
      <th>Description</th>
      <th>Rating</th>
      <th>Reviews</th>
      <th>Features</th>
      <th>Order</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>SponsoredFolly by Nick &amp; Scott</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Unit 27, Souk Madinat Jumeriah, Dubai United A...</td>
      <td>+971 4 430 8535</td>
      <td>http://folly.ae/</td>
      <td>https://folly.ae/food/</td>
      <td>$$$$</td>
      <td>International Vegetarian Friendly Vegan Options</td>
      <td>4.5</td>
      <td>291</td>
      <td>Reservations, Outdoor Seating, Private Dining,...</td>
      <td>#316</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1. Asil Restaurant</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Jumeirah Beach Residence - The Walk Ground Flo...</td>
      <td>+971 52 160 0333</td>
      <td>http://www.asilrestaurant.com/</td>
      <td>https://www.asilrestaurant.com/downloads/alaca...</td>
      <td>$$$$</td>
      <td>Lebanese Moroccan Turkish</td>
      <td>5.0</td>
      <td>233</td>
      <td>Takeout, Reservations, Outdoor Seating, Seatin...</td>
      <td>#1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2. MezzaLuna</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Lobby Level, Intercontinental Residence Suites...</td>
      <td>+971 4 701 1128</td>
      <td>http://www.diningdfc.com/Restaurant-details/24...</td>
      <td>https://a62be139-804e-413a-9f69-68bbb2441a0f.f...</td>
      <td>$$ - $$$</td>
      <td>Mediterranean European Vegetarian Friendly</td>
      <td>5.0</td>
      <td>248</td>
      <td>No Features</td>
      <td>#2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3. Cadiz - Ahlan Lounge @ Gate B26</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Terminal 3, Concourse B, near Gate B26. Dubai ...</td>
      <td>+971 4 505 2000</td>
      <td>http://www.dubaiintlhotels.com/dining/ahlan-lo...</td>
      <td>https://www.dubaiintlhotels.com/dining/ahlan-l...</td>
      <td>$$ - $$$</td>
      <td>Bar International Vegetarian Friendly</td>
      <td>5.0</td>
      <td>737</td>
      <td>No Features</td>
      <td>#4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4. BLVD on One</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>No 1, Palm Jumeirah FIVE Palm Jumeirah, Dubai ...</td>
      <td>+971 4 455 9989</td>
      <td>http://fivehotelsandresorts.com/dine-drink-dan...</td>
      <td>https://www.fivehotelsandresorts.com/media/503...</td>
      <td>$$ - $$$</td>
      <td>European Central European Vegetarian Friendly</td>
      <td>5.0</td>
      <td>1152</td>
      <td>No Features</td>
      <td>#5</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5. Purani Dilli Dubai</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Mankhool, Street 4C, Bur Dubai, Dubai Ground F...</td>
      <td>+971 50 211 6816</td>
      <td>http://www.puranidillidubai.com/</td>
      <td>https://www.puranidillidubai.com/our-menus</td>
      <td>$$ - $$$</td>
      <td>Indian Vegetarian Friendly Vegan Options</td>
      <td>5.0</td>
      <td>1396</td>
      <td>No Features</td>
      <td>#8</td>
    </tr>
    <tr>
      <th>6</th>
      <td>SponsoredGrapeskin Grape Bar and Kitchen</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Al Multaqa Street La Ville Hotel &amp; Suites City...</td>
      <td>+971 4 403 3111</td>
      <td>http://www.livelaville.com/dining/Grapeskin/in...</td>
      <td>https://livelaville.com/dining/Grapeskin/index...</td>
      <td>$$ - $$$</td>
      <td>Bar European Wine Bar</td>
      <td>4.5</td>
      <td>111</td>
      <td>No Features</td>
      <td>#397</td>
    </tr>
    <tr>
      <th>7</th>
      <td>6. Trattoria By Cinque</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>District 14, Street 1, Jumeirah Village Circle...</td>
      <td>+971 4 455 9989</td>
      <td>http://jumeirahvillage.fivehotelsandresorts.co...</td>
      <td>https://five.kitchen/tbc/</td>
      <td>$$ - $$$</td>
      <td>International Vegetarian Friendly Vegan Options</td>
      <td>5.0</td>
      <td>437</td>
      <td>No Features</td>
      <td>#9</td>
    </tr>
    <tr>
      <th>8</th>
      <td>7. Doors Freestyle Grill</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>8/5 - 314 Al Seef St, Dubai United Arab Emirates</td>
      <td>+971 4 204 9299</td>
      <td>http://www.doorsdubai.com/en</td>
      <td>https://www.doorsdubai.com/en/menu/</td>
      <td>$$$$</td>
      <td>Steakhouse Seafood International</td>
      <td>5.0</td>
      <td>1372</td>
      <td>Reservations, Outdoor Seating, Private Dining,...</td>
      <td>#10</td>
    </tr>
    <tr>
      <th>9</th>
      <td>8. Urban Bar &amp; Kitchen - ubk</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Cluster A, Jumeriah Lakes Towers Movenpick Hot...</td>
      <td>+971 4 438 0000</td>
      <td>http://www.movenpick.com/en/middle-east/uae/du...</td>
      <td>https://www.movenpick.com/fileadmin/files/Hote...</td>
      <td>$$ - $$$</td>
      <td>Bar International Pub</td>
      <td>5.0</td>
      <td>1105</td>
      <td>No Features</td>
      <td>#11</td>
    </tr>
    <tr>
      <th>10</th>
      <td>9. Barefoot Lounge</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Jumeirah 1 Opp Grand Jumeirah Mosque, Dubai 51...</td>
      <td>+971 4 346 1111</td>
      <td>http://www.dxbmarine.com/</td>
      <td>Error in Menu Url</td>
      <td>$$ - $$$</td>
      <td>Bar Seafood Grill</td>
      <td>5.0</td>
      <td>558</td>
      <td>No Features</td>
      <td>#12</td>
    </tr>
    <tr>
      <th>11</th>
      <td>10. Mina Brasserie</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Four Seasons Hotel DIFC, Podium Level, Buildin...</td>
      <td>+971 4 506 0100</td>
      <td>http://www.minabrasserie.com/</td>
      <td>http://www.minabrasserie.com/#menu</td>
      <td>$$$$</td>
      <td>French American European</td>
      <td>5.0</td>
      <td>291</td>
      <td>Reservations, Outdoor Seating, Seating, Serves...</td>
      <td>#13</td>
    </tr>
    <tr>
      <th>12</th>
      <td>SponsoredGraze Gastro Grill</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Al Multaqa Street La Ville Hotel &amp; Suites, Dub...</td>
      <td>+971 4 403 3111</td>
      <td>http://www.livelaville.com/dining/Graze/index....</td>
      <td>https://www.livelaville.com/dining/graze/index...</td>
      <td>$$ - $$$</td>
      <td>Steakhouse European Vegetarian Friendly</td>
      <td>4.5</td>
      <td>106</td>
      <td>No Features</td>
      <td>#467</td>
    </tr>
    <tr>
      <th>13</th>
      <td>11. Al Sarab Rooftop Lounge</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Al Qudra Rd Bab Al Shams Desert Resort &amp; Spa, ...</td>
      <td>+971 4 809 6100</td>
      <td>http://www.meydanhotels.com/babalshams/dining.htm</td>
      <td>https://babalshams.com/sites/default/files/202...</td>
      <td>$$ - $$$</td>
      <td>Lebanese Bar Mediterranean</td>
      <td>5.0</td>
      <td>1229</td>
      <td>No Features</td>
      <td>#14</td>
    </tr>
    <tr>
      <th>14</th>
      <td>12. Soul Street</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>District 14, Street 1, Jumeirah Village Circle...</td>
      <td>+971 4 455 9989</td>
      <td>http://soul.st/</td>
      <td>https://five.kitchen/ss/</td>
      <td>$$ - $$$</td>
      <td>Mexican Bar International</td>
      <td>5.0</td>
      <td>457</td>
      <td>Reservations, Outdoor Seating, Seating, Parkin...</td>
      <td>#15</td>
    </tr>
    <tr>
      <th>15</th>
      <td>13. Bebemos</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Airport Road Le Méridien Dubai Hotel &amp; Confere...</td>
      <td>+971 4 702 2455</td>
      <td>http://www.bebemosdubai.com/</td>
      <td>https://www.bebemosdubai.com/our-menus</td>
      <td>$$ - $$$</td>
      <td>Spanish Catalan Vegetarian Friendly</td>
      <td>5.0</td>
      <td>272</td>
      <td>No Features</td>
      <td>#17</td>
    </tr>
    <tr>
      <th>16</th>
      <td>14. Awtar</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Sheikh Rashid Road Grand Hyatt Dubai, Dubai 79...</td>
      <td>+971 4 317 2221</td>
      <td>https://www.hyattrestaurants.com/en/dining/uae...</td>
      <td>https://www.hyattrestaurants.com/en/dining/uae...</td>
      <td>$$$$</td>
      <td>Lebanese Vegetarian Friendly Vegan Options</td>
      <td>5.0</td>
      <td>367</td>
      <td>Outdoor Seating, Seating, Parking Available, V...</td>
      <td>#18</td>
    </tr>
    <tr>
      <th>17</th>
      <td>15. Tribes Carnivore</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Shikh Mohamed bin rashid Blvd Dubai Mall, Duba...</td>
      <td>+971 4 226 4974</td>
      <td>http://tribesrestaurant.com/</td>
      <td>https://deliveroo.ae/menu/dubai/al-barsha-1/tr...</td>
      <td>$$ - $$$</td>
      <td>Steakhouse African International</td>
      <td>5.0</td>
      <td>839</td>
      <td>Takeout, Reservations, Outdoor Seating, Seatin...</td>
      <td>#19</td>
    </tr>
    <tr>
      <th>18</th>
      <td>SponsoredSushi Nations</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Sheikh Zayed Rd Latifa Tower, Shop No.L2, Grou...</td>
      <td>+971 56 188 8522</td>
      <td>https://sushinations.ae/</td>
      <td>http://order.chatfood.io/sushi-nations</td>
      <td>$$ - $$$</td>
      <td>Japanese Seafood Sushi</td>
      <td>4.5</td>
      <td>180</td>
      <td>No Features</td>
      <td>#838</td>
    </tr>
    <tr>
      <th>19</th>
      <td>16. Al Dawaar Revolving Restaurant</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Hyatt Regency Dubai Hotel Al Khaleej Road, Dei...</td>
      <td>+971 4 209 6912</td>
      <td>http://www.hyattrestaurants.com/en/dining/uae/...</td>
      <td>https://www.hyattrestaurants.com/en/dining/uae...</td>
      <td>$$$$</td>
      <td>International Mediterranean Sushi</td>
      <td>5.0</td>
      <td>3074</td>
      <td>Reservations, Buffet, Seating, Parking Availab...</td>
      <td>#20</td>
    </tr>
    <tr>
      <th>20</th>
      <td>17. Khyber</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Palm Jumeirah Dukes Dubai Oceana, Dubai United...</td>
      <td>+971 4 455 1111</td>
      <td>https://www.dukesdubai.com/khyber/</td>
      <td>Error in Menu Url</td>
      <td>$$ - $$$</td>
      <td>Indian Vegetarian Friendly Vegan Options</td>
      <td>5.0</td>
      <td>555</td>
      <td>No Features</td>
      <td>#21</td>
    </tr>
    <tr>
      <th>21</th>
      <td>18. Danial Restaurant</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Twin Towers 3rd Flr Baniyas Rd, Dubai United A...</td>
      <td>+971 4 227 7669</td>
      <td>http://www.danialrestaurant.com/</td>
      <td>Error in Menu Url</td>
      <td>$$ - $$$</td>
      <td>Middle Eastern Persian Arabic</td>
      <td>5.0</td>
      <td>370</td>
      <td>No Features</td>
      <td>#22</td>
    </tr>
    <tr>
      <th>22</th>
      <td>19. Eve Penthouse &amp; Lounge</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Hyatt Regency Dubai Creek Heights Dubai Health...</td>
      <td>+971 4 553 1214</td>
      <td>http://www.hyattrestaurants.com/en/dining/uae/...</td>
      <td>https://www.hyattrestaurants.com/en/dining/uae...</td>
      <td>$$ - $$$</td>
      <td>Bar Vegetarian Friendly Vegan Options</td>
      <td>5.0</td>
      <td>402</td>
      <td>No Features</td>
      <td>#23</td>
    </tr>
    <tr>
      <th>23</th>
      <td>20. The Grill Shack</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>The Dubai Mall Second Floor Food Court, Dubai ...</td>
      <td>+971 4 388 2382</td>
      <td>http://www.thegrilllshack.com/</td>
      <td>http://www.thegrilllshack.com/wp-content/uploa...</td>
      <td>$$ - $$$</td>
      <td>American Steakhouse Barbecue</td>
      <td>5.0</td>
      <td>518</td>
      <td>No Features</td>
      <td>#24</td>
    </tr>
    <tr>
      <th>24</th>
      <td>SponsoredAmritsr Restaurant</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Al Attar Center, Dubai 318-836 United Arab Emi...</td>
      <td>+971 50 678 0096</td>
      <td>http://amritsruae.com/</td>
      <td>http://www.amritsruae.com/menu.html</td>
      <td>$</td>
      <td>Indian Asian Vegetarian Friendly</td>
      <td>4.5</td>
      <td>64</td>
      <td>No Features</td>
      <td>#778</td>
    </tr>
    <tr>
      <th>25</th>
      <td>21. Maiden Shanghai</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>No.1, Palm Jumeirah FIVE Palm Jumeirah, Dubai ...</td>
      <td>+971 4 455 9989</td>
      <td>http://fivehotelsandresorts.com/dine-drink-dan...</td>
      <td>https://five.kitchen/ms/</td>
      <td>$$$$</td>
      <td>Chinese Shanghai Vegetarian Friendly</td>
      <td>5.0</td>
      <td>1235</td>
      <td>Reservations, Outdoor Seating, Private Dining,...</td>
      <td>#25</td>
    </tr>
    <tr>
      <th>26</th>
      <td>22. Purani Dilli Sheikh Zayed Road</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Four Points by Sheraton Sheikh Zayed Road, Dub...</td>
      <td>+971 4 316 9726</td>
      <td>http://www.puranidillidubai.com/sheikhzayedroad</td>
      <td>https://www.puranidillidubai.com/our-menus</td>
      <td>$$ - $$$</td>
      <td>Indian Asian Vegetarian Friendly</td>
      <td>5.0</td>
      <td>223</td>
      <td>Takeout, Reservations, Seating, Parking Availa...</td>
      <td>#26</td>
    </tr>
    <tr>
      <th>27</th>
      <td>23. Level 43 Sky Lounge</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Sheikh Zayed Road Four Points by Sheraton, Dub...</td>
      <td>+971 56 414 2213</td>
      <td>http://www.level43lounge.com/</td>
      <td>https://www.level43lounge.com/our-menus</td>
      <td>$$ - $$$</td>
      <td>Bar Sushi Vegetarian Friendly</td>
      <td>4.5</td>
      <td>1619</td>
      <td>Outdoor Seating, Seating, Parking Available, V...</td>
      <td>#27</td>
    </tr>
    <tr>
      <th>28</th>
      <td>24. Black Tap Craft Burgers &amp; Shakes Dubai Mall</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Dubai Mall, Fountain Entrance, Dubai United Ar...</td>
      <td>+971 4 330 5103</td>
      <td>http://www.blacktapme.com/</td>
      <td>https://www.facebook.com/BlackTapDubai/menu/</td>
      <td>$$ - $$$</td>
      <td>American</td>
      <td>5.0</td>
      <td>96</td>
      <td>No Features</td>
      <td>#28</td>
    </tr>
    <tr>
      <th>29</th>
      <td>25. Beef Bistro</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Le Meridien Dubai Airport Road, Dubai 10001 Un...</td>
      <td>+971 4 702 2455</td>
      <td>http://www.beefbistrodubai.com/</td>
      <td>https://www.beefbistrodubai.com/our-menus</td>
      <td>$$ - $$$</td>
      <td>Steakhouse Halal Gluten Free Options</td>
      <td>5.0</td>
      <td>683</td>
      <td>Reservations, Outdoor Seating, Seating, Parkin...</td>
      <td>#29</td>
    </tr>
    <tr>
      <th>30</th>
      <td>SponsoredVerde Dubai</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Restaurant village Four Seasons Hotel, Jumeira...</td>
      <td>+971 4 333 8025</td>
      <td>http://www.verde-dubai.com/</td>
      <td>http://verde-dubai.com/en_en/menu/</td>
      <td>$$$$</td>
      <td>French European</td>
      <td>4.5</td>
      <td>45</td>
      <td>No Features</td>
      <td>#1,077</td>
    </tr>
    <tr>
      <th>31</th>
      <td>26. Nido Tapas Restaurant &amp; Bar</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>3 Sheikh Zayed Road 5th Floor, Sheraton Grand ...</td>
      <td>+971 4 333 3055</td>
      <td>http://nidodxb.com/</td>
      <td>Error in Menu Url</td>
      <td>$$ - $$$</td>
      <td>Latin Mediterranean Spanish</td>
      <td>5.0</td>
      <td>230</td>
      <td>No Features</td>
      <td>#30</td>
    </tr>
    <tr>
      <th>32</th>
      <td>27. Shamiana</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>DMCC Plot No. 2-27, Al Thanyah Taj Jumeirah La...</td>
      <td>+971 4 574 1111</td>
      <td>http://www.tajhotels.com/en-in/taj/taj-jumeira...</td>
      <td>https://tajhotels-my.sharepoint.com/:b:/p/denn...</td>
      <td>$$$$</td>
      <td>Indian Vegan Options Halal</td>
      <td>5.0</td>
      <td>86</td>
      <td>No Features</td>
      <td>#31</td>
    </tr>
    <tr>
      <th>33</th>
      <td>28. Kinara by Vikas Khanna</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Dubai, United Arab Emirates, Dubai 9255 United...</td>
      <td>+971 4 814 5555</td>
      <td>http://www.kinaradubai.com/</td>
      <td>Error in Menu Url</td>
      <td>$$$$</td>
      <td>Indian Asian Vegetarian Friendly</td>
      <td>5.0</td>
      <td>210</td>
      <td>Reservations, Outdoor Seating, Private Dining,...</td>
      <td>#32</td>
    </tr>
    <tr>
      <th>34</th>
      <td>29. Little Miss India</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Fairmont The Palm Palm Jumeirah, Dubai 72413 U...</td>
      <td>+971 4 457 3457</td>
      <td>http://www.fairmont.com/palm-dubai/dining/litt...</td>
      <td>http://palmdining.com/uploads/little-miss-indi...</td>
      <td>$$$$</td>
      <td>Indian Asian Vegetarian Friendly</td>
      <td>5.0</td>
      <td>604</td>
      <td>No Features</td>
      <td>#33</td>
    </tr>
    <tr>
      <th>35</th>
      <td>30. Fish Hut Asmak Al Sultan Seafood Restaurant</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Umm Suqeim Road Al Barsha 2, Dubai 120730 Unit...</td>
      <td>+971 58 128 2886</td>
      <td>http://dubaifishhutrestaurant.com/index.php</td>
      <td>https://www.dubaifishhutrestaurant.com/menu</td>
      <td>$</td>
      <td>International Vegetarian Friendly Halal</td>
      <td>5.0</td>
      <td>729</td>
      <td>No Features</td>
      <td>#34</td>
    </tr>
    <tr>
      <th>36</th>
      <td>SponsoredChival</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Al Multaqa Street City Walk, Dubai 414433 Unit...</td>
      <td>+971 4 403 3111</td>
      <td>http://www.chivallaville.com/</td>
      <td>https://livelaville.com/dining/chival/index.aspx</td>
      <td>$$ - $$$</td>
      <td>International Mediterranean Vegetarian Friendly</td>
      <td>4.5</td>
      <td>125</td>
      <td>No Features</td>
      <td>#250</td>
    </tr>
  </tbody>
</table>
</div>




```python
api_key=getpass.getpass(prompt='API Key: ', stream=None) 
gmaps_key=googlemaps.Client(key=api_key)

df['lat']=None
df['lng']=None
```

    API Key: ········
    


```python
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
```

                                                  Title  \
    0                    SponsoredFolly by Nick & Scott   
    1                                1. Asil Restaurant   
    2                                      2. MezzaLuna   
    3                3. Cadiz - Ahlan Lounge @ Gate B26   
    4                                    4. BLVD on One   
    5                             5. Purani Dilli Dubai   
    6          SponsoredGrapeskin Grape Bar and Kitchen   
    7                            6. Trattoria By Cinque   
    8                          7. Doors Freestyle Grill   
    9                      8. Urban Bar & Kitchen - ubk   
    10                               9. Barefoot Lounge   
    11                               10. Mina Brasserie   
    12                      SponsoredGraze Gastro Grill   
    13                      11. Al Sarab Rooftop Lounge   
    14                                  12. Soul Street   
    15                                      13. Bebemos   
    16                                        14. Awtar   
    17                             15. Tribes Carnivore   
    18                           SponsoredSushi Nations   
    19               16. Al Dawaar Revolving Restaurant   
    20                                       17. Khyber   
    21                            18. Danial Restaurant   
    22                       19. Eve Penthouse & Lounge   
    23                              20. The Grill Shack   
    24                      SponsoredAmritsr Restaurant   
    25                              21. Maiden Shanghai   
    26               22. Purani Dilli Sheikh Zayed Road   
    27                          23. Level 43 Sky Lounge   
    28  24. Black Tap Craft Burgers & Shakes Dubai Mall   
    29                                  25. Beef Bistro   
    30                             SponsoredVerde Dubai   
    31                  26. Nido Tapas Restaurant & Bar   
    32                                     27. Shamiana   
    33                       28. Kinara by Vikas Khanna   
    34                            29. Little Miss India   
    35  30. Fish Hut Asmak Al Sultan Seafood Restaurant   
    36                                  SponsoredChival   
    
                                                     Link  \
    0   https://www.tripadvisor.com//Restaurant_Review...   
    1   https://www.tripadvisor.com//Restaurant_Review...   
    2   https://www.tripadvisor.com//Restaurant_Review...   
    3   https://www.tripadvisor.com//Restaurant_Review...   
    4   https://www.tripadvisor.com//Restaurant_Review...   
    5   https://www.tripadvisor.com//Restaurant_Review...   
    6   https://www.tripadvisor.com//Restaurant_Review...   
    7   https://www.tripadvisor.com//Restaurant_Review...   
    8   https://www.tripadvisor.com//Restaurant_Review...   
    9   https://www.tripadvisor.com//Restaurant_Review...   
    10  https://www.tripadvisor.com//Restaurant_Review...   
    11  https://www.tripadvisor.com//Restaurant_Review...   
    12  https://www.tripadvisor.com//Restaurant_Review...   
    13  https://www.tripadvisor.com//Restaurant_Review...   
    14  https://www.tripadvisor.com//Restaurant_Review...   
    15  https://www.tripadvisor.com//Restaurant_Review...   
    16  https://www.tripadvisor.com//Restaurant_Review...   
    17  https://www.tripadvisor.com//Restaurant_Review...   
    18  https://www.tripadvisor.com//Restaurant_Review...   
    19  https://www.tripadvisor.com//Restaurant_Review...   
    20  https://www.tripadvisor.com//Restaurant_Review...   
    21  https://www.tripadvisor.com//Restaurant_Review...   
    22  https://www.tripadvisor.com//Restaurant_Review...   
    23  https://www.tripadvisor.com//Restaurant_Review...   
    24  https://www.tripadvisor.com//Restaurant_Review...   
    25  https://www.tripadvisor.com//Restaurant_Review...   
    26  https://www.tripadvisor.com//Restaurant_Review...   
    27  https://www.tripadvisor.com//Restaurant_Review...   
    28  https://www.tripadvisor.com//Restaurant_Review...   
    29  https://www.tripadvisor.com//Restaurant_Review...   
    30  https://www.tripadvisor.com//Restaurant_Review...   
    31  https://www.tripadvisor.com//Restaurant_Review...   
    32  https://www.tripadvisor.com//Restaurant_Review...   
    33  https://www.tripadvisor.com//Restaurant_Review...   
    34  https://www.tripadvisor.com//Restaurant_Review...   
    35  https://www.tripadvisor.com//Restaurant_Review...   
    36  https://www.tripadvisor.com//Restaurant_Review...   
    
                                                 Location         Telephone  \
    0   Unit 27, Souk Madinat Jumeriah, Dubai United A...   +971 4 430 8535   
    1   Jumeirah Beach Residence - The Walk Ground Flo...  +971 52 160 0333   
    2   Lobby Level, Intercontinental Residence Suites...   +971 4 701 1128   
    3   Terminal 3, Concourse B, near Gate B26. Dubai ...   +971 4 505 2000   
    4   No 1, Palm Jumeirah FIVE Palm Jumeirah, Dubai ...   +971 4 455 9989   
    5   Mankhool, Street 4C, Bur Dubai, Dubai Ground F...  +971 50 211 6816   
    6   Al Multaqa Street La Ville Hotel & Suites City...   +971 4 403 3111   
    7   District 14, Street 1, Jumeirah Village Circle...   +971 4 455 9989   
    8    8/5 - 314 Al Seef St, Dubai United Arab Emirates   +971 4 204 9299   
    9   Cluster A, Jumeriah Lakes Towers Movenpick Hot...   +971 4 438 0000   
    10  Jumeirah 1 Opp Grand Jumeirah Mosque, Dubai 51...   +971 4 346 1111   
    11  Four Seasons Hotel DIFC, Podium Level, Buildin...   +971 4 506 0100   
    12  Al Multaqa Street La Ville Hotel & Suites, Dub...   +971 4 403 3111   
    13  Al Qudra Rd Bab Al Shams Desert Resort & Spa, ...   +971 4 809 6100   
    14  District 14, Street 1, Jumeirah Village Circle...   +971 4 455 9989   
    15  Airport Road Le Méridien Dubai Hotel & Confere...   +971 4 702 2455   
    16  Sheikh Rashid Road Grand Hyatt Dubai, Dubai 79...   +971 4 317 2221   
    17  Shikh Mohamed bin rashid Blvd Dubai Mall, Duba...   +971 4 226 4974   
    18  Sheikh Zayed Rd Latifa Tower, Shop No.L2, Grou...  +971 56 188 8522   
    19  Hyatt Regency Dubai Hotel Al Khaleej Road, Dei...   +971 4 209 6912   
    20  Palm Jumeirah Dukes Dubai Oceana, Dubai United...   +971 4 455 1111   
    21  Twin Towers 3rd Flr Baniyas Rd, Dubai United A...   +971 4 227 7669   
    22  Hyatt Regency Dubai Creek Heights Dubai Health...   +971 4 553 1214   
    23  The Dubai Mall Second Floor Food Court, Dubai ...   +971 4 388 2382   
    24  Al Attar Center, Dubai 318-836 United Arab Emi...  +971 50 678 0096   
    25  No.1, Palm Jumeirah FIVE Palm Jumeirah, Dubai ...   +971 4 455 9989   
    26  Four Points by Sheraton Sheikh Zayed Road, Dub...   +971 4 316 9726   
    27  Sheikh Zayed Road Four Points by Sheraton, Dub...  +971 56 414 2213   
    28  Dubai Mall, Fountain Entrance, Dubai United Ar...   +971 4 330 5103   
    29  Le Meridien Dubai Airport Road, Dubai 10001 Un...   +971 4 702 2455   
    30  Restaurant village Four Seasons Hotel, Jumeira...   +971 4 333 8025   
    31  3 Sheikh Zayed Road 5th Floor, Sheraton Grand ...   +971 4 333 3055   
    32  DMCC Plot No. 2-27, Al Thanyah Taj Jumeirah La...   +971 4 574 1111   
    33  Dubai, United Arab Emirates, Dubai 9255 United...   +971 4 814 5555   
    34  Fairmont The Palm Palm Jumeirah, Dubai 72413 U...   +971 4 457 3457   
    35  Umm Suqeim Road Al Barsha 2, Dubai 120730 Unit...  +971 58 128 2886   
    36  Al Multaqa Street City Walk, Dubai 414433 Unit...   +971 4 403 3111   
    
                                                  Website  \
    0                                    http://folly.ae/   
    1                      http://www.asilrestaurant.com/   
    2   http://www.diningdfc.com/Restaurant-details/24...   
    3   http://www.dubaiintlhotels.com/dining/ahlan-lo...   
    4   http://fivehotelsandresorts.com/dine-drink-dan...   
    5                    http://www.puranidillidubai.com/   
    6   http://www.livelaville.com/dining/Grapeskin/in...   
    7   http://jumeirahvillage.fivehotelsandresorts.co...   
    8                        http://www.doorsdubai.com/en   
    9   http://www.movenpick.com/en/middle-east/uae/du...   
    10                          http://www.dxbmarine.com/   
    11                      http://www.minabrasserie.com/   
    12  http://www.livelaville.com/dining/Graze/index....   
    13  http://www.meydanhotels.com/babalshams/dining.htm   
    14                                    http://soul.st/   
    15                       http://www.bebemosdubai.com/   
    16  https://www.hyattrestaurants.com/en/dining/uae...   
    17                       http://tribesrestaurant.com/   
    18                           https://sushinations.ae/   
    19  http://www.hyattrestaurants.com/en/dining/uae/...   
    20                 https://www.dukesdubai.com/khyber/   
    21                   http://www.danialrestaurant.com/   
    22  http://www.hyattrestaurants.com/en/dining/uae/...   
    23                     http://www.thegrilllshack.com/   
    24                             http://amritsruae.com/   
    25  http://fivehotelsandresorts.com/dine-drink-dan...   
    26    http://www.puranidillidubai.com/sheikhzayedroad   
    27                      http://www.level43lounge.com/   
    28                         http://www.blacktapme.com/   
    29                    http://www.beefbistrodubai.com/   
    30                        http://www.verde-dubai.com/   
    31                                http://nidodxb.com/   
    32  http://www.tajhotels.com/en-in/taj/taj-jumeira...   
    33                        http://www.kinaradubai.com/   
    34  http://www.fairmont.com/palm-dubai/dining/litt...   
    35        http://dubaifishhutrestaurant.com/index.php   
    36                      http://www.chivallaville.com/   
    
                                                 Menu Url      Cost  \
    0                              https://folly.ae/food/      $$$$   
    1   https://www.asilrestaurant.com/downloads/alaca...      $$$$   
    2   https://a62be139-804e-413a-9f69-68bbb2441a0f.f...  $$ - $$$   
    3   https://www.dubaiintlhotels.com/dining/ahlan-l...  $$ - $$$   
    4   https://www.fivehotelsandresorts.com/media/503...  $$ - $$$   
    5          https://www.puranidillidubai.com/our-menus  $$ - $$$   
    6   https://livelaville.com/dining/Grapeskin/index...  $$ - $$$   
    7                           https://five.kitchen/tbc/  $$ - $$$   
    8                 https://www.doorsdubai.com/en/menu/      $$$$   
    9   https://www.movenpick.com/fileadmin/files/Hote...  $$ - $$$   
    10                                  Error in Menu Url  $$ - $$$   
    11                 http://www.minabrasserie.com/#menu      $$$$   
    12  https://www.livelaville.com/dining/graze/index...  $$ - $$$   
    13  https://babalshams.com/sites/default/files/202...  $$ - $$$   
    14                           https://five.kitchen/ss/  $$ - $$$   
    15             https://www.bebemosdubai.com/our-menus  $$ - $$$   
    16  https://www.hyattrestaurants.com/en/dining/uae...      $$$$   
    17  https://deliveroo.ae/menu/dubai/al-barsha-1/tr...  $$ - $$$   
    18             http://order.chatfood.io/sushi-nations  $$ - $$$   
    19  https://www.hyattrestaurants.com/en/dining/uae...      $$$$   
    20                                  Error in Menu Url  $$ - $$$   
    21                                  Error in Menu Url  $$ - $$$   
    22  https://www.hyattrestaurants.com/en/dining/uae...  $$ - $$$   
    23  http://www.thegrilllshack.com/wp-content/uploa...  $$ - $$$   
    24                http://www.amritsruae.com/menu.html         $   
    25                           https://five.kitchen/ms/      $$$$   
    26         https://www.puranidillidubai.com/our-menus  $$ - $$$   
    27            https://www.level43lounge.com/our-menus  $$ - $$$   
    28       https://www.facebook.com/BlackTapDubai/menu/  $$ - $$$   
    29          https://www.beefbistrodubai.com/our-menus  $$ - $$$   
    30                 http://verde-dubai.com/en_en/menu/      $$$$   
    31                                  Error in Menu Url  $$ - $$$   
    32  https://tajhotels-my.sharepoint.com/:b:/p/denn...      $$$$   
    33                                  Error in Menu Url      $$$$   
    34  http://palmdining.com/uploads/little-miss-indi...      $$$$   
    35        https://www.dubaifishhutrestaurant.com/menu         $   
    36   https://livelaville.com/dining/chival/index.aspx  $$ - $$$   
    
                                            Description  Rating  Reviews  \
    0   International Vegetarian Friendly Vegan Options     4.5      291   
    1                         Lebanese Moroccan Turkish     5.0      233   
    2        Mediterranean European Vegetarian Friendly     5.0      248   
    3             Bar International Vegetarian Friendly     5.0      737   
    4     European Central European Vegetarian Friendly     5.0     1152   
    5          Indian Vegetarian Friendly Vegan Options     5.0     1396   
    6                             Bar European Wine Bar     4.5      111   
    7   International Vegetarian Friendly Vegan Options     5.0      437   
    8                  Steakhouse Seafood International     5.0     1372   
    9                             Bar International Pub     5.0     1105   
    10                                Bar Seafood Grill     5.0      558   
    11                         French American European     5.0      291   
    12          Steakhouse European Vegetarian Friendly     4.5      106   
    13                       Lebanese Bar Mediterranean     5.0     1229   
    14                        Mexican Bar International     5.0      457   
    15              Spanish Catalan Vegetarian Friendly     5.0      272   
    16       Lebanese Vegetarian Friendly Vegan Options     5.0      367   
    17                 Steakhouse African International     5.0      839   
    18                           Japanese Seafood Sushi     4.5      180   
    19                International Mediterranean Sushi     5.0     3074   
    20         Indian Vegetarian Friendly Vegan Options     5.0      555   
    21                    Middle Eastern Persian Arabic     5.0      370   
    22            Bar Vegetarian Friendly Vegan Options     5.0      402   
    23                     American Steakhouse Barbecue     5.0      518   
    24                 Indian Asian Vegetarian Friendly     4.5       64   
    25             Chinese Shanghai Vegetarian Friendly     5.0     1235   
    26                 Indian Asian Vegetarian Friendly     5.0      223   
    27                    Bar Sushi Vegetarian Friendly     4.5     1619   
    28                                         American     5.0       96   
    29             Steakhouse Halal Gluten Free Options     5.0      683   
    30                                  French European     4.5       45   
    31                      Latin Mediterranean Spanish     5.0      230   
    32                       Indian Vegan Options Halal     5.0       86   
    33                 Indian Asian Vegetarian Friendly     5.0      210   
    34                 Indian Asian Vegetarian Friendly     5.0      604   
    35          International Vegetarian Friendly Halal     5.0      729   
    36  International Mediterranean Vegetarian Friendly     4.5      125   
    
                                                 Features   Order      lat  \
    0   Reservations, Outdoor Seating, Private Dining,...    #316  25.1339   
    1   Takeout, Reservations, Outdoor Seating, Seatin...      #1  25.0806   
    2                                         No Features      #2  25.2315   
    3                                         No Features      #4  25.2532   
    4                                         No Features      #5  25.1043   
    5                                         No Features      #8  25.2481   
    6                                         No Features    #397  25.2083   
    7                                         No Features      #9  25.1043   
    8   Reservations, Outdoor Seating, Private Dining,...     #10  25.2569   
    9                                         No Features     #11  25.0658   
    10                                        No Features     #12  25.2338   
    11  Reservations, Outdoor Seating, Seating, Serves...     #13  25.2126   
    12                                        No Features    #467  25.2083   
    13                                        No Features     #14  24.8168   
    14  Reservations, Outdoor Seating, Seating, Parkin...     #15  25.0463   
    15                                        No Features     #17  25.2492   
    16  Outdoor Seating, Seating, Parking Available, V...     #18  25.2288   
    17  Takeout, Reservations, Outdoor Seating, Seatin...     #19  25.1988   
    18                                        No Features    #838  25.2216   
    19  Reservations, Buffet, Seating, Parking Availab...     #20  25.2789   
    20                                        No Features     #21  25.1114   
    21                                        No Features     #22  25.2663   
    22                                        No Features     #23  25.2344   
    23                                        No Features     #24  25.1988   
    24                                        No Features    #778  25.2479   
    25  Reservations, Outdoor Seating, Private Dining,...     #25  25.1043   
    26  Takeout, Reservations, Seating, Parking Availa...     #26   25.214   
    27  Outdoor Seating, Seating, Parking Available, V...     #27   25.214   
    28                                        No Features     #28  25.1952   
    29  Reservations, Outdoor Seating, Seating, Parkin...     #29  25.2492   
    30                                        No Features  #1,077  25.2024   
    31                                        No Features     #30  25.2295   
    32                                        No Features     #31  25.0805   
    33  Reservations, Outdoor Seating, Private Dining,...     #32  25.2048   
    34                                        No Features     #33  25.1108   
    35                                        No Features     #34  25.1103   
    36                                        No Features    #250  25.2083   
    
            lng  
    0   55.1848  
    1   55.1355  
    2    55.347  
    3   55.3657  
    4   55.1488  
    5   55.2867  
    6   55.2606  
    7   55.1488  
    8   55.3121  
    9   55.1381  
    10  55.2655  
    11  55.2824  
    12  55.2606  
    13  55.2313  
    14   55.203  
    15  55.3471  
    16  55.3268  
    17  55.2796  
    18  55.2808  
    19  55.3045  
    20  55.1372  
    21  55.3088  
    22   55.324  
    23  55.2796  
    24  55.3005  
    25  55.1488  
    26  55.2761  
    27  55.2761  
    28  55.2752  
    29  55.3471  
    30  55.2397  
    31  55.2867  
    32  55.1542  
    33  55.2708  
    34  55.1399  
    35  55.2206  
    36  55.2606  
    


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Title</th>
      <th>Link</th>
      <th>Location</th>
      <th>Telephone</th>
      <th>Website</th>
      <th>Menu Url</th>
      <th>Cost</th>
      <th>Description</th>
      <th>Rating</th>
      <th>Reviews</th>
      <th>Features</th>
      <th>Order</th>
      <th>lat</th>
      <th>lng</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>SponsoredFolly by Nick &amp; Scott</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Unit 27, Souk Madinat Jumeriah, Dubai United A...</td>
      <td>+971 4 430 8535</td>
      <td>http://folly.ae/</td>
      <td>https://folly.ae/food/</td>
      <td>$$$$</td>
      <td>International Vegetarian Friendly Vegan Options</td>
      <td>4.5</td>
      <td>291</td>
      <td>Reservations, Outdoor Seating, Private Dining,...</td>
      <td>#316</td>
      <td>25.1339</td>
      <td>55.1848</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1. Asil Restaurant</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Jumeirah Beach Residence - The Walk Ground Flo...</td>
      <td>+971 52 160 0333</td>
      <td>http://www.asilrestaurant.com/</td>
      <td>https://www.asilrestaurant.com/downloads/alaca...</td>
      <td>$$$$</td>
      <td>Lebanese Moroccan Turkish</td>
      <td>5.0</td>
      <td>233</td>
      <td>Takeout, Reservations, Outdoor Seating, Seatin...</td>
      <td>#1</td>
      <td>25.0806</td>
      <td>55.1355</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2. MezzaLuna</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Lobby Level, Intercontinental Residence Suites...</td>
      <td>+971 4 701 1128</td>
      <td>http://www.diningdfc.com/Restaurant-details/24...</td>
      <td>https://a62be139-804e-413a-9f69-68bbb2441a0f.f...</td>
      <td>$$ - $$$</td>
      <td>Mediterranean European Vegetarian Friendly</td>
      <td>5.0</td>
      <td>248</td>
      <td>No Features</td>
      <td>#2</td>
      <td>25.2315</td>
      <td>55.347</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3. Cadiz - Ahlan Lounge @ Gate B26</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Terminal 3, Concourse B, near Gate B26. Dubai ...</td>
      <td>+971 4 505 2000</td>
      <td>http://www.dubaiintlhotels.com/dining/ahlan-lo...</td>
      <td>https://www.dubaiintlhotels.com/dining/ahlan-l...</td>
      <td>$$ - $$$</td>
      <td>Bar International Vegetarian Friendly</td>
      <td>5.0</td>
      <td>737</td>
      <td>No Features</td>
      <td>#4</td>
      <td>25.2532</td>
      <td>55.3657</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4. BLVD on One</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>No 1, Palm Jumeirah FIVE Palm Jumeirah, Dubai ...</td>
      <td>+971 4 455 9989</td>
      <td>http://fivehotelsandresorts.com/dine-drink-dan...</td>
      <td>https://www.fivehotelsandresorts.com/media/503...</td>
      <td>$$ - $$$</td>
      <td>European Central European Vegetarian Friendly</td>
      <td>5.0</td>
      <td>1152</td>
      <td>No Features</td>
      <td>#5</td>
      <td>25.1043</td>
      <td>55.1488</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5. Purani Dilli Dubai</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Mankhool, Street 4C, Bur Dubai, Dubai Ground F...</td>
      <td>+971 50 211 6816</td>
      <td>http://www.puranidillidubai.com/</td>
      <td>https://www.puranidillidubai.com/our-menus</td>
      <td>$$ - $$$</td>
      <td>Indian Vegetarian Friendly Vegan Options</td>
      <td>5.0</td>
      <td>1396</td>
      <td>No Features</td>
      <td>#8</td>
      <td>25.2481</td>
      <td>55.2867</td>
    </tr>
    <tr>
      <th>6</th>
      <td>SponsoredGrapeskin Grape Bar and Kitchen</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Al Multaqa Street La Ville Hotel &amp; Suites City...</td>
      <td>+971 4 403 3111</td>
      <td>http://www.livelaville.com/dining/Grapeskin/in...</td>
      <td>https://livelaville.com/dining/Grapeskin/index...</td>
      <td>$$ - $$$</td>
      <td>Bar European Wine Bar</td>
      <td>4.5</td>
      <td>111</td>
      <td>No Features</td>
      <td>#397</td>
      <td>25.2083</td>
      <td>55.2606</td>
    </tr>
    <tr>
      <th>7</th>
      <td>6. Trattoria By Cinque</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>District 14, Street 1, Jumeirah Village Circle...</td>
      <td>+971 4 455 9989</td>
      <td>http://jumeirahvillage.fivehotelsandresorts.co...</td>
      <td>https://five.kitchen/tbc/</td>
      <td>$$ - $$$</td>
      <td>International Vegetarian Friendly Vegan Options</td>
      <td>5.0</td>
      <td>437</td>
      <td>No Features</td>
      <td>#9</td>
      <td>25.1043</td>
      <td>55.1488</td>
    </tr>
    <tr>
      <th>8</th>
      <td>7. Doors Freestyle Grill</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>8/5 - 314 Al Seef St, Dubai United Arab Emirates</td>
      <td>+971 4 204 9299</td>
      <td>http://www.doorsdubai.com/en</td>
      <td>https://www.doorsdubai.com/en/menu/</td>
      <td>$$$$</td>
      <td>Steakhouse Seafood International</td>
      <td>5.0</td>
      <td>1372</td>
      <td>Reservations, Outdoor Seating, Private Dining,...</td>
      <td>#10</td>
      <td>25.2569</td>
      <td>55.3121</td>
    </tr>
    <tr>
      <th>9</th>
      <td>8. Urban Bar &amp; Kitchen - ubk</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Cluster A, Jumeriah Lakes Towers Movenpick Hot...</td>
      <td>+971 4 438 0000</td>
      <td>http://www.movenpick.com/en/middle-east/uae/du...</td>
      <td>https://www.movenpick.com/fileadmin/files/Hote...</td>
      <td>$$ - $$$</td>
      <td>Bar International Pub</td>
      <td>5.0</td>
      <td>1105</td>
      <td>No Features</td>
      <td>#11</td>
      <td>25.0658</td>
      <td>55.1381</td>
    </tr>
    <tr>
      <th>10</th>
      <td>9. Barefoot Lounge</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Jumeirah 1 Opp Grand Jumeirah Mosque, Dubai 51...</td>
      <td>+971 4 346 1111</td>
      <td>http://www.dxbmarine.com/</td>
      <td>Error in Menu Url</td>
      <td>$$ - $$$</td>
      <td>Bar Seafood Grill</td>
      <td>5.0</td>
      <td>558</td>
      <td>No Features</td>
      <td>#12</td>
      <td>25.2338</td>
      <td>55.2655</td>
    </tr>
    <tr>
      <th>11</th>
      <td>10. Mina Brasserie</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Four Seasons Hotel DIFC, Podium Level, Buildin...</td>
      <td>+971 4 506 0100</td>
      <td>http://www.minabrasserie.com/</td>
      <td>http://www.minabrasserie.com/#menu</td>
      <td>$$$$</td>
      <td>French American European</td>
      <td>5.0</td>
      <td>291</td>
      <td>Reservations, Outdoor Seating, Seating, Serves...</td>
      <td>#13</td>
      <td>25.2126</td>
      <td>55.2824</td>
    </tr>
    <tr>
      <th>12</th>
      <td>SponsoredGraze Gastro Grill</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Al Multaqa Street La Ville Hotel &amp; Suites, Dub...</td>
      <td>+971 4 403 3111</td>
      <td>http://www.livelaville.com/dining/Graze/index....</td>
      <td>https://www.livelaville.com/dining/graze/index...</td>
      <td>$$ - $$$</td>
      <td>Steakhouse European Vegetarian Friendly</td>
      <td>4.5</td>
      <td>106</td>
      <td>No Features</td>
      <td>#467</td>
      <td>25.2083</td>
      <td>55.2606</td>
    </tr>
    <tr>
      <th>13</th>
      <td>11. Al Sarab Rooftop Lounge</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Al Qudra Rd Bab Al Shams Desert Resort &amp; Spa, ...</td>
      <td>+971 4 809 6100</td>
      <td>http://www.meydanhotels.com/babalshams/dining.htm</td>
      <td>https://babalshams.com/sites/default/files/202...</td>
      <td>$$ - $$$</td>
      <td>Lebanese Bar Mediterranean</td>
      <td>5.0</td>
      <td>1229</td>
      <td>No Features</td>
      <td>#14</td>
      <td>24.8168</td>
      <td>55.2313</td>
    </tr>
    <tr>
      <th>14</th>
      <td>12. Soul Street</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>District 14, Street 1, Jumeirah Village Circle...</td>
      <td>+971 4 455 9989</td>
      <td>http://soul.st/</td>
      <td>https://five.kitchen/ss/</td>
      <td>$$ - $$$</td>
      <td>Mexican Bar International</td>
      <td>5.0</td>
      <td>457</td>
      <td>Reservations, Outdoor Seating, Seating, Parkin...</td>
      <td>#15</td>
      <td>25.0463</td>
      <td>55.203</td>
    </tr>
    <tr>
      <th>15</th>
      <td>13. Bebemos</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Airport Road Le Méridien Dubai Hotel &amp; Confere...</td>
      <td>+971 4 702 2455</td>
      <td>http://www.bebemosdubai.com/</td>
      <td>https://www.bebemosdubai.com/our-menus</td>
      <td>$$ - $$$</td>
      <td>Spanish Catalan Vegetarian Friendly</td>
      <td>5.0</td>
      <td>272</td>
      <td>No Features</td>
      <td>#17</td>
      <td>25.2492</td>
      <td>55.3471</td>
    </tr>
    <tr>
      <th>16</th>
      <td>14. Awtar</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Sheikh Rashid Road Grand Hyatt Dubai, Dubai 79...</td>
      <td>+971 4 317 2221</td>
      <td>https://www.hyattrestaurants.com/en/dining/uae...</td>
      <td>https://www.hyattrestaurants.com/en/dining/uae...</td>
      <td>$$$$</td>
      <td>Lebanese Vegetarian Friendly Vegan Options</td>
      <td>5.0</td>
      <td>367</td>
      <td>Outdoor Seating, Seating, Parking Available, V...</td>
      <td>#18</td>
      <td>25.2288</td>
      <td>55.3268</td>
    </tr>
    <tr>
      <th>17</th>
      <td>15. Tribes Carnivore</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Shikh Mohamed bin rashid Blvd Dubai Mall, Duba...</td>
      <td>+971 4 226 4974</td>
      <td>http://tribesrestaurant.com/</td>
      <td>https://deliveroo.ae/menu/dubai/al-barsha-1/tr...</td>
      <td>$$ - $$$</td>
      <td>Steakhouse African International</td>
      <td>5.0</td>
      <td>839</td>
      <td>Takeout, Reservations, Outdoor Seating, Seatin...</td>
      <td>#19</td>
      <td>25.1988</td>
      <td>55.2796</td>
    </tr>
    <tr>
      <th>18</th>
      <td>SponsoredSushi Nations</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Sheikh Zayed Rd Latifa Tower, Shop No.L2, Grou...</td>
      <td>+971 56 188 8522</td>
      <td>https://sushinations.ae/</td>
      <td>http://order.chatfood.io/sushi-nations</td>
      <td>$$ - $$$</td>
      <td>Japanese Seafood Sushi</td>
      <td>4.5</td>
      <td>180</td>
      <td>No Features</td>
      <td>#838</td>
      <td>25.2216</td>
      <td>55.2808</td>
    </tr>
    <tr>
      <th>19</th>
      <td>16. Al Dawaar Revolving Restaurant</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Hyatt Regency Dubai Hotel Al Khaleej Road, Dei...</td>
      <td>+971 4 209 6912</td>
      <td>http://www.hyattrestaurants.com/en/dining/uae/...</td>
      <td>https://www.hyattrestaurants.com/en/dining/uae...</td>
      <td>$$$$</td>
      <td>International Mediterranean Sushi</td>
      <td>5.0</td>
      <td>3074</td>
      <td>Reservations, Buffet, Seating, Parking Availab...</td>
      <td>#20</td>
      <td>25.2789</td>
      <td>55.3045</td>
    </tr>
    <tr>
      <th>20</th>
      <td>17. Khyber</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Palm Jumeirah Dukes Dubai Oceana, Dubai United...</td>
      <td>+971 4 455 1111</td>
      <td>https://www.dukesdubai.com/khyber/</td>
      <td>Error in Menu Url</td>
      <td>$$ - $$$</td>
      <td>Indian Vegetarian Friendly Vegan Options</td>
      <td>5.0</td>
      <td>555</td>
      <td>No Features</td>
      <td>#21</td>
      <td>25.1114</td>
      <td>55.1372</td>
    </tr>
    <tr>
      <th>21</th>
      <td>18. Danial Restaurant</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Twin Towers 3rd Flr Baniyas Rd, Dubai United A...</td>
      <td>+971 4 227 7669</td>
      <td>http://www.danialrestaurant.com/</td>
      <td>Error in Menu Url</td>
      <td>$$ - $$$</td>
      <td>Middle Eastern Persian Arabic</td>
      <td>5.0</td>
      <td>370</td>
      <td>No Features</td>
      <td>#22</td>
      <td>25.2663</td>
      <td>55.3088</td>
    </tr>
    <tr>
      <th>22</th>
      <td>19. Eve Penthouse &amp; Lounge</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Hyatt Regency Dubai Creek Heights Dubai Health...</td>
      <td>+971 4 553 1214</td>
      <td>http://www.hyattrestaurants.com/en/dining/uae/...</td>
      <td>https://www.hyattrestaurants.com/en/dining/uae...</td>
      <td>$$ - $$$</td>
      <td>Bar Vegetarian Friendly Vegan Options</td>
      <td>5.0</td>
      <td>402</td>
      <td>No Features</td>
      <td>#23</td>
      <td>25.2344</td>
      <td>55.324</td>
    </tr>
    <tr>
      <th>23</th>
      <td>20. The Grill Shack</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>The Dubai Mall Second Floor Food Court, Dubai ...</td>
      <td>+971 4 388 2382</td>
      <td>http://www.thegrilllshack.com/</td>
      <td>http://www.thegrilllshack.com/wp-content/uploa...</td>
      <td>$$ - $$$</td>
      <td>American Steakhouse Barbecue</td>
      <td>5.0</td>
      <td>518</td>
      <td>No Features</td>
      <td>#24</td>
      <td>25.1988</td>
      <td>55.2796</td>
    </tr>
    <tr>
      <th>24</th>
      <td>SponsoredAmritsr Restaurant</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Al Attar Center, Dubai 318-836 United Arab Emi...</td>
      <td>+971 50 678 0096</td>
      <td>http://amritsruae.com/</td>
      <td>http://www.amritsruae.com/menu.html</td>
      <td>$</td>
      <td>Indian Asian Vegetarian Friendly</td>
      <td>4.5</td>
      <td>64</td>
      <td>No Features</td>
      <td>#778</td>
      <td>25.2479</td>
      <td>55.3005</td>
    </tr>
    <tr>
      <th>25</th>
      <td>21. Maiden Shanghai</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>No.1, Palm Jumeirah FIVE Palm Jumeirah, Dubai ...</td>
      <td>+971 4 455 9989</td>
      <td>http://fivehotelsandresorts.com/dine-drink-dan...</td>
      <td>https://five.kitchen/ms/</td>
      <td>$$$$</td>
      <td>Chinese Shanghai Vegetarian Friendly</td>
      <td>5.0</td>
      <td>1235</td>
      <td>Reservations, Outdoor Seating, Private Dining,...</td>
      <td>#25</td>
      <td>25.1043</td>
      <td>55.1488</td>
    </tr>
    <tr>
      <th>26</th>
      <td>22. Purani Dilli Sheikh Zayed Road</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Four Points by Sheraton Sheikh Zayed Road, Dub...</td>
      <td>+971 4 316 9726</td>
      <td>http://www.puranidillidubai.com/sheikhzayedroad</td>
      <td>https://www.puranidillidubai.com/our-menus</td>
      <td>$$ - $$$</td>
      <td>Indian Asian Vegetarian Friendly</td>
      <td>5.0</td>
      <td>223</td>
      <td>Takeout, Reservations, Seating, Parking Availa...</td>
      <td>#26</td>
      <td>25.214</td>
      <td>55.2761</td>
    </tr>
    <tr>
      <th>27</th>
      <td>23. Level 43 Sky Lounge</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Sheikh Zayed Road Four Points by Sheraton, Dub...</td>
      <td>+971 56 414 2213</td>
      <td>http://www.level43lounge.com/</td>
      <td>https://www.level43lounge.com/our-menus</td>
      <td>$$ - $$$</td>
      <td>Bar Sushi Vegetarian Friendly</td>
      <td>4.5</td>
      <td>1619</td>
      <td>Outdoor Seating, Seating, Parking Available, V...</td>
      <td>#27</td>
      <td>25.214</td>
      <td>55.2761</td>
    </tr>
    <tr>
      <th>28</th>
      <td>24. Black Tap Craft Burgers &amp; Shakes Dubai Mall</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Dubai Mall, Fountain Entrance, Dubai United Ar...</td>
      <td>+971 4 330 5103</td>
      <td>http://www.blacktapme.com/</td>
      <td>https://www.facebook.com/BlackTapDubai/menu/</td>
      <td>$$ - $$$</td>
      <td>American</td>
      <td>5.0</td>
      <td>96</td>
      <td>No Features</td>
      <td>#28</td>
      <td>25.1952</td>
      <td>55.2752</td>
    </tr>
    <tr>
      <th>29</th>
      <td>25. Beef Bistro</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Le Meridien Dubai Airport Road, Dubai 10001 Un...</td>
      <td>+971 4 702 2455</td>
      <td>http://www.beefbistrodubai.com/</td>
      <td>https://www.beefbistrodubai.com/our-menus</td>
      <td>$$ - $$$</td>
      <td>Steakhouse Halal Gluten Free Options</td>
      <td>5.0</td>
      <td>683</td>
      <td>Reservations, Outdoor Seating, Seating, Parkin...</td>
      <td>#29</td>
      <td>25.2492</td>
      <td>55.3471</td>
    </tr>
    <tr>
      <th>30</th>
      <td>SponsoredVerde Dubai</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Restaurant village Four Seasons Hotel, Jumeira...</td>
      <td>+971 4 333 8025</td>
      <td>http://www.verde-dubai.com/</td>
      <td>http://verde-dubai.com/en_en/menu/</td>
      <td>$$$$</td>
      <td>French European</td>
      <td>4.5</td>
      <td>45</td>
      <td>No Features</td>
      <td>#1,077</td>
      <td>25.2024</td>
      <td>55.2397</td>
    </tr>
    <tr>
      <th>31</th>
      <td>26. Nido Tapas Restaurant &amp; Bar</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>3 Sheikh Zayed Road 5th Floor, Sheraton Grand ...</td>
      <td>+971 4 333 3055</td>
      <td>http://nidodxb.com/</td>
      <td>Error in Menu Url</td>
      <td>$$ - $$$</td>
      <td>Latin Mediterranean Spanish</td>
      <td>5.0</td>
      <td>230</td>
      <td>No Features</td>
      <td>#30</td>
      <td>25.2295</td>
      <td>55.2867</td>
    </tr>
    <tr>
      <th>32</th>
      <td>27. Shamiana</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>DMCC Plot No. 2-27, Al Thanyah Taj Jumeirah La...</td>
      <td>+971 4 574 1111</td>
      <td>http://www.tajhotels.com/en-in/taj/taj-jumeira...</td>
      <td>https://tajhotels-my.sharepoint.com/:b:/p/denn...</td>
      <td>$$$$</td>
      <td>Indian Vegan Options Halal</td>
      <td>5.0</td>
      <td>86</td>
      <td>No Features</td>
      <td>#31</td>
      <td>25.0805</td>
      <td>55.1542</td>
    </tr>
    <tr>
      <th>33</th>
      <td>28. Kinara by Vikas Khanna</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Dubai, United Arab Emirates, Dubai 9255 United...</td>
      <td>+971 4 814 5555</td>
      <td>http://www.kinaradubai.com/</td>
      <td>Error in Menu Url</td>
      <td>$$$$</td>
      <td>Indian Asian Vegetarian Friendly</td>
      <td>5.0</td>
      <td>210</td>
      <td>Reservations, Outdoor Seating, Private Dining,...</td>
      <td>#32</td>
      <td>25.2048</td>
      <td>55.2708</td>
    </tr>
    <tr>
      <th>34</th>
      <td>29. Little Miss India</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Fairmont The Palm Palm Jumeirah, Dubai 72413 U...</td>
      <td>+971 4 457 3457</td>
      <td>http://www.fairmont.com/palm-dubai/dining/litt...</td>
      <td>http://palmdining.com/uploads/little-miss-indi...</td>
      <td>$$$$</td>
      <td>Indian Asian Vegetarian Friendly</td>
      <td>5.0</td>
      <td>604</td>
      <td>No Features</td>
      <td>#33</td>
      <td>25.1108</td>
      <td>55.1399</td>
    </tr>
    <tr>
      <th>35</th>
      <td>30. Fish Hut Asmak Al Sultan Seafood Restaurant</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Umm Suqeim Road Al Barsha 2, Dubai 120730 Unit...</td>
      <td>+971 58 128 2886</td>
      <td>http://dubaifishhutrestaurant.com/index.php</td>
      <td>https://www.dubaifishhutrestaurant.com/menu</td>
      <td>$</td>
      <td>International Vegetarian Friendly Halal</td>
      <td>5.0</td>
      <td>729</td>
      <td>No Features</td>
      <td>#34</td>
      <td>25.1103</td>
      <td>55.2206</td>
    </tr>
    <tr>
      <th>36</th>
      <td>SponsoredChival</td>
      <td>https://www.tripadvisor.com//Restaurant_Review...</td>
      <td>Al Multaqa Street City Walk, Dubai 414433 Unit...</td>
      <td>+971 4 403 3111</td>
      <td>http://www.chivallaville.com/</td>
      <td>https://livelaville.com/dining/chival/index.aspx</td>
      <td>$$ - $$$</td>
      <td>International Mediterranean Vegetarian Friendly</td>
      <td>4.5</td>
      <td>125</td>
      <td>No Features</td>
      <td>#250</td>
      <td>25.2083</td>
      <td>55.2606</td>
    </tr>
  </tbody>
</table>
</div>




```python
dubai_lat=25.2048
dubai_lng=55.2708
```


```python
restaurant_map = folium.Map(location=[dubai_lat, dubai_lng], zoom_start=15)
restaurant_map
```




<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><span style="color:#565656">Make this Notebook Trusted to load map: File -> Trust Notebook</span><iframe src="about:blank" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" data-html=PCFET0NUWVBFIGh0bWw+CjxoZWFkPiAgICAKICAgIDxtZXRhIGh0dHAtZXF1aXY9ImNvbnRlbnQtdHlwZSIgY29udGVudD0idGV4dC9odG1sOyBjaGFyc2V0PVVURi04IiAvPgogICAgCiAgICAgICAgPHNjcmlwdD4KICAgICAgICAgICAgTF9OT19UT1VDSCA9IGZhbHNlOwogICAgICAgICAgICBMX0RJU0FCTEVfM0QgPSBmYWxzZTsKICAgICAgICA8L3NjcmlwdD4KICAgIAogICAgPHNjcmlwdCBzcmM9Imh0dHBzOi8vY2RuLmpzZGVsaXZyLm5ldC9ucG0vbGVhZmxldEAxLjYuMC9kaXN0L2xlYWZsZXQuanMiPjwvc2NyaXB0PgogICAgPHNjcmlwdCBzcmM9Imh0dHBzOi8vY29kZS5qcXVlcnkuY29tL2pxdWVyeS0xLjEyLjQubWluLmpzIj48L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL21heGNkbi5ib290c3RyYXBjZG4uY29tL2Jvb3RzdHJhcC8zLjIuMC9qcy9ib290c3RyYXAubWluLmpzIj48L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2NkbmpzLmNsb3VkZmxhcmUuY29tL2FqYXgvbGlicy9MZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy8yLjAuMi9sZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy5qcyI+PC9zY3JpcHQ+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vY2RuLmpzZGVsaXZyLm5ldC9ucG0vbGVhZmxldEAxLjYuMC9kaXN0L2xlYWZsZXQuY3NzIi8+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vbWF4Y2RuLmJvb3RzdHJhcGNkbi5jb20vYm9vdHN0cmFwLzMuMi4wL2Nzcy9ib290c3RyYXAubWluLmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL21heGNkbi5ib290c3RyYXBjZG4uY29tL2Jvb3RzdHJhcC8zLjIuMC9jc3MvYm9vdHN0cmFwLXRoZW1lLm1pbi5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9mb250LWF3ZXNvbWUvNC42LjMvY3NzL2ZvbnQtYXdlc29tZS5taW4uY3NzIi8+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vY2RuanMuY2xvdWRmbGFyZS5jb20vYWpheC9saWJzL0xlYWZsZXQuYXdlc29tZS1tYXJrZXJzLzIuMC4yL2xlYWZsZXQuYXdlc29tZS1tYXJrZXJzLmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL3Jhd2Nkbi5naXRoYWNrLmNvbS9weXRob24tdmlzdWFsaXphdGlvbi9mb2xpdW0vbWFzdGVyL2ZvbGl1bS90ZW1wbGF0ZXMvbGVhZmxldC5hd2Vzb21lLnJvdGF0ZS5jc3MiLz4KICAgIDxzdHlsZT5odG1sLCBib2R5IHt3aWR0aDogMTAwJTtoZWlnaHQ6IDEwMCU7bWFyZ2luOiAwO3BhZGRpbmc6IDA7fTwvc3R5bGU+CiAgICA8c3R5bGU+I21hcCB7cG9zaXRpb246YWJzb2x1dGU7dG9wOjA7Ym90dG9tOjA7cmlnaHQ6MDtsZWZ0OjA7fTwvc3R5bGU+CiAgICAKICAgICAgICAgICAgPG1ldGEgbmFtZT0idmlld3BvcnQiIGNvbnRlbnQ9IndpZHRoPWRldmljZS13aWR0aCwKICAgICAgICAgICAgICAgIGluaXRpYWwtc2NhbGU9MS4wLCBtYXhpbXVtLXNjYWxlPTEuMCwgdXNlci1zY2FsYWJsZT1ubyIgLz4KICAgICAgICAgICAgPHN0eWxlPgogICAgICAgICAgICAgICAgI21hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCB7CiAgICAgICAgICAgICAgICAgICAgcG9zaXRpb246IHJlbGF0aXZlOwogICAgICAgICAgICAgICAgICAgIHdpZHRoOiAxMDAuMCU7CiAgICAgICAgICAgICAgICAgICAgaGVpZ2h0OiAxMDAuMCU7CiAgICAgICAgICAgICAgICAgICAgbGVmdDogMC4wJTsKICAgICAgICAgICAgICAgICAgICB0b3A6IDAuMCU7CiAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgIDwvc3R5bGU+CiAgICAgICAgCjwvaGVhZD4KPGJvZHk+ICAgIAogICAgCiAgICAgICAgICAgIDxkaXYgY2xhc3M9ImZvbGl1bS1tYXAiIGlkPSJtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgiID48L2Rpdj4KICAgICAgICAKPC9ib2R5Pgo8c2NyaXB0PiAgICAKICAgIAogICAgICAgICAgICB2YXIgbWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4ID0gTC5tYXAoCiAgICAgICAgICAgICAgICAibWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4IiwKICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICBjZW50ZXI6IFsyNS4yMDQ4LCA1NS4yNzA4XSwKICAgICAgICAgICAgICAgICAgICBjcnM6IEwuQ1JTLkVQU0czODU3LAogICAgICAgICAgICAgICAgICAgIHpvb206IDE1LAogICAgICAgICAgICAgICAgICAgIHpvb21Db250cm9sOiB0cnVlLAogICAgICAgICAgICAgICAgICAgIHByZWZlckNhbnZhczogZmFsc2UsCiAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICk7CgogICAgICAgICAgICAKCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHRpbGVfbGF5ZXJfZmQyNzBhYTRkMWIzNDYyNjkyN2NjODZlNTg1NTYwYmUgPSBMLnRpbGVMYXllcigKICAgICAgICAgICAgICAgICJodHRwczovL3tzfS50aWxlLm9wZW5zdHJlZXRtYXAub3JnL3t6fS97eH0ve3l9LnBuZyIsCiAgICAgICAgICAgICAgICB7ImF0dHJpYnV0aW9uIjogIkRhdGEgYnkgXHUwMDI2Y29weTsgXHUwMDNjYSBocmVmPVwiaHR0cDovL29wZW5zdHJlZXRtYXAub3JnXCJcdTAwM2VPcGVuU3RyZWV0TWFwXHUwMDNjL2FcdTAwM2UsIHVuZGVyIFx1MDAzY2EgaHJlZj1cImh0dHA6Ly93d3cub3BlbnN0cmVldG1hcC5vcmcvY29weXJpZ2h0XCJcdTAwM2VPRGJMXHUwMDNjL2FcdTAwM2UuIiwgImRldGVjdFJldGluYSI6IGZhbHNlLCAibWF4TmF0aXZlWm9vbSI6IDE4LCAibWF4Wm9vbSI6IDE4LCAibWluWm9vbSI6IDAsICJub1dyYXAiOiBmYWxzZSwgIm9wYWNpdHkiOiAxLCAic3ViZG9tYWlucyI6ICJhYmMiLCAidG1zIjogZmFsc2V9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKPC9zY3JpcHQ+ onload="this.contentDocument.open();this.contentDocument.write(atob(this.getAttribute('data-html')));this.contentDocument.close();" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>




```python
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
```




<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><span style="color:#565656">Make this Notebook Trusted to load map: File -> Trust Notebook</span><iframe src="about:blank" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" data-html=PCFET0NUWVBFIGh0bWw+CjxoZWFkPiAgICAKICAgIDxtZXRhIGh0dHAtZXF1aXY9ImNvbnRlbnQtdHlwZSIgY29udGVudD0idGV4dC9odG1sOyBjaGFyc2V0PVVURi04IiAvPgogICAgCiAgICAgICAgPHNjcmlwdD4KICAgICAgICAgICAgTF9OT19UT1VDSCA9IGZhbHNlOwogICAgICAgICAgICBMX0RJU0FCTEVfM0QgPSBmYWxzZTsKICAgICAgICA8L3NjcmlwdD4KICAgIAogICAgPHNjcmlwdCBzcmM9Imh0dHBzOi8vY2RuLmpzZGVsaXZyLm5ldC9ucG0vbGVhZmxldEAxLjYuMC9kaXN0L2xlYWZsZXQuanMiPjwvc2NyaXB0PgogICAgPHNjcmlwdCBzcmM9Imh0dHBzOi8vY29kZS5qcXVlcnkuY29tL2pxdWVyeS0xLjEyLjQubWluLmpzIj48L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL21heGNkbi5ib290c3RyYXBjZG4uY29tL2Jvb3RzdHJhcC8zLjIuMC9qcy9ib290c3RyYXAubWluLmpzIj48L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2NkbmpzLmNsb3VkZmxhcmUuY29tL2FqYXgvbGlicy9MZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy8yLjAuMi9sZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy5qcyI+PC9zY3JpcHQ+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vY2RuLmpzZGVsaXZyLm5ldC9ucG0vbGVhZmxldEAxLjYuMC9kaXN0L2xlYWZsZXQuY3NzIi8+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vbWF4Y2RuLmJvb3RzdHJhcGNkbi5jb20vYm9vdHN0cmFwLzMuMi4wL2Nzcy9ib290c3RyYXAubWluLmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL21heGNkbi5ib290c3RyYXBjZG4uY29tL2Jvb3RzdHJhcC8zLjIuMC9jc3MvYm9vdHN0cmFwLXRoZW1lLm1pbi5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9mb250LWF3ZXNvbWUvNC42LjMvY3NzL2ZvbnQtYXdlc29tZS5taW4uY3NzIi8+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vY2RuanMuY2xvdWRmbGFyZS5jb20vYWpheC9saWJzL0xlYWZsZXQuYXdlc29tZS1tYXJrZXJzLzIuMC4yL2xlYWZsZXQuYXdlc29tZS1tYXJrZXJzLmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL3Jhd2Nkbi5naXRoYWNrLmNvbS9weXRob24tdmlzdWFsaXphdGlvbi9mb2xpdW0vbWFzdGVyL2ZvbGl1bS90ZW1wbGF0ZXMvbGVhZmxldC5hd2Vzb21lLnJvdGF0ZS5jc3MiLz4KICAgIDxzdHlsZT5odG1sLCBib2R5IHt3aWR0aDogMTAwJTtoZWlnaHQ6IDEwMCU7bWFyZ2luOiAwO3BhZGRpbmc6IDA7fTwvc3R5bGU+CiAgICA8c3R5bGU+I21hcCB7cG9zaXRpb246YWJzb2x1dGU7dG9wOjA7Ym90dG9tOjA7cmlnaHQ6MDtsZWZ0OjA7fTwvc3R5bGU+CiAgICAKICAgICAgICAgICAgPG1ldGEgbmFtZT0idmlld3BvcnQiIGNvbnRlbnQ9IndpZHRoPWRldmljZS13aWR0aCwKICAgICAgICAgICAgICAgIGluaXRpYWwtc2NhbGU9MS4wLCBtYXhpbXVtLXNjYWxlPTEuMCwgdXNlci1zY2FsYWJsZT1ubyIgLz4KICAgICAgICAgICAgPHN0eWxlPgogICAgICAgICAgICAgICAgI21hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCB7CiAgICAgICAgICAgICAgICAgICAgcG9zaXRpb246IHJlbGF0aXZlOwogICAgICAgICAgICAgICAgICAgIHdpZHRoOiAxMDAuMCU7CiAgICAgICAgICAgICAgICAgICAgaGVpZ2h0OiAxMDAuMCU7CiAgICAgICAgICAgICAgICAgICAgbGVmdDogMC4wJTsKICAgICAgICAgICAgICAgICAgICB0b3A6IDAuMCU7CiAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgIDwvc3R5bGU+CiAgICAgICAgCjwvaGVhZD4KPGJvZHk+ICAgIAogICAgCiAgICAgICAgICAgIDxkaXYgY2xhc3M9ImZvbGl1bS1tYXAiIGlkPSJtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgiID48L2Rpdj4KICAgICAgICAKPC9ib2R5Pgo8c2NyaXB0PiAgICAKICAgIAogICAgICAgICAgICB2YXIgbWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4ID0gTC5tYXAoCiAgICAgICAgICAgICAgICAibWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4IiwKICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICBjZW50ZXI6IFsyNS4yMDQ4LCA1NS4yNzA4XSwKICAgICAgICAgICAgICAgICAgICBjcnM6IEwuQ1JTLkVQU0czODU3LAogICAgICAgICAgICAgICAgICAgIHpvb206IDE1LAogICAgICAgICAgICAgICAgICAgIHpvb21Db250cm9sOiB0cnVlLAogICAgICAgICAgICAgICAgICAgIHByZWZlckNhbnZhczogZmFsc2UsCiAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICk7CgogICAgICAgICAgICAKCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHRpbGVfbGF5ZXJfZmQyNzBhYTRkMWIzNDYyNjkyN2NjODZlNTg1NTYwYmUgPSBMLnRpbGVMYXllcigKICAgICAgICAgICAgICAgICJodHRwczovL3tzfS50aWxlLm9wZW5zdHJlZXRtYXAub3JnL3t6fS97eH0ve3l9LnBuZyIsCiAgICAgICAgICAgICAgICB7ImF0dHJpYnV0aW9uIjogIkRhdGEgYnkgXHUwMDI2Y29weTsgXHUwMDNjYSBocmVmPVwiaHR0cDovL29wZW5zdHJlZXRtYXAub3JnXCJcdTAwM2VPcGVuU3RyZWV0TWFwXHUwMDNjL2FcdTAwM2UsIHVuZGVyIFx1MDAzY2EgaHJlZj1cImh0dHA6Ly93d3cub3BlbnN0cmVldG1hcC5vcmcvY29weXJpZ2h0XCJcdTAwM2VPRGJMXHUwMDNjL2FcdTAwM2UuIiwgImRldGVjdFJldGluYSI6IGZhbHNlLCAibWF4TmF0aXZlWm9vbSI6IDE4LCAibWF4Wm9vbSI6IDE4LCAibWluWm9vbSI6IDAsICJub1dyYXAiOiBmYWxzZSwgIm9wYWNpdHkiOiAxLCAic3ViZG9tYWlucyI6ICJhYmMiLCAidG1zIjogZmFsc2V9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl83OWM1ZDQ2NGI3MWQ0YjlhYTNhMjI5ZTNiMzE2ZjllYyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjEzMzg3NzcsIDU1LjE4NDc2MjVdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogImIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiYiIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogMC42NzQ5OTk5OTk5OTk5OTk5LCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF9iZTAyOGIzOGI2YWM0MTcyODMzYmY5MzlmZTUwNmQ3YyA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfNzgyN2JjNmM1ZDU0NDFiNDhmNWZkZTVjM2NiYzJhM2QgPSAkKGA8ZGl2IGlkPSJodG1sXzc4MjdiYzZjNWQ1NDQxYjQ4ZjVmZGU1YzNjYmMyYTNkIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogU3BvbnNvcmVkZm9sbHkgYnkgbmljayAmIHNjb3R0PGJyPlRlbGVwaG9uZTogKzk3MSA0IDQzMCA4NTM1PGJyPnVybDogaHR0cDovL2ZvbGx5LmFlLzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF9iZTAyOGIzOGI2YWM0MTcyODMzYmY5MzlmZTUwNmQ3Yy5zZXRDb250ZW50KGh0bWxfNzgyN2JjNmM1ZDU0NDFiNDhmNWZkZTVjM2NiYzJhM2QpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyXzc5YzVkNDY0YjcxZDRiOWFhM2EyMjllM2IzMTZmOWVjLmJpbmRQb3B1cChwb3B1cF9iZTAyOGIzOGI2YWM0MTcyODMzYmY5MzlmZTUwNmQ3YykKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfOTEyZjNhMjg5YmFkNDE2ZTgzZjgwNjExMjQzMDdjYzMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4wODA2MzYsIDU1LjEzNTUzMThdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogImIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiYiIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogMC43NSwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfMTI1YjZiZDQzZjk4NDMwZmI4NTliNTcyY2NmYmNkMTcgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sX2JlOGU0MDY5NWM3MjQxODdiMTMyZTgxNjk3OGQzMDE1ID0gJChgPGRpdiBpZD0iaHRtbF9iZThlNDA2OTVjNzI0MTg3YjEzMmU4MTY5NzhkMzAxNSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDEuIGFzaWwgcmVzdGF1cmFudDxicj5UZWxlcGhvbmU6ICs5NzEgNTIgMTYwIDAzMzM8YnI+dXJsOiBodHRwOi8vd3d3LmFzaWxyZXN0YXVyYW50LmNvbS88L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfMTI1YjZiZDQzZjk4NDMwZmI4NTliNTcyY2NmYmNkMTcuc2V0Q29udGVudChodG1sX2JlOGU0MDY5NWM3MjQxODdiMTMyZTgxNjk3OGQzMDE1KTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl85MTJmM2EyODliYWQ0MTZlODNmODA2MTEyNDMwN2NjMy5iaW5kUG9wdXAocG9wdXBfMTI1YjZiZDQzZjk4NDMwZmI4NTliNTcyY2NmYmNkMTcpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzc5OTQzOGFhM2NjZDRlNzdiOTRiNTI5N2FmNjc3MDVlID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMjMxNDk4MiwgNTUuMzQ2OTU1OV0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiYiIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJiIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiAwLjc1LCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF84NDI0OTNiYmUwZTE0NWYzODg3YzYxZTBkNjVlMzRkZiA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfMGIyZWVkNDE1Y2I1NGYyMGEzNGQ5NDA1Y2FkZDZmZDUgPSAkKGA8ZGl2IGlkPSJodG1sXzBiMmVlZDQxNWNiNTRmMjBhMzRkOTQwNWNhZGQ2ZmQ1IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogMi4gbWV6emFsdW5hPGJyPlRlbGVwaG9uZTogKzk3MSA0IDcwMSAxMTI4PGJyPnVybDogaHR0cDovL3d3dy5kaW5pbmdkZmMuY29tL1Jlc3RhdXJhbnQtZGV0YWlscy8yNC9NZXp6YUx1bmE8L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfODQyNDkzYmJlMGUxNDVmMzg4N2M2MWUwZDY1ZTM0ZGYuc2V0Q29udGVudChodG1sXzBiMmVlZDQxNWNiNTRmMjBhMzRkOTQwNWNhZGQ2ZmQ1KTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl83OTk0MzhhYTNjY2Q0ZTc3Yjk0YjUyOTdhZjY3NzA1ZS5iaW5kUG9wdXAocG9wdXBfODQyNDkzYmJlMGUxNDVmMzg4N2M2MWUwZDY1ZTM0ZGYpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2E5NzZmMDA4MzJkZjQyMjk4ZDIyZWM4MTVmZmY5NzFhID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMjUzMTc0NSwgNTUuMzY1NjcyOF0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiYiIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJiIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiAwLjc1LCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF8zMmY2NjliMzk5OGI0YmRjYjU4MWY1MTQzOGNlODgzYyA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfYjI1YzIzZTI4OGJjNDVlYTlmYTdjNjYwMmNhMWM0MWMgPSAkKGA8ZGl2IGlkPSJodG1sX2IyNWMyM2UyODhiYzQ1ZWE5ZmE3YzY2MDJjYTFjNDFjIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogMy4gY2FkaXogLSBhaGxhbiBsb3VuZ2UgQCBnYXRlIGIyNjxicj5UZWxlcGhvbmU6ICs5NzEgNCA1MDUgMjAwMDxicj51cmw6IGh0dHA6Ly93d3cuZHViYWlpbnRsaG90ZWxzLmNvbS9kaW5pbmcvYWhsYW4tbG91bmdlLWI8L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfMzJmNjY5YjM5OThiNGJkY2I1ODFmNTE0MzhjZTg4M2Muc2V0Q29udGVudChodG1sX2IyNWMyM2UyODhiYzQ1ZWE5ZmE3YzY2MDJjYTFjNDFjKTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl9hOTc2ZjAwODMyZGY0MjI5OGQyMmVjODE1ZmZmOTcxYS5iaW5kUG9wdXAocG9wdXBfMzJmNjY5YjM5OThiNGJkY2I1ODFmNTE0MzhjZTg4M2MpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzBhMWJkMjkyYTliYzQ2NDdiMzM2YjQxYzEyMTE0YjJkID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMTA0MzI5NiwgNTUuMTQ4NzY5MV0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiYiIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJiIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiAwLjc1LCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF8zZTZhMGI4NWJhOGI0MDFhOTBhNjFkNjE4MmNiZWQzMCA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfMDNmMDU0OWE4YWI2NGYxN2E1NWZjZDE2OWU2ODM4ODkgPSAkKGA8ZGl2IGlkPSJodG1sXzAzZjA1NDlhOGFiNjRmMTdhNTVmY2QxNjllNjgzODg5IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogNC4gYmx2ZCBvbiBvbmU8YnI+VGVsZXBob25lOiArOTcxIDQgNDU1IDk5ODk8YnI+dXJsOiBodHRwOi8vZml2ZWhvdGVsc2FuZHJlc29ydHMuY29tL2RpbmUtZHJpbmstZGFuY2UvcmVzdGF1cmFudHMvYmx2ZC1vbi1vbmUvPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwXzNlNmEwYjg1YmE4YjQwMWE5MGE2MWQ2MTgyY2JlZDMwLnNldENvbnRlbnQoaHRtbF8wM2YwNTQ5YThhYjY0ZjE3YTU1ZmNkMTY5ZTY4Mzg4OSk7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfMGExYmQyOTJhOWJjNDY0N2IzMzZiNDFjMTIxMTRiMmQuYmluZFBvcHVwKHBvcHVwXzNlNmEwYjg1YmE4YjQwMWE5MGE2MWQ2MTgyY2JlZDMwKQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl84MjM4ZTBkYWYwZGM0YzVlYmUwY2M1NWUwMTY5YzJjYSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjI0ODE0NjIsIDU1LjI4NjY1MjVdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogImIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiYiIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogMC43NSwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfMDA2OGI1MWJlMTk1NDk2OWI0NDE2ODQxNWZmNzU3NzggPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sX2RlYTQ0N2I0ZDFlMDQ3YjliZjJjMjVhMjRmMDgyZDhhID0gJChgPGRpdiBpZD0iaHRtbF9kZWE0NDdiNGQxZTA0N2I5YmYyYzI1YTI0ZjA4MmQ4YSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDUuIHB1cmFuaSBkaWxsaSBkdWJhaTxicj5UZWxlcGhvbmU6ICs5NzEgNTAgMjExIDY4MTY8YnI+dXJsOiBodHRwOi8vd3d3LnB1cmFuaWRpbGxpZHViYWkuY29tLzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF8wMDY4YjUxYmUxOTU0OTY5YjQ0MTY4NDE1ZmY3NTc3OC5zZXRDb250ZW50KGh0bWxfZGVhNDQ3YjRkMWUwNDdiOWJmMmMyNWEyNGYwODJkOGEpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyXzgyMzhlMGRhZjBkYzRjNWViZTBjYzU1ZTAxNjljMmNhLmJpbmRQb3B1cChwb3B1cF8wMDY4YjUxYmUxOTU0OTY5YjQ0MTY4NDE1ZmY3NTc3OCkKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfY2Q2YTdmNTM3YWE1NGM0Mzk2MGJhMTQ3NTVhMTQ2MWYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4yMDgyNzMsIDU1LjI2MDYwMTVdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogImIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiYiIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogMC42NzQ5OTk5OTk5OTk5OTk5LCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF85MjI4NjA5MzNhM2U0N2M3YjI2NWU4MzQxMjRmODRhMCA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfN2E2MjA3Mjk5NzRhNDA3YWE4YzljMTNlNGE0ZDhkZTIgPSAkKGA8ZGl2IGlkPSJodG1sXzdhNjIwNzI5OTc0YTQwN2FhOGM5YzEzZTRhNGQ4ZGUyIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogU3BvbnNvcmVkZ3JhcGVza2luIGdyYXBlIGJhciBhbmQga2l0Y2hlbjxicj5UZWxlcGhvbmU6ICs5NzEgNCA0MDMgMzExMTxicj51cmw6IGh0dHA6Ly93d3cubGl2ZWxhdmlsbGUuY29tL2RpbmluZy9HcmFwZXNraW4vaW5kZXguYXNweDwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF85MjI4NjA5MzNhM2U0N2M3YjI2NWU4MzQxMjRmODRhMC5zZXRDb250ZW50KGh0bWxfN2E2MjA3Mjk5NzRhNDA3YWE4YzljMTNlNGE0ZDhkZTIpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyX2NkNmE3ZjUzN2FhNTRjNDM5NjBiYTE0NzU1YTE0NjFmLmJpbmRQb3B1cChwb3B1cF85MjI4NjA5MzNhM2U0N2M3YjI2NWU4MzQxMjRmODRhMCkKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYjNmNmY2MjRlYzU1NDJjMGFiY2QzYjViYTUzOTRlODEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4xMDQzMjk2LCA1NS4xNDg3NjkxXSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJiIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogImIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDAuNzUsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwX2Y3ZjBlZTc4NTRlYzQ1MmU5NmQ1YmFjYTVkMDYzMjExID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF82NDNmNTU0ZGE3MDY0ZTAzODM1OTRiNWY0ZTdlMWY3OSA9ICQoYDxkaXYgaWQ9Imh0bWxfNjQzZjU1NGRhNzA2NGUwMzgzNTk0YjVmNGU3ZTFmNzkiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiA2LiB0cmF0dG9yaWEgYnkgY2lucXVlPGJyPlRlbGVwaG9uZTogKzk3MSA0IDQ1NSA5OTg5PGJyPnVybDogaHR0cDovL2p1bWVpcmFodmlsbGFnZS5maXZlaG90ZWxzYW5kcmVzb3J0cy5jb20vbWVldC1taW5nbGUvdHJhdHRvcmlhLWJ5LWNpbnF1ZTwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF9mN2YwZWU3ODU0ZWM0NTJlOTZkNWJhY2E1ZDA2MzIxMS5zZXRDb250ZW50KGh0bWxfNjQzZjU1NGRhNzA2NGUwMzgzNTk0YjVmNGU3ZTFmNzkpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyX2IzZjZmNjI0ZWM1NTQyYzBhYmNkM2I1YmE1Mzk0ZTgxLmJpbmRQb3B1cChwb3B1cF9mN2YwZWU3ODU0ZWM0NTJlOTZkNWJhY2E1ZDA2MzIxMSkKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMDU2MzEwZWE5ZGVhNGNjZjg3Mzc2MGE3N2ZhOTkwMzcgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4yNTY4NzU3LCA1NS4zMTIwODExXSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJiIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogImIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDAuNzUsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwXzA0ODljNWI4MjA2MDRjOTM4NmZlMDY4ODQzMDk3YTNjID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF82ZjQ5YWJjNDQzMmE0ZDZhYTVlYjM2N2U1NWMzZjFhMSA9ICQoYDxkaXYgaWQ9Imh0bWxfNmY0OWFiYzQ0MzJhNGQ2YWE1ZWIzNjdlNTVjM2YxYTEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiA3LiBkb29ycyBmcmVlc3R5bGUgZ3JpbGw8YnI+VGVsZXBob25lOiArOTcxIDQgMjA0IDkyOTk8YnI+dXJsOiBodHRwOi8vd3d3LmRvb3JzZHViYWkuY29tL2VuPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwXzA0ODljNWI4MjA2MDRjOTM4NmZlMDY4ODQzMDk3YTNjLnNldENvbnRlbnQoaHRtbF82ZjQ5YWJjNDQzMmE0ZDZhYTVlYjM2N2U1NWMzZjFhMSk7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfMDU2MzEwZWE5ZGVhNGNjZjg3Mzc2MGE3N2ZhOTkwMzcuYmluZFBvcHVwKHBvcHVwXzA0ODljNWI4MjA2MDRjOTM4NmZlMDY4ODQzMDk3YTNjKQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl80ZGNmMDkzZDY5MzI0M2FhODk2OThhZjBjNzY0ZWRlNyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjA2NTc5MzQsIDU1LjEzODExNTldLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogImIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiYiIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogMC43NSwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfMDc4N2Y4ZWNiMDA5NGNhYmEwZjFiNzJmNTZjY2U3NjIgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzFmZGVmNDkwNTRiMjQzYTU5MTk4ZjM5MzNlMzc4ODM0ID0gJChgPGRpdiBpZD0iaHRtbF8xZmRlZjQ5MDU0YjI0M2E1OTE5OGYzOTMzZTM3ODgzNCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDguIHVyYmFuIGJhciAmIGtpdGNoZW4gLSB1Yms8YnI+VGVsZXBob25lOiArOTcxIDQgNDM4IDAwMDA8YnI+dXJsOiBodHRwOi8vd3d3Lm1vdmVucGljay5jb20vZW4vbWlkZGxlLWVhc3QvdWFlL2R1YmFpL2R1YmFpLWp1bWVpcmFoLWxha2VzLXRvd2Vycy9yZXN0YXVyYW50cy9yZXN0YXVyYW50cy91cmJhbi1iYXIta2l0Y2hlbi11Yms8L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfMDc4N2Y4ZWNiMDA5NGNhYmEwZjFiNzJmNTZjY2U3NjIuc2V0Q29udGVudChodG1sXzFmZGVmNDkwNTRiMjQzYTU5MTk4ZjM5MzNlMzc4ODM0KTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl80ZGNmMDkzZDY5MzI0M2FhODk2OThhZjBjNzY0ZWRlNy5iaW5kUG9wdXAocG9wdXBfMDc4N2Y4ZWNiMDA5NGNhYmEwZjFiNzJmNTZjY2U3NjIpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzE2N2ZjYjAwMzUyODRmNDBiNDRmOTVmMDBiZDk0NmQzID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMjMzODQ0MSwgNTUuMjY1NDgxMl0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiYiIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJiIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiAwLjc1LCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF83ZTkxZmUzNWM0NmY0MTM2YTc5Y2Y4NmNjZTEzZmM3YSA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfM2JlMDJmZDU0NmFkNDlhNWI5NmQ0ZTk4NjQ0ODY1NmIgPSAkKGA8ZGl2IGlkPSJodG1sXzNiZTAyZmQ1NDZhZDQ5YTViOTZkNGU5ODY0NDg2NTZiIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogOS4gYmFyZWZvb3QgbG91bmdlPGJyPlRlbGVwaG9uZTogKzk3MSA0IDM0NiAxMTExPGJyPnVybDogaHR0cDovL3d3dy5keGJtYXJpbmUuY29tLzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF83ZTkxZmUzNWM0NmY0MTM2YTc5Y2Y4NmNjZTEzZmM3YS5zZXRDb250ZW50KGh0bWxfM2JlMDJmZDU0NmFkNDlhNWI5NmQ0ZTk4NjQ0ODY1NmIpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyXzE2N2ZjYjAwMzUyODRmNDBiNDRmOTVmMDBiZDk0NmQzLmJpbmRQb3B1cChwb3B1cF83ZTkxZmUzNWM0NmY0MTM2YTc5Y2Y4NmNjZTEzZmM3YSkKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfOTY5ZTFlOGI1NzI2NGY4ZGE4ZWMwZDk3YTg1YmNjMzQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4yMTI2NDI2LCA1NS4yODI0MDVdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogImIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiYiIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogMC43NSwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfNzVmNTEwMjQ3ZDcxNGQzM2JmODNlZGE3N2RlMmQ0NDYgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzg4YjM2ZGQ5Y2Q4ZTRmZTY5MTQyODQ2NzhjMzRjNzNiID0gJChgPGRpdiBpZD0iaHRtbF84OGIzNmRkOWNkOGU0ZmU2OTE0Mjg0Njc4YzM0YzczYiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDEwLiBtaW5hIGJyYXNzZXJpZTxicj5UZWxlcGhvbmU6ICs5NzEgNCA1MDYgMDEwMDxicj51cmw6IGh0dHA6Ly93d3cubWluYWJyYXNzZXJpZS5jb20vPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwXzc1ZjUxMDI0N2Q3MTRkMzNiZjgzZWRhNzdkZTJkNDQ2LnNldENvbnRlbnQoaHRtbF84OGIzNmRkOWNkOGU0ZmU2OTE0Mjg0Njc4YzM0YzczYik7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfOTY5ZTFlOGI1NzI2NGY4ZGE4ZWMwZDk3YTg1YmNjMzQuYmluZFBvcHVwKHBvcHVwXzc1ZjUxMDI0N2Q3MTRkMzNiZjgzZWRhNzdkZTJkNDQ2KQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8xMmVmNjMyYjlhMGE0MGQ1YWI5MzdmMzE5YjEyZDhkMiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjIwODI3MywgNTUuMjYwNjAxNV0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiYiIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJiIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiAwLjY3NDk5OTk5OTk5OTk5OTksICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwXzZkMjdjYzA0M2U1NTRlZmZhYTdkZDMzNjM1YTVjMTllID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF8wYTY2Njg5NGE5OTU0NzRhOGExN2Q0MGNkNDY3ZGFjZSA9ICQoYDxkaXYgaWQ9Imh0bWxfMGE2NjY4OTRhOTk1NDc0YThhMTdkNDBjZDQ2N2RhY2UiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiBTcG9uc29yZWRncmF6ZSBnYXN0cm8gZ3JpbGw8YnI+VGVsZXBob25lOiArOTcxIDQgNDAzIDMxMTE8YnI+dXJsOiBodHRwOi8vd3d3LmxpdmVsYXZpbGxlLmNvbS9kaW5pbmcvR3JhemUvaW5kZXguaHRtbDwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF82ZDI3Y2MwNDNlNTU0ZWZmYWE3ZGQzMzYzNWE1YzE5ZS5zZXRDb250ZW50KGh0bWxfMGE2NjY4OTRhOTk1NDc0YThhMTdkNDBjZDQ2N2RhY2UpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyXzEyZWY2MzJiOWEwYTQwZDVhYjkzN2YzMTliMTJkOGQyLmJpbmRQb3B1cChwb3B1cF82ZDI3Y2MwNDNlNTU0ZWZmYWE3ZGQzMzYzNWE1YzE5ZSkKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNTZlMDgzMjE3OGFlNDRmYzllNjdmZWRjMzI2NTBiYTMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNC44MTY4MjA2LCA1NS4yMzEyODcyXSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJiIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogImIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDAuNzUsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwXzdmNGFkM2IwOTkyNTQ5YjRhMTIyNmEwZjZlOTc1ZTBiID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF83MGFhYTFkZjFiMTE0OGYyYTgxNzZmY2EwYTA2YjY3ZSA9ICQoYDxkaXYgaWQ9Imh0bWxfNzBhYWExZGYxYjExNDhmMmE4MTc2ZmNhMGEwNmI2N2UiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiAxMS4gYWwgc2FyYWIgcm9vZnRvcCBsb3VuZ2U8YnI+VGVsZXBob25lOiArOTcxIDQgODA5IDYxMDA8YnI+dXJsOiBodHRwOi8vd3d3Lm1leWRhbmhvdGVscy5jb20vYmFiYWxzaGFtcy9kaW5pbmcuaHRtPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwXzdmNGFkM2IwOTkyNTQ5YjRhMTIyNmEwZjZlOTc1ZTBiLnNldENvbnRlbnQoaHRtbF83MGFhYTFkZjFiMTE0OGYyYTgxNzZmY2EwYTA2YjY3ZSk7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfNTZlMDgzMjE3OGFlNDRmYzllNjdmZWRjMzI2NTBiYTMuYmluZFBvcHVwKHBvcHVwXzdmNGFkM2IwOTkyNTQ5YjRhMTIyNmEwZjZlOTc1ZTBiKQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9iNDE4MGYzYmFkZDk0Y2E4YTkyYmU1MjFmY2YxMDYxNiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjA0NjI5NDYsIDU1LjIwMzA0MTE5OTk5OTk5XSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJiIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogImIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDAuNzUsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwX2E4MDdkOTRmYWNhZTRmYzZhNzE1YjlmOWNjOTIyNTQ1ID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF9kZjEyOTAzNmVhNzM0MWJiYjYzN2ZlZWNhODY0Mzg5YyA9ICQoYDxkaXYgaWQ9Imh0bWxfZGYxMjkwMzZlYTczNDFiYmI2MzdmZWVjYTg2NDM4OWMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiAxMi4gc291bCBzdHJlZXQ8YnI+VGVsZXBob25lOiArOTcxIDQgNDU1IDk5ODk8YnI+dXJsOiBodHRwOi8vc291bC5zdC88L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfYTgwN2Q5NGZhY2FlNGZjNmE3MTViOWY5Y2M5MjI1NDUuc2V0Q29udGVudChodG1sX2RmMTI5MDM2ZWE3MzQxYmJiNjM3ZmVlY2E4NjQzODljKTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl9iNDE4MGYzYmFkZDk0Y2E4YTkyYmU1MjFmY2YxMDYxNi5iaW5kUG9wdXAocG9wdXBfYTgwN2Q5NGZhY2FlNGZjNmE3MTViOWY5Y2M5MjI1NDUpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzQ0YjlkMDI2YmFlOTQ1YTBhMzIyMTQxNjYzNWU2ZWM4ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMjQ5MTU0OSwgNTUuMzQ3MTM5NjAwMDAwMDFdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogImIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiYiIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogMC43NSwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfMzQ0OWQzYjlhNWQzNGRmYWI0ZWJhN2U2MGQ1NTFjYjggPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzhiODJjZWQ3MmM1YjQwZTU4MDhjNTQyMTFlZTZiOTgzID0gJChgPGRpdiBpZD0iaHRtbF84YjgyY2VkNzJjNWI0MGU1ODA4YzU0MjExZWU2Yjk4MyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDEzLiBiZWJlbW9zPGJyPlRlbGVwaG9uZTogKzk3MSA0IDcwMiAyNDU1PGJyPnVybDogaHR0cDovL3d3dy5iZWJlbW9zZHViYWkuY29tLzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF8zNDQ5ZDNiOWE1ZDM0ZGZhYjRlYmE3ZTYwZDU1MWNiOC5zZXRDb250ZW50KGh0bWxfOGI4MmNlZDcyYzViNDBlNTgwOGM1NDIxMWVlNmI5ODMpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyXzQ0YjlkMDI2YmFlOTQ1YTBhMzIyMTQxNjYzNWU2ZWM4LmJpbmRQb3B1cChwb3B1cF8zNDQ5ZDNiOWE1ZDM0ZGZhYjRlYmE3ZTYwZDU1MWNiOCkKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYTgxMGY0MzExZGMwNGIzY2FmNzNjZmNjMGY0ODcxYWYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4yMjg4Mzk0LCA1NS4zMjY4MTI1XSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJiIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogImIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDAuNzUsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwXzEwMzdhN2U1MmFlYjRmOWJiNmQxMjU5ODhmNjM5MDU2ID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF81YjI5YzBmNmI0NTU0Zjc0YjhlNjZlN2Y5NjY3MDdiMCA9ICQoYDxkaXYgaWQ9Imh0bWxfNWIyOWMwZjZiNDU1NGY3NGI4ZTY2ZTdmOTY2NzA3YjAiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiAxNC4gYXd0YXI8YnI+VGVsZXBob25lOiArOTcxIDQgMzE3IDIyMjE8YnI+dXJsOiBodHRwczovL3d3dy5oeWF0dHJlc3RhdXJhbnRzLmNvbS9lbi9kaW5pbmcvdWFlL2R1YmFpL21pZGRsZS1lYXN0ZXJuLXJlc3RhdXJhbnQtaW4tZ2FyaG91ZC1hd3Rhcj91dG1fc291cmNlPWdtYmxpc3RpbmdfZHhiZ2gmdXRtX21lZGl1bT1hd3RhciZ1dG1fY2FtcGFpZ249R01CPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwXzEwMzdhN2U1MmFlYjRmOWJiNmQxMjU5ODhmNjM5MDU2LnNldENvbnRlbnQoaHRtbF81YjI5YzBmNmI0NTU0Zjc0YjhlNjZlN2Y5NjY3MDdiMCk7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfYTgxMGY0MzExZGMwNGIzY2FmNzNjZmNjMGY0ODcxYWYuYmluZFBvcHVwKHBvcHVwXzEwMzdhN2U1MmFlYjRmOWJiNmQxMjU5ODhmNjM5MDU2KQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl80NjI0ZTA4MWIxMTA0NTRiYTJkMzg1NmU3Zjc5MjVhMiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjE5ODc2NSwgNTUuMjc5NjA1M10sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiYiIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJiIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiAwLjc1LCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF80ODliY2NjZTc5OGI0MDg2YWMzY2M5ZDk0OGEwOGMwMiA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfN2U4ZTdiODIwZWI3NDAxNDg2YmU2YTU4ZTEyYzg5MzUgPSAkKGA8ZGl2IGlkPSJodG1sXzdlOGU3YjgyMGViNzQwMTQ4NmJlNmE1OGUxMmM4OTM1IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogMTUuIHRyaWJlcyBjYXJuaXZvcmU8YnI+VGVsZXBob25lOiArOTcxIDQgMjI2IDQ5NzQ8YnI+dXJsOiBodHRwOi8vdHJpYmVzcmVzdGF1cmFudC5jb20vPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwXzQ4OWJjY2NlNzk4YjQwODZhYzNjYzlkOTQ4YTA4YzAyLnNldENvbnRlbnQoaHRtbF83ZThlN2I4MjBlYjc0MDE0ODZiZTZhNThlMTJjODkzNSk7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfNDYyNGUwODFiMTEwNDU0YmEyZDM4NTZlN2Y3OTI1YTIuYmluZFBvcHVwKHBvcHVwXzQ4OWJjY2NlNzk4YjQwODZhYzNjYzlkOTQ4YTA4YzAyKQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl84MDFkYWUxODZjMzU0ZjVjYThiZGUxY2Y0MzcyZWE5MiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjIyMTYwMywgNTUuMjgwODI2Ml0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiYiIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJiIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiAwLjY3NDk5OTk5OTk5OTk5OTksICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwXzZjNDUyY2U0MDgwMzQ5ZTQ4YzEzMTM4YjdjOTg3NzNhID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF9iN2U0ZmRiYzZhYjE0MWQ4YTQyNzE5MmZjMWJjMDg3ZiA9ICQoYDxkaXYgaWQ9Imh0bWxfYjdlNGZkYmM2YWIxNDFkOGE0MjcxOTJmYzFiYzA4N2YiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiBTcG9uc29yZWRzdXNoaSBuYXRpb25zPGJyPlRlbGVwaG9uZTogKzk3MSA1NiAxODggODUyMjxicj51cmw6IGh0dHBzOi8vc3VzaGluYXRpb25zLmFlLzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF82YzQ1MmNlNDA4MDM0OWU0OGMxMzEzOGI3Yzk4NzczYS5zZXRDb250ZW50KGh0bWxfYjdlNGZkYmM2YWIxNDFkOGE0MjcxOTJmYzFiYzA4N2YpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyXzgwMWRhZTE4NmMzNTRmNWNhOGJkZTFjZjQzNzJlYTkyLmJpbmRQb3B1cChwb3B1cF82YzQ1MmNlNDA4MDM0OWU0OGMxMzEzOGI3Yzk4NzczYSkKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMWU4OWFjZTQzZTc5NDFkM2I3NGRjMDA2NGYwM2RjNmMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4yNzg4OTgsIDU1LjMwNDQ2MDddLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogImIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiYiIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogMC43NSwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfNTQ4MDgyZjA5Nzc3NGRkYThmMTE1OTc4ODI2NGFkNzMgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzdlZjY2Y2MwYzRhNDRmMDk4MGZmM2JiOTY3MWVmNjY3ID0gJChgPGRpdiBpZD0iaHRtbF83ZWY2NmNjMGM0YTQ0ZjA5ODBmZjNiYjk2NzFlZjY2NyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDE2LiBhbCBkYXdhYXIgcmV2b2x2aW5nIHJlc3RhdXJhbnQ8YnI+VGVsZXBob25lOiArOTcxIDQgMjA5IDY5MTI8YnI+dXJsOiBodHRwOi8vd3d3Lmh5YXR0cmVzdGF1cmFudHMuY29tL2VuL2RpbmluZy91YWUvZHViYWkvaW50ZXJuYXRpb25hbC1yZXN0YXVyYW50LWluLWRlaXJhLWNvcm5pY2hlLWFsLWRhd2Fhci1yZXZvbHZpbmctcmVzdGF1cmFudDwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF81NDgwODJmMDk3Nzc0ZGRhOGYxMTU5Nzg4MjY0YWQ3My5zZXRDb250ZW50KGh0bWxfN2VmNjZjYzBjNGE0NGYwOTgwZmYzYmI5NjcxZWY2NjcpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyXzFlODlhY2U0M2U3OTQxZDNiNzRkYzAwNjRmMDNkYzZjLmJpbmRQb3B1cChwb3B1cF81NDgwODJmMDk3Nzc0ZGRhOGYxMTU5Nzg4MjY0YWQ3MykKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfODdjNTkyZjkxZTllNDdhM2E0YjBkZWIxYzRhYmEwZmIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4xMTEzOTkxLCA1NS4xMzcyMTU4XSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJiIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogImIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDAuNzUsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwXzRiMDMxYjU5NTI4MTQxNzU5NGYyN2U4YzhkZTA1ZmQ1ID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF9hMTg4MGM4MDVkZGE0MmQ5YmU2MzcwYzQ4OWQ1MTUzNiA9ICQoYDxkaXYgaWQ9Imh0bWxfYTE4ODBjODA1ZGRhNDJkOWJlNjM3MGM0ODlkNTE1MzYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiAxNy4ga2h5YmVyPGJyPlRlbGVwaG9uZTogKzk3MSA0IDQ1NSAxMTExPGJyPnVybDogaHR0cHM6Ly93d3cuZHVrZXNkdWJhaS5jb20va2h5YmVyLzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF80YjAzMWI1OTUyODE0MTc1OTRmMjdlOGM4ZGUwNWZkNS5zZXRDb250ZW50KGh0bWxfYTE4ODBjODA1ZGRhNDJkOWJlNjM3MGM0ODlkNTE1MzYpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyXzg3YzU5MmY5MWU5ZTQ3YTNhNGIwZGViMWM0YWJhMGZiLmJpbmRQb3B1cChwb3B1cF80YjAzMWI1OTUyODE0MTc1OTRmMjdlOGM4ZGUwNWZkNSkKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfODhmMzQ1NDQ4M2U4NDI0ZTk0MjAyMmEyZTc1MmU1NDMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4yNjYyNjc4LCA1NS4zMDg3ODc0OTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiYiIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJiIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiAwLjc1LCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF8xMTUyNjQ1MTUxNGI0YTBlOWMyMzIyNjU5ODc0NmZhMiA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfZGZhNWQxMjc2MmFkNDY2MjkxMTExOTA1YmEzZTE3NTAgPSAkKGA8ZGl2IGlkPSJodG1sX2RmYTVkMTI3NjJhZDQ2NjI5MTExMTkwNWJhM2UxNzUwIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogMTguIGRhbmlhbCByZXN0YXVyYW50PGJyPlRlbGVwaG9uZTogKzk3MSA0IDIyNyA3NjY5PGJyPnVybDogaHR0cDovL3d3dy5kYW5pYWxyZXN0YXVyYW50LmNvbS88L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfMTE1MjY0NTE1MTRiNGEwZTljMjMyMjY1OTg3NDZmYTIuc2V0Q29udGVudChodG1sX2RmYTVkMTI3NjJhZDQ2NjI5MTExMTkwNWJhM2UxNzUwKTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl84OGYzNDU0NDgzZTg0MjRlOTQyMDIyYTJlNzUyZTU0My5iaW5kUG9wdXAocG9wdXBfMTE1MjY0NTE1MTRiNGEwZTljMjMyMjY1OTg3NDZmYTIpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzIyMWNmNjg2M2Q5ZDRhODI5YTY2MDQzMWNlYWI2ZDI5ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMjM0MzU1LCA1NS4zMjQwMTQ3XSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJiIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogImIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDAuNzUsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwX2U1OWJlNjc1MDRlYzRkNWJhZDQwY2RlZDdkMzIwNzRiID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF9iNjI5MDIxZmE4Yzc0Y2I3YTk0YTYyZmVmNGJhMzQ1MCA9ICQoYDxkaXYgaWQ9Imh0bWxfYjYyOTAyMWZhOGM3NGNiN2E5NGE2MmZlZjRiYTM0NTAiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiAxOS4gZXZlIHBlbnRob3VzZSAmIGxvdW5nZTxicj5UZWxlcGhvbmU6ICs5NzEgNCA1NTMgMTIxNDxicj51cmw6IGh0dHA6Ly93d3cuaHlhdHRyZXN0YXVyYW50cy5jb20vZW4vZGluaW5nL3VhZS9kdWJhaS9pbnRlcm5hdGlvbmFsLXJlc3RhdXJhbnQtaW4tb3VkLW1ldGhhLXJvYWQtZXZlLXBlbnRob3VzZS1sb3VuZ2U/dXRtX3NvdXJjZT1XZWJzaXRlX2R4YmhjJnV0bV9tZWRpdW09ZXZlJnV0bV9jYW1wYWlnbj1IeWF0dDwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF9lNTliZTY3NTA0ZWM0ZDViYWQ0MGNkZWQ3ZDMyMDc0Yi5zZXRDb250ZW50KGh0bWxfYjYyOTAyMWZhOGM3NGNiN2E5NGE2MmZlZjRiYTM0NTApOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyXzIyMWNmNjg2M2Q5ZDRhODI5YTY2MDQzMWNlYWI2ZDI5LmJpbmRQb3B1cChwb3B1cF9lNTliZTY3NTA0ZWM0ZDViYWQ0MGNkZWQ3ZDMyMDc0YikKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMWQ5NGZjNzllOGU0NGIzMTg3ZDdhYTU1ZDBmMDhlMmUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4xOTg3NjUsIDU1LjI3OTYwNTNdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogImIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiYiIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogMC43NSwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfZmZmYjcwZjk4ZTM4NDdjNTllN2I3ZDU4MDc0NjM4NDMgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzVkZDhiZDQ4ZTNmYzQwNWU4YjcyZjg0NjQyYTRmMGRiID0gJChgPGRpdiBpZD0iaHRtbF81ZGQ4YmQ0OGUzZmM0MDVlOGI3MmY4NDY0MmE0ZjBkYiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDIwLiB0aGUgZ3JpbGwgc2hhY2s8YnI+VGVsZXBob25lOiArOTcxIDQgMzg4IDIzODI8YnI+dXJsOiBodHRwOi8vd3d3LnRoZWdyaWxsbHNoYWNrLmNvbS88L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfZmZmYjcwZjk4ZTM4NDdjNTllN2I3ZDU4MDc0NjM4NDMuc2V0Q29udGVudChodG1sXzVkZDhiZDQ4ZTNmYzQwNWU4YjcyZjg0NjQyYTRmMGRiKTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl8xZDk0ZmM3OWU4ZTQ0YjMxODdkN2FhNTVkMGYwOGUyZS5iaW5kUG9wdXAocG9wdXBfZmZmYjcwZjk4ZTM4NDdjNTllN2I3ZDU4MDc0NjM4NDMpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzM1Y2NjZGI1NDI1NTQzYTBiMWMyYTIwMWRkNTgxMDg1ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMjQ3ODY3LCA1NS4zMDA0OTI1XSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJiIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogImIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDAuNjc0OTk5OTk5OTk5OTk5OSwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfYWZkNmI4ZDM0YzU5NDViNDk4ZWY0ZDNmZDg0YjE5MjggPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzM1NTI1MjBkNDQwNzQ5YzM4ZDg1NGE1ODNlOGRjMDcyID0gJChgPGRpdiBpZD0iaHRtbF8zNTUyNTIwZDQ0MDc0OWMzOGQ4NTRhNTgzZThkYzA3MiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IFNwb25zb3JlZGFtcml0c3IgcmVzdGF1cmFudDxicj5UZWxlcGhvbmU6ICs5NzEgNTAgNjc4IDAwOTY8YnI+dXJsOiBodHRwOi8vYW1yaXRzcnVhZS5jb20vPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwX2FmZDZiOGQzNGM1OTQ1YjQ5OGVmNGQzZmQ4NGIxOTI4LnNldENvbnRlbnQoaHRtbF8zNTUyNTIwZDQ0MDc0OWMzOGQ4NTRhNTgzZThkYzA3Mik7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfMzVjY2NkYjU0MjU1NDNhMGIxYzJhMjAxZGQ1ODEwODUuYmluZFBvcHVwKHBvcHVwX2FmZDZiOGQzNGM1OTQ1YjQ5OGVmNGQzZmQ4NGIxOTI4KQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9mMzE5NGZiNTg4N2M0ZWU1YWY4OWQ2NGFkYTQ5M2NlYiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjEwNDMyOTYsIDU1LjE0ODc2OTFdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogImIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiYiIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogMC43NSwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfYmRmOTE1YThmZDdmNDg1N2E2ZWNjNDIyMzlkY2VmZjAgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzRlYzA0ZWFmNTYwNzQ1Mjg5MjY5MzNiZmVhMmE5ZWFmID0gJChgPGRpdiBpZD0iaHRtbF80ZWMwNGVhZjU2MDc0NTI4OTI2OTMzYmZlYTJhOWVhZiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDIxLiBtYWlkZW4gc2hhbmdoYWk8YnI+VGVsZXBob25lOiArOTcxIDQgNDU1IDk5ODk8YnI+dXJsOiBodHRwOi8vZml2ZWhvdGVsc2FuZHJlc29ydHMuY29tL2RpbmUtZHJpbmstZGFuY2UvcmVzdGF1cmFudHMvbWFpZGVuLXNoYW5naGFpLzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF9iZGY5MTVhOGZkN2Y0ODU3YTZlY2M0MjIzOWRjZWZmMC5zZXRDb250ZW50KGh0bWxfNGVjMDRlYWY1NjA3NDUyODkyNjkzM2JmZWEyYTllYWYpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyX2YzMTk0ZmI1ODg3YzRlZTVhZjg5ZDY0YWRhNDkzY2ViLmJpbmRQb3B1cChwb3B1cF9iZGY5MTVhOGZkN2Y0ODU3YTZlY2M0MjIzOWRjZWZmMCkKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYTAyN2I5MzZmNmI2NGVlNGI4YjRiMDlhZWNhMzA5NDAgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4yMTQwMTMzLCA1NS4yNzYwODg1XSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJiIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogImIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDAuNzUsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwX2YxYmIxOGJjZjE4ODRkNGY5ZTg5ZTcyMzVkYzI2ZDhhID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF85OGRkNTFlZWNjMGQ0NDdkYjk1YzhhODVmZjJlNDY3ZCA9ICQoYDxkaXYgaWQ9Imh0bWxfOThkZDUxZWVjYzBkNDQ3ZGI5NWM4YTg1ZmYyZTQ2N2QiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiAyMi4gcHVyYW5pIGRpbGxpIHNoZWlraCB6YXllZCByb2FkPGJyPlRlbGVwaG9uZTogKzk3MSA0IDMxNiA5NzI2PGJyPnVybDogaHR0cDovL3d3dy5wdXJhbmlkaWxsaWR1YmFpLmNvbS9zaGVpa2h6YXllZHJvYWQ8L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfZjFiYjE4YmNmMTg4NGQ0ZjllODllNzIzNWRjMjZkOGEuc2V0Q29udGVudChodG1sXzk4ZGQ1MWVlY2MwZDQ0N2RiOTVjOGE4NWZmMmU0NjdkKTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl9hMDI3YjkzNmY2YjY0ZWU0YjhiNGIwOWFlY2EzMDk0MC5iaW5kUG9wdXAocG9wdXBfZjFiYjE4YmNmMTg4NGQ0ZjllODllNzIzNWRjMjZkOGEpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2VmMjI1Y2RhNWNhMTQwZTQ4ZDBmYmU5NjkzODFhOWRmID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMjE0MDEzMywgNTUuMjc2MDg4NV0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiYiIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJiIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiAwLjY3NDk5OTk5OTk5OTk5OTksICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwX2FiY2Q2NDhjYWI4ZTRiYTBhMjAzZDI2OTMyYWVlMTk5ID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF9lZGIyMDFiMGZmYmQ0MzA1YWNmOTg5NmYzYzdmMjcyMSA9ICQoYDxkaXYgaWQ9Imh0bWxfZWRiMjAxYjBmZmJkNDMwNWFjZjk4OTZmM2M3ZjI3MjEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiAyMy4gbGV2ZWwgNDMgc2t5IGxvdW5nZTxicj5UZWxlcGhvbmU6ICs5NzEgNTYgNDE0IDIyMTM8YnI+dXJsOiBodHRwOi8vd3d3LmxldmVsNDNsb3VuZ2UuY29tLzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF9hYmNkNjQ4Y2FiOGU0YmEwYTIwM2QyNjkzMmFlZTE5OS5zZXRDb250ZW50KGh0bWxfZWRiMjAxYjBmZmJkNDMwNWFjZjk4OTZmM2M3ZjI3MjEpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyX2VmMjI1Y2RhNWNhMTQwZTQ4ZDBmYmU5NjkzODFhOWRmLmJpbmRQb3B1cChwb3B1cF9hYmNkNjQ4Y2FiOGU0YmEwYTIwM2QyNjkzMmFlZTE5OSkKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNjZjY2EzODI1OTcxNGQ1YjgyMjI4ZGI3MDU3YTM4NDMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4xOTUxNTU0LCA1NS4yNzUxNTc5XSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJiIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogImIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDAuNzUsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwX2MxMzY5YzhiNzRhNDRiM2Y5ODVjNWFlMjViYmVmZDM2ID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF81ZTIxYmViOTM5NDE0OTY3OTg2ZWY1NDBhNTE4MGQxNCA9ICQoYDxkaXYgaWQ9Imh0bWxfNWUyMWJlYjkzOTQxNDk2Nzk4NmVmNTQwYTUxODBkMTQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiAyNC4gYmxhY2sgdGFwIGNyYWZ0IGJ1cmdlcnMgJiBzaGFrZXMgZHViYWkgbWFsbDxicj5UZWxlcGhvbmU6ICs5NzEgNCAzMzAgNTEwMzxicj51cmw6IGh0dHA6Ly93d3cuYmxhY2t0YXBtZS5jb20vPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwX2MxMzY5YzhiNzRhNDRiM2Y5ODVjNWFlMjViYmVmZDM2LnNldENvbnRlbnQoaHRtbF81ZTIxYmViOTM5NDE0OTY3OTg2ZWY1NDBhNTE4MGQxNCk7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfNjZjY2EzODI1OTcxNGQ1YjgyMjI4ZGI3MDU3YTM4NDMuYmluZFBvcHVwKHBvcHVwX2MxMzY5YzhiNzRhNDRiM2Y5ODVjNWFlMjViYmVmZDM2KQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8wMmI1NGNiYzk4Zjk0Y2NlOTk4NzNjN2U5ZjJjM2Y4YSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjI0OTE1NDksIDU1LjM0NzEzOTYwMDAwMDAxXSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJiIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogImIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDAuNzUsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwXzE2M2YwMmE4ZDMyYzQzYzJiMzkyN2I4YTdlNzE4ZTg4ID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF83MDgzYzZiM2E0YTY0YTkwOTFlNDNjOTI3MWRhNmEwYyA9ICQoYDxkaXYgaWQ9Imh0bWxfNzA4M2M2YjNhNGE2NGE5MDkxZTQzYzkyNzFkYTZhMGMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiAyNS4gYmVlZiBiaXN0cm88YnI+VGVsZXBob25lOiArOTcxIDQgNzAyIDI0NTU8YnI+dXJsOiBodHRwOi8vd3d3LmJlZWZiaXN0cm9kdWJhaS5jb20vPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwXzE2M2YwMmE4ZDMyYzQzYzJiMzkyN2I4YTdlNzE4ZTg4LnNldENvbnRlbnQoaHRtbF83MDgzYzZiM2E0YTY0YTkwOTFlNDNjOTI3MWRhNmEwYyk7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfMDJiNTRjYmM5OGY5NGNjZTk5ODczYzdlOWYyYzNmOGEuYmluZFBvcHVwKHBvcHVwXzE2M2YwMmE4ZDMyYzQzYzJiMzkyN2I4YTdlNzE4ZTg4KQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9iMDg0OGZjOTI2MTg0Yjc3OTQyYWNjN2QyZWRiNjc4NyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjIwMjQ0ODUsIDU1LjIzOTY1MjVdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogImIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiYiIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogMC42NzQ5OTk5OTk5OTk5OTk5LCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF8zZmYyNjg3NzFmOWY0MDBiYjhjOWJhMWE2YjA1OWM2YSA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfNDEzYmQ1MWE1NWFhNGNmNjg0ZGFhYTY3ZjU5MjVmZGYgPSAkKGA8ZGl2IGlkPSJodG1sXzQxM2JkNTFhNTVhYTRjZjY4NGRhYWE2N2Y1OTI1ZmRmIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogU3BvbnNvcmVkdmVyZGUgZHViYWk8YnI+VGVsZXBob25lOiArOTcxIDQgMzMzIDgwMjU8YnI+dXJsOiBodHRwOi8vd3d3LnZlcmRlLWR1YmFpLmNvbS88L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfM2ZmMjY4NzcxZjlmNDAwYmI4YzliYTFhNmIwNTljNmEuc2V0Q29udGVudChodG1sXzQxM2JkNTFhNTVhYTRjZjY4NGRhYWE2N2Y1OTI1ZmRmKTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl9iMDg0OGZjOTI2MTg0Yjc3OTQyYWNjN2QyZWRiNjc4Ny5iaW5kUG9wdXAocG9wdXBfM2ZmMjY4NzcxZjlmNDAwYmI4YzliYTFhNmIwNTljNmEpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzYxMGU5YjY4NDE3YTRjNjE4OTkzNDIxZTllNDIxYTUxID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMjI5NTMwOSwgNTUuMjg2NjcyOF0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiYiIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJiIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiAwLjc1LCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF8yMTMzMTE3ODVjOWE0Yzk3YTI5ZTY5YzNiMjliNGMyZSA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfMTk4YmM4NDYyNTU0NGVjMTk5NDM3YjliOTZiMDQ2NjYgPSAkKGA8ZGl2IGlkPSJodG1sXzE5OGJjODQ2MjU1NDRlYzE5OTQzN2I5Yjk2YjA0NjY2IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogMjYuIG5pZG8gdGFwYXMgcmVzdGF1cmFudCAmIGJhcjxicj5UZWxlcGhvbmU6ICs5NzEgNCAzMzMgMzA1NTxicj51cmw6IGh0dHA6Ly9uaWRvZHhiLmNvbS88L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfMjEzMzExNzg1YzlhNGM5N2EyOWU2OWMzYjI5YjRjMmUuc2V0Q29udGVudChodG1sXzE5OGJjODQ2MjU1NDRlYzE5OTQzN2I5Yjk2YjA0NjY2KTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl82MTBlOWI2ODQxN2E0YzYxODk5MzQyMWU5ZTQyMWE1MS5iaW5kUG9wdXAocG9wdXBfMjEzMzExNzg1YzlhNGM5N2EyOWU2OWMzYjI5YjRjMmUpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2E3NjUxNjIyOTA4MzRiNjg4MzdjZDQ2ZWJhNDJhODYxID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMDgwNDc3NywgNTUuMTU0MTk0MzAwMDAwMDFdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogImIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiYiIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogMC43NSwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfMDgyNTAyYjkyY2MxNGYzZjg3YjI4NWU2NWY4NjAzNWYgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzVhM2Y1MWQ0MTMyMTQ4OTk4OTg3ZWE2YmViNDc3ZjU0ID0gJChgPGRpdiBpZD0iaHRtbF81YTNmNTFkNDEzMjE0ODk5ODk4N2VhNmJlYjQ3N2Y1NCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDI3LiBzaGFtaWFuYTxicj5UZWxlcGhvbmU6ICs5NzEgNCA1NzQgMTExMTxicj51cmw6IGh0dHA6Ly93d3cudGFqaG90ZWxzLmNvbS9lbi1pbi90YWovdGFqLWp1bWVpcmFoLWxha2VzLXRvd2Vycy9yZXN0YXVyYW50cy9zaGFtaWFuYS88L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfMDgyNTAyYjkyY2MxNGYzZjg3YjI4NWU2NWY4NjAzNWYuc2V0Q29udGVudChodG1sXzVhM2Y1MWQ0MTMyMTQ4OTk4OTg3ZWE2YmViNDc3ZjU0KTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl9hNzY1MTYyMjkwODM0YjY4ODM3Y2Q0NmViYTQyYTg2MS5iaW5kUG9wdXAocG9wdXBfMDgyNTAyYjkyY2MxNGYzZjg3YjI4NWU2NWY4NjAzNWYpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzQyYTg3OWZjM2Q2YjQ5MTZhMmVhZmEzNDdmM2JiYWE3ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMjA0ODQ5MywgNTUuMjcwNzgyOF0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiYiIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJiIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiAwLjc1LCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF9hNDZlZWM1ZWNmOWU0MzY4OThiMDU1NTZmY2VhOGY5MiA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfMzJlYmYxNzJkMzNmNDkxYjlkNTBkMDAxNDA2YmY3MTIgPSAkKGA8ZGl2IGlkPSJodG1sXzMyZWJmMTcyZDMzZjQ5MWI5ZDUwZDAwMTQwNmJmNzEyIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogMjguIGtpbmFyYSBieSB2aWthcyBraGFubmE8YnI+VGVsZXBob25lOiArOTcxIDQgODE0IDU1NTU8YnI+dXJsOiBodHRwOi8vd3d3LmtpbmFyYWR1YmFpLmNvbS88L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfYTQ2ZWVjNWVjZjllNDM2ODk4YjA1NTU2ZmNlYThmOTIuc2V0Q29udGVudChodG1sXzMyZWJmMTcyZDMzZjQ5MWI5ZDUwZDAwMTQwNmJmNzEyKTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl80MmE4NzlmYzNkNmI0OTE2YTJlYWZhMzQ3ZjNiYmFhNy5iaW5kUG9wdXAocG9wdXBfYTQ2ZWVjNWVjZjllNDM2ODk4YjA1NTU2ZmNlYThmOTIpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzI4OWQ4ZjJiZGI0MDQzNDRhMGY3ZWFmMGI1MDFkMjljID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMTEwODIwMiwgNTUuMTM5OTE4NDAwMDAwMDFdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogImIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiYiIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogMC43NSwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfN2E2ZDQ4MjAzMmUwNDVmOThjMzg4Yzc3MjM3MmU3OWYgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzg5Mjc2ODExZGY5YjRmZmI4Nzc0ZjE0ZWIyMGQ3NzA1ID0gJChgPGRpdiBpZD0iaHRtbF84OTI3NjgxMWRmOWI0ZmZiODc3NGYxNGViMjBkNzcwNSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDI5LiBsaXR0bGUgbWlzcyBpbmRpYTxicj5UZWxlcGhvbmU6ICs5NzEgNCA0NTcgMzQ1Nzxicj51cmw6IGh0dHA6Ly93d3cuZmFpcm1vbnQuY29tL3BhbG0tZHViYWkvZGluaW5nL2xpdHRsZS1taXNzLWluZGlhLzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF83YTZkNDgyMDMyZTA0NWY5OGMzODhjNzcyMzcyZTc5Zi5zZXRDb250ZW50KGh0bWxfODkyNzY4MTFkZjliNGZmYjg3NzRmMTRlYjIwZDc3MDUpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyXzI4OWQ4ZjJiZGI0MDQzNDRhMGY3ZWFmMGI1MDFkMjljLmJpbmRQb3B1cChwb3B1cF83YTZkNDgyMDMyZTA0NWY5OGMzODhjNzcyMzcyZTc5ZikKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYTQ0NWEyZDQxMmM5NGU1NWFmNjFiYjRmYjZjYjAyOWEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4xMTAzNDcsIDU1LjIyMDYyODI5OTk5OTk5XSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJiIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogImIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDAuNzUsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwXzA4Y2Y2MGRhOGI0MjRmZGM5NzFlN2Y5MmRiMTczZTYxID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF8xODc2OGZkYjQ4NjU0ODEwYTQzZTllZGE4N2U2NzZjMCA9ICQoYDxkaXYgaWQ9Imh0bWxfMTg3NjhmZGI0ODY1NDgxMGE0M2U5ZWRhODdlNjc2YzAiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiAzMC4gZmlzaCBodXQgYXNtYWsgYWwgc3VsdGFuIHNlYWZvb2QgcmVzdGF1cmFudDxicj5UZWxlcGhvbmU6ICs5NzEgNTggMTI4IDI4ODY8YnI+dXJsOiBodHRwOi8vZHViYWlmaXNoaHV0cmVzdGF1cmFudC5jb20vaW5kZXgucGhwPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwXzA4Y2Y2MGRhOGI0MjRmZGM5NzFlN2Y5MmRiMTczZTYxLnNldENvbnRlbnQoaHRtbF8xODc2OGZkYjQ4NjU0ODEwYTQzZTllZGE4N2U2NzZjMCk7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfYTQ0NWEyZDQxMmM5NGU1NWFmNjFiYjRmYjZjYjAyOWEuYmluZFBvcHVwKHBvcHVwXzA4Y2Y2MGRhOGI0MjRmZGM5NzFlN2Y5MmRiMTczZTYxKQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9kYmViZmNiNDE3Y2E0ZDNlYjE4NmMxMGFjZmQ5YTExNCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjIwODI3MywgNTUuMjYwNjAxNV0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiYiIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJiIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiAwLjY3NDk5OTk5OTk5OTk5OTksICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwX2NlNTBlZGVhMjJlZDRkNmM4ZjZmMDUwZDRhNmZhNGQzID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF9kOTdiOWE2Mzg4NTQ0NzNjODhmODBmNTk5MWQ4NjI0ZiA9ICQoYDxkaXYgaWQ9Imh0bWxfZDk3YjlhNjM4ODU0NDczYzg4ZjgwZjU5OTFkODYyNGYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiBTcG9uc29yZWRjaGl2YWw8YnI+VGVsZXBob25lOiArOTcxIDQgNDAzIDMxMTE8YnI+dXJsOiBodHRwOi8vd3d3LmNoaXZhbGxhdmlsbGUuY29tLzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF9jZTUwZWRlYTIyZWQ0ZDZjOGY2ZjA1MGQ0YTZmYTRkMy5zZXRDb250ZW50KGh0bWxfZDk3YjlhNjM4ODU0NDczYzg4ZjgwZjU5OTFkODYyNGYpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyX2RiZWJmY2I0MTdjYTRkM2ViMTg2YzEwYWNmZDlhMTE0LmJpbmRQb3B1cChwb3B1cF9jZTUwZWRlYTIyZWQ0ZDZjOGY2ZjA1MGQ0YTZmYTRkMykKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZWM4MzIwZDgyOGVhNGIzMDljZjY0YThjNDJkMGFiMzggPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4xMzM4Nzc3LCA1NS4xODQ3NjI1XSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJiIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogImIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDIsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwXzU2Y2U4MmMzYzNhYjQyMTY4Zjg4YjkwODkyYzA0OWNiID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF9mYThkNGU0NjdhMWE0Zjc3OGU1NGEwMGEwYmZmMmNlOCA9ICQoYDxkaXYgaWQ9Imh0bWxfZmE4ZDRlNDY3YTFhNGY3NzhlNTRhMDBhMGJmZjJjZTgiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiBTcG9uc29yZWRmb2xseSBieSBuaWNrICYgc2NvdHQ8YnI+VGVsZXBob25lOiArOTcxIDQgNDMwIDg1MzU8YnI+dXJsOiBodHRwOi8vZm9sbHkuYWUvPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwXzU2Y2U4MmMzYzNhYjQyMTY4Zjg4YjkwODkyYzA0OWNiLnNldENvbnRlbnQoaHRtbF9mYThkNGU0NjdhMWE0Zjc3OGU1NGEwMGEwYmZmMmNlOCk7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfZWM4MzIwZDgyOGVhNGIzMDljZjY0YThjNDJkMGFiMzguYmluZFBvcHVwKHBvcHVwXzU2Y2U4MmMzYzNhYjQyMTY4Zjg4YjkwODkyYzA0OWNiKQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl85MTMwNGE0YjFjNzA0NjYxOTEwNWNhMjI3MWIzNzA2NiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjA4MDYzNiwgNTUuMTM1NTMxOF0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiYiIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJiIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiAyLCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF82OGY0MzEwMGNjMWY0YWMzOWY5MTc0OTY1NzY5YjQ2ZCA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfOTJiNWExNjY4NTNkNDJmZGFlM2IwZWRmOTBlMzE2ODEgPSAkKGA8ZGl2IGlkPSJodG1sXzkyYjVhMTY2ODUzZDQyZmRhZTNiMGVkZjkwZTMxNjgxIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogMS4gYXNpbCByZXN0YXVyYW50PGJyPlRlbGVwaG9uZTogKzk3MSA1MiAxNjAgMDMzMzxicj51cmw6IGh0dHA6Ly93d3cuYXNpbHJlc3RhdXJhbnQuY29tLzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF82OGY0MzEwMGNjMWY0YWMzOWY5MTc0OTY1NzY5YjQ2ZC5zZXRDb250ZW50KGh0bWxfOTJiNWExNjY4NTNkNDJmZGFlM2IwZWRmOTBlMzE2ODEpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyXzkxMzA0YTRiMWM3MDQ2NjE5MTA1Y2EyMjcxYjM3MDY2LmJpbmRQb3B1cChwb3B1cF82OGY0MzEwMGNjMWY0YWMzOWY5MTc0OTY1NzY5YjQ2ZCkKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMWE3MTEzZDMxY2QyNDA5ZWI2N2JhNTYxMWJhNjRmOTkgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4yMzE0OTgyLCA1NS4zNDY5NTU5XSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJiIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogImIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDIsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwXzMwYmVjZjBjMTg4MTQ3M2VhYTBhYTc4ZmU5Mjg5MzliID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF80MzE4M2IxNDRhYmE0NTNkOWI4MjU2ZDY0Y2Q5MjIyYiA9ICQoYDxkaXYgaWQ9Imh0bWxfNDMxODNiMTQ0YWJhNDUzZDliODI1NmQ2NGNkOTIyMmIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiAyLiBtZXp6YWx1bmE8YnI+VGVsZXBob25lOiArOTcxIDQgNzAxIDExMjg8YnI+dXJsOiBodHRwOi8vd3d3LmRpbmluZ2RmYy5jb20vUmVzdGF1cmFudC1kZXRhaWxzLzI0L01lenphTHVuYTwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF8zMGJlY2YwYzE4ODE0NzNlYWEwYWE3OGZlOTI4OTM5Yi5zZXRDb250ZW50KGh0bWxfNDMxODNiMTQ0YWJhNDUzZDliODI1NmQ2NGNkOTIyMmIpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyXzFhNzExM2QzMWNkMjQwOWViNjdiYTU2MTFiYTY0Zjk5LmJpbmRQb3B1cChwb3B1cF8zMGJlY2YwYzE4ODE0NzNlYWEwYWE3OGZlOTI4OTM5YikKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNGU2ODc5MjVhZTllNGNhM2E1YjgyNTUyZjE0OGIzYmIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4yNTMxNzQ1LCA1NS4zNjU2NzI4XSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJiIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogImIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDIsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwX2I5YjI5NzQwNmFlODQ0YTFhMGRkNDU2MWY1Mzg4YzIzID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF81ZmZmNjA2OTE4NDY0OTJmYTE0MTg3MzBkZTBhNWQxMSA9ICQoYDxkaXYgaWQ9Imh0bWxfNWZmZjYwNjkxODQ2NDkyZmExNDE4NzMwZGUwYTVkMTEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiAzLiBjYWRpeiAtIGFobGFuIGxvdW5nZSBAIGdhdGUgYjI2PGJyPlRlbGVwaG9uZTogKzk3MSA0IDUwNSAyMDAwPGJyPnVybDogaHR0cDovL3d3dy5kdWJhaWludGxob3RlbHMuY29tL2RpbmluZy9haGxhbi1sb3VuZ2UtYjwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF9iOWIyOTc0MDZhZTg0NGExYTBkZDQ1NjFmNTM4OGMyMy5zZXRDb250ZW50KGh0bWxfNWZmZjYwNjkxODQ2NDkyZmExNDE4NzMwZGUwYTVkMTEpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyXzRlNjg3OTI1YWU5ZTRjYTNhNWI4MjU1MmYxNDhiM2JiLmJpbmRQb3B1cChwb3B1cF9iOWIyOTc0MDZhZTg0NGExYTBkZDQ1NjFmNTM4OGMyMykKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMjg2Yjg1NWQwYjc2NGQ2OWE3MmNhYzk3MmZjMGU0NWUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4xMDQzMjk2LCA1NS4xNDg3NjkxXSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJiIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogImIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDIsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwXzg5ODNiOTMyZTkwMTQyNGI5NDc0MWFkZGNjM2IxZDI2ID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF83YjFlODIxMDA3MWE0NjliOTM1Y2ExNmJkZDEyNzk0YiA9ICQoYDxkaXYgaWQ9Imh0bWxfN2IxZTgyMTAwNzFhNDY5YjkzNWNhMTZiZGQxMjc5NGIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiA0LiBibHZkIG9uIG9uZTxicj5UZWxlcGhvbmU6ICs5NzEgNCA0NTUgOTk4OTxicj51cmw6IGh0dHA6Ly9maXZlaG90ZWxzYW5kcmVzb3J0cy5jb20vZGluZS1kcmluay1kYW5jZS9yZXN0YXVyYW50cy9ibHZkLW9uLW9uZS88L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfODk4M2I5MzJlOTAxNDI0Yjk0NzQxYWRkY2MzYjFkMjYuc2V0Q29udGVudChodG1sXzdiMWU4MjEwMDcxYTQ2OWI5MzVjYTE2YmRkMTI3OTRiKTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl8yODZiODU1ZDBiNzY0ZDY5YTcyY2FjOTcyZmMwZTQ1ZS5iaW5kUG9wdXAocG9wdXBfODk4M2I5MzJlOTAxNDI0Yjk0NzQxYWRkY2MzYjFkMjYpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2VlYmZmMTRhMmE3YzQ2NzE4MzA4MTExMjU4MjI5MzZmID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMjQ4MTQ2MiwgNTUuMjg2NjUyNV0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiYiIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJiIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiAyLCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF8xMzkzY2UwY2UzNjg0OWMyOGFmZjdiMWQyNGRlYzUzMiA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfMDZlNmIyYzUxZDgwNDU2NjkyZjE2ZWNjODUwZGMzMjYgPSAkKGA8ZGl2IGlkPSJodG1sXzA2ZTZiMmM1MWQ4MDQ1NjY5MmYxNmVjYzg1MGRjMzI2IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogNS4gcHVyYW5pIGRpbGxpIGR1YmFpPGJyPlRlbGVwaG9uZTogKzk3MSA1MCAyMTEgNjgxNjxicj51cmw6IGh0dHA6Ly93d3cucHVyYW5pZGlsbGlkdWJhaS5jb20vPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwXzEzOTNjZTBjZTM2ODQ5YzI4YWZmN2IxZDI0ZGVjNTMyLnNldENvbnRlbnQoaHRtbF8wNmU2YjJjNTFkODA0NTY2OTJmMTZlY2M4NTBkYzMyNik7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfZWViZmYxNGEyYTdjNDY3MTgzMDgxMTEyNTgyMjkzNmYuYmluZFBvcHVwKHBvcHVwXzEzOTNjZTBjZTM2ODQ5YzI4YWZmN2IxZDI0ZGVjNTMyKQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl83OWJmNWQ2ZjU5ZjY0MjA4YWViNGYwOWJmOTgxZWNhOSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjIwODI3MywgNTUuMjYwNjAxNV0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiYiIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJiIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiAyLCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF84NjM3ZTgxMTZjYzU0NjFkOTc2NTUyN2Y2ZWZlOTJiNSA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfODU2ZmJmYTRjOGZhNDkxMDk2Mjk4NGIxM2QwNDdmZTQgPSAkKGA8ZGl2IGlkPSJodG1sXzg1NmZiZmE0YzhmYTQ5MTA5NjI5ODRiMTNkMDQ3ZmU0IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogU3BvbnNvcmVkZ3JhcGVza2luIGdyYXBlIGJhciBhbmQga2l0Y2hlbjxicj5UZWxlcGhvbmU6ICs5NzEgNCA0MDMgMzExMTxicj51cmw6IGh0dHA6Ly93d3cubGl2ZWxhdmlsbGUuY29tL2RpbmluZy9HcmFwZXNraW4vaW5kZXguYXNweDwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF84NjM3ZTgxMTZjYzU0NjFkOTc2NTUyN2Y2ZWZlOTJiNS5zZXRDb250ZW50KGh0bWxfODU2ZmJmYTRjOGZhNDkxMDk2Mjk4NGIxM2QwNDdmZTQpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyXzc5YmY1ZDZmNTlmNjQyMDhhZWI0ZjA5YmY5ODFlY2E5LmJpbmRQb3B1cChwb3B1cF84NjM3ZTgxMTZjYzU0NjFkOTc2NTUyN2Y2ZWZlOTJiNSkKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYzNmZDY4M2RlYWQzNGI4NzhhNmVjNzkyMzFjZTY1ZmMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4xMDQzMjk2LCA1NS4xNDg3NjkxXSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJiIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogImIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDIsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwXzgyNzg3MmVmNzQzZDQyMWNhMWE2NmY1MTM3YzllODcyID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF82NWQxYTYxMzUyNzg0YmYwYWI3MjBiYWZiODkxNzBjNSA9ICQoYDxkaXYgaWQ9Imh0bWxfNjVkMWE2MTM1Mjc4NGJmMGFiNzIwYmFmYjg5MTcwYzUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiA2LiB0cmF0dG9yaWEgYnkgY2lucXVlPGJyPlRlbGVwaG9uZTogKzk3MSA0IDQ1NSA5OTg5PGJyPnVybDogaHR0cDovL2p1bWVpcmFodmlsbGFnZS5maXZlaG90ZWxzYW5kcmVzb3J0cy5jb20vbWVldC1taW5nbGUvdHJhdHRvcmlhLWJ5LWNpbnF1ZTwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF84Mjc4NzJlZjc0M2Q0MjFjYTFhNjZmNTEzN2M5ZTg3Mi5zZXRDb250ZW50KGh0bWxfNjVkMWE2MTM1Mjc4NGJmMGFiNzIwYmFmYjg5MTcwYzUpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyX2MzZmQ2ODNkZWFkMzRiODc4YTZlYzc5MjMxY2U2NWZjLmJpbmRQb3B1cChwb3B1cF84Mjc4NzJlZjc0M2Q0MjFjYTFhNjZmNTEzN2M5ZTg3MikKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZWViN2I3MjdlNTcxNDY5YWJlYjBmYTAxOGRmMzI1ZTggPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4yNTY4NzU3LCA1NS4zMTIwODExXSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJiIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogImIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDIsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwX2M4NjE3YjBjMzNjNjQ4YjQ4NDVlOThmNjBmZjQxYmZlID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF80YWMxZmE1OTFlZGE0MDA1OWQ0MjJiN2IyMTY0Mjc1MCA9ICQoYDxkaXYgaWQ9Imh0bWxfNGFjMWZhNTkxZWRhNDAwNTlkNDIyYjdiMjE2NDI3NTAiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiA3LiBkb29ycyBmcmVlc3R5bGUgZ3JpbGw8YnI+VGVsZXBob25lOiArOTcxIDQgMjA0IDkyOTk8YnI+dXJsOiBodHRwOi8vd3d3LmRvb3JzZHViYWkuY29tL2VuPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwX2M4NjE3YjBjMzNjNjQ4YjQ4NDVlOThmNjBmZjQxYmZlLnNldENvbnRlbnQoaHRtbF80YWMxZmE1OTFlZGE0MDA1OWQ0MjJiN2IyMTY0Mjc1MCk7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfZWViN2I3MjdlNTcxNDY5YWJlYjBmYTAxOGRmMzI1ZTguYmluZFBvcHVwKHBvcHVwX2M4NjE3YjBjMzNjNjQ4YjQ4NDVlOThmNjBmZjQxYmZlKQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9mM2Q5ZDQwMzg2Zjg0NzBlODY4NmM3OTQ4YjQwMGI4MSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjA2NTc5MzQsIDU1LjEzODExNTldLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogImIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiYiIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogMiwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfMjVlMTI0ZTI4NmEwNDA1MDlmYTVjZTY3NTliNmY3MDQgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sX2Q0YzczZjhlOTk3NjQ2MmY5NjNkZTNhMjdmMGNiYmM5ID0gJChgPGRpdiBpZD0iaHRtbF9kNGM3M2Y4ZTk5NzY0NjJmOTYzZGUzYTI3ZjBjYmJjOSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDguIHVyYmFuIGJhciAmIGtpdGNoZW4gLSB1Yms8YnI+VGVsZXBob25lOiArOTcxIDQgNDM4IDAwMDA8YnI+dXJsOiBodHRwOi8vd3d3Lm1vdmVucGljay5jb20vZW4vbWlkZGxlLWVhc3QvdWFlL2R1YmFpL2R1YmFpLWp1bWVpcmFoLWxha2VzLXRvd2Vycy9yZXN0YXVyYW50cy9yZXN0YXVyYW50cy91cmJhbi1iYXIta2l0Y2hlbi11Yms8L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfMjVlMTI0ZTI4NmEwNDA1MDlmYTVjZTY3NTliNmY3MDQuc2V0Q29udGVudChodG1sX2Q0YzczZjhlOTk3NjQ2MmY5NjNkZTNhMjdmMGNiYmM5KTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl9mM2Q5ZDQwMzg2Zjg0NzBlODY4NmM3OTQ4YjQwMGI4MS5iaW5kUG9wdXAocG9wdXBfMjVlMTI0ZTI4NmEwNDA1MDlmYTVjZTY3NTliNmY3MDQpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2NlYWRlZDYyNDE1MzRhMWZiMTM1OTNlODA4MDM5MGY0ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMjMzODQ0MSwgNTUuMjY1NDgxMl0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiYiIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJiIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiAyLCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF9mOWExZWY0MjMzYWQ0OTM0YTI5NDU2ZWEzZWQ4MWUwNSA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfZDM3MzA3OWY4MjNkNGU0OWJlOTg3MGYwYTEyNjgzNjYgPSAkKGA8ZGl2IGlkPSJodG1sX2QzNzMwNzlmODIzZDRlNDliZTk4NzBmMGExMjY4MzY2IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogOS4gYmFyZWZvb3QgbG91bmdlPGJyPlRlbGVwaG9uZTogKzk3MSA0IDM0NiAxMTExPGJyPnVybDogaHR0cDovL3d3dy5keGJtYXJpbmUuY29tLzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF9mOWExZWY0MjMzYWQ0OTM0YTI5NDU2ZWEzZWQ4MWUwNS5zZXRDb250ZW50KGh0bWxfZDM3MzA3OWY4MjNkNGU0OWJlOTg3MGYwYTEyNjgzNjYpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyX2NlYWRlZDYyNDE1MzRhMWZiMTM1OTNlODA4MDM5MGY0LmJpbmRQb3B1cChwb3B1cF9mOWExZWY0MjMzYWQ0OTM0YTI5NDU2ZWEzZWQ4MWUwNSkKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNTBhNjIzZjUxNGIzNDI5MjgyNGNmYzcxNTQzMmIzYzYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4yMTI2NDI2LCA1NS4yODI0MDVdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogImIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiYiIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogMiwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfMDlkM2Y2MTczNWY2NGJiMGI4NTY4ODRjNzkwNTEwYjMgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzYwMWE2NGZiYmUzYTQ1MzE4ZDkxZTM5OTkwMzA3MTE4ID0gJChgPGRpdiBpZD0iaHRtbF82MDFhNjRmYmJlM2E0NTMxOGQ5MWUzOTk5MDMwNzExOCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDEwLiBtaW5hIGJyYXNzZXJpZTxicj5UZWxlcGhvbmU6ICs5NzEgNCA1MDYgMDEwMDxicj51cmw6IGh0dHA6Ly93d3cubWluYWJyYXNzZXJpZS5jb20vPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwXzA5ZDNmNjE3MzVmNjRiYjBiODU2ODg0Yzc5MDUxMGIzLnNldENvbnRlbnQoaHRtbF82MDFhNjRmYmJlM2E0NTMxOGQ5MWUzOTk5MDMwNzExOCk7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfNTBhNjIzZjUxNGIzNDI5MjgyNGNmYzcxNTQzMmIzYzYuYmluZFBvcHVwKHBvcHVwXzA5ZDNmNjE3MzVmNjRiYjBiODU2ODg0Yzc5MDUxMGIzKQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9lMjQ1OTBiNmFhMmI0ZGY0OTAzZTQ5YmEzNTI4MWRlNCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjIwODI3MywgNTUuMjYwNjAxNV0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiYiIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJiIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiAyLCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF82N2E5OGE1NjA4NGQ0M2VlOGZkNmNhYjVmMGUwYzRjOCA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfMTQxMTU4ZDNkMmUzNDEyYjlkZTE0YmE5ZThjNzViMzEgPSAkKGA8ZGl2IGlkPSJodG1sXzE0MTE1OGQzZDJlMzQxMmI5ZGUxNGJhOWU4Yzc1YjMxIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogU3BvbnNvcmVkZ3JhemUgZ2FzdHJvIGdyaWxsPGJyPlRlbGVwaG9uZTogKzk3MSA0IDQwMyAzMTExPGJyPnVybDogaHR0cDovL3d3dy5saXZlbGF2aWxsZS5jb20vZGluaW5nL0dyYXplL2luZGV4Lmh0bWw8L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfNjdhOThhNTYwODRkNDNlZThmZDZjYWI1ZjBlMGM0Yzguc2V0Q29udGVudChodG1sXzE0MTE1OGQzZDJlMzQxMmI5ZGUxNGJhOWU4Yzc1YjMxKTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl9lMjQ1OTBiNmFhMmI0ZGY0OTAzZTQ5YmEzNTI4MWRlNC5iaW5kUG9wdXAocG9wdXBfNjdhOThhNTYwODRkNDNlZThmZDZjYWI1ZjBlMGM0YzgpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzI2ZmI2YzIzZGExZjQ2NzNhNTlmZDdkNjUzOWQxODdhID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjQuODE2ODIwNiwgNTUuMjMxMjg3Ml0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiYiIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJiIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiAyLCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF9jM2NiY2YzZDE2NmI0NGI4OTc5ZTUwMWNiYWUxMjMxOCA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfMjBmYTFlMDkxNmFhNDhlZTg5NmE0YzgzMTZjYzM2MGQgPSAkKGA8ZGl2IGlkPSJodG1sXzIwZmExZTA5MTZhYTQ4ZWU4OTZhNGM4MzE2Y2MzNjBkIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogMTEuIGFsIHNhcmFiIHJvb2Z0b3AgbG91bmdlPGJyPlRlbGVwaG9uZTogKzk3MSA0IDgwOSA2MTAwPGJyPnVybDogaHR0cDovL3d3dy5tZXlkYW5ob3RlbHMuY29tL2JhYmFsc2hhbXMvZGluaW5nLmh0bTwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF9jM2NiY2YzZDE2NmI0NGI4OTc5ZTUwMWNiYWUxMjMxOC5zZXRDb250ZW50KGh0bWxfMjBmYTFlMDkxNmFhNDhlZTg5NmE0YzgzMTZjYzM2MGQpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyXzI2ZmI2YzIzZGExZjQ2NzNhNTlmZDdkNjUzOWQxODdhLmJpbmRQb3B1cChwb3B1cF9jM2NiY2YzZDE2NmI0NGI4OTc5ZTUwMWNiYWUxMjMxOCkKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYmMxODhjYWU4MDM4NDI5ZWFhMTVkNTM1ZDFlZmYxOTUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4wNDYyOTQ2LCA1NS4yMDMwNDExOTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiYiIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJiIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiAyLCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF9hZTQyZTQwODM5ZWE0NDM3YWYxOWU3MTVjZGNlN2ZiZiA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfZjU5ZTUyY2RlOTM2NDM3ZWI1YjZiODk2ZWNkNTliNDQgPSAkKGA8ZGl2IGlkPSJodG1sX2Y1OWU1MmNkZTkzNjQzN2ViNWI2Yjg5NmVjZDU5YjQ0IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogMTIuIHNvdWwgc3RyZWV0PGJyPlRlbGVwaG9uZTogKzk3MSA0IDQ1NSA5OTg5PGJyPnVybDogaHR0cDovL3NvdWwuc3QvPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwX2FlNDJlNDA4MzllYTQ0MzdhZjE5ZTcxNWNkY2U3ZmJmLnNldENvbnRlbnQoaHRtbF9mNTllNTJjZGU5MzY0MzdlYjViNmI4OTZlY2Q1OWI0NCk7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfYmMxODhjYWU4MDM4NDI5ZWFhMTVkNTM1ZDFlZmYxOTUuYmluZFBvcHVwKHBvcHVwX2FlNDJlNDA4MzllYTQ0MzdhZjE5ZTcxNWNkY2U3ZmJmKQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9mMzc1Yjc3NGQ5NWE0NzkzYjQ2YTkxMjRkYjIxODY0ZSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjI0OTE1NDksIDU1LjM0NzEzOTYwMDAwMDAxXSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJiIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogImIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDIsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwX2E2MWZjZWI5NTAyZTRiZWFiMTdiMWIxYmRlNjA4ZWIwID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF8yYTA3ZjFlNjBhN2U0MWFlODE3ZjU2MDQ0OWE5NWExYiA9ICQoYDxkaXYgaWQ9Imh0bWxfMmEwN2YxZTYwYTdlNDFhZTgxN2Y1NjA0NDlhOTVhMWIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiAxMy4gYmViZW1vczxicj5UZWxlcGhvbmU6ICs5NzEgNCA3MDIgMjQ1NTxicj51cmw6IGh0dHA6Ly93d3cuYmViZW1vc2R1YmFpLmNvbS88L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfYTYxZmNlYjk1MDJlNGJlYWIxN2IxYjFiZGU2MDhlYjAuc2V0Q29udGVudChodG1sXzJhMDdmMWU2MGE3ZTQxYWU4MTdmNTYwNDQ5YTk1YTFiKTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl9mMzc1Yjc3NGQ5NWE0NzkzYjQ2YTkxMjRkYjIxODY0ZS5iaW5kUG9wdXAocG9wdXBfYTYxZmNlYjk1MDJlNGJlYWIxN2IxYjFiZGU2MDhlYjApCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2E0YmE3OTljZWQwNDRhZjE5ZGViMDRhOGVjNzU5MGZkID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMjI4ODM5NCwgNTUuMzI2ODEyNV0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiYiIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJiIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiAyLCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF9lMzdiZDYzMjNhYTM0YWFjYjY5ODk0ODM5YjNmMzBjOSA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfY2U4ZDI3MmVlY2Y3NDk2M2ExZThlNDc0OGRmNWM5NTUgPSAkKGA8ZGl2IGlkPSJodG1sX2NlOGQyNzJlZWNmNzQ5NjNhMWU4ZTQ3NDhkZjVjOTU1IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogMTQuIGF3dGFyPGJyPlRlbGVwaG9uZTogKzk3MSA0IDMxNyAyMjIxPGJyPnVybDogaHR0cHM6Ly93d3cuaHlhdHRyZXN0YXVyYW50cy5jb20vZW4vZGluaW5nL3VhZS9kdWJhaS9taWRkbGUtZWFzdGVybi1yZXN0YXVyYW50LWluLWdhcmhvdWQtYXd0YXI/dXRtX3NvdXJjZT1nbWJsaXN0aW5nX2R4YmdoJnV0bV9tZWRpdW09YXd0YXImdXRtX2NhbXBhaWduPUdNQjwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF9lMzdiZDYzMjNhYTM0YWFjYjY5ODk0ODM5YjNmMzBjOS5zZXRDb250ZW50KGh0bWxfY2U4ZDI3MmVlY2Y3NDk2M2ExZThlNDc0OGRmNWM5NTUpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyX2E0YmE3OTljZWQwNDRhZjE5ZGViMDRhOGVjNzU5MGZkLmJpbmRQb3B1cChwb3B1cF9lMzdiZDYzMjNhYTM0YWFjYjY5ODk0ODM5YjNmMzBjOSkKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfM2U3NGJjMTFiZjljNDJlMmIwN2Q4N2E3OGQ3NGU3NjkgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4xOTg3NjUsIDU1LjI3OTYwNTNdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogImIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiYiIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogMiwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfNmQxZTJjM2UwYmYzNDgyODlkMzFlZTFjMGVlZjY1ODYgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzRjMzFmZmU3OWM0MjQ2NzU4ODFmOTdjYzc1YjMyMmMzID0gJChgPGRpdiBpZD0iaHRtbF80YzMxZmZlNzljNDI0Njc1ODgxZjk3Y2M3NWIzMjJjMyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDE1LiB0cmliZXMgY2Fybml2b3JlPGJyPlRlbGVwaG9uZTogKzk3MSA0IDIyNiA0OTc0PGJyPnVybDogaHR0cDovL3RyaWJlc3Jlc3RhdXJhbnQuY29tLzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF82ZDFlMmMzZTBiZjM0ODI4OWQzMWVlMWMwZWVmNjU4Ni5zZXRDb250ZW50KGh0bWxfNGMzMWZmZTc5YzQyNDY3NTg4MWY5N2NjNzViMzIyYzMpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyXzNlNzRiYzExYmY5YzQyZTJiMDdkODdhNzhkNzRlNzY5LmJpbmRQb3B1cChwb3B1cF82ZDFlMmMzZTBiZjM0ODI4OWQzMWVlMWMwZWVmNjU4NikKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfOGEyNzgyYjk4YzFlNGQ2NjkwMzQwZDJlNThlMjNjZmUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4yMjE2MDMsIDU1LjI4MDgyNjJdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogImIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiYiIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogMiwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfYTNjNTVlOTRmZTRhNDg5N2JmYmFiZjFkNjBmNTA0MDcgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sX2Q5YjI4NTU3OGJlMjRjZWJiMzE4ZjA1YzZmZjIyOTkzID0gJChgPGRpdiBpZD0iaHRtbF9kOWIyODU1NzhiZTI0Y2ViYjMxOGYwNWM2ZmYyMjk5MyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IFNwb25zb3JlZHN1c2hpIG5hdGlvbnM8YnI+VGVsZXBob25lOiArOTcxIDU2IDE4OCA4NTIyPGJyPnVybDogaHR0cHM6Ly9zdXNoaW5hdGlvbnMuYWUvPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwX2EzYzU1ZTk0ZmU0YTQ4OTdiZmJhYmYxZDYwZjUwNDA3LnNldENvbnRlbnQoaHRtbF9kOWIyODU1NzhiZTI0Y2ViYjMxOGYwNWM2ZmYyMjk5Myk7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfOGEyNzgyYjk4YzFlNGQ2NjkwMzQwZDJlNThlMjNjZmUuYmluZFBvcHVwKHBvcHVwX2EzYzU1ZTk0ZmU0YTQ4OTdiZmJhYmYxZDYwZjUwNDA3KQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl80ZTM3YjJhMmUxOTE0NjlhOTUxZGE3NjJlNmFkMDAzNiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjI3ODg5OCwgNTUuMzA0NDYwN10sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiYiIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJiIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiAyLCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF9hMTVjNDQ2YmE2MmY0OWY4YjdlYmVkMWJlOGU5ODIyNCA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfMTlkYjg2ZjA0YmQzNDg3ZmE2YmRlOWM1YTQxMGY4OGIgPSAkKGA8ZGl2IGlkPSJodG1sXzE5ZGI4NmYwNGJkMzQ4N2ZhNmJkZTljNWE0MTBmODhiIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogMTYuIGFsIGRhd2FhciByZXZvbHZpbmcgcmVzdGF1cmFudDxicj5UZWxlcGhvbmU6ICs5NzEgNCAyMDkgNjkxMjxicj51cmw6IGh0dHA6Ly93d3cuaHlhdHRyZXN0YXVyYW50cy5jb20vZW4vZGluaW5nL3VhZS9kdWJhaS9pbnRlcm5hdGlvbmFsLXJlc3RhdXJhbnQtaW4tZGVpcmEtY29ybmljaGUtYWwtZGF3YWFyLXJldm9sdmluZy1yZXN0YXVyYW50PC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwX2ExNWM0NDZiYTYyZjQ5ZjhiN2ViZWQxYmU4ZTk4MjI0LnNldENvbnRlbnQoaHRtbF8xOWRiODZmMDRiZDM0ODdmYTZiZGU5YzVhNDEwZjg4Yik7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfNGUzN2IyYTJlMTkxNDY5YTk1MWRhNzYyZTZhZDAwMzYuYmluZFBvcHVwKHBvcHVwX2ExNWM0NDZiYTYyZjQ5ZjhiN2ViZWQxYmU4ZTk4MjI0KQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl82MDA2NjQ1NjQxMTA0YzMxOGU5NTg5OGZhOTdhY2IzNSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjExMTM5OTEsIDU1LjEzNzIxNThdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogImIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiYiIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogMiwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfZjQ0MjQwNGU3MTJlNDg0NzlmNjJiMmVmYTU2YTM4MjEgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sX2UzZTU2MjQxNDYxMTQzMjQ5NzE2NjMyNmM2ZDM0MDNjID0gJChgPGRpdiBpZD0iaHRtbF9lM2U1NjI0MTQ2MTE0MzI0OTcxNjYzMjZjNmQzNDAzYyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDE3LiBraHliZXI8YnI+VGVsZXBob25lOiArOTcxIDQgNDU1IDExMTE8YnI+dXJsOiBodHRwczovL3d3dy5kdWtlc2R1YmFpLmNvbS9raHliZXIvPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwX2Y0NDI0MDRlNzEyZTQ4NDc5ZjYyYjJlZmE1NmEzODIxLnNldENvbnRlbnQoaHRtbF9lM2U1NjI0MTQ2MTE0MzI0OTcxNjYzMjZjNmQzNDAzYyk7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfNjAwNjY0NTY0MTEwNGMzMThlOTU4OThmYTk3YWNiMzUuYmluZFBvcHVwKHBvcHVwX2Y0NDI0MDRlNzEyZTQ4NDc5ZjYyYjJlZmE1NmEzODIxKQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9lNmU2NmU5MDUyNWU0YTNiYjM1NDU0MjlkZGI3N2Y0NyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjI2NjI2NzgsIDU1LjMwODc4NzQ5OTk5OTk5XSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJiIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogImIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDIsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwXzBiNmYyYmVmYTM2ZjQzNzlhMzI3YTQ0YWI5NTdiZGU2ID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF80OGVkZGFhODA1ZTA0NjhmODU1ZWI1OGVjZjYzNWEyOCA9ICQoYDxkaXYgaWQ9Imh0bWxfNDhlZGRhYTgwNWUwNDY4Zjg1NWViNThlY2Y2MzVhMjgiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiAxOC4gZGFuaWFsIHJlc3RhdXJhbnQ8YnI+VGVsZXBob25lOiArOTcxIDQgMjI3IDc2Njk8YnI+dXJsOiBodHRwOi8vd3d3LmRhbmlhbHJlc3RhdXJhbnQuY29tLzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF8wYjZmMmJlZmEzNmY0Mzc5YTMyN2E0NGFiOTU3YmRlNi5zZXRDb250ZW50KGh0bWxfNDhlZGRhYTgwNWUwNDY4Zjg1NWViNThlY2Y2MzVhMjgpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyX2U2ZTY2ZTkwNTI1ZTRhM2JiMzU0NTQyOWRkYjc3ZjQ3LmJpbmRQb3B1cChwb3B1cF8wYjZmMmJlZmEzNmY0Mzc5YTMyN2E0NGFiOTU3YmRlNikKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNDA0MTc1MGJjZGMyNDM0NDgzMTk5MGIyZDc1MWRlOWYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4yMzQzNTUsIDU1LjMyNDAxNDddLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogImIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiYiIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogMiwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfY2FkZjA0Y2QzNmMzNGUyYzhhZGQyZmM1MzkyNjRlN2QgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzg3ZWE1MTVmYzM3ODRiZmM4NGNlNDQ4NDkxNjVlNGUzID0gJChgPGRpdiBpZD0iaHRtbF84N2VhNTE1ZmMzNzg0YmZjODRjZTQ0ODQ5MTY1ZTRlMyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDE5LiBldmUgcGVudGhvdXNlICYgbG91bmdlPGJyPlRlbGVwaG9uZTogKzk3MSA0IDU1MyAxMjE0PGJyPnVybDogaHR0cDovL3d3dy5oeWF0dHJlc3RhdXJhbnRzLmNvbS9lbi9kaW5pbmcvdWFlL2R1YmFpL2ludGVybmF0aW9uYWwtcmVzdGF1cmFudC1pbi1vdWQtbWV0aGEtcm9hZC1ldmUtcGVudGhvdXNlLWxvdW5nZT91dG1fc291cmNlPVdlYnNpdGVfZHhiaGMmdXRtX21lZGl1bT1ldmUmdXRtX2NhbXBhaWduPUh5YXR0PC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwX2NhZGYwNGNkMzZjMzRlMmM4YWRkMmZjNTM5MjY0ZTdkLnNldENvbnRlbnQoaHRtbF84N2VhNTE1ZmMzNzg0YmZjODRjZTQ0ODQ5MTY1ZTRlMyk7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfNDA0MTc1MGJjZGMyNDM0NDgzMTk5MGIyZDc1MWRlOWYuYmluZFBvcHVwKHBvcHVwX2NhZGYwNGNkMzZjMzRlMmM4YWRkMmZjNTM5MjY0ZTdkKQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8wNzVkZTlkMjE3YWM0OTM5YWM5ZmViMWQ0YjM2ZDkxYiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjE5ODc2NSwgNTUuMjc5NjA1M10sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiYiIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJiIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiAyLCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF82MjRmMGM4ZjNiMWY0ZDA2YWY5NWFiZjM4OWNlYjdmNiA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfN2UwZWJlYjc1YmI1NDJkNWE0YzdiZmQ0NDQ2ZTQxN2UgPSAkKGA8ZGl2IGlkPSJodG1sXzdlMGViZWI3NWJiNTQyZDVhNGM3YmZkNDQ0NmU0MTdlIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogMjAuIHRoZSBncmlsbCBzaGFjazxicj5UZWxlcGhvbmU6ICs5NzEgNCAzODggMjM4Mjxicj51cmw6IGh0dHA6Ly93d3cudGhlZ3JpbGxsc2hhY2suY29tLzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF82MjRmMGM4ZjNiMWY0ZDA2YWY5NWFiZjM4OWNlYjdmNi5zZXRDb250ZW50KGh0bWxfN2UwZWJlYjc1YmI1NDJkNWE0YzdiZmQ0NDQ2ZTQxN2UpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyXzA3NWRlOWQyMTdhYzQ5MzlhYzlmZWIxZDRiMzZkOTFiLmJpbmRQb3B1cChwb3B1cF82MjRmMGM4ZjNiMWY0ZDA2YWY5NWFiZjM4OWNlYjdmNikKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYTY4NzQ4N2ZjODMyNGMwOWJhNDAzZmQ3NmNlNzc1NWIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4yNDc4NjcsIDU1LjMwMDQ5MjVdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogImIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiYiIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogMiwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfMThkNThjNDExYmY5NDNkNmI1ODI4YjI4MWRjYmVjMjcgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzhlNWI2YjUyZDAyNjRhZDdiNTA0ODQzYjEwMDZiMjNhID0gJChgPGRpdiBpZD0iaHRtbF84ZTViNmI1MmQwMjY0YWQ3YjUwNDg0M2IxMDA2YjIzYSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IFNwb25zb3JlZGFtcml0c3IgcmVzdGF1cmFudDxicj5UZWxlcGhvbmU6ICs5NzEgNTAgNjc4IDAwOTY8YnI+dXJsOiBodHRwOi8vYW1yaXRzcnVhZS5jb20vPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwXzE4ZDU4YzQxMWJmOTQzZDZiNTgyOGIyODFkY2JlYzI3LnNldENvbnRlbnQoaHRtbF84ZTViNmI1MmQwMjY0YWQ3YjUwNDg0M2IxMDA2YjIzYSk7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfYTY4NzQ4N2ZjODMyNGMwOWJhNDAzZmQ3NmNlNzc1NWIuYmluZFBvcHVwKHBvcHVwXzE4ZDU4YzQxMWJmOTQzZDZiNTgyOGIyODFkY2JlYzI3KQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9kOTk1OWNjYjU4YmY0YTY5YWFhOGEwMzBjOWI1Mjk5ZiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjEwNDMyOTYsIDU1LjE0ODc2OTFdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogImIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiYiIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogMiwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfZmRjOGM2N2Q2YzY2NDBkOTlmNzBkNzI4MWNmYWQ1NmYgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzMwNWVjYWE4MDYxYTQ3MzlhNmQ0NmI4ZTMwNDAxYTAwID0gJChgPGRpdiBpZD0iaHRtbF8zMDVlY2FhODA2MWE0NzM5YTZkNDZiOGUzMDQwMWEwMCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDIxLiBtYWlkZW4gc2hhbmdoYWk8YnI+VGVsZXBob25lOiArOTcxIDQgNDU1IDk5ODk8YnI+dXJsOiBodHRwOi8vZml2ZWhvdGVsc2FuZHJlc29ydHMuY29tL2RpbmUtZHJpbmstZGFuY2UvcmVzdGF1cmFudHMvbWFpZGVuLXNoYW5naGFpLzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF9mZGM4YzY3ZDZjNjY0MGQ5OWY3MGQ3MjgxY2ZhZDU2Zi5zZXRDb250ZW50KGh0bWxfMzA1ZWNhYTgwNjFhNDczOWE2ZDQ2YjhlMzA0MDFhMDApOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyX2Q5OTU5Y2NiNThiZjRhNjlhYWE4YTAzMGM5YjUyOTlmLmJpbmRQb3B1cChwb3B1cF9mZGM4YzY3ZDZjNjY0MGQ5OWY3MGQ3MjgxY2ZhZDU2ZikKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMTBiNTQ0ODhjNGQ4NGQzZWE2NTRjOGZkZjA1NjIzZDAgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4yMTQwMTMzLCA1NS4yNzYwODg1XSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJiIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogImIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDIsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwXzMwY2FjNmYxNjQ4YjQ0N2NiN2FhYjEyYWFlZTNjZjQ2ID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF8wMDY5MzFkYzBlMzQ0NDU1OTVkNTY2Yzk0MjM2YmQ5NCA9ICQoYDxkaXYgaWQ9Imh0bWxfMDA2OTMxZGMwZTM0NDQ1NTk1ZDU2NmM5NDIzNmJkOTQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiAyMi4gcHVyYW5pIGRpbGxpIHNoZWlraCB6YXllZCByb2FkPGJyPlRlbGVwaG9uZTogKzk3MSA0IDMxNiA5NzI2PGJyPnVybDogaHR0cDovL3d3dy5wdXJhbmlkaWxsaWR1YmFpLmNvbS9zaGVpa2h6YXllZHJvYWQ8L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfMzBjYWM2ZjE2NDhiNDQ3Y2I3YWFiMTJhYWVlM2NmNDYuc2V0Q29udGVudChodG1sXzAwNjkzMWRjMGUzNDQ0NTU5NWQ1NjZjOTQyMzZiZDk0KTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl8xMGI1NDQ4OGM0ZDg0ZDNlYTY1NGM4ZmRmMDU2MjNkMC5iaW5kUG9wdXAocG9wdXBfMzBjYWM2ZjE2NDhiNDQ3Y2I3YWFiMTJhYWVlM2NmNDYpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzFmMGQ1MWJmMmQwMDQ5MTQ4Y2RiNGFmMDBkMTg2YWE4ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMjE0MDEzMywgNTUuMjc2MDg4NV0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiYiIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJiIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiAyLCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF9iYzdiYTM1OWRlOTQ0NWVhYTYzMWZiZDA1NzRmODZkNCA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfMWY3ZjJkNDY1ZDhkNGU0MDk3NDU2ZjYxNWU5ZGM2ZDYgPSAkKGA8ZGl2IGlkPSJodG1sXzFmN2YyZDQ2NWQ4ZDRlNDA5NzQ1NmY2MTVlOWRjNmQ2IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogMjMuIGxldmVsIDQzIHNreSBsb3VuZ2U8YnI+VGVsZXBob25lOiArOTcxIDU2IDQxNCAyMjEzPGJyPnVybDogaHR0cDovL3d3dy5sZXZlbDQzbG91bmdlLmNvbS88L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfYmM3YmEzNTlkZTk0NDVlYWE2MzFmYmQwNTc0Zjg2ZDQuc2V0Q29udGVudChodG1sXzFmN2YyZDQ2NWQ4ZDRlNDA5NzQ1NmY2MTVlOWRjNmQ2KTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl8xZjBkNTFiZjJkMDA0OTE0OGNkYjRhZjAwZDE4NmFhOC5iaW5kUG9wdXAocG9wdXBfYmM3YmEzNTlkZTk0NDVlYWE2MzFmYmQwNTc0Zjg2ZDQpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzBjYzczYTNiYzkyZDRiYzg4MDYyMGZjOWI0Y2UwMDUxID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMTk1MTU1NCwgNTUuMjc1MTU3OV0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiYiIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJiIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiAyLCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF84YmMxMWU5ZjhjOTI0MTEwODIwYzc2ZmFhZjI5YThjMyA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfZGIwYTc1OTFkYWRlNGViYzgyYzlhODZjMDBmMzAwYWEgPSAkKGA8ZGl2IGlkPSJodG1sX2RiMGE3NTkxZGFkZTRlYmM4MmM5YTg2YzAwZjMwMGFhIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogMjQuIGJsYWNrIHRhcCBjcmFmdCBidXJnZXJzICYgc2hha2VzIGR1YmFpIG1hbGw8YnI+VGVsZXBob25lOiArOTcxIDQgMzMwIDUxMDM8YnI+dXJsOiBodHRwOi8vd3d3LmJsYWNrdGFwbWUuY29tLzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF84YmMxMWU5ZjhjOTI0MTEwODIwYzc2ZmFhZjI5YThjMy5zZXRDb250ZW50KGh0bWxfZGIwYTc1OTFkYWRlNGViYzgyYzlhODZjMDBmMzAwYWEpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyXzBjYzczYTNiYzkyZDRiYzg4MDYyMGZjOWI0Y2UwMDUxLmJpbmRQb3B1cChwb3B1cF84YmMxMWU5ZjhjOTI0MTEwODIwYzc2ZmFhZjI5YThjMykKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfY2FjNmNlYzY3ZTYzNDM0MTlmYmUzMDk0ZjIwZjQyNWUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4yNDkxNTQ5LCA1NS4zNDcxMzk2MDAwMDAwMV0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiYiIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJiIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiAyLCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF9iMDYxNTdhOGQ4NDM0MzM0Yjk1OTcxMTRkYjc1ODgxNyA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfZGIzMTUyZGVhNjFhNDVlOGEyNTQwMmQ1YWMwMWU1YTYgPSAkKGA8ZGl2IGlkPSJodG1sX2RiMzE1MmRlYTYxYTQ1ZThhMjU0MDJkNWFjMDFlNWE2IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogMjUuIGJlZWYgYmlzdHJvPGJyPlRlbGVwaG9uZTogKzk3MSA0IDcwMiAyNDU1PGJyPnVybDogaHR0cDovL3d3dy5iZWVmYmlzdHJvZHViYWkuY29tLzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF9iMDYxNTdhOGQ4NDM0MzM0Yjk1OTcxMTRkYjc1ODgxNy5zZXRDb250ZW50KGh0bWxfZGIzMTUyZGVhNjFhNDVlOGEyNTQwMmQ1YWMwMWU1YTYpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyX2NhYzZjZWM2N2U2MzQzNDE5ZmJlMzA5NGYyMGY0MjVlLmJpbmRQb3B1cChwb3B1cF9iMDYxNTdhOGQ4NDM0MzM0Yjk1OTcxMTRkYjc1ODgxNykKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMWZlOTc2OTMxOTgwNGE1MmFkMDUwYTg5ZGNhNmQxYzMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4yMDI0NDg1LCA1NS4yMzk2NTI1XSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJiIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogImIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDIsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwXzhjOGMwMTMzM2I1MTQ3Yzc4MTVjNzJkMzE0OTk5MTMzID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF82ZGM2ODNmMDI5MDM0NjliODFhMDIyZmNiYWQzNTZmNCA9ICQoYDxkaXYgaWQ9Imh0bWxfNmRjNjgzZjAyOTAzNDY5YjgxYTAyMmZjYmFkMzU2ZjQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiBTcG9uc29yZWR2ZXJkZSBkdWJhaTxicj5UZWxlcGhvbmU6ICs5NzEgNCAzMzMgODAyNTxicj51cmw6IGh0dHA6Ly93d3cudmVyZGUtZHViYWkuY29tLzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF84YzhjMDEzMzNiNTE0N2M3ODE1YzcyZDMxNDk5OTEzMy5zZXRDb250ZW50KGh0bWxfNmRjNjgzZjAyOTAzNDY5YjgxYTAyMmZjYmFkMzU2ZjQpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyXzFmZTk3NjkzMTk4MDRhNTJhZDA1MGE4OWRjYTZkMWMzLmJpbmRQb3B1cChwb3B1cF84YzhjMDEzMzNiNTE0N2M3ODE1YzcyZDMxNDk5OTEzMykKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZjU1NTMzMzAxYmI5NDIyYjg2OGMzMzYxZTFiYTI0ZjMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4yMjk1MzA5LCA1NS4yODY2NzI4XSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJiIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogImIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDIsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwXzEyNTJmYmRhMjNmZDRjMDE5MzkzNzI5ZDU2OGU1YjBlID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF84MWQzMjdmNzA5NTI0YzJhYmE3M2NkNzI5MzQ5NTI1ZiA9ICQoYDxkaXYgaWQ9Imh0bWxfODFkMzI3ZjcwOTUyNGMyYWJhNzNjZDcyOTM0OTUyNWYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiAyNi4gbmlkbyB0YXBhcyByZXN0YXVyYW50ICYgYmFyPGJyPlRlbGVwaG9uZTogKzk3MSA0IDMzMyAzMDU1PGJyPnVybDogaHR0cDovL25pZG9keGIuY29tLzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF8xMjUyZmJkYTIzZmQ0YzAxOTM5MzcyOWQ1NjhlNWIwZS5zZXRDb250ZW50KGh0bWxfODFkMzI3ZjcwOTUyNGMyYWJhNzNjZDcyOTM0OTUyNWYpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyX2Y1NTUzMzMwMWJiOTQyMmI4NjhjMzM2MWUxYmEyNGYzLmJpbmRQb3B1cChwb3B1cF8xMjUyZmJkYTIzZmQ0YzAxOTM5MzcyOWQ1NjhlNWIwZSkKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYTUyZTEzZTdkYTQyNDI5MGEzNDU1OGQ4YjEzYTE5MDUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4wODA0Nzc3LCA1NS4xNTQxOTQzMDAwMDAwMV0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiYiIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJiIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiAyLCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF8xMGZhMWE3MWNjN2U0ODg5YWY0YTJhOGViNjEyMzdhMyA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfYzNjZDBlYWM0NjAxNDE2ZmJhZjQyMDAwNjdhYzQ1NDkgPSAkKGA8ZGl2IGlkPSJodG1sX2MzY2QwZWFjNDYwMTQxNmZiYWY0MjAwMDY3YWM0NTQ5IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogMjcuIHNoYW1pYW5hPGJyPlRlbGVwaG9uZTogKzk3MSA0IDU3NCAxMTExPGJyPnVybDogaHR0cDovL3d3dy50YWpob3RlbHMuY29tL2VuLWluL3Rhai90YWotanVtZWlyYWgtbGFrZXMtdG93ZXJzL3Jlc3RhdXJhbnRzL3NoYW1pYW5hLzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF8xMGZhMWE3MWNjN2U0ODg5YWY0YTJhOGViNjEyMzdhMy5zZXRDb250ZW50KGh0bWxfYzNjZDBlYWM0NjAxNDE2ZmJhZjQyMDAwNjdhYzQ1NDkpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyX2E1MmUxM2U3ZGE0MjQyOTBhMzQ1NThkOGIxM2ExOTA1LmJpbmRQb3B1cChwb3B1cF8xMGZhMWE3MWNjN2U0ODg5YWY0YTJhOGViNjEyMzdhMykKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYTM4M2I5YjZlOGU1NDllMGE3MTdlN2NjZTdkYjc0ZmIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4yMDQ4NDkzLCA1NS4yNzA3ODI4XSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJiIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogImIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDIsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwXzhkOTM2N2NlNzZlMzQ4MzJhNGExMjc0MjkzYzhiYTAxID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF9kZTNkYzUwNWViZWM0NzUxOTg3YTA2YmQ4ZWMxYWVkMiA9ICQoYDxkaXYgaWQ9Imh0bWxfZGUzZGM1MDVlYmVjNDc1MTk4N2EwNmJkOGVjMWFlZDIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiAyOC4ga2luYXJhIGJ5IHZpa2FzIGtoYW5uYTxicj5UZWxlcGhvbmU6ICs5NzEgNCA4MTQgNTU1NTxicj51cmw6IGh0dHA6Ly93d3cua2luYXJhZHViYWkuY29tLzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF84ZDkzNjdjZTc2ZTM0ODMyYTRhMTI3NDI5M2M4YmEwMS5zZXRDb250ZW50KGh0bWxfZGUzZGM1MDVlYmVjNDc1MTk4N2EwNmJkOGVjMWFlZDIpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyX2EzODNiOWI2ZThlNTQ5ZTBhNzE3ZTdjY2U3ZGI3NGZiLmJpbmRQb3B1cChwb3B1cF84ZDkzNjdjZTc2ZTM0ODMyYTRhMTI3NDI5M2M4YmEwMSkKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMzVkYWM2NTFhNDdjNDAzZWFjMWZlNjYwMTEyZGU5OTMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4xMTA4MjAyLCA1NS4xMzk5MTg0MDAwMDAwMV0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiYiIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJiIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiAyLCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF9hZTYzOWFhNWI4ZDA0YjA0OTA1OWY0MTMwMmVkNzIzOSA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfMWM0MDFhZjg1NzQ5NDhlMWE1ZTU1YzU3NjNlZjkxMGEgPSAkKGA8ZGl2IGlkPSJodG1sXzFjNDAxYWY4NTc0OTQ4ZTFhNWU1NWM1NzYzZWY5MTBhIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogMjkuIGxpdHRsZSBtaXNzIGluZGlhPGJyPlRlbGVwaG9uZTogKzk3MSA0IDQ1NyAzNDU3PGJyPnVybDogaHR0cDovL3d3dy5mYWlybW9udC5jb20vcGFsbS1kdWJhaS9kaW5pbmcvbGl0dGxlLW1pc3MtaW5kaWEvPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwX2FlNjM5YWE1YjhkMDRiMDQ5MDU5ZjQxMzAyZWQ3MjM5LnNldENvbnRlbnQoaHRtbF8xYzQwMWFmODU3NDk0OGUxYTVlNTVjNTc2M2VmOTEwYSk7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfMzVkYWM2NTFhNDdjNDAzZWFjMWZlNjYwMTEyZGU5OTMuYmluZFBvcHVwKHBvcHVwX2FlNjM5YWE1YjhkMDRiMDQ5MDU5ZjQxMzAyZWQ3MjM5KQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9hYmRmNzAzYWMxZjM0MTg1ODJlY2M1MzFjNjJiZjNkMSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjExMDM0NywgNTUuMjIwNjI4Mjk5OTk5OTldLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogImIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiYiIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogMiwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfOTlmNzJkZDQzZDE1NGIyZjkwN2U1MzE5ZGU1NWUxY2YgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sX2QzZDBkYjZmNDRkNDRhOTJhZDJjZTNmN2VlMWVkNTJlID0gJChgPGRpdiBpZD0iaHRtbF9kM2QwZGI2ZjQ0ZDQ0YTkyYWQyY2UzZjdlZTFlZDUyZSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDMwLiBmaXNoIGh1dCBhc21hayBhbCBzdWx0YW4gc2VhZm9vZCByZXN0YXVyYW50PGJyPlRlbGVwaG9uZTogKzk3MSA1OCAxMjggMjg4Njxicj51cmw6IGh0dHA6Ly9kdWJhaWZpc2hodXRyZXN0YXVyYW50LmNvbS9pbmRleC5waHA8L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfOTlmNzJkZDQzZDE1NGIyZjkwN2U1MzE5ZGU1NWUxY2Yuc2V0Q29udGVudChodG1sX2QzZDBkYjZmNDRkNDRhOTJhZDJjZTNmN2VlMWVkNTJlKTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl9hYmRmNzAzYWMxZjM0MTg1ODJlY2M1MzFjNjJiZjNkMS5iaW5kUG9wdXAocG9wdXBfOTlmNzJkZDQzZDE1NGIyZjkwN2U1MzE5ZGU1NWUxY2YpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzZlNzgyMGQ2NTQ3NTQyODhiYWFhYjIyNzczMDRiYTM0ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMjA4MjczLCA1NS4yNjA2MDE1XSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJiIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogImIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDIsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwXzcwM2Y2MTBjY2EzMjRkNzg5ZDBjNmFmOTU2MzE2YjYyID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF85N2MxN2VmZGFjMDU0ZGQ4YWM2ZDMzNjBkYzc2NmU5OSA9ICQoYDxkaXYgaWQ9Imh0bWxfOTdjMTdlZmRhYzA1NGRkOGFjNmQzMzYwZGM3NjZlOTkiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiBTcG9uc29yZWRjaGl2YWw8YnI+VGVsZXBob25lOiArOTcxIDQgNDAzIDMxMTE8YnI+dXJsOiBodHRwOi8vd3d3LmNoaXZhbGxhdmlsbGUuY29tLzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF83MDNmNjEwY2NhMzI0ZDc4OWQwYzZhZjk1NjMxNmI2Mi5zZXRDb250ZW50KGh0bWxfOTdjMTdlZmRhYzA1NGRkOGFjNmQzMzYwZGM3NjZlOTkpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyXzZlNzgyMGQ2NTQ3NTQyODhiYWFhYjIyNzczMDRiYTM0LmJpbmRQb3B1cChwb3B1cF83MDNmNjEwY2NhMzI0ZDc4OWQwYzZhZjk1NjMxNmI2MikKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMWFmMzRlMmVlN2M2NGNlZWI3OWJkMzMzYThkZWVhZjYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4xMzM4Nzc3LCA1NS4xODQ3NjI1XSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJiIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogImIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDEwLCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF8wYzZiYTBjOGMwZDk0Y2QxOTEyYTUxMDM4ZjgwOGMzOSA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfOTVkYzUwZDU1OWEzNDc1NjkzNGU1MmYzMjMxYzEyZTQgPSAkKGA8ZGl2IGlkPSJodG1sXzk1ZGM1MGQ1NTlhMzQ3NTY5MzRlNTJmMzIzMWMxMmU0IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogU3BvbnNvcmVkZm9sbHkgYnkgbmljayAmIHNjb3R0PGJyPlRlbGVwaG9uZTogKzk3MSA0IDQzMCA4NTM1PGJyPnVybDogaHR0cDovL2ZvbGx5LmFlLzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF8wYzZiYTBjOGMwZDk0Y2QxOTEyYTUxMDM4ZjgwOGMzOS5zZXRDb250ZW50KGh0bWxfOTVkYzUwZDU1OWEzNDc1NjkzNGU1MmYzMjMxYzEyZTQpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyXzFhZjM0ZTJlZTdjNjRjZWViNzliZDMzM2E4ZGVlYWY2LmJpbmRQb3B1cChwb3B1cF8wYzZiYTBjOGMwZDk0Y2QxOTEyYTUxMDM4ZjgwOGMzOSkKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZTQxNDM3MGViOGNkNDlmYzg0YWU3MGJlY2U2OTdmMWEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4wODA2MzYsIDU1LjEzNTUzMThdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogImIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiYiIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogMTAsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwXzNhNzU5MDEwMzQ2YjQ3ZWNhMDBjZDJlYmRjNDRmMzVlID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF80Mjg0MjhkZDk4MGQ0M2Q3OTZiYWI1ZmUzYjAyZTk2OSA9ICQoYDxkaXYgaWQ9Imh0bWxfNDI4NDI4ZGQ5ODBkNDNkNzk2YmFiNWZlM2IwMmU5NjkiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiAxLiBhc2lsIHJlc3RhdXJhbnQ8YnI+VGVsZXBob25lOiArOTcxIDUyIDE2MCAwMzMzPGJyPnVybDogaHR0cDovL3d3dy5hc2lscmVzdGF1cmFudC5jb20vPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwXzNhNzU5MDEwMzQ2YjQ3ZWNhMDBjZDJlYmRjNDRmMzVlLnNldENvbnRlbnQoaHRtbF80Mjg0MjhkZDk4MGQ0M2Q3OTZiYWI1ZmUzYjAyZTk2OSk7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfZTQxNDM3MGViOGNkNDlmYzg0YWU3MGJlY2U2OTdmMWEuYmluZFBvcHVwKHBvcHVwXzNhNzU5MDEwMzQ2YjQ3ZWNhMDBjZDJlYmRjNDRmMzVlKQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9kOTAyOWU0NTcxYTI0NTVlYjVjZGMyN2QwOGEyMzg1YSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjIzMTQ5ODIsIDU1LjM0Njk1NTldLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogImIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiYiIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogMTAsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwXzI3ZTc5YzA0MDgxYTQ4MDJiYjgwNmJmMGYzODI4MzU3ID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF8wNjA2NGE5MzQ0OTE0YTFiYTE1YTJiNGUyYTMwY2FiZCA9ICQoYDxkaXYgaWQ9Imh0bWxfMDYwNjRhOTM0NDkxNGExYmExNWEyYjRlMmEzMGNhYmQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiAyLiBtZXp6YWx1bmE8YnI+VGVsZXBob25lOiArOTcxIDQgNzAxIDExMjg8YnI+dXJsOiBodHRwOi8vd3d3LmRpbmluZ2RmYy5jb20vUmVzdGF1cmFudC1kZXRhaWxzLzI0L01lenphTHVuYTwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF8yN2U3OWMwNDA4MWE0ODAyYmI4MDZiZjBmMzgyODM1Ny5zZXRDb250ZW50KGh0bWxfMDYwNjRhOTM0NDkxNGExYmExNWEyYjRlMmEzMGNhYmQpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyX2Q5MDI5ZTQ1NzFhMjQ1NWViNWNkYzI3ZDA4YTIzODVhLmJpbmRQb3B1cChwb3B1cF8yN2U3OWMwNDA4MWE0ODAyYmI4MDZiZjBmMzgyODM1NykKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYjRkOTZjY2JkOTBhNDNkNjk2NTY3MjQwNzFjZjc5ODkgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4yNTMxNzQ1LCA1NS4zNjU2NzI4XSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJiIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogImIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDEwLCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF9hMGZlNjdiNjZlNjQ0YWIxYWRjNjM5N2RkODYwZTU2MCA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfZDY1ZGNkMmIyNzA0NDgyMmExYmUwMDBjNGUxMWRjZjkgPSAkKGA8ZGl2IGlkPSJodG1sX2Q2NWRjZDJiMjcwNDQ4MjJhMWJlMDAwYzRlMTFkY2Y5IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogMy4gY2FkaXogLSBhaGxhbiBsb3VuZ2UgQCBnYXRlIGIyNjxicj5UZWxlcGhvbmU6ICs5NzEgNCA1MDUgMjAwMDxicj51cmw6IGh0dHA6Ly93d3cuZHViYWlpbnRsaG90ZWxzLmNvbS9kaW5pbmcvYWhsYW4tbG91bmdlLWI8L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfYTBmZTY3YjY2ZTY0NGFiMWFkYzYzOTdkZDg2MGU1NjAuc2V0Q29udGVudChodG1sX2Q2NWRjZDJiMjcwNDQ4MjJhMWJlMDAwYzRlMTFkY2Y5KTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl9iNGQ5NmNjYmQ5MGE0M2Q2OTY1NjcyNDA3MWNmNzk4OS5iaW5kUG9wdXAocG9wdXBfYTBmZTY3YjY2ZTY0NGFiMWFkYzYzOTdkZDg2MGU1NjApCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzA5Y2RmZGI4NjZhNjRjMTRhOGMxYTY2OTY0OGUyZDNlID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMTA0MzI5NiwgNTUuMTQ4NzY5MV0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiYiIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJiIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiAxMCwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfNTE3YjFkNmI3NTFjNGRhMzk2MmY4OTc3OTFiNTQzMzUgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzI5ODI2NWE2OTVmOTQxMTc5MDE0ZGNiMDg3ODMxOWJmID0gJChgPGRpdiBpZD0iaHRtbF8yOTgyNjVhNjk1Zjk0MTE3OTAxNGRjYjA4NzgzMTliZiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDQuIGJsdmQgb24gb25lPGJyPlRlbGVwaG9uZTogKzk3MSA0IDQ1NSA5OTg5PGJyPnVybDogaHR0cDovL2ZpdmVob3RlbHNhbmRyZXNvcnRzLmNvbS9kaW5lLWRyaW5rLWRhbmNlL3Jlc3RhdXJhbnRzL2JsdmQtb24tb25lLzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF81MTdiMWQ2Yjc1MWM0ZGEzOTYyZjg5Nzc5MWI1NDMzNS5zZXRDb250ZW50KGh0bWxfMjk4MjY1YTY5NWY5NDExNzkwMTRkY2IwODc4MzE5YmYpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyXzA5Y2RmZGI4NjZhNjRjMTRhOGMxYTY2OTY0OGUyZDNlLmJpbmRQb3B1cChwb3B1cF81MTdiMWQ2Yjc1MWM0ZGEzOTYyZjg5Nzc5MWI1NDMzNSkKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZWIzZjlhMDhhZDJkNGFjOGE0ZTk3MzZhZGU4NDU2YzggPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4yNDgxNDYyLCA1NS4yODY2NTI1XSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJiIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogImIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDEwLCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF80OTQyNTAwMzkxMjI0NDFlODE1YWU0MDEyZWJmMTU2MyA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfNWIwMjVmMjUxYjhmNDgzMmFiZjZhNjA4NTQ4ZmRmODQgPSAkKGA8ZGl2IGlkPSJodG1sXzViMDI1ZjI1MWI4ZjQ4MzJhYmY2YTYwODU0OGZkZjg0IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogNS4gcHVyYW5pIGRpbGxpIGR1YmFpPGJyPlRlbGVwaG9uZTogKzk3MSA1MCAyMTEgNjgxNjxicj51cmw6IGh0dHA6Ly93d3cucHVyYW5pZGlsbGlkdWJhaS5jb20vPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwXzQ5NDI1MDAzOTEyMjQ0MWU4MTVhZTQwMTJlYmYxNTYzLnNldENvbnRlbnQoaHRtbF81YjAyNWYyNTFiOGY0ODMyYWJmNmE2MDg1NDhmZGY4NCk7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfZWIzZjlhMDhhZDJkNGFjOGE0ZTk3MzZhZGU4NDU2YzguYmluZFBvcHVwKHBvcHVwXzQ5NDI1MDAzOTEyMjQ0MWU4MTVhZTQwMTJlYmYxNTYzKQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8xYTRhNzY4NGMxN2Q0ZTgzYThkYjlmMjAxNjcyNWE0OSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjIwODI3MywgNTUuMjYwNjAxNV0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiYiIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJiIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiAxMCwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfMTRkNTBlYzg3MTNiNDkwNDg3Y2ZkNjAxYjE5MWQ4NWYgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzAxMWQ1OGNmNWM1MzRmNjFhNGY5YzdmMTQ1NGU0MzAzID0gJChgPGRpdiBpZD0iaHRtbF8wMTFkNThjZjVjNTM0ZjYxYTRmOWM3ZjE0NTRlNDMwMyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IFNwb25zb3JlZGdyYXBlc2tpbiBncmFwZSBiYXIgYW5kIGtpdGNoZW48YnI+VGVsZXBob25lOiArOTcxIDQgNDAzIDMxMTE8YnI+dXJsOiBodHRwOi8vd3d3LmxpdmVsYXZpbGxlLmNvbS9kaW5pbmcvR3JhcGVza2luL2luZGV4LmFzcHg8L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfMTRkNTBlYzg3MTNiNDkwNDg3Y2ZkNjAxYjE5MWQ4NWYuc2V0Q29udGVudChodG1sXzAxMWQ1OGNmNWM1MzRmNjFhNGY5YzdmMTQ1NGU0MzAzKTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl8xYTRhNzY4NGMxN2Q0ZTgzYThkYjlmMjAxNjcyNWE0OS5iaW5kUG9wdXAocG9wdXBfMTRkNTBlYzg3MTNiNDkwNDg3Y2ZkNjAxYjE5MWQ4NWYpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzMyZDEyYTZjOGI1NTQ1NTBiMWQ5ODAxOGMwYjE0YmQwID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMTA0MzI5NiwgNTUuMTQ4NzY5MV0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiYiIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJiIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiAxMCwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfY2Y5ZjhhNGU1NDlmNDg2YThjYjYxODBjMmI4YTVhM2YgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzc1Mzg2ODYwYmM1ZjRhNGFhMDdiOWU1MzA5NzRkNWI2ID0gJChgPGRpdiBpZD0iaHRtbF83NTM4Njg2MGJjNWY0YTRhYTA3YjllNTMwOTc0ZDViNiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDYuIHRyYXR0b3JpYSBieSBjaW5xdWU8YnI+VGVsZXBob25lOiArOTcxIDQgNDU1IDk5ODk8YnI+dXJsOiBodHRwOi8vanVtZWlyYWh2aWxsYWdlLmZpdmVob3RlbHNhbmRyZXNvcnRzLmNvbS9tZWV0LW1pbmdsZS90cmF0dG9yaWEtYnktY2lucXVlPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwX2NmOWY4YTRlNTQ5ZjQ4NmE4Y2I2MTgwYzJiOGE1YTNmLnNldENvbnRlbnQoaHRtbF83NTM4Njg2MGJjNWY0YTRhYTA3YjllNTMwOTc0ZDViNik7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfMzJkMTJhNmM4YjU1NDU1MGIxZDk4MDE4YzBiMTRiZDAuYmluZFBvcHVwKHBvcHVwX2NmOWY4YTRlNTQ5ZjQ4NmE4Y2I2MTgwYzJiOGE1YTNmKQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl84MjA3ZjkwZDMwODc0ODk2OWU0OGZjMWM2OWE2YWQ2ZSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjI1Njg3NTcsIDU1LjMxMjA4MTFdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogImIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiYiIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogMTAsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwXzNmNWNkZDVmZTBlYzQ3ZjliNWFlZjljZDI3NGJhZmE5ID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF9mYTkwYjJlMDAxYzE0OGQwOWJmMWM4MzgzOTYzOTY0ZSA9ICQoYDxkaXYgaWQ9Imh0bWxfZmE5MGIyZTAwMWMxNDhkMDliZjFjODM4Mzk2Mzk2NGUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiA3LiBkb29ycyBmcmVlc3R5bGUgZ3JpbGw8YnI+VGVsZXBob25lOiArOTcxIDQgMjA0IDkyOTk8YnI+dXJsOiBodHRwOi8vd3d3LmRvb3JzZHViYWkuY29tL2VuPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwXzNmNWNkZDVmZTBlYzQ3ZjliNWFlZjljZDI3NGJhZmE5LnNldENvbnRlbnQoaHRtbF9mYTkwYjJlMDAxYzE0OGQwOWJmMWM4MzgzOTYzOTY0ZSk7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfODIwN2Y5MGQzMDg3NDg5NjllNDhmYzFjNjlhNmFkNmUuYmluZFBvcHVwKHBvcHVwXzNmNWNkZDVmZTBlYzQ3ZjliNWFlZjljZDI3NGJhZmE5KQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8xOWYwZjYwYTExODU0MjcxYTc5NWQ1Mjk4N2UzODk3NyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjA2NTc5MzQsIDU1LjEzODExNTldLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogImIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiYiIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogMTAsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwXzc5MjE0OTlkZWQyNjRjM2JiOTQ1NGM1ZTAyMzAzNjQ0ID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF9mNmFlYjFhNjdjZWE0OTIzYjE1OTNlYmQ1ZGRmYzdlNiA9ICQoYDxkaXYgaWQ9Imh0bWxfZjZhZWIxYTY3Y2VhNDkyM2IxNTkzZWJkNWRkZmM3ZTYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiA4LiB1cmJhbiBiYXIgJiBraXRjaGVuIC0gdWJrPGJyPlRlbGVwaG9uZTogKzk3MSA0IDQzOCAwMDAwPGJyPnVybDogaHR0cDovL3d3dy5tb3ZlbnBpY2suY29tL2VuL21pZGRsZS1lYXN0L3VhZS9kdWJhaS9kdWJhaS1qdW1laXJhaC1sYWtlcy10b3dlcnMvcmVzdGF1cmFudHMvcmVzdGF1cmFudHMvdXJiYW4tYmFyLWtpdGNoZW4tdWJrPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwXzc5MjE0OTlkZWQyNjRjM2JiOTQ1NGM1ZTAyMzAzNjQ0LnNldENvbnRlbnQoaHRtbF9mNmFlYjFhNjdjZWE0OTIzYjE1OTNlYmQ1ZGRmYzdlNik7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfMTlmMGY2MGExMTg1NDI3MWE3OTVkNTI5ODdlMzg5NzcuYmluZFBvcHVwKHBvcHVwXzc5MjE0OTlkZWQyNjRjM2JiOTQ1NGM1ZTAyMzAzNjQ0KQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9hZDAxYzZjOGRhODE0Y2VjYmI5YTg3NTM5NmU3Mzc1MiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjIzMzg0NDEsIDU1LjI2NTQ4MTJdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogImIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiYiIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogMTAsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwXzY3ZGIzMWQwMTJhOTQ2ZjZhY2VmMDk3YWVkZThmNWJmID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF83Njk3YThkZGRiN2E0MWYwYWRhZjA5OGY2YzdjY2MwZCA9ICQoYDxkaXYgaWQ9Imh0bWxfNzY5N2E4ZGRkYjdhNDFmMGFkYWYwOThmNmM3Y2NjMGQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiA5LiBiYXJlZm9vdCBsb3VuZ2U8YnI+VGVsZXBob25lOiArOTcxIDQgMzQ2IDExMTE8YnI+dXJsOiBodHRwOi8vd3d3LmR4Ym1hcmluZS5jb20vPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwXzY3ZGIzMWQwMTJhOTQ2ZjZhY2VmMDk3YWVkZThmNWJmLnNldENvbnRlbnQoaHRtbF83Njk3YThkZGRiN2E0MWYwYWRhZjA5OGY2YzdjY2MwZCk7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfYWQwMWM2YzhkYTgxNGNlY2JiOWE4NzUzOTZlNzM3NTIuYmluZFBvcHVwKHBvcHVwXzY3ZGIzMWQwMTJhOTQ2ZjZhY2VmMDk3YWVkZThmNWJmKQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9lYjJiM2RiMTNiNmE0YmFkODYwZTExMDM0MGY3YWYzNSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjIxMjY0MjYsIDU1LjI4MjQwNV0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiYiIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJiIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiAxMCwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfZDVmMjYzOWIyYzljNGE5ODhhYjQ2NDdhYjhiNmY4MjcgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzljZTRlYjgzMzJlYzQyZTNiZDIwYTQzMTc1ZTUyMGJjID0gJChgPGRpdiBpZD0iaHRtbF85Y2U0ZWI4MzMyZWM0MmUzYmQyMGE0MzE3NWU1MjBiYyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDEwLiBtaW5hIGJyYXNzZXJpZTxicj5UZWxlcGhvbmU6ICs5NzEgNCA1MDYgMDEwMDxicj51cmw6IGh0dHA6Ly93d3cubWluYWJyYXNzZXJpZS5jb20vPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwX2Q1ZjI2MzliMmM5YzRhOTg4YWI0NjQ3YWI4YjZmODI3LnNldENvbnRlbnQoaHRtbF85Y2U0ZWI4MzMyZWM0MmUzYmQyMGE0MzE3NWU1MjBiYyk7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfZWIyYjNkYjEzYjZhNGJhZDg2MGUxMTAzNDBmN2FmMzUuYmluZFBvcHVwKHBvcHVwX2Q1ZjI2MzliMmM5YzRhOTg4YWI0NjQ3YWI4YjZmODI3KQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9iOWM2MDViZWQ1OGE0NTMxYTg4YmJhYWJkZmZjMjY0NCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjIwODI3MywgNTUuMjYwNjAxNV0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiYiIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJiIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiAxMCwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfODEzZWJiZDMxZjQ0NDk3Njk2MDdjMDI5MzlmYTVmMGEgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sX2I5ZmE3YmNhYTEyMDQ1ZGE4NDEyMzQ3NmM4NThlYzQ4ID0gJChgPGRpdiBpZD0iaHRtbF9iOWZhN2JjYWExMjA0NWRhODQxMjM0NzZjODU4ZWM0OCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IFNwb25zb3JlZGdyYXplIGdhc3RybyBncmlsbDxicj5UZWxlcGhvbmU6ICs5NzEgNCA0MDMgMzExMTxicj51cmw6IGh0dHA6Ly93d3cubGl2ZWxhdmlsbGUuY29tL2RpbmluZy9HcmF6ZS9pbmRleC5odG1sPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwXzgxM2ViYmQzMWY0NDQ5NzY5NjA3YzAyOTM5ZmE1ZjBhLnNldENvbnRlbnQoaHRtbF9iOWZhN2JjYWExMjA0NWRhODQxMjM0NzZjODU4ZWM0OCk7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfYjljNjA1YmVkNThhNDUzMWE4OGJiYWFiZGZmYzI2NDQuYmluZFBvcHVwKHBvcHVwXzgxM2ViYmQzMWY0NDQ5NzY5NjA3YzAyOTM5ZmE1ZjBhKQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8xYTA5ZDhhZDBhMDU0MTcwYjlhMjI0NzM1ZjcwYTg2MiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI0LjgxNjgyMDYsIDU1LjIzMTI4NzJdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogImIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiYiIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogMTAsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwXzZhZWZlZGZjMjE4NTRiODA4ODRjZDg2Yjc1ZGI1MzA5ID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF83ZjViNzlhOWVlOTM0NmU1OTUxOTg4ODQ2MzA4MmQxOCA9ICQoYDxkaXYgaWQ9Imh0bWxfN2Y1Yjc5YTllZTkzNDZlNTk1MTk4ODg0NjMwODJkMTgiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiAxMS4gYWwgc2FyYWIgcm9vZnRvcCBsb3VuZ2U8YnI+VGVsZXBob25lOiArOTcxIDQgODA5IDYxMDA8YnI+dXJsOiBodHRwOi8vd3d3Lm1leWRhbmhvdGVscy5jb20vYmFiYWxzaGFtcy9kaW5pbmcuaHRtPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwXzZhZWZlZGZjMjE4NTRiODA4ODRjZDg2Yjc1ZGI1MzA5LnNldENvbnRlbnQoaHRtbF83ZjViNzlhOWVlOTM0NmU1OTUxOTg4ODQ2MzA4MmQxOCk7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfMWEwOWQ4YWQwYTA1NDE3MGI5YTIyNDczNWY3MGE4NjIuYmluZFBvcHVwKHBvcHVwXzZhZWZlZGZjMjE4NTRiODA4ODRjZDg2Yjc1ZGI1MzA5KQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9mNmE1NzRkMGMwZWU0ZDk0YTg1YTgxMGM4OGI4NWYzZiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjA0NjI5NDYsIDU1LjIwMzA0MTE5OTk5OTk5XSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJiIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogImIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDEwLCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF8yYjUwMmZjNGQzMTU0MGZhYTg1ODVkM2ZiNTA5OTRkYyA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfNjU3MTk4ZTJiNDJlNDU4MDkyNjZhNGU1ZmE4MTgwMjAgPSAkKGA8ZGl2IGlkPSJodG1sXzY1NzE5OGUyYjQyZTQ1ODA5MjY2YTRlNWZhODE4MDIwIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogMTIuIHNvdWwgc3RyZWV0PGJyPlRlbGVwaG9uZTogKzk3MSA0IDQ1NSA5OTg5PGJyPnVybDogaHR0cDovL3NvdWwuc3QvPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwXzJiNTAyZmM0ZDMxNTQwZmFhODU4NWQzZmI1MDk5NGRjLnNldENvbnRlbnQoaHRtbF82NTcxOThlMmI0MmU0NTgwOTI2NmE0ZTVmYTgxODAyMCk7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfZjZhNTc0ZDBjMGVlNGQ5NGE4NWE4MTBjODhiODVmM2YuYmluZFBvcHVwKHBvcHVwXzJiNTAyZmM0ZDMxNTQwZmFhODU4NWQzZmI1MDk5NGRjKQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl83OGJlMzEzOGJiMmU0YWY0OGM4OTIwZjMxMGI3MjNlNiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjI0OTE1NDksIDU1LjM0NzEzOTYwMDAwMDAxXSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJiIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogImIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDEwLCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF84OTVlNDYxYjM2MjM0Yjc1YmRlNTUxNDQzYzllODdmMSA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfZGVjYmU4OTY5YjJlNGMzYTljMDI0ZWQzMjgzNDYyNmIgPSAkKGA8ZGl2IGlkPSJodG1sX2RlY2JlODk2OWIyZTRjM2E5YzAyNGVkMzI4MzQ2MjZiIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogMTMuIGJlYmVtb3M8YnI+VGVsZXBob25lOiArOTcxIDQgNzAyIDI0NTU8YnI+dXJsOiBodHRwOi8vd3d3LmJlYmVtb3NkdWJhaS5jb20vPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwXzg5NWU0NjFiMzYyMzRiNzViZGU1NTE0NDNjOWU4N2YxLnNldENvbnRlbnQoaHRtbF9kZWNiZTg5NjliMmU0YzNhOWMwMjRlZDMyODM0NjI2Yik7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfNzhiZTMxMzhiYjJlNGFmNDhjODkyMGYzMTBiNzIzZTYuYmluZFBvcHVwKHBvcHVwXzg5NWU0NjFiMzYyMzRiNzViZGU1NTE0NDNjOWU4N2YxKQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl82NGE5ZGE1MWI4Y2M0OGRkOGI4OWYyMjJkZmNhMTBlMSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjIyODgzOTQsIDU1LjMyNjgxMjVdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogImIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiYiIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogMTAsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwXzcxMjJkZmYzMjFlOTQyYjFhMWNiN2Q0ZDZmZGZlMTYzID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF9lZTA5YTMxOTVhM2I0MDYyOTVmMjE5NGJlMjZhZmRhNCA9ICQoYDxkaXYgaWQ9Imh0bWxfZWUwOWEzMTk1YTNiNDA2Mjk1ZjIxOTRiZTI2YWZkYTQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiAxNC4gYXd0YXI8YnI+VGVsZXBob25lOiArOTcxIDQgMzE3IDIyMjE8YnI+dXJsOiBodHRwczovL3d3dy5oeWF0dHJlc3RhdXJhbnRzLmNvbS9lbi9kaW5pbmcvdWFlL2R1YmFpL21pZGRsZS1lYXN0ZXJuLXJlc3RhdXJhbnQtaW4tZ2FyaG91ZC1hd3Rhcj91dG1fc291cmNlPWdtYmxpc3RpbmdfZHhiZ2gmdXRtX21lZGl1bT1hd3RhciZ1dG1fY2FtcGFpZ249R01CPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwXzcxMjJkZmYzMjFlOTQyYjFhMWNiN2Q0ZDZmZGZlMTYzLnNldENvbnRlbnQoaHRtbF9lZTA5YTMxOTVhM2I0MDYyOTVmMjE5NGJlMjZhZmRhNCk7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfNjRhOWRhNTFiOGNjNDhkZDhiODlmMjIyZGZjYTEwZTEuYmluZFBvcHVwKHBvcHVwXzcxMjJkZmYzMjFlOTQyYjFhMWNiN2Q0ZDZmZGZlMTYzKQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8yYmJkZjM1ODBlM2M0YWZkOTIwY2M3NmE5ZjhkYjYwNSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjE5ODc2NSwgNTUuMjc5NjA1M10sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiYiIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJiIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiAxMCwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfMTkwNmFiMGY4MGY5NDAwZmFmZGEzODYzNmYyYzFiNGYgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzRmYjI5MzU0YzJiYjQzNDc4ZDE3MTgyYmVlNzJjODEzID0gJChgPGRpdiBpZD0iaHRtbF80ZmIyOTM1NGMyYmI0MzQ3OGQxNzE4MmJlZTcyYzgxMyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDE1LiB0cmliZXMgY2Fybml2b3JlPGJyPlRlbGVwaG9uZTogKzk3MSA0IDIyNiA0OTc0PGJyPnVybDogaHR0cDovL3RyaWJlc3Jlc3RhdXJhbnQuY29tLzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF8xOTA2YWIwZjgwZjk0MDBmYWZkYTM4NjM2ZjJjMWI0Zi5zZXRDb250ZW50KGh0bWxfNGZiMjkzNTRjMmJiNDM0NzhkMTcxODJiZWU3MmM4MTMpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyXzJiYmRmMzU4MGUzYzRhZmQ5MjBjYzc2YTlmOGRiNjA1LmJpbmRQb3B1cChwb3B1cF8xOTA2YWIwZjgwZjk0MDBmYWZkYTM4NjM2ZjJjMWI0ZikKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfODMzOTMzOWQ5MGU0NDZjNWIyYjhlZjA5ZTNlNjVkMzUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4yMjE2MDMsIDU1LjI4MDgyNjJdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogImIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiYiIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogMTAsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwX2MzOTEzYjY0YmY1MDRiZGE5YjY5NjU0M2QzZDAzNGEwID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF8zOWZhOWMzY2YzYjM0NWY1OTk4ZDAyOTg1MjVmZDUyMCA9ICQoYDxkaXYgaWQ9Imh0bWxfMzlmYTljM2NmM2IzNDVmNTk5OGQwMjk4NTI1ZmQ1MjAiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiBTcG9uc29yZWRzdXNoaSBuYXRpb25zPGJyPlRlbGVwaG9uZTogKzk3MSA1NiAxODggODUyMjxicj51cmw6IGh0dHBzOi8vc3VzaGluYXRpb25zLmFlLzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF9jMzkxM2I2NGJmNTA0YmRhOWI2OTY1NDNkM2QwMzRhMC5zZXRDb250ZW50KGh0bWxfMzlmYTljM2NmM2IzNDVmNTk5OGQwMjk4NTI1ZmQ1MjApOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyXzgzMzkzMzlkOTBlNDQ2YzViMmI4ZWYwOWUzZTY1ZDM1LmJpbmRQb3B1cChwb3B1cF9jMzkxM2I2NGJmNTA0YmRhOWI2OTY1NDNkM2QwMzRhMCkKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYWExMjgwYTljYWZmNDhmOTg3NjRmZDE0ZTY1Y2Q5MjggPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4yNzg4OTgsIDU1LjMwNDQ2MDddLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogImIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiYiIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogMTAsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwXzQxZTIxMWEyZTJiZTQ4YWU4NmMxNWM4ZTI1NDUxNjlmID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF9lNmM4MGQ3ZDFiMjE0ZDNkYTg5YmVlNWIwNjM0YWY4NCA9ICQoYDxkaXYgaWQ9Imh0bWxfZTZjODBkN2QxYjIxNGQzZGE4OWJlZTViMDYzNGFmODQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiAxNi4gYWwgZGF3YWFyIHJldm9sdmluZyByZXN0YXVyYW50PGJyPlRlbGVwaG9uZTogKzk3MSA0IDIwOSA2OTEyPGJyPnVybDogaHR0cDovL3d3dy5oeWF0dHJlc3RhdXJhbnRzLmNvbS9lbi9kaW5pbmcvdWFlL2R1YmFpL2ludGVybmF0aW9uYWwtcmVzdGF1cmFudC1pbi1kZWlyYS1jb3JuaWNoZS1hbC1kYXdhYXItcmV2b2x2aW5nLXJlc3RhdXJhbnQ8L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfNDFlMjExYTJlMmJlNDhhZTg2YzE1YzhlMjU0NTE2OWYuc2V0Q29udGVudChodG1sX2U2YzgwZDdkMWIyMTRkM2RhODliZWU1YjA2MzRhZjg0KTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl9hYTEyODBhOWNhZmY0OGY5ODc2NGZkMTRlNjVjZDkyOC5iaW5kUG9wdXAocG9wdXBfNDFlMjExYTJlMmJlNDhhZTg2YzE1YzhlMjU0NTE2OWYpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzQ5YTgwYzg0Y2UyYjQ0OGU4YTAwMTFjMDYzNTU0NGRhID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMTExMzk5MSwgNTUuMTM3MjE1OF0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiYiIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJiIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiAxMCwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfYTk3MGRiNjRmMGRkNDM4NWJmODViNmY2ODZmOTEwOWIgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sX2JkMzE1ZGRhMTI2MzRkMGZhYWRmZWQ2N2NkNDU0Nzg3ID0gJChgPGRpdiBpZD0iaHRtbF9iZDMxNWRkYTEyNjM0ZDBmYWFkZmVkNjdjZDQ1NDc4NyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDE3LiBraHliZXI8YnI+VGVsZXBob25lOiArOTcxIDQgNDU1IDExMTE8YnI+dXJsOiBodHRwczovL3d3dy5kdWtlc2R1YmFpLmNvbS9raHliZXIvPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwX2E5NzBkYjY0ZjBkZDQzODViZjg1YjZmNjg2ZjkxMDliLnNldENvbnRlbnQoaHRtbF9iZDMxNWRkYTEyNjM0ZDBmYWFkZmVkNjdjZDQ1NDc4Nyk7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfNDlhODBjODRjZTJiNDQ4ZThhMDAxMWMwNjM1NTQ0ZGEuYmluZFBvcHVwKHBvcHVwX2E5NzBkYjY0ZjBkZDQzODViZjg1YjZmNjg2ZjkxMDliKQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl82MjA0Y2VhZDQxY2U0M2Q2YjJiZDI1YzExM2QwMjkwOCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjI2NjI2NzgsIDU1LjMwODc4NzQ5OTk5OTk5XSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJiIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogImIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDEwLCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF8zMTBhODYyYzYzMjg0NzAzYTY0YTY0ZTE1YzBmYjZmMCA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfOWYzNmY5M2MzMDQwNDhkZjgxNjMxZDg4MmY3M2M0YjggPSAkKGA8ZGl2IGlkPSJodG1sXzlmMzZmOTNjMzA0MDQ4ZGY4MTYzMWQ4ODJmNzNjNGI4IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogMTguIGRhbmlhbCByZXN0YXVyYW50PGJyPlRlbGVwaG9uZTogKzk3MSA0IDIyNyA3NjY5PGJyPnVybDogaHR0cDovL3d3dy5kYW5pYWxyZXN0YXVyYW50LmNvbS88L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfMzEwYTg2MmM2MzI4NDcwM2E2NGE2NGUxNWMwZmI2ZjAuc2V0Q29udGVudChodG1sXzlmMzZmOTNjMzA0MDQ4ZGY4MTYzMWQ4ODJmNzNjNGI4KTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl82MjA0Y2VhZDQxY2U0M2Q2YjJiZDI1YzExM2QwMjkwOC5iaW5kUG9wdXAocG9wdXBfMzEwYTg2MmM2MzI4NDcwM2E2NGE2NGUxNWMwZmI2ZjApCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2MwODEyZjAwZGI3ODQ4MWViNjUyZTQ3OTJhZTViYTRjID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMjM0MzU1LCA1NS4zMjQwMTQ3XSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJiIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogImIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDEwLCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF9kNmRkYzkzZWE3N2Q0NjM2YTBlYjgzNDEwOWMwMGRlYiA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfNTdhZGQ1Yjk1MTc1NDI4YWI5MTU5ZGVhYzUxNzE3MTAgPSAkKGA8ZGl2IGlkPSJodG1sXzU3YWRkNWI5NTE3NTQyOGFiOTE1OWRlYWM1MTcxNzEwIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogMTkuIGV2ZSBwZW50aG91c2UgJiBsb3VuZ2U8YnI+VGVsZXBob25lOiArOTcxIDQgNTUzIDEyMTQ8YnI+dXJsOiBodHRwOi8vd3d3Lmh5YXR0cmVzdGF1cmFudHMuY29tL2VuL2RpbmluZy91YWUvZHViYWkvaW50ZXJuYXRpb25hbC1yZXN0YXVyYW50LWluLW91ZC1tZXRoYS1yb2FkLWV2ZS1wZW50aG91c2UtbG91bmdlP3V0bV9zb3VyY2U9V2Vic2l0ZV9keGJoYyZ1dG1fbWVkaXVtPWV2ZSZ1dG1fY2FtcGFpZ249SHlhdHQ8L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfZDZkZGM5M2VhNzdkNDYzNmEwZWI4MzQxMDljMDBkZWIuc2V0Q29udGVudChodG1sXzU3YWRkNWI5NTE3NTQyOGFiOTE1OWRlYWM1MTcxNzEwKTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl9jMDgxMmYwMGRiNzg0ODFlYjY1MmU0NzkyYWU1YmE0Yy5iaW5kUG9wdXAocG9wdXBfZDZkZGM5M2VhNzdkNDYzNmEwZWI4MzQxMDljMDBkZWIpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzEzNTRhNGU2ODRmNTRkMjI5MDRiMTZkNzk2NGVjMDU4ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMTk4NzY1LCA1NS4yNzk2MDUzXSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJiIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogImIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDEwLCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF9hNWQxNmJmYjNkYTY0NzE0OWFkMDRkNzczMzIxNTQ3ZiA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfYTI2MjE0NzJmYmI0NGIzOGE3ZjU1MWRhNTM2ZTMxMTEgPSAkKGA8ZGl2IGlkPSJodG1sX2EyNjIxNDcyZmJiNDRiMzhhN2Y1NTFkYTUzNmUzMTExIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogMjAuIHRoZSBncmlsbCBzaGFjazxicj5UZWxlcGhvbmU6ICs5NzEgNCAzODggMjM4Mjxicj51cmw6IGh0dHA6Ly93d3cudGhlZ3JpbGxsc2hhY2suY29tLzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF9hNWQxNmJmYjNkYTY0NzE0OWFkMDRkNzczMzIxNTQ3Zi5zZXRDb250ZW50KGh0bWxfYTI2MjE0NzJmYmI0NGIzOGE3ZjU1MWRhNTM2ZTMxMTEpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyXzEzNTRhNGU2ODRmNTRkMjI5MDRiMTZkNzk2NGVjMDU4LmJpbmRQb3B1cChwb3B1cF9hNWQxNmJmYjNkYTY0NzE0OWFkMDRkNzczMzIxNTQ3ZikKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYzcyOTMyZTNkMmZkNGZiNThkODAyMmY3YWU1OTYxZmEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4yNDc4NjcsIDU1LjMwMDQ5MjVdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogImIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiYiIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogMTAsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwXzE3YzhkNzFmYzJjMDRiYmJhN2FkMmZjNTQ0YzM1OWEyID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF9jYTJjODFkMTc2OWQ0OTc5YWU3NzFkNzQyOTM1MjJmMyA9ICQoYDxkaXYgaWQ9Imh0bWxfY2EyYzgxZDE3NjlkNDk3OWFlNzcxZDc0MjkzNTIyZjMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiBTcG9uc29yZWRhbXJpdHNyIHJlc3RhdXJhbnQ8YnI+VGVsZXBob25lOiArOTcxIDUwIDY3OCAwMDk2PGJyPnVybDogaHR0cDovL2Ftcml0c3J1YWUuY29tLzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF8xN2M4ZDcxZmMyYzA0YmJiYTdhZDJmYzU0NGMzNTlhMi5zZXRDb250ZW50KGh0bWxfY2EyYzgxZDE3NjlkNDk3OWFlNzcxZDc0MjkzNTIyZjMpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyX2M3MjkzMmUzZDJmZDRmYjU4ZDgwMjJmN2FlNTk2MWZhLmJpbmRQb3B1cChwb3B1cF8xN2M4ZDcxZmMyYzA0YmJiYTdhZDJmYzU0NGMzNTlhMikKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNDY0MGI3YjI0MDcxNDRiOThmMDVmNTVjZTBmZWM0YzkgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4xMDQzMjk2LCA1NS4xNDg3NjkxXSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJiIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogImIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDEwLCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF8zYjI1Y2ZkMjA0NDc0MjE2YjliZTBkYTNhZDA0OTkyNSA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfOTUxNzE2NmEwY2Q5NDViZjhjZmVkNWFhNWFlNThhNDAgPSAkKGA8ZGl2IGlkPSJodG1sXzk1MTcxNjZhMGNkOTQ1YmY4Y2ZlZDVhYTVhZTU4YTQwIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogMjEuIG1haWRlbiBzaGFuZ2hhaTxicj5UZWxlcGhvbmU6ICs5NzEgNCA0NTUgOTk4OTxicj51cmw6IGh0dHA6Ly9maXZlaG90ZWxzYW5kcmVzb3J0cy5jb20vZGluZS1kcmluay1kYW5jZS9yZXN0YXVyYW50cy9tYWlkZW4tc2hhbmdoYWkvPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwXzNiMjVjZmQyMDQ0NzQyMTZiOWJlMGRhM2FkMDQ5OTI1LnNldENvbnRlbnQoaHRtbF85NTE3MTY2YTBjZDk0NWJmOGNmZWQ1YWE1YWU1OGE0MCk7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfNDY0MGI3YjI0MDcxNDRiOThmMDVmNTVjZTBmZWM0YzkuYmluZFBvcHVwKHBvcHVwXzNiMjVjZmQyMDQ0NzQyMTZiOWJlMGRhM2FkMDQ5OTI1KQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8zMmVhYTA0YTMxMGU0NmQ4YmJjZjk5Mjc5Y2E1MjVkNCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjIxNDAxMzMsIDU1LjI3NjA4ODVdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogImIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiYiIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogMTAsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwX2E1ODkyMzFlN2MxZTQ5NjE4MjcyYzBiYTEwZjg0NDg0ID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF8xOGZjYTk4ZDRhMzg0ZGM1OGU4ZWZlYmUzN2M0NDU4ZiA9ICQoYDxkaXYgaWQ9Imh0bWxfMThmY2E5OGQ0YTM4NGRjNThlOGVmZWJlMzdjNDQ1OGYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiAyMi4gcHVyYW5pIGRpbGxpIHNoZWlraCB6YXllZCByb2FkPGJyPlRlbGVwaG9uZTogKzk3MSA0IDMxNiA5NzI2PGJyPnVybDogaHR0cDovL3d3dy5wdXJhbmlkaWxsaWR1YmFpLmNvbS9zaGVpa2h6YXllZHJvYWQ8L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfYTU4OTIzMWU3YzFlNDk2MTgyNzJjMGJhMTBmODQ0ODQuc2V0Q29udGVudChodG1sXzE4ZmNhOThkNGEzODRkYzU4ZThlZmViZTM3YzQ0NThmKTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl8zMmVhYTA0YTMxMGU0NmQ4YmJjZjk5Mjc5Y2E1MjVkNC5iaW5kUG9wdXAocG9wdXBfYTU4OTIzMWU3YzFlNDk2MTgyNzJjMGJhMTBmODQ0ODQpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2NkMzMwYTExZWFjNzQ0MTk5Zjc0OTYzNjVlMTY5MmIwID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMjE0MDEzMywgNTUuMjc2MDg4NV0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiYiIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJiIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiAxMCwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfZWYyZWMzMWFjNTU4NGEyNWJkMDM2NTZhNDM5ODIzZjggPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sX2NkZGRkMzZkNmUxNzRlMTc4MmExYjJiNzRhM2JjYmMwID0gJChgPGRpdiBpZD0iaHRtbF9jZGRkZDM2ZDZlMTc0ZTE3ODJhMWIyYjc0YTNiY2JjMCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDIzLiBsZXZlbCA0MyBza3kgbG91bmdlPGJyPlRlbGVwaG9uZTogKzk3MSA1NiA0MTQgMjIxMzxicj51cmw6IGh0dHA6Ly93d3cubGV2ZWw0M2xvdW5nZS5jb20vPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwX2VmMmVjMzFhYzU1ODRhMjViZDAzNjU2YTQzOTgyM2Y4LnNldENvbnRlbnQoaHRtbF9jZGRkZDM2ZDZlMTc0ZTE3ODJhMWIyYjc0YTNiY2JjMCk7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfY2QzMzBhMTFlYWM3NDQxOTlmNzQ5NjM2NWUxNjkyYjAuYmluZFBvcHVwKHBvcHVwX2VmMmVjMzFhYzU1ODRhMjViZDAzNjU2YTQzOTgyM2Y4KQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl80ZTljODE0NjM0NGY0ZTM2ODJmYzk3NzUyMzAwZWIxNCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjE5NTE1NTQsIDU1LjI3NTE1NzldLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogImIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiYiIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogMTAsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwX2VjNjkyYzk3ZDA5YjRkOGY5NmU0NzY5M2Y0ZDlhMmQxID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF9lMzY5NTczNmI5NmE0ODcwODVhNzU1YzZlNzAwMDlmMyA9ICQoYDxkaXYgaWQ9Imh0bWxfZTM2OTU3MzZiOTZhNDg3MDg1YTc1NWM2ZTcwMDA5ZjMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiAyNC4gYmxhY2sgdGFwIGNyYWZ0IGJ1cmdlcnMgJiBzaGFrZXMgZHViYWkgbWFsbDxicj5UZWxlcGhvbmU6ICs5NzEgNCAzMzAgNTEwMzxicj51cmw6IGh0dHA6Ly93d3cuYmxhY2t0YXBtZS5jb20vPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwX2VjNjkyYzk3ZDA5YjRkOGY5NmU0NzY5M2Y0ZDlhMmQxLnNldENvbnRlbnQoaHRtbF9lMzY5NTczNmI5NmE0ODcwODVhNzU1YzZlNzAwMDlmMyk7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfNGU5YzgxNDYzNDRmNGUzNjgyZmM5Nzc1MjMwMGViMTQuYmluZFBvcHVwKHBvcHVwX2VjNjkyYzk3ZDA5YjRkOGY5NmU0NzY5M2Y0ZDlhMmQxKQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl85MWQ3ZjQxNTQzZjE0ZDY3YTI3ODY2NTI2YjgwZjgwZSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjI0OTE1NDksIDU1LjM0NzEzOTYwMDAwMDAxXSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJiIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogImIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDEwLCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF9hZWY4MzhlOTdkOGM0NWJhOTZkNzk5OTE3NzJjMWVjOSA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfZGQ0YTIxYzcyMDNiNDliY2E0YmI4YTEyMWYxNjQ2NWUgPSAkKGA8ZGl2IGlkPSJodG1sX2RkNGEyMWM3MjAzYjQ5YmNhNGJiOGExMjFmMTY0NjVlIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogMjUuIGJlZWYgYmlzdHJvPGJyPlRlbGVwaG9uZTogKzk3MSA0IDcwMiAyNDU1PGJyPnVybDogaHR0cDovL3d3dy5iZWVmYmlzdHJvZHViYWkuY29tLzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF9hZWY4MzhlOTdkOGM0NWJhOTZkNzk5OTE3NzJjMWVjOS5zZXRDb250ZW50KGh0bWxfZGQ0YTIxYzcyMDNiNDliY2E0YmI4YTEyMWYxNjQ2NWUpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyXzkxZDdmNDE1NDNmMTRkNjdhMjc4NjY1MjZiODBmODBlLmJpbmRQb3B1cChwb3B1cF9hZWY4MzhlOTdkOGM0NWJhOTZkNzk5OTE3NzJjMWVjOSkKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfOGY0YzBiNmM2YzllNDhjODg3NzI1MTFlZDYyMzI2ZTQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4yMDI0NDg1LCA1NS4yMzk2NTI1XSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJiIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogImIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDEwLCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF81ZTY5YWYzMjg0YTc0ZTg0OWQzMmJkNWRhZDc1M2UwZSA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfYWMxYjJiY2ZlOGYwNDZhOGFlMTM4YTczMDVlNjBlN2UgPSAkKGA8ZGl2IGlkPSJodG1sX2FjMWIyYmNmZThmMDQ2YThhZTEzOGE3MzA1ZTYwZTdlIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogU3BvbnNvcmVkdmVyZGUgZHViYWk8YnI+VGVsZXBob25lOiArOTcxIDQgMzMzIDgwMjU8YnI+dXJsOiBodHRwOi8vd3d3LnZlcmRlLWR1YmFpLmNvbS88L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfNWU2OWFmMzI4NGE3NGU4NDlkMzJiZDVkYWQ3NTNlMGUuc2V0Q29udGVudChodG1sX2FjMWIyYmNmZThmMDQ2YThhZTEzOGE3MzA1ZTYwZTdlKTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl84ZjRjMGI2YzZjOWU0OGM4ODc3MjUxMWVkNjIzMjZlNC5iaW5kUG9wdXAocG9wdXBfNWU2OWFmMzI4NGE3NGU4NDlkMzJiZDVkYWQ3NTNlMGUpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzM1ZWI2YjU4YjM2ZTRiN2NiMWM1NWI2OTNhNGQ5YmNmID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMjI5NTMwOSwgNTUuMjg2NjcyOF0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiYiIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJiIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiAxMCwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfMmI0YzMzYmM1ZWMxNDJjNGEzYjU0NmIwNjkzOWNiZjAgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzViYzc1ZWFhODk4MzRlNTI4NTdiMDQzNTAxNjEzN2Q5ID0gJChgPGRpdiBpZD0iaHRtbF81YmM3NWVhYTg5ODM0ZTUyODU3YjA0MzUwMTYxMzdkOSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDI2LiBuaWRvIHRhcGFzIHJlc3RhdXJhbnQgJiBiYXI8YnI+VGVsZXBob25lOiArOTcxIDQgMzMzIDMwNTU8YnI+dXJsOiBodHRwOi8vbmlkb2R4Yi5jb20vPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwXzJiNGMzM2JjNWVjMTQyYzRhM2I1NDZiMDY5MzljYmYwLnNldENvbnRlbnQoaHRtbF81YmM3NWVhYTg5ODM0ZTUyODU3YjA0MzUwMTYxMzdkOSk7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfMzVlYjZiNThiMzZlNGI3Y2IxYzU1YjY5M2E0ZDliY2YuYmluZFBvcHVwKHBvcHVwXzJiNGMzM2JjNWVjMTQyYzRhM2I1NDZiMDY5MzljYmYwKQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8zYTA4Y2Y2NGJkNTI0NGUzODc4MDNmZjQ2MzlmOTRjNyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjA4MDQ3NzcsIDU1LjE1NDE5NDMwMDAwMDAxXSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJiIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogImIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDEwLCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF8zNTg3NmE2NDlkZWU0N2Y4OTI5NWJjMjE4YTRmNDc5OCA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfNDQ4YTZjOTQ1NTQwNGQ1Mzk5NzEwOWNkYmY5MzQ2NjEgPSAkKGA8ZGl2IGlkPSJodG1sXzQ0OGE2Yzk0NTU0MDRkNTM5OTcxMDljZGJmOTM0NjYxIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogMjcuIHNoYW1pYW5hPGJyPlRlbGVwaG9uZTogKzk3MSA0IDU3NCAxMTExPGJyPnVybDogaHR0cDovL3d3dy50YWpob3RlbHMuY29tL2VuLWluL3Rhai90YWotanVtZWlyYWgtbGFrZXMtdG93ZXJzL3Jlc3RhdXJhbnRzL3NoYW1pYW5hLzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF8zNTg3NmE2NDlkZWU0N2Y4OTI5NWJjMjE4YTRmNDc5OC5zZXRDb250ZW50KGh0bWxfNDQ4YTZjOTQ1NTQwNGQ1Mzk5NzEwOWNkYmY5MzQ2NjEpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyXzNhMDhjZjY0YmQ1MjQ0ZTM4NzgwM2ZmNDYzOWY5NGM3LmJpbmRQb3B1cChwb3B1cF8zNTg3NmE2NDlkZWU0N2Y4OTI5NWJjMjE4YTRmNDc5OCkKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZmFjZDViNDM0NmIzNGNiZGJiZjA4ZGYxNDdjNjQ0ZjggPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4yMDQ4NDkzLCA1NS4yNzA3ODI4XSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJiIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogImIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDEwLCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF82OTExOWQ5YTdhNzI0NjY1YmE0MDFkZGEyNGE3Y2NkMiA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfYmU1ODNkMDFjMDNhNDc4ZThhM2IxMjNmZWRiOGRjZDIgPSAkKGA8ZGl2IGlkPSJodG1sX2JlNTgzZDAxYzAzYTQ3OGU4YTNiMTIzZmVkYjhkY2QyIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogMjguIGtpbmFyYSBieSB2aWthcyBraGFubmE8YnI+VGVsZXBob25lOiArOTcxIDQgODE0IDU1NTU8YnI+dXJsOiBodHRwOi8vd3d3LmtpbmFyYWR1YmFpLmNvbS88L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfNjkxMTlkOWE3YTcyNDY2NWJhNDAxZGRhMjRhN2NjZDIuc2V0Q29udGVudChodG1sX2JlNTgzZDAxYzAzYTQ3OGU4YTNiMTIzZmVkYjhkY2QyKTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl9mYWNkNWI0MzQ2YjM0Y2JkYmJmMDhkZjE0N2M2NDRmOC5iaW5kUG9wdXAocG9wdXBfNjkxMTlkOWE3YTcyNDY2NWJhNDAxZGRhMjRhN2NjZDIpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzhjYTQ3ZTM1ODA1YTRjY2RhYmZmNmZkNmIzMjUzNDYxID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMTEwODIwMiwgNTUuMTM5OTE4NDAwMDAwMDFdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogImIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiYiIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogMTAsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwXzI5MjQxOTQ4OWY3NTQzMTRhY2IyMjJkNDFhMDg1MTIzID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF9jMjQ3MzY5NjEzYzc0N2M5OTliNzc4MjQzNjk3YTM2YyA9ICQoYDxkaXYgaWQ9Imh0bWxfYzI0NzM2OTYxM2M3NDdjOTk5Yjc3ODI0MzY5N2EzNmMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiAyOS4gbGl0dGxlIG1pc3MgaW5kaWE8YnI+VGVsZXBob25lOiArOTcxIDQgNDU3IDM0NTc8YnI+dXJsOiBodHRwOi8vd3d3LmZhaXJtb250LmNvbS9wYWxtLWR1YmFpL2RpbmluZy9saXR0bGUtbWlzcy1pbmRpYS88L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfMjkyNDE5NDg5Zjc1NDMxNGFjYjIyMmQ0MWEwODUxMjMuc2V0Q29udGVudChodG1sX2MyNDczNjk2MTNjNzQ3Yzk5OWI3NzgyNDM2OTdhMzZjKTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl84Y2E0N2UzNTgwNWE0Y2NkYWJmZjZmZDZiMzI1MzQ2MS5iaW5kUG9wdXAocG9wdXBfMjkyNDE5NDg5Zjc1NDMxNGFjYjIyMmQ0MWEwODUxMjMpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzNhYjA0MTUwZWQ0ZjRlNDVhZWQxYjg2MGYzNTcxZWJmID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMTEwMzQ3LCA1NS4yMjA2MjgyOTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiYiIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJiIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiAxMCwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfNTkwZTQwM2Y5ZTBkNDhlMzllMWFjYWVmODUyZTQyMzMgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sX2IzNGZkYmVjOTI0NzRhN2M5ZGM4NGExOTYyMWNmODEwID0gJChgPGRpdiBpZD0iaHRtbF9iMzRmZGJlYzkyNDc0YTdjOWRjODRhMTk2MjFjZjgxMCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDMwLiBmaXNoIGh1dCBhc21hayBhbCBzdWx0YW4gc2VhZm9vZCByZXN0YXVyYW50PGJyPlRlbGVwaG9uZTogKzk3MSA1OCAxMjggMjg4Njxicj51cmw6IGh0dHA6Ly9kdWJhaWZpc2hodXRyZXN0YXVyYW50LmNvbS9pbmRleC5waHA8L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfNTkwZTQwM2Y5ZTBkNDhlMzllMWFjYWVmODUyZTQyMzMuc2V0Q29udGVudChodG1sX2IzNGZkYmVjOTI0NzRhN2M5ZGM4NGExOTYyMWNmODEwKTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl8zYWIwNDE1MGVkNGY0ZTQ1YWVkMWI4NjBmMzU3MWViZi5iaW5kUG9wdXAocG9wdXBfNTkwZTQwM2Y5ZTBkNDhlMzllMWFjYWVmODUyZTQyMzMpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2FmYTIxNzJjMTJlZTQxZDliZjczMmExYjdhNjE4ZTE2ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMjA4MjczLCA1NS4yNjA2MDE1XSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJiIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogImIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDEwLCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF8wMGFhY2FjYTcxODQ0OGFjYWU3OWVmMjMwYzc3OWM4OCA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfZjMwZmE5MThjZGUwNDMyNGFjMmEyYTc2MmE0MjFiOGEgPSAkKGA8ZGl2IGlkPSJodG1sX2YzMGZhOTE4Y2RlMDQzMjRhYzJhMmE3NjJhNDIxYjhhIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogU3BvbnNvcmVkY2hpdmFsPGJyPlRlbGVwaG9uZTogKzk3MSA0IDQwMyAzMTExPGJyPnVybDogaHR0cDovL3d3dy5jaGl2YWxsYXZpbGxlLmNvbS88L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfMDBhYWNhY2E3MTg0NDhhY2FlNzllZjIzMGM3NzljODguc2V0Q29udGVudChodG1sX2YzMGZhOTE4Y2RlMDQzMjRhYzJhMmE3NjJhNDIxYjhhKTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl9hZmEyMTcyYzEyZWU0MWQ5YmY3MzJhMWI3YTYxOGUxNi5iaW5kUG9wdXAocG9wdXBfMDBhYWNhY2E3MTg0NDhhY2FlNzllZjIzMGM3NzljODgpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzJmYWY4MzA2YTc5MDQzNDI4MjEwMWIyZDQyODg1OTVkID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMTMzODc3NywgNTUuMTg0NzYyNV0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiYiIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJiIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiA1LCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF9jMjRiMzdhMWVjMGM0YmU1YTlkZGY0ZjBlMTNlMWE0OSA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfY2Y0MGVlNTAzYTM4NGI2Y2I2NWE1Y2JhMzliMWU0ODEgPSAkKGA8ZGl2IGlkPSJodG1sX2NmNDBlZTUwM2EzODRiNmNiNjVhNWNiYTM5YjFlNDgxIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogU3BvbnNvcmVkZm9sbHkgYnkgbmljayAmIHNjb3R0PGJyPlRlbGVwaG9uZTogKzk3MSA0IDQzMCA4NTM1PGJyPnVybDogaHR0cDovL2ZvbGx5LmFlLzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF9jMjRiMzdhMWVjMGM0YmU1YTlkZGY0ZjBlMTNlMWE0OS5zZXRDb250ZW50KGh0bWxfY2Y0MGVlNTAzYTM4NGI2Y2I2NWE1Y2JhMzliMWU0ODEpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyXzJmYWY4MzA2YTc5MDQzNDI4MjEwMWIyZDQyODg1OTVkLmJpbmRQb3B1cChwb3B1cF9jMjRiMzdhMWVjMGM0YmU1YTlkZGY0ZjBlMTNlMWE0OSkKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNDVhMTg0N2YxYjkwNDQ2MjhkNDFiODA1YjY5YzBhNjEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4wODA2MzYsIDU1LjEzNTUzMThdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogImIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiYiIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogNSwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfMGYzZjg4ZWIwOWZlNDNlNzgzMDIzOWQ3NDQyZWEyNWYgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzg3NGZkNDBlZWM2NTRhOTdhM2YxNzEyY2MwODdmZmE2ID0gJChgPGRpdiBpZD0iaHRtbF84NzRmZDQwZWVjNjU0YTk3YTNmMTcxMmNjMDg3ZmZhNiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDEuIGFzaWwgcmVzdGF1cmFudDxicj5UZWxlcGhvbmU6ICs5NzEgNTIgMTYwIDAzMzM8YnI+dXJsOiBodHRwOi8vd3d3LmFzaWxyZXN0YXVyYW50LmNvbS88L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfMGYzZjg4ZWIwOWZlNDNlNzgzMDIzOWQ3NDQyZWEyNWYuc2V0Q29udGVudChodG1sXzg3NGZkNDBlZWM2NTRhOTdhM2YxNzEyY2MwODdmZmE2KTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl80NWExODQ3ZjFiOTA0NDYyOGQ0MWI4MDViNjljMGE2MS5iaW5kUG9wdXAocG9wdXBfMGYzZjg4ZWIwOWZlNDNlNzgzMDIzOWQ3NDQyZWEyNWYpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzFlNjI3ZDczODRmOTQ0MTQ4MzNlNzgwZjdhNDcyMzhkID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMjMxNDk4MiwgNTUuMzQ2OTU1OV0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiYiIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJiIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiA1LCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF9kODEwMDRkNjgxNDk0YTI1OGJmY2NlYjEwOTI0Njg1YiA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfZTc1OGFkMzFkY2M5NDNhNmEyOGJlODQ1ZDYxMDRmMjIgPSAkKGA8ZGl2IGlkPSJodG1sX2U3NThhZDMxZGNjOTQzYTZhMjhiZTg0NWQ2MTA0ZjIyIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogMi4gbWV6emFsdW5hPGJyPlRlbGVwaG9uZTogKzk3MSA0IDcwMSAxMTI4PGJyPnVybDogaHR0cDovL3d3dy5kaW5pbmdkZmMuY29tL1Jlc3RhdXJhbnQtZGV0YWlscy8yNC9NZXp6YUx1bmE8L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfZDgxMDA0ZDY4MTQ5NGEyNThiZmNjZWIxMDkyNDY4NWIuc2V0Q29udGVudChodG1sX2U3NThhZDMxZGNjOTQzYTZhMjhiZTg0NWQ2MTA0ZjIyKTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl8xZTYyN2Q3Mzg0Zjk0NDE0ODMzZTc4MGY3YTQ3MjM4ZC5iaW5kUG9wdXAocG9wdXBfZDgxMDA0ZDY4MTQ5NGEyNThiZmNjZWIxMDkyNDY4NWIpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2RlYWUwYjI4ZmI1MzQ1OTU4NTEwYTFmNzM5ZDkzYmQ5ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMjUzMTc0NSwgNTUuMzY1NjcyOF0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiYiIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJiIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiA1LCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF9hNzZmYWMzNTlhOWE0NmM3YWNiMDZmYTVkYzMzYjIwNyA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfN2RjMjQwNjgxOTdkNGVkYmE1ZjViNjViMDhlN2FmYTYgPSAkKGA8ZGl2IGlkPSJodG1sXzdkYzI0MDY4MTk3ZDRlZGJhNWY1YjY1YjA4ZTdhZmE2IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogMy4gY2FkaXogLSBhaGxhbiBsb3VuZ2UgQCBnYXRlIGIyNjxicj5UZWxlcGhvbmU6ICs5NzEgNCA1MDUgMjAwMDxicj51cmw6IGh0dHA6Ly93d3cuZHViYWlpbnRsaG90ZWxzLmNvbS9kaW5pbmcvYWhsYW4tbG91bmdlLWI8L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfYTc2ZmFjMzU5YTlhNDZjN2FjYjA2ZmE1ZGMzM2IyMDcuc2V0Q29udGVudChodG1sXzdkYzI0MDY4MTk3ZDRlZGJhNWY1YjY1YjA4ZTdhZmE2KTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl9kZWFlMGIyOGZiNTM0NTk1ODUxMGExZjczOWQ5M2JkOS5iaW5kUG9wdXAocG9wdXBfYTc2ZmFjMzU5YTlhNDZjN2FjYjA2ZmE1ZGMzM2IyMDcpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzAwMDRhMzIwOTc5NDQ2ODFiNjJkZDBhNDg5ZDBhZGZhID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMTA0MzI5NiwgNTUuMTQ4NzY5MV0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiYiIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJiIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiA1LCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF9lMzUwODdlNzgzYTE0NDg3YTk3Njk2ZDNmMDlmYjM3OCA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfMTA5NTkzOTI0NGZhNDA2NGEyNjFiNGFlYjU2NDdmNWIgPSAkKGA8ZGl2IGlkPSJodG1sXzEwOTU5MzkyNDRmYTQwNjRhMjYxYjRhZWI1NjQ3ZjViIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogNC4gYmx2ZCBvbiBvbmU8YnI+VGVsZXBob25lOiArOTcxIDQgNDU1IDk5ODk8YnI+dXJsOiBodHRwOi8vZml2ZWhvdGVsc2FuZHJlc29ydHMuY29tL2RpbmUtZHJpbmstZGFuY2UvcmVzdGF1cmFudHMvYmx2ZC1vbi1vbmUvPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwX2UzNTA4N2U3ODNhMTQ0ODdhOTc2OTZkM2YwOWZiMzc4LnNldENvbnRlbnQoaHRtbF8xMDk1OTM5MjQ0ZmE0MDY0YTI2MWI0YWViNTY0N2Y1Yik7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfMDAwNGEzMjA5Nzk0NDY4MWI2MmRkMGE0ODlkMGFkZmEuYmluZFBvcHVwKHBvcHVwX2UzNTA4N2U3ODNhMTQ0ODdhOTc2OTZkM2YwOWZiMzc4KQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9iZTFmMjg0NmZkNzA0OGZkOTZiYWY4MzY2MDFkZjc2MCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjI0ODE0NjIsIDU1LjI4NjY1MjVdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogImIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiYiIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogNSwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfNzM4NDY4ZjVlZWZmNGJjZTljMDZhNGE4YTIxY2ZiODEgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzliNDRjOGY0Yjg1YzRkMWZiOTQwNDliYTRkMGM3NmUxID0gJChgPGRpdiBpZD0iaHRtbF85YjQ0YzhmNGI4NWM0ZDFmYjk0MDQ5YmE0ZDBjNzZlMSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDUuIHB1cmFuaSBkaWxsaSBkdWJhaTxicj5UZWxlcGhvbmU6ICs5NzEgNTAgMjExIDY4MTY8YnI+dXJsOiBodHRwOi8vd3d3LnB1cmFuaWRpbGxpZHViYWkuY29tLzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF83Mzg0NjhmNWVlZmY0YmNlOWMwNmE0YThhMjFjZmI4MS5zZXRDb250ZW50KGh0bWxfOWI0NGM4ZjRiODVjNGQxZmI5NDA0OWJhNGQwYzc2ZTEpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyX2JlMWYyODQ2ZmQ3MDQ4ZmQ5NmJhZjgzNjYwMWRmNzYwLmJpbmRQb3B1cChwb3B1cF83Mzg0NjhmNWVlZmY0YmNlOWMwNmE0YThhMjFjZmI4MSkKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNGMwYTY5MDU1Y2RjNDg0MTkyZTFlYTlhZWI3NzRmZTUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4yMDgyNzMsIDU1LjI2MDYwMTVdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogImIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiYiIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogNSwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfZTZmNjlkYTA1N2QwNDNiMzhhYzM3MmRjYWM5OGQ3NmUgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzdkZGUyMTliYjNmMDQ3YmE4OWE3NzdhMzJlZGFjMzBhID0gJChgPGRpdiBpZD0iaHRtbF83ZGRlMjE5YmIzZjA0N2JhODlhNzc3YTMyZWRhYzMwYSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IFNwb25zb3JlZGdyYXBlc2tpbiBncmFwZSBiYXIgYW5kIGtpdGNoZW48YnI+VGVsZXBob25lOiArOTcxIDQgNDAzIDMxMTE8YnI+dXJsOiBodHRwOi8vd3d3LmxpdmVsYXZpbGxlLmNvbS9kaW5pbmcvR3JhcGVza2luL2luZGV4LmFzcHg8L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfZTZmNjlkYTA1N2QwNDNiMzhhYzM3MmRjYWM5OGQ3NmUuc2V0Q29udGVudChodG1sXzdkZGUyMTliYjNmMDQ3YmE4OWE3NzdhMzJlZGFjMzBhKTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl80YzBhNjkwNTVjZGM0ODQxOTJlMWVhOWFlYjc3NGZlNS5iaW5kUG9wdXAocG9wdXBfZTZmNjlkYTA1N2QwNDNiMzhhYzM3MmRjYWM5OGQ3NmUpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzJiMWYyNmRiZTZiNTRiMTFiNjM1MjllNmE5YzJmNGY2ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMTA0MzI5NiwgNTUuMTQ4NzY5MV0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiYiIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJiIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiA1LCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF8zMTUyYjExM2VlZmQ0ZTgwYmRmMjUyYjE5NmI1NWU0MCA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfZmIxMDdjYmJmYzkyNDc0YjgzNzIyMThlYmFlOWRkNGEgPSAkKGA8ZGl2IGlkPSJodG1sX2ZiMTA3Y2JiZmM5MjQ3NGI4MzcyMjE4ZWJhZTlkZDRhIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogNi4gdHJhdHRvcmlhIGJ5IGNpbnF1ZTxicj5UZWxlcGhvbmU6ICs5NzEgNCA0NTUgOTk4OTxicj51cmw6IGh0dHA6Ly9qdW1laXJhaHZpbGxhZ2UuZml2ZWhvdGVsc2FuZHJlc29ydHMuY29tL21lZXQtbWluZ2xlL3RyYXR0b3JpYS1ieS1jaW5xdWU8L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfMzE1MmIxMTNlZWZkNGU4MGJkZjI1MmIxOTZiNTVlNDAuc2V0Q29udGVudChodG1sX2ZiMTA3Y2JiZmM5MjQ3NGI4MzcyMjE4ZWJhZTlkZDRhKTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl8yYjFmMjZkYmU2YjU0YjExYjYzNTI5ZTZhOWMyZjRmNi5iaW5kUG9wdXAocG9wdXBfMzE1MmIxMTNlZWZkNGU4MGJkZjI1MmIxOTZiNTVlNDApCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2QzNGRhMDNjODE5MjRiZTQ4MWVlOTVmMTY3NThhZTAxID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMjU2ODc1NywgNTUuMzEyMDgxMV0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiYiIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJiIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiA1LCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF9iZGI2OTdkOTRjMjE0NjY5OTJlY2Y5MWI4Mjc0ODYxMCA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfNTk3NTJmZDE3NGUyNDAxY2I4MDVhODAxOGRmMTc2NzQgPSAkKGA8ZGl2IGlkPSJodG1sXzU5NzUyZmQxNzRlMjQwMWNiODA1YTgwMThkZjE3Njc0IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogNy4gZG9vcnMgZnJlZXN0eWxlIGdyaWxsPGJyPlRlbGVwaG9uZTogKzk3MSA0IDIwNCA5Mjk5PGJyPnVybDogaHR0cDovL3d3dy5kb29yc2R1YmFpLmNvbS9lbjwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF9iZGI2OTdkOTRjMjE0NjY5OTJlY2Y5MWI4Mjc0ODYxMC5zZXRDb250ZW50KGh0bWxfNTk3NTJmZDE3NGUyNDAxY2I4MDVhODAxOGRmMTc2NzQpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyX2QzNGRhMDNjODE5MjRiZTQ4MWVlOTVmMTY3NThhZTAxLmJpbmRQb3B1cChwb3B1cF9iZGI2OTdkOTRjMjE0NjY5OTJlY2Y5MWI4Mjc0ODYxMCkKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfN2E0YjZjNWQzMTgxNGJkMjkzMWQ5NjU2NDEzNzU2MzggPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4wNjU3OTM0LCA1NS4xMzgxMTU5XSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJiIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogImIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDUsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwX2NmMDYyNjQxNWM3NzQyZDRiMWIyY2M5N2NjZjc1OGUxID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF9mMzI3MTIwN2RmZDk0MDA1YWQzZjNkOGU1Y2M4YWM4YyA9ICQoYDxkaXYgaWQ9Imh0bWxfZjMyNzEyMDdkZmQ5NDAwNWFkM2YzZDhlNWNjOGFjOGMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiA4LiB1cmJhbiBiYXIgJiBraXRjaGVuIC0gdWJrPGJyPlRlbGVwaG9uZTogKzk3MSA0IDQzOCAwMDAwPGJyPnVybDogaHR0cDovL3d3dy5tb3ZlbnBpY2suY29tL2VuL21pZGRsZS1lYXN0L3VhZS9kdWJhaS9kdWJhaS1qdW1laXJhaC1sYWtlcy10b3dlcnMvcmVzdGF1cmFudHMvcmVzdGF1cmFudHMvdXJiYW4tYmFyLWtpdGNoZW4tdWJrPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwX2NmMDYyNjQxNWM3NzQyZDRiMWIyY2M5N2NjZjc1OGUxLnNldENvbnRlbnQoaHRtbF9mMzI3MTIwN2RmZDk0MDA1YWQzZjNkOGU1Y2M4YWM4Yyk7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfN2E0YjZjNWQzMTgxNGJkMjkzMWQ5NjU2NDEzNzU2MzguYmluZFBvcHVwKHBvcHVwX2NmMDYyNjQxNWM3NzQyZDRiMWIyY2M5N2NjZjc1OGUxKQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl81ZjNkZDNlZTdjOTE0ZGVmOWZhY2FmMzVlYmMwOTU1NiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjIzMzg0NDEsIDU1LjI2NTQ4MTJdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogImIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiYiIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogNSwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfMWQ0NjQ1YmQ3ODNmNDkyZDg4Mjk1OGEzNzY0NjQ4MTQgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sX2ZhMGJhZWNhMDBlZTQ0NDlhZjY3MGQ0MzExNDc5ODBhID0gJChgPGRpdiBpZD0iaHRtbF9mYTBiYWVjYTAwZWU0NDQ5YWY2NzBkNDMxMTQ3OTgwYSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDkuIGJhcmVmb290IGxvdW5nZTxicj5UZWxlcGhvbmU6ICs5NzEgNCAzNDYgMTExMTxicj51cmw6IGh0dHA6Ly93d3cuZHhibWFyaW5lLmNvbS88L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfMWQ0NjQ1YmQ3ODNmNDkyZDg4Mjk1OGEzNzY0NjQ4MTQuc2V0Q29udGVudChodG1sX2ZhMGJhZWNhMDBlZTQ0NDlhZjY3MGQ0MzExNDc5ODBhKTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl81ZjNkZDNlZTdjOTE0ZGVmOWZhY2FmMzVlYmMwOTU1Ni5iaW5kUG9wdXAocG9wdXBfMWQ0NjQ1YmQ3ODNmNDkyZDg4Mjk1OGEzNzY0NjQ4MTQpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzZkM2I4OTcwY2QxNzRlMWRhNGY4ODFkYTUzNmZiOTZkID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMjEyNjQyNiwgNTUuMjgyNDA1XSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJiIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogImIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDUsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwXzQ4NzYxN2U2NmFhYzQ0YWQ4NWJlNzBiYWU3OWQ5ZTJmID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF83YmYxYTgwNDFlZmU0NWUwYjMwNmIwNjgwNjY5ZGU2NyA9ICQoYDxkaXYgaWQ9Imh0bWxfN2JmMWE4MDQxZWZlNDVlMGIzMDZiMDY4MDY2OWRlNjciIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiAxMC4gbWluYSBicmFzc2VyaWU8YnI+VGVsZXBob25lOiArOTcxIDQgNTA2IDAxMDA8YnI+dXJsOiBodHRwOi8vd3d3Lm1pbmFicmFzc2VyaWUuY29tLzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF80ODc2MTdlNjZhYWM0NGFkODViZTcwYmFlNzlkOWUyZi5zZXRDb250ZW50KGh0bWxfN2JmMWE4MDQxZWZlNDVlMGIzMDZiMDY4MDY2OWRlNjcpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyXzZkM2I4OTcwY2QxNzRlMWRhNGY4ODFkYTUzNmZiOTZkLmJpbmRQb3B1cChwb3B1cF80ODc2MTdlNjZhYWM0NGFkODViZTcwYmFlNzlkOWUyZikKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNmNjM2IzYzA2YmFjNGE0NmFjNWI5MzM4YmFlYWNjZDUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4yMDgyNzMsIDU1LjI2MDYwMTVdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogImIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiYiIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogNSwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfZjE4NWM4YWEyZTI5NDI5OThlZGU1NDQ0ODhhMWIzOWMgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzgzNjQ0ZDhlYWZkZjRmODVhYjI0MmE1MjJmNmQ4ZGI0ID0gJChgPGRpdiBpZD0iaHRtbF84MzY0NGQ4ZWFmZGY0Zjg1YWIyNDJhNTIyZjZkOGRiNCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IFNwb25zb3JlZGdyYXplIGdhc3RybyBncmlsbDxicj5UZWxlcGhvbmU6ICs5NzEgNCA0MDMgMzExMTxicj51cmw6IGh0dHA6Ly93d3cubGl2ZWxhdmlsbGUuY29tL2RpbmluZy9HcmF6ZS9pbmRleC5odG1sPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwX2YxODVjOGFhMmUyOTQyOTk4ZWRlNTQ0NDg4YTFiMzljLnNldENvbnRlbnQoaHRtbF84MzY0NGQ4ZWFmZGY0Zjg1YWIyNDJhNTIyZjZkOGRiNCk7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfNmNjM2IzYzA2YmFjNGE0NmFjNWI5MzM4YmFlYWNjZDUuYmluZFBvcHVwKHBvcHVwX2YxODVjOGFhMmUyOTQyOTk4ZWRlNTQ0NDg4YTFiMzljKQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl82NTg0MmNjYzQwNTQ0N2U5YWM0NzVkZDNkNTUzOWNhNyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI0LjgxNjgyMDYsIDU1LjIzMTI4NzJdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogImIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiYiIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogNSwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfMzIzMmE3MDc5NWEzNGRiNGI3OTg0MDExZmEzMGNkN2IgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sX2U2YWJjOTU1YzI3MjRmNmQ4ODJjZDYyYmM0MzQ2YjlmID0gJChgPGRpdiBpZD0iaHRtbF9lNmFiYzk1NWMyNzI0ZjZkODgyY2Q2MmJjNDM0NmI5ZiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDExLiBhbCBzYXJhYiByb29mdG9wIGxvdW5nZTxicj5UZWxlcGhvbmU6ICs5NzEgNCA4MDkgNjEwMDxicj51cmw6IGh0dHA6Ly93d3cubWV5ZGFuaG90ZWxzLmNvbS9iYWJhbHNoYW1zL2RpbmluZy5odG08L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfMzIzMmE3MDc5NWEzNGRiNGI3OTg0MDExZmEzMGNkN2Iuc2V0Q29udGVudChodG1sX2U2YWJjOTU1YzI3MjRmNmQ4ODJjZDYyYmM0MzQ2YjlmKTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl82NTg0MmNjYzQwNTQ0N2U5YWM0NzVkZDNkNTUzOWNhNy5iaW5kUG9wdXAocG9wdXBfMzIzMmE3MDc5NWEzNGRiNGI3OTg0MDExZmEzMGNkN2IpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzViNzM4OGVmODZiMzRlM2ViZWJkMjY3OWI4MDZkYjYwID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMDQ2Mjk0NiwgNTUuMjAzMDQxMTk5OTk5OTldLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogImIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiYiIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogNSwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfMTI5Nzc2NjA4YmNiNGY5NjlkOWNiMjZmZDM5ODI2ZDQgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzYwZTBmNTU3ZGQ1YTQyMjU5ZjZlMmJjMjA4OTYyYWJkID0gJChgPGRpdiBpZD0iaHRtbF82MGUwZjU1N2RkNWE0MjI1OWY2ZTJiYzIwODk2MmFiZCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDEyLiBzb3VsIHN0cmVldDxicj5UZWxlcGhvbmU6ICs5NzEgNCA0NTUgOTk4OTxicj51cmw6IGh0dHA6Ly9zb3VsLnN0LzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF8xMjk3NzY2MDhiY2I0Zjk2OWQ5Y2IyNmZkMzk4MjZkNC5zZXRDb250ZW50KGh0bWxfNjBlMGY1NTdkZDVhNDIyNTlmNmUyYmMyMDg5NjJhYmQpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyXzViNzM4OGVmODZiMzRlM2ViZWJkMjY3OWI4MDZkYjYwLmJpbmRQb3B1cChwb3B1cF8xMjk3NzY2MDhiY2I0Zjk2OWQ5Y2IyNmZkMzk4MjZkNCkKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNTYxNDhlMGQyNTNiNDdkZGExM2ExZjlmODE3NTdkNGEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4yNDkxNTQ5LCA1NS4zNDcxMzk2MDAwMDAwMV0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiYiIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJiIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiA1LCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF9jMDM0NzVmNWU0ZTg0N2Q4OTlkZjJiNTYwNmQ5OTU0ZiA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfYTZkNWNkZTE2NzkxNGVlNWE5N2UxOWMzMjQ1YjlmOWQgPSAkKGA8ZGl2IGlkPSJodG1sX2E2ZDVjZGUxNjc5MTRlZTVhOTdlMTljMzI0NWI5ZjlkIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogMTMuIGJlYmVtb3M8YnI+VGVsZXBob25lOiArOTcxIDQgNzAyIDI0NTU8YnI+dXJsOiBodHRwOi8vd3d3LmJlYmVtb3NkdWJhaS5jb20vPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwX2MwMzQ3NWY1ZTRlODQ3ZDg5OWRmMmI1NjA2ZDk5NTRmLnNldENvbnRlbnQoaHRtbF9hNmQ1Y2RlMTY3OTE0ZWU1YTk3ZTE5YzMyNDViOWY5ZCk7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfNTYxNDhlMGQyNTNiNDdkZGExM2ExZjlmODE3NTdkNGEuYmluZFBvcHVwKHBvcHVwX2MwMzQ3NWY1ZTRlODQ3ZDg5OWRmMmI1NjA2ZDk5NTRmKQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9lNzhkNDBhZTQ4NjY0ODA0ODk1NWVkY2E1OGU5OGIxNyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjIyODgzOTQsIDU1LjMyNjgxMjVdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogImIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiYiIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogNSwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfYjgxZWNkZGI3ODgwNDg3MmIxZWQ1MTQ1MWMwODZiMzEgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzhhZjE3MWJlMDAzYjRmYmE5YTUzNTRjN2Q4YjhlZDU2ID0gJChgPGRpdiBpZD0iaHRtbF84YWYxNzFiZTAwM2I0ZmJhOWE1MzU0YzdkOGI4ZWQ1NiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDE0LiBhd3Rhcjxicj5UZWxlcGhvbmU6ICs5NzEgNCAzMTcgMjIyMTxicj51cmw6IGh0dHBzOi8vd3d3Lmh5YXR0cmVzdGF1cmFudHMuY29tL2VuL2RpbmluZy91YWUvZHViYWkvbWlkZGxlLWVhc3Rlcm4tcmVzdGF1cmFudC1pbi1nYXJob3VkLWF3dGFyP3V0bV9zb3VyY2U9Z21ibGlzdGluZ19keGJnaCZ1dG1fbWVkaXVtPWF3dGFyJnV0bV9jYW1wYWlnbj1HTUI8L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfYjgxZWNkZGI3ODgwNDg3MmIxZWQ1MTQ1MWMwODZiMzEuc2V0Q29udGVudChodG1sXzhhZjE3MWJlMDAzYjRmYmE5YTUzNTRjN2Q4YjhlZDU2KTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl9lNzhkNDBhZTQ4NjY0ODA0ODk1NWVkY2E1OGU5OGIxNy5iaW5kUG9wdXAocG9wdXBfYjgxZWNkZGI3ODgwNDg3MmIxZWQ1MTQ1MWMwODZiMzEpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzQ3NjVkZjcxZWE3MzQxM2JhMWJkMTM0MmZiMTU0MjJkID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMTk4NzY1LCA1NS4yNzk2MDUzXSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJiIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogImIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDUsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwXzdhNzc0YjlkYmQ2YTRiNDlhMWU2OGRmMDAzNDBkN2NlID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF8yMzBiNGMxOWQwZTY0Y2M4YmU2ZGEyNmEwZjFiNDUwMiA9ICQoYDxkaXYgaWQ9Imh0bWxfMjMwYjRjMTlkMGU2NGNjOGJlNmRhMjZhMGYxYjQ1MDIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiAxNS4gdHJpYmVzIGNhcm5pdm9yZTxicj5UZWxlcGhvbmU6ICs5NzEgNCAyMjYgNDk3NDxicj51cmw6IGh0dHA6Ly90cmliZXNyZXN0YXVyYW50LmNvbS88L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfN2E3NzRiOWRiZDZhNGI0OWExZTY4ZGYwMDM0MGQ3Y2Uuc2V0Q29udGVudChodG1sXzIzMGI0YzE5ZDBlNjRjYzhiZTZkYTI2YTBmMWI0NTAyKTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl80NzY1ZGY3MWVhNzM0MTNiYTFiZDEzNDJmYjE1NDIyZC5iaW5kUG9wdXAocG9wdXBfN2E3NzRiOWRiZDZhNGI0OWExZTY4ZGYwMDM0MGQ3Y2UpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2U1NjBiNTMyMmIxYjRmN2NiZGIyYWY2YjVlYTVhZGE5ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMjIxNjAzLCA1NS4yODA4MjYyXSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJiIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogImIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDUsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwX2YyYzkzNDY4ODk4ZjRmMGZiMTkyZGY3Njk5MjI0ZjM3ID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF85OGJkMDgyMWUwYWY0ZDU2OGQ2OTcwOGI2YzI1MjEwMiA9ICQoYDxkaXYgaWQ9Imh0bWxfOThiZDA4MjFlMGFmNGQ1NjhkNjk3MDhiNmMyNTIxMDIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiBTcG9uc29yZWRzdXNoaSBuYXRpb25zPGJyPlRlbGVwaG9uZTogKzk3MSA1NiAxODggODUyMjxicj51cmw6IGh0dHBzOi8vc3VzaGluYXRpb25zLmFlLzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF9mMmM5MzQ2ODg5OGY0ZjBmYjE5MmRmNzY5OTIyNGYzNy5zZXRDb250ZW50KGh0bWxfOThiZDA4MjFlMGFmNGQ1NjhkNjk3MDhiNmMyNTIxMDIpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyX2U1NjBiNTMyMmIxYjRmN2NiZGIyYWY2YjVlYTVhZGE5LmJpbmRQb3B1cChwb3B1cF9mMmM5MzQ2ODg5OGY0ZjBmYjE5MmRmNzY5OTIyNGYzNykKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMTZjNWRlYzQwMmU2NDNiYzljMmEwOTg2NjJmNjRlNjIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4yNzg4OTgsIDU1LjMwNDQ2MDddLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogImIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiYiIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogNSwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfOTkxN2M4NGU2NTBlNDlmZjkyZDdjNWQ4ZWJiOGMxNzIgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzRlNGVkYTYyOGVjYTRmZWI4M2RiOWFmODQxMTQ1ZjJlID0gJChgPGRpdiBpZD0iaHRtbF80ZTRlZGE2MjhlY2E0ZmViODNkYjlhZjg0MTE0NWYyZSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDE2LiBhbCBkYXdhYXIgcmV2b2x2aW5nIHJlc3RhdXJhbnQ8YnI+VGVsZXBob25lOiArOTcxIDQgMjA5IDY5MTI8YnI+dXJsOiBodHRwOi8vd3d3Lmh5YXR0cmVzdGF1cmFudHMuY29tL2VuL2RpbmluZy91YWUvZHViYWkvaW50ZXJuYXRpb25hbC1yZXN0YXVyYW50LWluLWRlaXJhLWNvcm5pY2hlLWFsLWRhd2Fhci1yZXZvbHZpbmctcmVzdGF1cmFudDwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF85OTE3Yzg0ZTY1MGU0OWZmOTJkN2M1ZDhlYmI4YzE3Mi5zZXRDb250ZW50KGh0bWxfNGU0ZWRhNjI4ZWNhNGZlYjgzZGI5YWY4NDExNDVmMmUpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyXzE2YzVkZWM0MDJlNjQzYmM5YzJhMDk4NjYyZjY0ZTYyLmJpbmRQb3B1cChwb3B1cF85OTE3Yzg0ZTY1MGU0OWZmOTJkN2M1ZDhlYmI4YzE3MikKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfOWJjNTlhMzJiN2U5NGZkNmE4Y2RjYmFlYjY0OTJmZTEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4xMTEzOTkxLCA1NS4xMzcyMTU4XSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJiIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogImIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDUsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwXzliZWIwODhjODg3YTRhYmM4MTM2YzczMzMwZTZiZjljID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF9mNjIyYTY4MWRmZDA0ODcwYmIzYzUwZmY1Y2Y1NTIyYiA9ICQoYDxkaXYgaWQ9Imh0bWxfZjYyMmE2ODFkZmQwNDg3MGJiM2M1MGZmNWNmNTUyMmIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiAxNy4ga2h5YmVyPGJyPlRlbGVwaG9uZTogKzk3MSA0IDQ1NSAxMTExPGJyPnVybDogaHR0cHM6Ly93d3cuZHVrZXNkdWJhaS5jb20va2h5YmVyLzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF85YmViMDg4Yzg4N2E0YWJjODEzNmM3MzMzMGU2YmY5Yy5zZXRDb250ZW50KGh0bWxfZjYyMmE2ODFkZmQwNDg3MGJiM2M1MGZmNWNmNTUyMmIpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyXzliYzU5YTMyYjdlOTRmZDZhOGNkY2JhZWI2NDkyZmUxLmJpbmRQb3B1cChwb3B1cF85YmViMDg4Yzg4N2E0YWJjODEzNmM3MzMzMGU2YmY5YykKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYzhjZjM5ZjFjYzYwNDE0MGIxMmNlNDU0N2ExYWVjZTMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4yNjYyNjc4LCA1NS4zMDg3ODc0OTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiYiIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJiIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiA1LCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF9mODk4NDg3MWI2MTg0ZDE2OWRhNDQzMDE4ZTYxYzcxYiA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfMGFkYTQ0NjNmZWIxNDM4NDg1N2IzYmFkNGEzMTAwY2EgPSAkKGA8ZGl2IGlkPSJodG1sXzBhZGE0NDYzZmViMTQzODQ4NTdiM2JhZDRhMzEwMGNhIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogMTguIGRhbmlhbCByZXN0YXVyYW50PGJyPlRlbGVwaG9uZTogKzk3MSA0IDIyNyA3NjY5PGJyPnVybDogaHR0cDovL3d3dy5kYW5pYWxyZXN0YXVyYW50LmNvbS88L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfZjg5ODQ4NzFiNjE4NGQxNjlkYTQ0MzAxOGU2MWM3MWIuc2V0Q29udGVudChodG1sXzBhZGE0NDYzZmViMTQzODQ4NTdiM2JhZDRhMzEwMGNhKTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl9jOGNmMzlmMWNjNjA0MTQwYjEyY2U0NTQ3YTFhZWNlMy5iaW5kUG9wdXAocG9wdXBfZjg5ODQ4NzFiNjE4NGQxNjlkYTQ0MzAxOGU2MWM3MWIpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzdjYzg0ZGRhYzE3YjQwYTI4ZDQ0YjZkN2M3ZTJjNzE0ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMjM0MzU1LCA1NS4zMjQwMTQ3XSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJiIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogImIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDUsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwXzg1YTE3NzU5MzRhZTQ3ODU5YWUyZjY3ODQ5MWU1NmQxID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF9kMjQzYTFjNGI0NDI0NTRmODFmMTc4ZmE2YTgwMjk3NSA9ICQoYDxkaXYgaWQ9Imh0bWxfZDI0M2ExYzRiNDQyNDU0ZjgxZjE3OGZhNmE4MDI5NzUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiAxOS4gZXZlIHBlbnRob3VzZSAmIGxvdW5nZTxicj5UZWxlcGhvbmU6ICs5NzEgNCA1NTMgMTIxNDxicj51cmw6IGh0dHA6Ly93d3cuaHlhdHRyZXN0YXVyYW50cy5jb20vZW4vZGluaW5nL3VhZS9kdWJhaS9pbnRlcm5hdGlvbmFsLXJlc3RhdXJhbnQtaW4tb3VkLW1ldGhhLXJvYWQtZXZlLXBlbnRob3VzZS1sb3VuZ2U/dXRtX3NvdXJjZT1XZWJzaXRlX2R4YmhjJnV0bV9tZWRpdW09ZXZlJnV0bV9jYW1wYWlnbj1IeWF0dDwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF84NWExNzc1OTM0YWU0Nzg1OWFlMmY2Nzg0OTFlNTZkMS5zZXRDb250ZW50KGh0bWxfZDI0M2ExYzRiNDQyNDU0ZjgxZjE3OGZhNmE4MDI5NzUpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyXzdjYzg0ZGRhYzE3YjQwYTI4ZDQ0YjZkN2M3ZTJjNzE0LmJpbmRQb3B1cChwb3B1cF84NWExNzc1OTM0YWU0Nzg1OWFlMmY2Nzg0OTFlNTZkMSkKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYjk4YWNmNTc5N2ZlNGQ0NmFjNjZlZmU2NGI3MWE4MzAgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4xOTg3NjUsIDU1LjI3OTYwNTNdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogImIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiYiIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogNSwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfMzkzYTA4NWRmOWNiNGNkNWE4MTU3ZDRjZWYyNjkxM2IgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzJiYmVmZTc3M2YxYTQwZmI5Zjg4YzUyMTRhMTdjMWYxID0gJChgPGRpdiBpZD0iaHRtbF8yYmJlZmU3NzNmMWE0MGZiOWY4OGM1MjE0YTE3YzFmMSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDIwLiB0aGUgZ3JpbGwgc2hhY2s8YnI+VGVsZXBob25lOiArOTcxIDQgMzg4IDIzODI8YnI+dXJsOiBodHRwOi8vd3d3LnRoZWdyaWxsbHNoYWNrLmNvbS88L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfMzkzYTA4NWRmOWNiNGNkNWE4MTU3ZDRjZWYyNjkxM2Iuc2V0Q29udGVudChodG1sXzJiYmVmZTc3M2YxYTQwZmI5Zjg4YzUyMTRhMTdjMWYxKTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl9iOThhY2Y1Nzk3ZmU0ZDQ2YWM2NmVmZTY0YjcxYTgzMC5iaW5kUG9wdXAocG9wdXBfMzkzYTA4NWRmOWNiNGNkNWE4MTU3ZDRjZWYyNjkxM2IpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2IzNzQ1ZmM0ZmUxMDQ4ZDE4YmFlZDczOTI2ZjZjZmEzID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMjQ3ODY3LCA1NS4zMDA0OTI1XSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJiIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogImIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDUsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwXzczOGFmMmI4YjZlNTRhNDZhNGRkZDgzYzRkNmQxZjdiID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF81YTM4MDY0OGQyZjY0ZDQyYTY3MTA0ZDU2OGMzZTk5NSA9ICQoYDxkaXYgaWQ9Imh0bWxfNWEzODA2NDhkMmY2NGQ0MmE2NzEwNGQ1NjhjM2U5OTUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiBTcG9uc29yZWRhbXJpdHNyIHJlc3RhdXJhbnQ8YnI+VGVsZXBob25lOiArOTcxIDUwIDY3OCAwMDk2PGJyPnVybDogaHR0cDovL2Ftcml0c3J1YWUuY29tLzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF83MzhhZjJiOGI2ZTU0YTQ2YTRkZGQ4M2M0ZDZkMWY3Yi5zZXRDb250ZW50KGh0bWxfNWEzODA2NDhkMmY2NGQ0MmE2NzEwNGQ1NjhjM2U5OTUpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyX2IzNzQ1ZmM0ZmUxMDQ4ZDE4YmFlZDczOTI2ZjZjZmEzLmJpbmRQb3B1cChwb3B1cF83MzhhZjJiOGI2ZTU0YTQ2YTRkZGQ4M2M0ZDZkMWY3YikKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfODExZjVhODRmZTliNDNlMTlhZTVhNmVhYjUzN2EyY2MgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4xMDQzMjk2LCA1NS4xNDg3NjkxXSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJiIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogImIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDUsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwXzkxZmU1NGZlNjQwOTRiY2U4Y2JmYTkxNjAwN2M1ZWEwID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF8wZWRmN2ZjYjEzY2Y0YmM1OThjYjQ5ZDVlZjYzY2UwNyA9ICQoYDxkaXYgaWQ9Imh0bWxfMGVkZjdmY2IxM2NmNGJjNTk4Y2I0OWQ1ZWY2M2NlMDciIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiAyMS4gbWFpZGVuIHNoYW5naGFpPGJyPlRlbGVwaG9uZTogKzk3MSA0IDQ1NSA5OTg5PGJyPnVybDogaHR0cDovL2ZpdmVob3RlbHNhbmRyZXNvcnRzLmNvbS9kaW5lLWRyaW5rLWRhbmNlL3Jlc3RhdXJhbnRzL21haWRlbi1zaGFuZ2hhaS88L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfOTFmZTU0ZmU2NDA5NGJjZThjYmZhOTE2MDA3YzVlYTAuc2V0Q29udGVudChodG1sXzBlZGY3ZmNiMTNjZjRiYzU5OGNiNDlkNWVmNjNjZTA3KTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl84MTFmNWE4NGZlOWI0M2UxOWFlNWE2ZWFiNTM3YTJjYy5iaW5kUG9wdXAocG9wdXBfOTFmZTU0ZmU2NDA5NGJjZThjYmZhOTE2MDA3YzVlYTApCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2JhNTBiN2FmZTk4YTQyMzNhOGM2MTFkOWE3OTg0NTRhID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMjE0MDEzMywgNTUuMjc2MDg4NV0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiYiIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJiIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiA1LCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF81OWM3ZjMyNzUxNzA0YWFiYjczZjQwYzMyZmRhNjQ0ZiA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfMzkwZWM3ZjI2NjgzNGU1MGJhNTEwN2RmNDBhMTM0NDcgPSAkKGA8ZGl2IGlkPSJodG1sXzM5MGVjN2YyNjY4MzRlNTBiYTUxMDdkZjQwYTEzNDQ3IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogMjIuIHB1cmFuaSBkaWxsaSBzaGVpa2ggemF5ZWQgcm9hZDxicj5UZWxlcGhvbmU6ICs5NzEgNCAzMTYgOTcyNjxicj51cmw6IGh0dHA6Ly93d3cucHVyYW5pZGlsbGlkdWJhaS5jb20vc2hlaWtoemF5ZWRyb2FkPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwXzU5YzdmMzI3NTE3MDRhYWJiNzNmNDBjMzJmZGE2NDRmLnNldENvbnRlbnQoaHRtbF8zOTBlYzdmMjY2ODM0ZTUwYmE1MTA3ZGY0MGExMzQ0Nyk7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfYmE1MGI3YWZlOThhNDIzM2E4YzYxMWQ5YTc5ODQ1NGEuYmluZFBvcHVwKHBvcHVwXzU5YzdmMzI3NTE3MDRhYWJiNzNmNDBjMzJmZGE2NDRmKQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl85ZDNkZTJhMDE2NjE0NjUxYjI5NGVjZjkzMzY1ZDZlNiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjIxNDAxMzMsIDU1LjI3NjA4ODVdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogImIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiYiIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogNSwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfYmM5ZDdiNDc3NmY3NDNlNTk3ZjExNTEwNjRkNDI3OWYgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzYxODk4MzlhZmQyZDQwMjBiMDZlYjRiYWZkMGExM2VhID0gJChgPGRpdiBpZD0iaHRtbF82MTg5ODM5YWZkMmQ0MDIwYjA2ZWI0YmFmZDBhMTNlYSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDIzLiBsZXZlbCA0MyBza3kgbG91bmdlPGJyPlRlbGVwaG9uZTogKzk3MSA1NiA0MTQgMjIxMzxicj51cmw6IGh0dHA6Ly93d3cubGV2ZWw0M2xvdW5nZS5jb20vPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwX2JjOWQ3YjQ3NzZmNzQzZTU5N2YxMTUxMDY0ZDQyNzlmLnNldENvbnRlbnQoaHRtbF82MTg5ODM5YWZkMmQ0MDIwYjA2ZWI0YmFmZDBhMTNlYSk7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfOWQzZGUyYTAxNjYxNDY1MWIyOTRlY2Y5MzM2NWQ2ZTYuYmluZFBvcHVwKHBvcHVwX2JjOWQ3YjQ3NzZmNzQzZTU5N2YxMTUxMDY0ZDQyNzlmKQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8yZTU3NTg1NTU0NTA0MTBlOGQwNjc0NmMwYzdlNjI2MiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjE5NTE1NTQsIDU1LjI3NTE1NzldLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogImIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiYiIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogNSwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfZWE3MmZhYmRkZjEwNDkxMmEyNzg0NDAzZmVjYTYzMjYgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzFiY2QxMmNlNzFkZDQxNzg5NjJiOTYwYzAwNzdlNGEwID0gJChgPGRpdiBpZD0iaHRtbF8xYmNkMTJjZTcxZGQ0MTc4OTYyYjk2MGMwMDc3ZTRhMCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDI0LiBibGFjayB0YXAgY3JhZnQgYnVyZ2VycyAmIHNoYWtlcyBkdWJhaSBtYWxsPGJyPlRlbGVwaG9uZTogKzk3MSA0IDMzMCA1MTAzPGJyPnVybDogaHR0cDovL3d3dy5ibGFja3RhcG1lLmNvbS88L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfZWE3MmZhYmRkZjEwNDkxMmEyNzg0NDAzZmVjYTYzMjYuc2V0Q29udGVudChodG1sXzFiY2QxMmNlNzFkZDQxNzg5NjJiOTYwYzAwNzdlNGEwKTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl8yZTU3NTg1NTU0NTA0MTBlOGQwNjc0NmMwYzdlNjI2Mi5iaW5kUG9wdXAocG9wdXBfZWE3MmZhYmRkZjEwNDkxMmEyNzg0NDAzZmVjYTYzMjYpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2UyODQ1MjAyZGM5YjQwNWViYmFjZTA5YTFjNDk4NzI4ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMjQ5MTU0OSwgNTUuMzQ3MTM5NjAwMDAwMDFdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogImIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiYiIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogNSwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfZmMxNWNjYmM5NmFiNDhmNmFlMzgzMGFmZmIwNmZmMzcgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzU2Y2M0YTYzNzdlYjQ1MTM5ODJlZmEzZDgwYzJlODZjID0gJChgPGRpdiBpZD0iaHRtbF81NmNjNGE2Mzc3ZWI0NTEzOTgyZWZhM2Q4MGMyZTg2YyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDI1LiBiZWVmIGJpc3Rybzxicj5UZWxlcGhvbmU6ICs5NzEgNCA3MDIgMjQ1NTxicj51cmw6IGh0dHA6Ly93d3cuYmVlZmJpc3Ryb2R1YmFpLmNvbS88L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfZmMxNWNjYmM5NmFiNDhmNmFlMzgzMGFmZmIwNmZmMzcuc2V0Q29udGVudChodG1sXzU2Y2M0YTYzNzdlYjQ1MTM5ODJlZmEzZDgwYzJlODZjKTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl9lMjg0NTIwMmRjOWI0MDVlYmJhY2UwOWExYzQ5ODcyOC5iaW5kUG9wdXAocG9wdXBfZmMxNWNjYmM5NmFiNDhmNmFlMzgzMGFmZmIwNmZmMzcpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2JiNWM2NGVlOTEyYjQyNGE4ODRkNWVjMzU5ZTY5MGM0ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMjAyNDQ4NSwgNTUuMjM5NjUyNV0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiYiIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJiIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiA1LCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF82ZmQ2ZTRlMWE5Y2M0MjQzOTE3MDVmYzg3NTI5NmY5OCA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfZTYyNTNhMWY2YTIyNGQzYmJlZjIxZDAzMTMwYzI1ZjQgPSAkKGA8ZGl2IGlkPSJodG1sX2U2MjUzYTFmNmEyMjRkM2JiZWYyMWQwMzEzMGMyNWY0IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogU3BvbnNvcmVkdmVyZGUgZHViYWk8YnI+VGVsZXBob25lOiArOTcxIDQgMzMzIDgwMjU8YnI+dXJsOiBodHRwOi8vd3d3LnZlcmRlLWR1YmFpLmNvbS88L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfNmZkNmU0ZTFhOWNjNDI0MzkxNzA1ZmM4NzUyOTZmOTguc2V0Q29udGVudChodG1sX2U2MjUzYTFmNmEyMjRkM2JiZWYyMWQwMzEzMGMyNWY0KTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl9iYjVjNjRlZTkxMmI0MjRhODg0ZDVlYzM1OWU2OTBjNC5iaW5kUG9wdXAocG9wdXBfNmZkNmU0ZTFhOWNjNDI0MzkxNzA1ZmM4NzUyOTZmOTgpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzg4MmY1OTIzZmM2NjQ3NDE5MTIyOWFlY2JiYTIyMmNiID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMjI5NTMwOSwgNTUuMjg2NjcyOF0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiYiIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJiIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiA1LCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF81YjVkYWUxMWZmNGY0YzhiYTNhMTAyNDZhOTY1ZDE1NyA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfZmE4MGQyNWE5MzIzNGM3ZmJjZmI1ZjdiM2VlOTFhYzIgPSAkKGA8ZGl2IGlkPSJodG1sX2ZhODBkMjVhOTMyMzRjN2ZiY2ZiNWY3YjNlZTkxYWMyIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogMjYuIG5pZG8gdGFwYXMgcmVzdGF1cmFudCAmIGJhcjxicj5UZWxlcGhvbmU6ICs5NzEgNCAzMzMgMzA1NTxicj51cmw6IGh0dHA6Ly9uaWRvZHhiLmNvbS88L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfNWI1ZGFlMTFmZjRmNGM4YmEzYTEwMjQ2YTk2NWQxNTcuc2V0Q29udGVudChodG1sX2ZhODBkMjVhOTMyMzRjN2ZiY2ZiNWY3YjNlZTkxYWMyKTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl84ODJmNTkyM2ZjNjY0NzQxOTEyMjlhZWNiYmEyMjJjYi5iaW5kUG9wdXAocG9wdXBfNWI1ZGFlMTFmZjRmNGM4YmEzYTEwMjQ2YTk2NWQxNTcpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzJlMjU1NDdhMWY4YTQyYWE4YWQxOGUzNjQxNmNlYjU2ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMDgwNDc3NywgNTUuMTU0MTk0MzAwMDAwMDFdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogImIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiYiIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogNSwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfNDAxMTk5MDdmMDY1NDVhOGEyM2JkOGM4Y2JiMjAxOTEgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzM2OGY5ODNmODgxNzQ4NWJhYmFhYTgxMWFjZjllYzk1ID0gJChgPGRpdiBpZD0iaHRtbF8zNjhmOTgzZjg4MTc0ODViYWJhYWE4MTFhY2Y5ZWM5NSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDI3LiBzaGFtaWFuYTxicj5UZWxlcGhvbmU6ICs5NzEgNCA1NzQgMTExMTxicj51cmw6IGh0dHA6Ly93d3cudGFqaG90ZWxzLmNvbS9lbi1pbi90YWovdGFqLWp1bWVpcmFoLWxha2VzLXRvd2Vycy9yZXN0YXVyYW50cy9zaGFtaWFuYS88L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfNDAxMTk5MDdmMDY1NDVhOGEyM2JkOGM4Y2JiMjAxOTEuc2V0Q29udGVudChodG1sXzM2OGY5ODNmODgxNzQ4NWJhYmFhYTgxMWFjZjllYzk1KTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl8yZTI1NTQ3YTFmOGE0MmFhOGFkMThlMzY0MTZjZWI1Ni5iaW5kUG9wdXAocG9wdXBfNDAxMTk5MDdmMDY1NDVhOGEyM2JkOGM4Y2JiMjAxOTEpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2NiODBiZDBhYzBmYTQ2NWVhMTRjOTJlNjI3MzYzZTQwID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMjA0ODQ5MywgNTUuMjcwNzgyOF0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiYiIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJiIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiA1LCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF9lMWRhODUwMmFiNDk0ZjQyOWY2MzEzNjJkNzY2YThkMyA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfMGM2ZTNiOTYwZTEyNDZiNTljYzgzODE4ZGY3NGI4NDggPSAkKGA8ZGl2IGlkPSJodG1sXzBjNmUzYjk2MGUxMjQ2YjU5Y2M4MzgxOGRmNzRiODQ4IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogMjguIGtpbmFyYSBieSB2aWthcyBraGFubmE8YnI+VGVsZXBob25lOiArOTcxIDQgODE0IDU1NTU8YnI+dXJsOiBodHRwOi8vd3d3LmtpbmFyYWR1YmFpLmNvbS88L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfZTFkYTg1MDJhYjQ5NGY0MjlmNjMxMzYyZDc2NmE4ZDMuc2V0Q29udGVudChodG1sXzBjNmUzYjk2MGUxMjQ2YjU5Y2M4MzgxOGRmNzRiODQ4KTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl9jYjgwYmQwYWMwZmE0NjVlYTE0YzkyZTYyNzM2M2U0MC5iaW5kUG9wdXAocG9wdXBfZTFkYTg1MDJhYjQ5NGY0MjlmNjMxMzYyZDc2NmE4ZDMpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzM2YmJmNWUxMWE2MjRjYzFiOTlmMDlkNzdjYzYwNmE2ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMTEwODIwMiwgNTUuMTM5OTE4NDAwMDAwMDFdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogImIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiYiIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogNSwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfNmY2MzI0ZjYxM2IxNGExYjk2YTUyMGE5OWNiMGY3NTMgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sX2Y3MDNkM2E2NzJiZTQ3OTQ5MzJhYmVlZGI4NmRjMDNhID0gJChgPGRpdiBpZD0iaHRtbF9mNzAzZDNhNjcyYmU0Nzk0OTMyYWJlZWRiODZkYzAzYSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDI5LiBsaXR0bGUgbWlzcyBpbmRpYTxicj5UZWxlcGhvbmU6ICs5NzEgNCA0NTcgMzQ1Nzxicj51cmw6IGh0dHA6Ly93d3cuZmFpcm1vbnQuY29tL3BhbG0tZHViYWkvZGluaW5nL2xpdHRsZS1taXNzLWluZGlhLzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF82ZjYzMjRmNjEzYjE0YTFiOTZhNTIwYTk5Y2IwZjc1My5zZXRDb250ZW50KGh0bWxfZjcwM2QzYTY3MmJlNDc5NDkzMmFiZWVkYjg2ZGMwM2EpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyXzM2YmJmNWUxMWE2MjRjYzFiOTlmMDlkNzdjYzYwNmE2LmJpbmRQb3B1cChwb3B1cF82ZjYzMjRmNjEzYjE0YTFiOTZhNTIwYTk5Y2IwZjc1MykKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNGE3YzljOGNmYzFjNGQ4ZTkyMzI3ZmVhMWNlYzFhMzIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4xMTAzNDcsIDU1LjIyMDYyODI5OTk5OTk5XSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJiIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogImIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDUsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwXzZkNGRiOWFhYmM3NDQzODc5MmFjYTAxOWUzMmVkMGRiID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF8xNWU0MzM2OWZjZGE0YjBjOGJkNDI0YjIzZmJhOWRkNiA9ICQoYDxkaXYgaWQ9Imh0bWxfMTVlNDMzNjlmY2RhNGIwYzhiZDQyNGIyM2ZiYTlkZDYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiAzMC4gZmlzaCBodXQgYXNtYWsgYWwgc3VsdGFuIHNlYWZvb2QgcmVzdGF1cmFudDxicj5UZWxlcGhvbmU6ICs5NzEgNTggMTI4IDI4ODY8YnI+dXJsOiBodHRwOi8vZHViYWlmaXNoaHV0cmVzdGF1cmFudC5jb20vaW5kZXgucGhwPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwXzZkNGRiOWFhYmM3NDQzODc5MmFjYTAxOWUzMmVkMGRiLnNldENvbnRlbnQoaHRtbF8xNWU0MzM2OWZjZGE0YjBjOGJkNDI0YjIzZmJhOWRkNik7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfNGE3YzljOGNmYzFjNGQ4ZTkyMzI3ZmVhMWNlYzFhMzIuYmluZFBvcHVwKHBvcHVwXzZkNGRiOWFhYmM3NDQzODc5MmFjYTAxOWUzMmVkMGRiKQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl80NmIxZmNiYmZiYTc0MzViODBiMTBlYTUzOWRlZmJiOSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjIwODI3MywgNTUuMjYwNjAxNV0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiYiIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJiIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiA1LCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF9kY2MxYjQ1ZDU5ZmM0ZjI1YWU2NjAxMGNiNDI2OTliNyA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfZTAyMTg5ZTBkMzYxNDI4ZTgwZjk3YmM2ZTEzMGYxZjMgPSAkKGA8ZGl2IGlkPSJodG1sX2UwMjE4OWUwZDM2MTQyOGU4MGY5N2JjNmUxMzBmMWYzIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogU3BvbnNvcmVkY2hpdmFsPGJyPlRlbGVwaG9uZTogKzk3MSA0IDQwMyAzMTExPGJyPnVybDogaHR0cDovL3d3dy5jaGl2YWxsYXZpbGxlLmNvbS88L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfZGNjMWI0NWQ1OWZjNGYyNWFlNjYwMTBjYjQyNjk5Yjcuc2V0Q29udGVudChodG1sX2UwMjE4OWUwZDM2MTQyOGU4MGY5N2JjNmUxMzBmMWYzKTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl80NmIxZmNiYmZiYTc0MzViODBiMTBlYTUzOWRlZmJiOS5iaW5kUG9wdXAocG9wdXBfZGNjMWI0NWQ1OWZjNGYyNWFlNjYwMTBjYjQyNjk5YjcpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzU5YzMwMTk2ZDc2NjRmNGZhNWJjMGMzYzJkYTM4NGU3ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMTMzODc3NywgNTUuMTg0NzYyNV0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiciIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJyIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiA1LCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF9lYjg5MjMyMjM3ZmI0MWYyYjZmMTlhOWRjY2VkYTk0MyA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfYzgxM2U5MDljOWY4NDM1MzliZDM4MDAxYWVhZTYyOGEgPSAkKGA8ZGl2IGlkPSJodG1sX2M4MTNlOTA5YzlmODQzNTM5YmQzODAwMWFlYWU2MjhhIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogU3BvbnNvcmVkZm9sbHkgYnkgbmljayAmIHNjb3R0PGJyPlRlbGVwaG9uZTogKzk3MSA0IDQzMCA4NTM1PGJyPnVybDogaHR0cDovL2ZvbGx5LmFlLzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF9lYjg5MjMyMjM3ZmI0MWYyYjZmMTlhOWRjY2VkYTk0My5zZXRDb250ZW50KGh0bWxfYzgxM2U5MDljOWY4NDM1MzliZDM4MDAxYWVhZTYyOGEpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyXzU5YzMwMTk2ZDc2NjRmNGZhNWJjMGMzYzJkYTM4NGU3LmJpbmRQb3B1cChwb3B1cF9lYjg5MjMyMjM3ZmI0MWYyYjZmMTlhOWRjY2VkYTk0MykKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNmY1YzA5ZGFhOTc0NDRmZmJjNjZjMjZiMzRkZTY2ZTggPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4wODA2MzYsIDU1LjEzNTUzMThdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogInIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiciIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogNSwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfMjcwMmJhNzRjOTgxNGQ5YWJjZDliYzdmZDAzZDA0ZGUgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sX2JjNTdlODY1Zjc0MTRiZWQ5NWE4ZGJlNTc3MGExMzJjID0gJChgPGRpdiBpZD0iaHRtbF9iYzU3ZTg2NWY3NDE0YmVkOTVhOGRiZTU3NzBhMTMyYyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDEuIGFzaWwgcmVzdGF1cmFudDxicj5UZWxlcGhvbmU6ICs5NzEgNTIgMTYwIDAzMzM8YnI+dXJsOiBodHRwOi8vd3d3LmFzaWxyZXN0YXVyYW50LmNvbS88L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfMjcwMmJhNzRjOTgxNGQ5YWJjZDliYzdmZDAzZDA0ZGUuc2V0Q29udGVudChodG1sX2JjNTdlODY1Zjc0MTRiZWQ5NWE4ZGJlNTc3MGExMzJjKTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl82ZjVjMDlkYWE5NzQ0NGZmYmM2NmMyNmIzNGRlNjZlOC5iaW5kUG9wdXAocG9wdXBfMjcwMmJhNzRjOTgxNGQ5YWJjZDliYzdmZDAzZDA0ZGUpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzA0NGNlYjE3YmMxNjQwMTk5ZTg2NGQyMTAyMTYzMjBhID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMjMxNDk4MiwgNTUuMzQ2OTU1OV0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiciIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJyIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiA1LCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF82YjI1ZTY2MDgwNGU0OTcyOTEwODQ5YjE3M2IwZDNkZiA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfM2QzZmQ1ODg2ZDIxNDdkZDk2YzllMzRmY2QyOWIwMzkgPSAkKGA8ZGl2IGlkPSJodG1sXzNkM2ZkNTg4NmQyMTQ3ZGQ5NmM5ZTM0ZmNkMjliMDM5IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogMi4gbWV6emFsdW5hPGJyPlRlbGVwaG9uZTogKzk3MSA0IDcwMSAxMTI4PGJyPnVybDogaHR0cDovL3d3dy5kaW5pbmdkZmMuY29tL1Jlc3RhdXJhbnQtZGV0YWlscy8yNC9NZXp6YUx1bmE8L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfNmIyNWU2NjA4MDRlNDk3MjkxMDg0OWIxNzNiMGQzZGYuc2V0Q29udGVudChodG1sXzNkM2ZkNTg4NmQyMTQ3ZGQ5NmM5ZTM0ZmNkMjliMDM5KTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl8wNDRjZWIxN2JjMTY0MDE5OWU4NjRkMjEwMjE2MzIwYS5iaW5kUG9wdXAocG9wdXBfNmIyNWU2NjA4MDRlNDk3MjkxMDg0OWIxNzNiMGQzZGYpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzIyYTBlYWNjMWYzYjRmOTQ4ZmY5NmQ0NTAwNmFjNzUyID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMjUzMTc0NSwgNTUuMzY1NjcyOF0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiciIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJyIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiA1LCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF80YmQ4ZDIxMTg2ZDE0NGZhOTVkODU0NmI2ZGFhODg0OCA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfNjA0YjU5ZWM1Yzk0NDhkODgxZTM5YmE3ZGViZDgzNzcgPSAkKGA8ZGl2IGlkPSJodG1sXzYwNGI1OWVjNWM5NDQ4ZDg4MWUzOWJhN2RlYmQ4Mzc3IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogMy4gY2FkaXogLSBhaGxhbiBsb3VuZ2UgQCBnYXRlIGIyNjxicj5UZWxlcGhvbmU6ICs5NzEgNCA1MDUgMjAwMDxicj51cmw6IGh0dHA6Ly93d3cuZHViYWlpbnRsaG90ZWxzLmNvbS9kaW5pbmcvYWhsYW4tbG91bmdlLWI8L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfNGJkOGQyMTE4NmQxNDRmYTk1ZDg1NDZiNmRhYTg4NDguc2V0Q29udGVudChodG1sXzYwNGI1OWVjNWM5NDQ4ZDg4MWUzOWJhN2RlYmQ4Mzc3KTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl8yMmEwZWFjYzFmM2I0Zjk0OGZmOTZkNDUwMDZhYzc1Mi5iaW5kUG9wdXAocG9wdXBfNGJkOGQyMTE4NmQxNDRmYTk1ZDg1NDZiNmRhYTg4NDgpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2ZmYWJjMTI4ZGM2NDQzMDc4NWE3M2I2NDVjMjZjMTljID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMTA0MzI5NiwgNTUuMTQ4NzY5MV0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiciIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJyIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiA1LCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF84OWVlMjk0MjJjYjY0Mjc0OWRmMzIxYmJlM2IzMTY0YiA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfNzc2NjFmMjA3NDc5NGE4YjhhMDUxNDlhYjI1OGUzMzYgPSAkKGA8ZGl2IGlkPSJodG1sXzc3NjYxZjIwNzQ3OTRhOGI4YTA1MTQ5YWIyNThlMzM2IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogNC4gYmx2ZCBvbiBvbmU8YnI+VGVsZXBob25lOiArOTcxIDQgNDU1IDk5ODk8YnI+dXJsOiBodHRwOi8vZml2ZWhvdGVsc2FuZHJlc29ydHMuY29tL2RpbmUtZHJpbmstZGFuY2UvcmVzdGF1cmFudHMvYmx2ZC1vbi1vbmUvPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwXzg5ZWUyOTQyMmNiNjQyNzQ5ZGYzMjFiYmUzYjMxNjRiLnNldENvbnRlbnQoaHRtbF83NzY2MWYyMDc0Nzk0YThiOGEwNTE0OWFiMjU4ZTMzNik7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfZmZhYmMxMjhkYzY0NDMwNzg1YTczYjY0NWMyNmMxOWMuYmluZFBvcHVwKHBvcHVwXzg5ZWUyOTQyMmNiNjQyNzQ5ZGYzMjFiYmUzYjMxNjRiKQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8wZmRhMTU1MjVhM2Q0Zjk4ODRmZTc3NTA5NTIwZDk4MiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjI0ODE0NjIsIDU1LjI4NjY1MjVdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogInIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiciIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogNSwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfNGNjMmE4NGY1YjQwNGVjMDhhNzU5NTAzZTcxNDVkZDQgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sX2I3ODgwY2JkNDI0ZDRlN2I4MzdjM2UzYWI2NzQ0NjE4ID0gJChgPGRpdiBpZD0iaHRtbF9iNzg4MGNiZDQyNGQ0ZTdiODM3YzNlM2FiNjc0NDYxOCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDUuIHB1cmFuaSBkaWxsaSBkdWJhaTxicj5UZWxlcGhvbmU6ICs5NzEgNTAgMjExIDY4MTY8YnI+dXJsOiBodHRwOi8vd3d3LnB1cmFuaWRpbGxpZHViYWkuY29tLzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF80Y2MyYTg0ZjViNDA0ZWMwOGE3NTk1MDNlNzE0NWRkNC5zZXRDb250ZW50KGh0bWxfYjc4ODBjYmQ0MjRkNGU3YjgzN2MzZTNhYjY3NDQ2MTgpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyXzBmZGExNTUyNWEzZDRmOTg4NGZlNzc1MDk1MjBkOTgyLmJpbmRQb3B1cChwb3B1cF80Y2MyYTg0ZjViNDA0ZWMwOGE3NTk1MDNlNzE0NWRkNCkKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMTk5OTRkNGI1OTkyNGRiY2JlNDAzZDdlYjYzNzY5OGUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4yMDgyNzMsIDU1LjI2MDYwMTVdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogInIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiciIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogNSwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfNmQ2YTQ1MDg1MmMwNDg2Njg2NDkyM2IyMDY5NDVkYWIgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzZiMDY1NDEyODJmMzRiMjdhMzYyZWFkMzM3NTk5NTIyID0gJChgPGRpdiBpZD0iaHRtbF82YjA2NTQxMjgyZjM0YjI3YTM2MmVhZDMzNzU5OTUyMiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IFNwb25zb3JlZGdyYXBlc2tpbiBncmFwZSBiYXIgYW5kIGtpdGNoZW48YnI+VGVsZXBob25lOiArOTcxIDQgNDAzIDMxMTE8YnI+dXJsOiBodHRwOi8vd3d3LmxpdmVsYXZpbGxlLmNvbS9kaW5pbmcvR3JhcGVza2luL2luZGV4LmFzcHg8L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfNmQ2YTQ1MDg1MmMwNDg2Njg2NDkyM2IyMDY5NDVkYWIuc2V0Q29udGVudChodG1sXzZiMDY1NDEyODJmMzRiMjdhMzYyZWFkMzM3NTk5NTIyKTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl8xOTk5NGQ0YjU5OTI0ZGJjYmU0MDNkN2ViNjM3Njk4ZS5iaW5kUG9wdXAocG9wdXBfNmQ2YTQ1MDg1MmMwNDg2Njg2NDkyM2IyMDY5NDVkYWIpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzAxMTgzNDM1YWQxNTQyZjZiMWM0Y2Y2M2U0OWI4ZmU1ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMTA0MzI5NiwgNTUuMTQ4NzY5MV0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiciIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJyIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiA1LCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF9kYzMxOTcxMmE2Mzc0ZjY1YjllZGE2OTA1ZTQzOTMxYSA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfNDkwZWQzNGY0OGFlNDE0NmJhMjU5ODEyNzI0MjkyZWIgPSAkKGA8ZGl2IGlkPSJodG1sXzQ5MGVkMzRmNDhhZTQxNDZiYTI1OTgxMjcyNDI5MmViIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogNi4gdHJhdHRvcmlhIGJ5IGNpbnF1ZTxicj5UZWxlcGhvbmU6ICs5NzEgNCA0NTUgOTk4OTxicj51cmw6IGh0dHA6Ly9qdW1laXJhaHZpbGxhZ2UuZml2ZWhvdGVsc2FuZHJlc29ydHMuY29tL21lZXQtbWluZ2xlL3RyYXR0b3JpYS1ieS1jaW5xdWU8L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfZGMzMTk3MTJhNjM3NGY2NWI5ZWRhNjkwNWU0MzkzMWEuc2V0Q29udGVudChodG1sXzQ5MGVkMzRmNDhhZTQxNDZiYTI1OTgxMjcyNDI5MmViKTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl8wMTE4MzQzNWFkMTU0MmY2YjFjNGNmNjNlNDliOGZlNS5iaW5kUG9wdXAocG9wdXBfZGMzMTk3MTJhNjM3NGY2NWI5ZWRhNjkwNWU0MzkzMWEpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2RjZTIyNTE5NzMyOTRlYjA5YmM1Y2FlMzQ5YTVkMjRhID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMjU2ODc1NywgNTUuMzEyMDgxMV0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiciIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJyIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiA1LCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF9lZTU1YTBkNGRiMGU0M2U0YTQwOTgwNGIyZjkxYTkwYyA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfMzNhNDg5NTJmMWM5NDgyYWI4OTZhZWUyNDc4NzY2M2UgPSAkKGA8ZGl2IGlkPSJodG1sXzMzYTQ4OTUyZjFjOTQ4MmFiODk2YWVlMjQ3ODc2NjNlIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogNy4gZG9vcnMgZnJlZXN0eWxlIGdyaWxsPGJyPlRlbGVwaG9uZTogKzk3MSA0IDIwNCA5Mjk5PGJyPnVybDogaHR0cDovL3d3dy5kb29yc2R1YmFpLmNvbS9lbjwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF9lZTU1YTBkNGRiMGU0M2U0YTQwOTgwNGIyZjkxYTkwYy5zZXRDb250ZW50KGh0bWxfMzNhNDg5NTJmMWM5NDgyYWI4OTZhZWUyNDc4NzY2M2UpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyX2RjZTIyNTE5NzMyOTRlYjA5YmM1Y2FlMzQ5YTVkMjRhLmJpbmRQb3B1cChwb3B1cF9lZTU1YTBkNGRiMGU0M2U0YTQwOTgwNGIyZjkxYTkwYykKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNGE1MTBkNjUzODM5NDJiYTlmNzcxNDU1ZjdmYWM0NDAgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4wNjU3OTM0LCA1NS4xMzgxMTU5XSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJyIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogInIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDUsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwX2U2Y2ZjMjE4MDFjODQxNTlhMTc3NTFlNmEzMDZmMjFiID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF8wN2UxNjVmZmI2MGE0MzcyYWMwYTI4MGI4YzlmNzYzOCA9ICQoYDxkaXYgaWQ9Imh0bWxfMDdlMTY1ZmZiNjBhNDM3MmFjMGEyODBiOGM5Zjc2MzgiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiA4LiB1cmJhbiBiYXIgJiBraXRjaGVuIC0gdWJrPGJyPlRlbGVwaG9uZTogKzk3MSA0IDQzOCAwMDAwPGJyPnVybDogaHR0cDovL3d3dy5tb3ZlbnBpY2suY29tL2VuL21pZGRsZS1lYXN0L3VhZS9kdWJhaS9kdWJhaS1qdW1laXJhaC1sYWtlcy10b3dlcnMvcmVzdGF1cmFudHMvcmVzdGF1cmFudHMvdXJiYW4tYmFyLWtpdGNoZW4tdWJrPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwX2U2Y2ZjMjE4MDFjODQxNTlhMTc3NTFlNmEzMDZmMjFiLnNldENvbnRlbnQoaHRtbF8wN2UxNjVmZmI2MGE0MzcyYWMwYTI4MGI4YzlmNzYzOCk7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfNGE1MTBkNjUzODM5NDJiYTlmNzcxNDU1ZjdmYWM0NDAuYmluZFBvcHVwKHBvcHVwX2U2Y2ZjMjE4MDFjODQxNTlhMTc3NTFlNmEzMDZmMjFiKQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8yMzVhMDIzYTkxYTg0MGVkOWE3ZWJkOTc1NDhmNjYyOSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjIzMzg0NDEsIDU1LjI2NTQ4MTJdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogInIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiciIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogNSwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfMjk5NTUyNDFhOTQzNGRiZmIyYzMwMGRmMGJhZjIwMzggPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sX2YzMzI0N2EyNGRlYzQ0NjViMzM5NTY5NDYyYzU0MDJjID0gJChgPGRpdiBpZD0iaHRtbF9mMzMyNDdhMjRkZWM0NDY1YjMzOTU2OTQ2MmM1NDAyYyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDkuIGJhcmVmb290IGxvdW5nZTxicj5UZWxlcGhvbmU6ICs5NzEgNCAzNDYgMTExMTxicj51cmw6IGh0dHA6Ly93d3cuZHhibWFyaW5lLmNvbS88L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfMjk5NTUyNDFhOTQzNGRiZmIyYzMwMGRmMGJhZjIwMzguc2V0Q29udGVudChodG1sX2YzMzI0N2EyNGRlYzQ0NjViMzM5NTY5NDYyYzU0MDJjKTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl8yMzVhMDIzYTkxYTg0MGVkOWE3ZWJkOTc1NDhmNjYyOS5iaW5kUG9wdXAocG9wdXBfMjk5NTUyNDFhOTQzNGRiZmIyYzMwMGRmMGJhZjIwMzgpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2JlNTNlYTE3ZDcwMjQ5MzhhNTcxN2Y0OGVmMDk2OTk5ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMjEyNjQyNiwgNTUuMjgyNDA1XSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJyIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogInIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDUsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwX2Q4YzIwY2M5YjIyODRlMWY5ZjBkMzAzNTI1NWJhNWQzID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF9hYmQ2NTY1MmYwODc0ZGNhODZmZDk4YmJmYmVjOWY0ZiA9ICQoYDxkaXYgaWQ9Imh0bWxfYWJkNjU2NTJmMDg3NGRjYTg2ZmQ5OGJiZmJlYzlmNGYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiAxMC4gbWluYSBicmFzc2VyaWU8YnI+VGVsZXBob25lOiArOTcxIDQgNTA2IDAxMDA8YnI+dXJsOiBodHRwOi8vd3d3Lm1pbmFicmFzc2VyaWUuY29tLzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF9kOGMyMGNjOWIyMjg0ZTFmOWYwZDMwMzUyNTViYTVkMy5zZXRDb250ZW50KGh0bWxfYWJkNjU2NTJmMDg3NGRjYTg2ZmQ5OGJiZmJlYzlmNGYpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyX2JlNTNlYTE3ZDcwMjQ5MzhhNTcxN2Y0OGVmMDk2OTk5LmJpbmRQb3B1cChwb3B1cF9kOGMyMGNjOWIyMjg0ZTFmOWYwZDMwMzUyNTViYTVkMykKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNjkyMjM0MTJlMmM2NGUyN2I3NDg2Nzk3NTlmNzc5NDAgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4yMDgyNzMsIDU1LjI2MDYwMTVdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogInIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiciIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogNSwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfMTJiMWUwMDdiZjU5NDM2NzllNTM0NjM4YTAzNmNiN2YgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sX2I0MDcyMTgyMzMyNDRjMmY5Y2VlNmUyZWMyOTNlMDg5ID0gJChgPGRpdiBpZD0iaHRtbF9iNDA3MjE4MjMzMjQ0YzJmOWNlZTZlMmVjMjkzZTA4OSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IFNwb25zb3JlZGdyYXplIGdhc3RybyBncmlsbDxicj5UZWxlcGhvbmU6ICs5NzEgNCA0MDMgMzExMTxicj51cmw6IGh0dHA6Ly93d3cubGl2ZWxhdmlsbGUuY29tL2RpbmluZy9HcmF6ZS9pbmRleC5odG1sPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwXzEyYjFlMDA3YmY1OTQzNjc5ZTUzNDYzOGEwMzZjYjdmLnNldENvbnRlbnQoaHRtbF9iNDA3MjE4MjMzMjQ0YzJmOWNlZTZlMmVjMjkzZTA4OSk7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfNjkyMjM0MTJlMmM2NGUyN2I3NDg2Nzk3NTlmNzc5NDAuYmluZFBvcHVwKHBvcHVwXzEyYjFlMDA3YmY1OTQzNjc5ZTUzNDYzOGEwMzZjYjdmKQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl82MmNiNTA3YWE4YTY0MzgzODZkNDhmZWEyZTkwYzc4NiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI0LjgxNjgyMDYsIDU1LjIzMTI4NzJdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogInIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiciIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogNSwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfNmRiYWUyYTkxMDQ4NGJmYTgwYzdmYmQ3OGYwMDg4ZGYgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sX2ZiODhhOGRmZmRmYTRjZTg5Nzc4YzJmYzE1OTVhNGM5ID0gJChgPGRpdiBpZD0iaHRtbF9mYjg4YThkZmZkZmE0Y2U4OTc3OGMyZmMxNTk1YTRjOSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDExLiBhbCBzYXJhYiByb29mdG9wIGxvdW5nZTxicj5UZWxlcGhvbmU6ICs5NzEgNCA4MDkgNjEwMDxicj51cmw6IGh0dHA6Ly93d3cubWV5ZGFuaG90ZWxzLmNvbS9iYWJhbHNoYW1zL2RpbmluZy5odG08L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfNmRiYWUyYTkxMDQ4NGJmYTgwYzdmYmQ3OGYwMDg4ZGYuc2V0Q29udGVudChodG1sX2ZiODhhOGRmZmRmYTRjZTg5Nzc4YzJmYzE1OTVhNGM5KTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl82MmNiNTA3YWE4YTY0MzgzODZkNDhmZWEyZTkwYzc4Ni5iaW5kUG9wdXAocG9wdXBfNmRiYWUyYTkxMDQ4NGJmYTgwYzdmYmQ3OGYwMDg4ZGYpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2U2OWE5NmM5MDAzNjRhODc4NDI3Njc4OTk2ZTNiMzJkID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMDQ2Mjk0NiwgNTUuMjAzMDQxMTk5OTk5OTldLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogInIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiciIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogNSwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfZDIyYWI1NjI0YjBjNDE0NWFhODA4ZWVkYTg3NGFiZjQgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzUwMWM4YzEyZDViMDQ1NmViYjc0YWQ2NmMyNzEyZDk4ID0gJChgPGRpdiBpZD0iaHRtbF81MDFjOGMxMmQ1YjA0NTZlYmI3NGFkNjZjMjcxMmQ5OCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDEyLiBzb3VsIHN0cmVldDxicj5UZWxlcGhvbmU6ICs5NzEgNCA0NTUgOTk4OTxicj51cmw6IGh0dHA6Ly9zb3VsLnN0LzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF9kMjJhYjU2MjRiMGM0MTQ1YWE4MDhlZWRhODc0YWJmNC5zZXRDb250ZW50KGh0bWxfNTAxYzhjMTJkNWIwNDU2ZWJiNzRhZDY2YzI3MTJkOTgpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyX2U2OWE5NmM5MDAzNjRhODc4NDI3Njc4OTk2ZTNiMzJkLmJpbmRQb3B1cChwb3B1cF9kMjJhYjU2MjRiMGM0MTQ1YWE4MDhlZWRhODc0YWJmNCkKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNzhjY2NjM2Q2MDI4NGRhZjhmMjA3NWFlOGU5ZGMxNDIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4yNDkxNTQ5LCA1NS4zNDcxMzk2MDAwMDAwMV0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiciIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJyIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiA1LCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF9kNmMwZjk0MDI5MWI0YTE4OWU3OTlmOGU0NmY5N2JiNiA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfZmM0NDVjM2RiZjg4NDcyNGJkNDg5ODY1OTQwZmYzMTAgPSAkKGA8ZGl2IGlkPSJodG1sX2ZjNDQ1YzNkYmY4ODQ3MjRiZDQ4OTg2NTk0MGZmMzEwIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogMTMuIGJlYmVtb3M8YnI+VGVsZXBob25lOiArOTcxIDQgNzAyIDI0NTU8YnI+dXJsOiBodHRwOi8vd3d3LmJlYmVtb3NkdWJhaS5jb20vPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwX2Q2YzBmOTQwMjkxYjRhMTg5ZTc5OWY4ZTQ2Zjk3YmI2LnNldENvbnRlbnQoaHRtbF9mYzQ0NWMzZGJmODg0NzI0YmQ0ODk4NjU5NDBmZjMxMCk7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfNzhjY2NjM2Q2MDI4NGRhZjhmMjA3NWFlOGU5ZGMxNDIuYmluZFBvcHVwKHBvcHVwX2Q2YzBmOTQwMjkxYjRhMTg5ZTc5OWY4ZTQ2Zjk3YmI2KQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl84MjkyZWU2NGYxNTY0ZmJkYTljNmRhNzhjYjVjN2M1NyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjIyODgzOTQsIDU1LjMyNjgxMjVdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogInIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiciIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogNSwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfNjcwYjRlOWI0MzY3NGMyMjg1M2NhZDRmNDVhNWE0YzQgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sX2MxNTZjZTBjNDVlZDQ3N2ViY2E3MDdmZjRiNzU2MjcwID0gJChgPGRpdiBpZD0iaHRtbF9jMTU2Y2UwYzQ1ZWQ0NzdlYmNhNzA3ZmY0Yjc1NjI3MCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDE0LiBhd3Rhcjxicj5UZWxlcGhvbmU6ICs5NzEgNCAzMTcgMjIyMTxicj51cmw6IGh0dHBzOi8vd3d3Lmh5YXR0cmVzdGF1cmFudHMuY29tL2VuL2RpbmluZy91YWUvZHViYWkvbWlkZGxlLWVhc3Rlcm4tcmVzdGF1cmFudC1pbi1nYXJob3VkLWF3dGFyP3V0bV9zb3VyY2U9Z21ibGlzdGluZ19keGJnaCZ1dG1fbWVkaXVtPWF3dGFyJnV0bV9jYW1wYWlnbj1HTUI8L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfNjcwYjRlOWI0MzY3NGMyMjg1M2NhZDRmNDVhNWE0YzQuc2V0Q29udGVudChodG1sX2MxNTZjZTBjNDVlZDQ3N2ViY2E3MDdmZjRiNzU2MjcwKTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl84MjkyZWU2NGYxNTY0ZmJkYTljNmRhNzhjYjVjN2M1Ny5iaW5kUG9wdXAocG9wdXBfNjcwYjRlOWI0MzY3NGMyMjg1M2NhZDRmNDVhNWE0YzQpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2Y1MTg1YThiODk5MzQyMmNiNDc2OTAxMGFiODlkMWFmID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMTk4NzY1LCA1NS4yNzk2MDUzXSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJyIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogInIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDUsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwXzVmOTdjMjBmMzU3YjQ4YjZiYWIwMzJhMjdhYjAzNWIwID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF8xNWQ5OGYwNjQwMTY0ZjRmYTE2NWFiYzNiYTg2ODg1NCA9ICQoYDxkaXYgaWQ9Imh0bWxfMTVkOThmMDY0MDE2NGY0ZmExNjVhYmMzYmE4Njg4NTQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiAxNS4gdHJpYmVzIGNhcm5pdm9yZTxicj5UZWxlcGhvbmU6ICs5NzEgNCAyMjYgNDk3NDxicj51cmw6IGh0dHA6Ly90cmliZXNyZXN0YXVyYW50LmNvbS88L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfNWY5N2MyMGYzNTdiNDhiNmJhYjAzMmEyN2FiMDM1YjAuc2V0Q29udGVudChodG1sXzE1ZDk4ZjA2NDAxNjRmNGZhMTY1YWJjM2JhODY4ODU0KTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl9mNTE4NWE4Yjg5OTM0MjJjYjQ3NjkwMTBhYjg5ZDFhZi5iaW5kUG9wdXAocG9wdXBfNWY5N2MyMGYzNTdiNDhiNmJhYjAzMmEyN2FiMDM1YjApCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzQ4MWUwYWM0YTVmOTQ4MDA4OTE3NGI2MTJmNjNhNmM1ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMjIxNjAzLCA1NS4yODA4MjYyXSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJyIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogInIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDUsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwXzgzNjg0MWQzMDBiMDQzN2ZhNDkyZmY3Njg4ODgzOGIxID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF8zOTlmYmVlNTAxMjk0NTMxOTMyM2NkNTc5MDk5NTg3MyA9ICQoYDxkaXYgaWQ9Imh0bWxfMzk5ZmJlZTUwMTI5NDUzMTkzMjNjZDU3OTA5OTU4NzMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiBTcG9uc29yZWRzdXNoaSBuYXRpb25zPGJyPlRlbGVwaG9uZTogKzk3MSA1NiAxODggODUyMjxicj51cmw6IGh0dHBzOi8vc3VzaGluYXRpb25zLmFlLzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF84MzY4NDFkMzAwYjA0MzdmYTQ5MmZmNzY4ODg4MzhiMS5zZXRDb250ZW50KGh0bWxfMzk5ZmJlZTUwMTI5NDUzMTkzMjNjZDU3OTA5OTU4NzMpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyXzQ4MWUwYWM0YTVmOTQ4MDA4OTE3NGI2MTJmNjNhNmM1LmJpbmRQb3B1cChwb3B1cF84MzY4NDFkMzAwYjA0MzdmYTQ5MmZmNzY4ODg4MzhiMSkKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNGQxMDQ1NTg2ZDgxNDhhYmE4MTE3NzllMTFiNjllMWUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4yNzg4OTgsIDU1LjMwNDQ2MDddLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogInIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiciIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogNSwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfNjEzNTJiNTI0ZDEyNDBmNDk5ZDViY2Y2ZGJhN2U4NmIgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzNiNTFmZDdiY2NhOTRiYmRiNGFiYmY1ZGU3YWEzODdmID0gJChgPGRpdiBpZD0iaHRtbF8zYjUxZmQ3YmNjYTk0YmJkYjRhYmJmNWRlN2FhMzg3ZiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDE2LiBhbCBkYXdhYXIgcmV2b2x2aW5nIHJlc3RhdXJhbnQ8YnI+VGVsZXBob25lOiArOTcxIDQgMjA5IDY5MTI8YnI+dXJsOiBodHRwOi8vd3d3Lmh5YXR0cmVzdGF1cmFudHMuY29tL2VuL2RpbmluZy91YWUvZHViYWkvaW50ZXJuYXRpb25hbC1yZXN0YXVyYW50LWluLWRlaXJhLWNvcm5pY2hlLWFsLWRhd2Fhci1yZXZvbHZpbmctcmVzdGF1cmFudDwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF82MTM1MmI1MjRkMTI0MGY0OTlkNWJjZjZkYmE3ZTg2Yi5zZXRDb250ZW50KGh0bWxfM2I1MWZkN2JjY2E5NGJiZGI0YWJiZjVkZTdhYTM4N2YpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyXzRkMTA0NTU4NmQ4MTQ4YWJhODExNzc5ZTExYjY5ZTFlLmJpbmRQb3B1cChwb3B1cF82MTM1MmI1MjRkMTI0MGY0OTlkNWJjZjZkYmE3ZTg2YikKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYWYzZTY5MTkwYTQwNGYwZDg4ZmZkNTBkNTYyODI0MDkgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4xMTEzOTkxLCA1NS4xMzcyMTU4XSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJyIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogInIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDUsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwXzBhYjk0OTRkZDBkZTRjODBhYTA5MTRjMmVkNTg3MTBhID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF8xZDgxMjA1MzI4NmE0NTA1ODk1ODZkYjc2Y2Y0MWJjMSA9ICQoYDxkaXYgaWQ9Imh0bWxfMWQ4MTIwNTMyODZhNDUwNTg5NTg2ZGI3NmNmNDFiYzEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiAxNy4ga2h5YmVyPGJyPlRlbGVwaG9uZTogKzk3MSA0IDQ1NSAxMTExPGJyPnVybDogaHR0cHM6Ly93d3cuZHVrZXNkdWJhaS5jb20va2h5YmVyLzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF8wYWI5NDk0ZGQwZGU0YzgwYWEwOTE0YzJlZDU4NzEwYS5zZXRDb250ZW50KGh0bWxfMWQ4MTIwNTMyODZhNDUwNTg5NTg2ZGI3NmNmNDFiYzEpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyX2FmM2U2OTE5MGE0MDRmMGQ4OGZmZDUwZDU2MjgyNDA5LmJpbmRQb3B1cChwb3B1cF8wYWI5NDk0ZGQwZGU0YzgwYWEwOTE0YzJlZDU4NzEwYSkKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMzFiM2NlYzNlNzYwNDc2OTkzYmZhZmJhNDJmZTJhYWMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4yNjYyNjc4LCA1NS4zMDg3ODc0OTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiciIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJyIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiA1LCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF83ZTIyYTE0MTA2MjQ0OWI3OWRmOTYwOWI0YjE2YjA5NSA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfY2MzYmY1ZmViMTE3NGRlMTk0ODJhY2EzMzNlMjkzMDEgPSAkKGA8ZGl2IGlkPSJodG1sX2NjM2JmNWZlYjExNzRkZTE5NDgyYWNhMzMzZTI5MzAxIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogMTguIGRhbmlhbCByZXN0YXVyYW50PGJyPlRlbGVwaG9uZTogKzk3MSA0IDIyNyA3NjY5PGJyPnVybDogaHR0cDovL3d3dy5kYW5pYWxyZXN0YXVyYW50LmNvbS88L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfN2UyMmExNDEwNjI0NDliNzlkZjk2MDliNGIxNmIwOTUuc2V0Q29udGVudChodG1sX2NjM2JmNWZlYjExNzRkZTE5NDgyYWNhMzMzZTI5MzAxKTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl8zMWIzY2VjM2U3NjA0NzY5OTNiZmFmYmE0MmZlMmFhYy5iaW5kUG9wdXAocG9wdXBfN2UyMmExNDEwNjI0NDliNzlkZjk2MDliNGIxNmIwOTUpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2IyZmNhZWM4ZmIyZDRmYmU5NzM3MmQxMGQ2ODlkZDlmID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMjM0MzU1LCA1NS4zMjQwMTQ3XSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJyIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogInIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDUsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwXzg1NWIxYmJhNmE4ODQ0OGY5MjI2ZWRlNWIyNmMyNDQ4ID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF9mMWFmOTRlMGUzYWY0Nzk1ODYzMGVmOTk0MmEzYTJkOSA9ICQoYDxkaXYgaWQ9Imh0bWxfZjFhZjk0ZTBlM2FmNDc5NTg2MzBlZjk5NDJhM2EyZDkiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiAxOS4gZXZlIHBlbnRob3VzZSAmIGxvdW5nZTxicj5UZWxlcGhvbmU6ICs5NzEgNCA1NTMgMTIxNDxicj51cmw6IGh0dHA6Ly93d3cuaHlhdHRyZXN0YXVyYW50cy5jb20vZW4vZGluaW5nL3VhZS9kdWJhaS9pbnRlcm5hdGlvbmFsLXJlc3RhdXJhbnQtaW4tb3VkLW1ldGhhLXJvYWQtZXZlLXBlbnRob3VzZS1sb3VuZ2U/dXRtX3NvdXJjZT1XZWJzaXRlX2R4YmhjJnV0bV9tZWRpdW09ZXZlJnV0bV9jYW1wYWlnbj1IeWF0dDwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF84NTViMWJiYTZhODg0NDhmOTIyNmVkZTViMjZjMjQ0OC5zZXRDb250ZW50KGh0bWxfZjFhZjk0ZTBlM2FmNDc5NTg2MzBlZjk5NDJhM2EyZDkpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyX2IyZmNhZWM4ZmIyZDRmYmU5NzM3MmQxMGQ2ODlkZDlmLmJpbmRQb3B1cChwb3B1cF84NTViMWJiYTZhODg0NDhmOTIyNmVkZTViMjZjMjQ0OCkKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYTYyNWRlNzRmZjc5NDA5Yzg5YTViMDg0MWU0Y2U0YmQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4xOTg3NjUsIDU1LjI3OTYwNTNdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogInIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiciIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogNSwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfODI2NjMwYTNhNGRkNDczZWJhYmRhN2I2YzFiY2U3NTMgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzRhMTYwYTM0NDUwYzQyZjdhZGEzYTRmMWZiNWQyMWRlID0gJChgPGRpdiBpZD0iaHRtbF80YTE2MGEzNDQ1MGM0MmY3YWRhM2E0ZjFmYjVkMjFkZSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDIwLiB0aGUgZ3JpbGwgc2hhY2s8YnI+VGVsZXBob25lOiArOTcxIDQgMzg4IDIzODI8YnI+dXJsOiBodHRwOi8vd3d3LnRoZWdyaWxsbHNoYWNrLmNvbS88L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfODI2NjMwYTNhNGRkNDczZWJhYmRhN2I2YzFiY2U3NTMuc2V0Q29udGVudChodG1sXzRhMTYwYTM0NDUwYzQyZjdhZGEzYTRmMWZiNWQyMWRlKTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl9hNjI1ZGU3NGZmNzk0MDljODlhNWIwODQxZTRjZTRiZC5iaW5kUG9wdXAocG9wdXBfODI2NjMwYTNhNGRkNDczZWJhYmRhN2I2YzFiY2U3NTMpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzZjZDVmZGE4N2NhMzQwZjA4OWRiMmQxN2I2ZjYxNGIzID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMjQ3ODY3LCA1NS4zMDA0OTI1XSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJyIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogInIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDUsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwX2Y5NThjZjNhZGFiMzQ3ZjI4MGQ5MDYyZWI3ZDhjNGRjID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF9kMmQwOTk4MzkyNzY0NmEyODI3NjZkYmE3NDZlMDI4ZiA9ICQoYDxkaXYgaWQ9Imh0bWxfZDJkMDk5ODM5Mjc2NDZhMjgyNzY2ZGJhNzQ2ZTAyOGYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiBTcG9uc29yZWRhbXJpdHNyIHJlc3RhdXJhbnQ8YnI+VGVsZXBob25lOiArOTcxIDUwIDY3OCAwMDk2PGJyPnVybDogaHR0cDovL2Ftcml0c3J1YWUuY29tLzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF9mOTU4Y2YzYWRhYjM0N2YyODBkOTA2MmViN2Q4YzRkYy5zZXRDb250ZW50KGh0bWxfZDJkMDk5ODM5Mjc2NDZhMjgyNzY2ZGJhNzQ2ZTAyOGYpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyXzZjZDVmZGE4N2NhMzQwZjA4OWRiMmQxN2I2ZjYxNGIzLmJpbmRQb3B1cChwb3B1cF9mOTU4Y2YzYWRhYjM0N2YyODBkOTA2MmViN2Q4YzRkYykKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYTQ2ODk1MDkyZjc3NDhjYWI2M2U0ZmMxMDk4MWIwOWMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4xMDQzMjk2LCA1NS4xNDg3NjkxXSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJyIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogInIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDUsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwXzFiNzMwODkyYzI1OTQyMmM5MWZiNmFhNWM1ZDAxNTQzID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF83YWIzOThiMjM3Yjk0ZTA4YjkwZGRhMzZmZjQ2ZjkxMCA9ICQoYDxkaXYgaWQ9Imh0bWxfN2FiMzk4YjIzN2I5NGUwOGI5MGRkYTM2ZmY0NmY5MTAiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiAyMS4gbWFpZGVuIHNoYW5naGFpPGJyPlRlbGVwaG9uZTogKzk3MSA0IDQ1NSA5OTg5PGJyPnVybDogaHR0cDovL2ZpdmVob3RlbHNhbmRyZXNvcnRzLmNvbS9kaW5lLWRyaW5rLWRhbmNlL3Jlc3RhdXJhbnRzL21haWRlbi1zaGFuZ2hhaS88L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfMWI3MzA4OTJjMjU5NDIyYzkxZmI2YWE1YzVkMDE1NDMuc2V0Q29udGVudChodG1sXzdhYjM5OGIyMzdiOTRlMDhiOTBkZGEzNmZmNDZmOTEwKTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl9hNDY4OTUwOTJmNzc0OGNhYjYzZTRmYzEwOTgxYjA5Yy5iaW5kUG9wdXAocG9wdXBfMWI3MzA4OTJjMjU5NDIyYzkxZmI2YWE1YzVkMDE1NDMpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzEyYWM0NWY3NWE2NjQ4ZDI5YzQzYWQ2NmE4NmFiMmE3ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMjE0MDEzMywgNTUuMjc2MDg4NV0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiciIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJyIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiA1LCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF9hMWIxYTM3ZjEwYmQ0NzE0ODg1ZjVhOTkyOGE0OTVhOCA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfYWYwZGFjYTg3ZjUwNGU0Y2I1ZTk4MGNmNGRiYmM4YmMgPSAkKGA8ZGl2IGlkPSJodG1sX2FmMGRhY2E4N2Y1MDRlNGNiNWU5ODBjZjRkYmJjOGJjIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogMjIuIHB1cmFuaSBkaWxsaSBzaGVpa2ggemF5ZWQgcm9hZDxicj5UZWxlcGhvbmU6ICs5NzEgNCAzMTYgOTcyNjxicj51cmw6IGh0dHA6Ly93d3cucHVyYW5pZGlsbGlkdWJhaS5jb20vc2hlaWtoemF5ZWRyb2FkPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwX2ExYjFhMzdmMTBiZDQ3MTQ4ODVmNWE5OTI4YTQ5NWE4LnNldENvbnRlbnQoaHRtbF9hZjBkYWNhODdmNTA0ZTRjYjVlOTgwY2Y0ZGJiYzhiYyk7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfMTJhYzQ1Zjc1YTY2NDhkMjljNDNhZDY2YTg2YWIyYTcuYmluZFBvcHVwKHBvcHVwX2ExYjFhMzdmMTBiZDQ3MTQ4ODVmNWE5OTI4YTQ5NWE4KQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl83ZDg3NzFmMzJkNDg0ZWI4YTNhMjA1ZjcyNzBkZjRmNCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjIxNDAxMzMsIDU1LjI3NjA4ODVdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogInIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiciIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogNSwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfNGVlODIwODNlNTRmNDMxMjlmZDAwYjg5OGJhNDhhZDIgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sX2JiZTM5OTcyYzg4YjRkOWI4NTc4ZDM3OGExYmU4ZWVjID0gJChgPGRpdiBpZD0iaHRtbF9iYmUzOTk3MmM4OGI0ZDliODU3OGQzNzhhMWJlOGVlYyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDIzLiBsZXZlbCA0MyBza3kgbG91bmdlPGJyPlRlbGVwaG9uZTogKzk3MSA1NiA0MTQgMjIxMzxicj51cmw6IGh0dHA6Ly93d3cubGV2ZWw0M2xvdW5nZS5jb20vPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwXzRlZTgyMDgzZTU0ZjQzMTI5ZmQwMGI4OThiYTQ4YWQyLnNldENvbnRlbnQoaHRtbF9iYmUzOTk3MmM4OGI0ZDliODU3OGQzNzhhMWJlOGVlYyk7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfN2Q4NzcxZjMyZDQ4NGViOGEzYTIwNWY3MjcwZGY0ZjQuYmluZFBvcHVwKHBvcHVwXzRlZTgyMDgzZTU0ZjQzMTI5ZmQwMGI4OThiYTQ4YWQyKQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8yNTIxOGNhMzk0NTA0NmM5ODViNThkNDM2OWY3MzE4MCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjE5NTE1NTQsIDU1LjI3NTE1NzldLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogInIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiciIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogNSwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfNGYzYzg5ZTJlZGUyNDMzM2I5YzYzZmU5YmU5YTQyNDYgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzAyYzc4NWNmODA5MDQyNTU5OGFkYWEyOWNmYWNjMDNlID0gJChgPGRpdiBpZD0iaHRtbF8wMmM3ODVjZjgwOTA0MjU1OThhZGFhMjljZmFjYzAzZSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDI0LiBibGFjayB0YXAgY3JhZnQgYnVyZ2VycyAmIHNoYWtlcyBkdWJhaSBtYWxsPGJyPlRlbGVwaG9uZTogKzk3MSA0IDMzMCA1MTAzPGJyPnVybDogaHR0cDovL3d3dy5ibGFja3RhcG1lLmNvbS88L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfNGYzYzg5ZTJlZGUyNDMzM2I5YzYzZmU5YmU5YTQyNDYuc2V0Q29udGVudChodG1sXzAyYzc4NWNmODA5MDQyNTU5OGFkYWEyOWNmYWNjMDNlKTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl8yNTIxOGNhMzk0NTA0NmM5ODViNThkNDM2OWY3MzE4MC5iaW5kUG9wdXAocG9wdXBfNGYzYzg5ZTJlZGUyNDMzM2I5YzYzZmU5YmU5YTQyNDYpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzBkNjY1M2QzNDY2NTRmMzBhNGE4MjM1YWJkNzY4ZDU1ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMjQ5MTU0OSwgNTUuMzQ3MTM5NjAwMDAwMDFdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogInIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiciIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogNSwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfY2RjMjIxYWVkMzM3NDMyNzljYzdiNjIwNDM5YzFiMjEgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzkxZTA4ZGJkZjAwOTQ5MmNiN2NjYzdkMzc1OTE0ODllID0gJChgPGRpdiBpZD0iaHRtbF85MWUwOGRiZGYwMDk0OTJjYjdjY2M3ZDM3NTkxNDg5ZSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDI1LiBiZWVmIGJpc3Rybzxicj5UZWxlcGhvbmU6ICs5NzEgNCA3MDIgMjQ1NTxicj51cmw6IGh0dHA6Ly93d3cuYmVlZmJpc3Ryb2R1YmFpLmNvbS88L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfY2RjMjIxYWVkMzM3NDMyNzljYzdiNjIwNDM5YzFiMjEuc2V0Q29udGVudChodG1sXzkxZTA4ZGJkZjAwOTQ5MmNiN2NjYzdkMzc1OTE0ODllKTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl8wZDY2NTNkMzQ2NjU0ZjMwYTRhODIzNWFiZDc2OGQ1NS5iaW5kUG9wdXAocG9wdXBfY2RjMjIxYWVkMzM3NDMyNzljYzdiNjIwNDM5YzFiMjEpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2Q5YWM4N2EzOWMzNTRiOWQ4ZWMzN2M4YjQ0YWZmNTQ0ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMjAyNDQ4NSwgNTUuMjM5NjUyNV0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiciIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJyIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiA1LCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF85MDM2N2QwNGU5YTQ0NDk2OGZlNjhlYzVkN2VjYTIzZiA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfZTE2YzRiNDVmNTlkNDQ2YzkwMTRiMzU2OTEzODI3MmMgPSAkKGA8ZGl2IGlkPSJodG1sX2UxNmM0YjQ1ZjU5ZDQ0NmM5MDE0YjM1NjkxMzgyNzJjIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogU3BvbnNvcmVkdmVyZGUgZHViYWk8YnI+VGVsZXBob25lOiArOTcxIDQgMzMzIDgwMjU8YnI+dXJsOiBodHRwOi8vd3d3LnZlcmRlLWR1YmFpLmNvbS88L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfOTAzNjdkMDRlOWE0NDQ5NjhmZTY4ZWM1ZDdlY2EyM2Yuc2V0Q29udGVudChodG1sX2UxNmM0YjQ1ZjU5ZDQ0NmM5MDE0YjM1NjkxMzgyNzJjKTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl9kOWFjODdhMzljMzU0YjlkOGVjMzdjOGI0NGFmZjU0NC5iaW5kUG9wdXAocG9wdXBfOTAzNjdkMDRlOWE0NDQ5NjhmZTY4ZWM1ZDdlY2EyM2YpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2QwMzI3YzgzOWE1YjQyMTViNzQ0OGNlN2Y0NjdkNmRlID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMjI5NTMwOSwgNTUuMjg2NjcyOF0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiciIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJyIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiA1LCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF84MGQwNGY3YjVkMzM0NzRhYTQ2MjRjMWNhMjI5ODEyYiA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfOGZiM2U5NDQwODc1NDgwOWJlOGQzYmE0Mjk2Y2Q5YzkgPSAkKGA8ZGl2IGlkPSJodG1sXzhmYjNlOTQ0MDg3NTQ4MDliZThkM2JhNDI5NmNkOWM5IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogMjYuIG5pZG8gdGFwYXMgcmVzdGF1cmFudCAmIGJhcjxicj5UZWxlcGhvbmU6ICs5NzEgNCAzMzMgMzA1NTxicj51cmw6IGh0dHA6Ly9uaWRvZHhiLmNvbS88L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfODBkMDRmN2I1ZDMzNDc0YWE0NjI0YzFjYTIyOTgxMmIuc2V0Q29udGVudChodG1sXzhmYjNlOTQ0MDg3NTQ4MDliZThkM2JhNDI5NmNkOWM5KTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl9kMDMyN2M4MzlhNWI0MjE1Yjc0NDhjZTdmNDY3ZDZkZS5iaW5kUG9wdXAocG9wdXBfODBkMDRmN2I1ZDMzNDc0YWE0NjI0YzFjYTIyOTgxMmIpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2Q5MGFhODAxZWIzZjQ3YjJiYjVhNTJkOGY0NzBlMjYwID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMDgwNDc3NywgNTUuMTU0MTk0MzAwMDAwMDFdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogInIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiciIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogNSwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfYzI3NmM1MzRmMjIwNGJkY2JlYTBkOGU2ZmFhNDEyNTAgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzIwYmZiNzA1ZjNmZjRlYmE4YTk4ZTA3OTk1MGMzZWIxID0gJChgPGRpdiBpZD0iaHRtbF8yMGJmYjcwNWYzZmY0ZWJhOGE5OGUwNzk5NTBjM2ViMSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDI3LiBzaGFtaWFuYTxicj5UZWxlcGhvbmU6ICs5NzEgNCA1NzQgMTExMTxicj51cmw6IGh0dHA6Ly93d3cudGFqaG90ZWxzLmNvbS9lbi1pbi90YWovdGFqLWp1bWVpcmFoLWxha2VzLXRvd2Vycy9yZXN0YXVyYW50cy9zaGFtaWFuYS88L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfYzI3NmM1MzRmMjIwNGJkY2JlYTBkOGU2ZmFhNDEyNTAuc2V0Q29udGVudChodG1sXzIwYmZiNzA1ZjNmZjRlYmE4YTk4ZTA3OTk1MGMzZWIxKTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl9kOTBhYTgwMWViM2Y0N2IyYmI1YTUyZDhmNDcwZTI2MC5iaW5kUG9wdXAocG9wdXBfYzI3NmM1MzRmMjIwNGJkY2JlYTBkOGU2ZmFhNDEyNTApCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2Q1MjhmYjY5OTU0MDRiYTBhYjg1ZGJhMTdkNTI3NzI5ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMjA0ODQ5MywgNTUuMjcwNzgyOF0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiciIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJyIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiA1LCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF85NDI4NzFhZGQ1Njc0YjZjYjk2YzE1ZjI0MGVkMmJkOSA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfYTJiZGIzNGYwMTk3NDcyMjkxNWE2YWFhMTRiMjJiNGUgPSAkKGA8ZGl2IGlkPSJodG1sX2EyYmRiMzRmMDE5NzQ3MjI5MTVhNmFhYTE0YjIyYjRlIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogMjguIGtpbmFyYSBieSB2aWthcyBraGFubmE8YnI+VGVsZXBob25lOiArOTcxIDQgODE0IDU1NTU8YnI+dXJsOiBodHRwOi8vd3d3LmtpbmFyYWR1YmFpLmNvbS88L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfOTQyODcxYWRkNTY3NGI2Y2I5NmMxNWYyNDBlZDJiZDkuc2V0Q29udGVudChodG1sX2EyYmRiMzRmMDE5NzQ3MjI5MTVhNmFhYTE0YjIyYjRlKTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl9kNTI4ZmI2OTk1NDA0YmEwYWI4NWRiYTE3ZDUyNzcyOS5iaW5kUG9wdXAocG9wdXBfOTQyODcxYWRkNTY3NGI2Y2I5NmMxNWYyNDBlZDJiZDkpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzlhZDhkMTNjODM0ZDQwNzI5OTNkY2UxN2EzZDUyNTRmID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMTEwODIwMiwgNTUuMTM5OTE4NDAwMDAwMDFdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogInIiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAiciIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogNSwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfZGYwMjdlYzk2ZmU1NGY0MjkyNzFkNDBiNDEwNjJiMzQgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sX2E1OWU1NjA3MjZlMDQxMTk5NDg2OTcwYmMxMmJiMzQ1ID0gJChgPGRpdiBpZD0iaHRtbF9hNTllNTYwNzI2ZTA0MTE5OTQ4Njk3MGJjMTJiYjM0NSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDI5LiBsaXR0bGUgbWlzcyBpbmRpYTxicj5UZWxlcGhvbmU6ICs5NzEgNCA0NTcgMzQ1Nzxicj51cmw6IGh0dHA6Ly93d3cuZmFpcm1vbnQuY29tL3BhbG0tZHViYWkvZGluaW5nL2xpdHRsZS1taXNzLWluZGlhLzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF9kZjAyN2VjOTZmZTU0ZjQyOTI3MWQ0MGI0MTA2MmIzNC5zZXRDb250ZW50KGh0bWxfYTU5ZTU2MDcyNmUwNDExOTk0ODY5NzBiYzEyYmIzNDUpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyXzlhZDhkMTNjODM0ZDQwNzI5OTNkY2UxN2EzZDUyNTRmLmJpbmRQb3B1cChwb3B1cF9kZjAyN2VjOTZmZTU0ZjQyOTI3MWQ0MGI0MTA2MmIzNCkKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMmI5ZWZiNzc5OTY5NDA1NGJjYmE0NWNmOGVkOWE0ZGUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4xMTAzNDcsIDU1LjIyMDYyODI5OTk5OTk5XSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJyIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogInIiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDUsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwXzg0ZTBmMGNjN2VmMTQ4ZWNhODM3N2Y0ZWI0MGNkNDM3ID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF9mMWIyODI3ZGM1Yzk0YWVkOGEyNDQ4Yzc5YzUxNjk0NCA9ICQoYDxkaXYgaWQ9Imh0bWxfZjFiMjgyN2RjNWM5NGFlZDhhMjQ0OGM3OWM1MTY5NDQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiAzMC4gZmlzaCBodXQgYXNtYWsgYWwgc3VsdGFuIHNlYWZvb2QgcmVzdGF1cmFudDxicj5UZWxlcGhvbmU6ICs5NzEgNTggMTI4IDI4ODY8YnI+dXJsOiBodHRwOi8vZHViYWlmaXNoaHV0cmVzdGF1cmFudC5jb20vaW5kZXgucGhwPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwXzg0ZTBmMGNjN2VmMTQ4ZWNhODM3N2Y0ZWI0MGNkNDM3LnNldENvbnRlbnQoaHRtbF9mMWIyODI3ZGM1Yzk0YWVkOGEyNDQ4Yzc5YzUxNjk0NCk7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfMmI5ZWZiNzc5OTY5NDA1NGJjYmE0NWNmOGVkOWE0ZGUuYmluZFBvcHVwKHBvcHVwXzg0ZTBmMGNjN2VmMTQ4ZWNhODM3N2Y0ZWI0MGNkNDM3KQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9iNTQyNDUxMDdhMzU0YmE0YjI3NjQ0MTZlNmJjZTY4NiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjIwODI3MywgNTUuMjYwNjAxNV0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAiciIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJyIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiA1LCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF80OTVkZmZjOWEwNmE0MjllYjc4ZDM4ZGVkZTUzZTEyNSA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfZDYyMTY2MTE1N2ZlNDA0MGJlN2Q1Njg3MWU5ZjlmN2EgPSAkKGA8ZGl2IGlkPSJodG1sX2Q2MjE2NjExNTdmZTQwNDBiZTdkNTY4NzFlOWY5ZjdhIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogU3BvbnNvcmVkY2hpdmFsPGJyPlRlbGVwaG9uZTogKzk3MSA0IDQwMyAzMTExPGJyPnVybDogaHR0cDovL3d3dy5jaGl2YWxsYXZpbGxlLmNvbS88L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfNDk1ZGZmYzlhMDZhNDI5ZWI3OGQzOGRlZGU1M2UxMjUuc2V0Q29udGVudChodG1sX2Q2MjE2NjExNTdmZTQwNDBiZTdkNTY4NzFlOWY5ZjdhKTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl9iNTQyNDUxMDdhMzU0YmE0YjI3NjQ0MTZlNmJjZTY4Ni5iaW5kUG9wdXAocG9wdXBfNDk1ZGZmYzlhMDZhNDI5ZWI3OGQzOGRlZGU1M2UxMjUpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzdmMWZkZWY4ZGEwMTQwODdiODYzOTI5MzAzYTQ0YjgxID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMTMzODc3NywgNTUuMTg0NzYyNV0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAicmVkIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogInJlZCIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogNSwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfNGZkOTk5ZDUzZjYwNDMyNjg4N2QwNDNmNTJhNDMzMDQgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzcwNjgxZWRkODJhOTRlM2M4ODhkNDIzNzlhZWI1N2RjID0gJChgPGRpdiBpZD0iaHRtbF83MDY4MWVkZDgyYTk0ZTNjODg4ZDQyMzc5YWViNTdkYyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IFNwb25zb3JlZGZvbGx5IGJ5IG5pY2sgJiBzY290dDxicj5UZWxlcGhvbmU6ICs5NzEgNCA0MzAgODUzNTxicj51cmw6IGh0dHA6Ly9mb2xseS5hZS88L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfNGZkOTk5ZDUzZjYwNDMyNjg4N2QwNDNmNTJhNDMzMDQuc2V0Q29udGVudChodG1sXzcwNjgxZWRkODJhOTRlM2M4ODhkNDIzNzlhZWI1N2RjKTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl83ZjFmZGVmOGRhMDE0MDg3Yjg2MzkyOTMwM2E0NGI4MS5iaW5kUG9wdXAocG9wdXBfNGZkOTk5ZDUzZjYwNDMyNjg4N2QwNDNmNTJhNDMzMDQpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzdlOGQxOTAwNDIzYzQyYjNhYjA2YmFiYWIxNWFkZWQwID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMDgwNjM2LCA1NS4xMzU1MzE4XSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJyZWQiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAicmVkIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiA1LCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF84MmU1NmRkMmUwZmY0ODUyOTM4M2NlMjBiMDNmM2NkYSA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfZjEyZmVkNzIzNDhiNDkxMjgzZTcxMDQ1ZjQ2NDA2Y2MgPSAkKGA8ZGl2IGlkPSJodG1sX2YxMmZlZDcyMzQ4YjQ5MTI4M2U3MTA0NWY0NjQwNmNjIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogMS4gYXNpbCByZXN0YXVyYW50PGJyPlRlbGVwaG9uZTogKzk3MSA1MiAxNjAgMDMzMzxicj51cmw6IGh0dHA6Ly93d3cuYXNpbHJlc3RhdXJhbnQuY29tLzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF84MmU1NmRkMmUwZmY0ODUyOTM4M2NlMjBiMDNmM2NkYS5zZXRDb250ZW50KGh0bWxfZjEyZmVkNzIzNDhiNDkxMjgzZTcxMDQ1ZjQ2NDA2Y2MpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyXzdlOGQxOTAwNDIzYzQyYjNhYjA2YmFiYWIxNWFkZWQwLmJpbmRQb3B1cChwb3B1cF84MmU1NmRkMmUwZmY0ODUyOTM4M2NlMjBiMDNmM2NkYSkKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfY2U3ZDM3ZDA3MzJkNDIyZjg5NzVkZmI2MTA4ZDY2ZjggPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4yMzE0OTgyLCA1NS4zNDY5NTU5XSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJyZWQiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAicmVkIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiA1LCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF9jNzk0NThjYWE5ZDI0NTY1YWNkMmY0YWRkNWExOGQ3YyA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfYzlhZWE1NTJiZTQwNDlmOTk2YTFhNzVmZmJiYTMwODUgPSAkKGA8ZGl2IGlkPSJodG1sX2M5YWVhNTUyYmU0MDQ5Zjk5NmExYTc1ZmZiYmEzMDg1IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogMi4gbWV6emFsdW5hPGJyPlRlbGVwaG9uZTogKzk3MSA0IDcwMSAxMTI4PGJyPnVybDogaHR0cDovL3d3dy5kaW5pbmdkZmMuY29tL1Jlc3RhdXJhbnQtZGV0YWlscy8yNC9NZXp6YUx1bmE8L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfYzc5NDU4Y2FhOWQyNDU2NWFjZDJmNGFkZDVhMThkN2Muc2V0Q29udGVudChodG1sX2M5YWVhNTUyYmU0MDQ5Zjk5NmExYTc1ZmZiYmEzMDg1KTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl9jZTdkMzdkMDczMmQ0MjJmODk3NWRmYjYxMDhkNjZmOC5iaW5kUG9wdXAocG9wdXBfYzc5NDU4Y2FhOWQyNDU2NWFjZDJmNGFkZDVhMThkN2MpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzY5NzIzNzhlNjFjMzRkNWE4MTZiOTI2MGY3Yzk5NjRmID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMjUzMTc0NSwgNTUuMzY1NjcyOF0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAicmVkIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogInJlZCIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogNSwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfMzRkODAwMGE3YTkzNGRjYzg5Yzc2OWM1YzcyN2U2MzkgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzM2NjQ5OTVlMDFkYTQxOGM4YWZlNTk4MTIwNTY1YzA5ID0gJChgPGRpdiBpZD0iaHRtbF8zNjY0OTk1ZTAxZGE0MThjOGFmZTU5ODEyMDU2NWMwOSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDMuIGNhZGl6IC0gYWhsYW4gbG91bmdlIEAgZ2F0ZSBiMjY8YnI+VGVsZXBob25lOiArOTcxIDQgNTA1IDIwMDA8YnI+dXJsOiBodHRwOi8vd3d3LmR1YmFpaW50bGhvdGVscy5jb20vZGluaW5nL2FobGFuLWxvdW5nZS1iPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwXzM0ZDgwMDBhN2E5MzRkY2M4OWM3NjljNWM3MjdlNjM5LnNldENvbnRlbnQoaHRtbF8zNjY0OTk1ZTAxZGE0MThjOGFmZTU5ODEyMDU2NWMwOSk7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfNjk3MjM3OGU2MWMzNGQ1YTgxNmI5MjYwZjdjOTk2NGYuYmluZFBvcHVwKHBvcHVwXzM0ZDgwMDBhN2E5MzRkY2M4OWM3NjljNWM3MjdlNjM5KQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8yODQxMTQwYjc2YjQ0ZDU4OTMzMGI3MmJjYTE1ZTZiOSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjEwNDMyOTYsIDU1LjE0ODc2OTFdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogInJlZCIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJyZWQiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDUsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwX2ExYWIxODFjNjUwNTQ1NjliOTI5ZWNhOTNmNjkyOGFiID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF8xYjJjY2FkYmMxMzI0NWRjOWFmZDY2NmM3MmJiNzc5ZCA9ICQoYDxkaXYgaWQ9Imh0bWxfMWIyY2NhZGJjMTMyNDVkYzlhZmQ2NjZjNzJiYjc3OWQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiA0LiBibHZkIG9uIG9uZTxicj5UZWxlcGhvbmU6ICs5NzEgNCA0NTUgOTk4OTxicj51cmw6IGh0dHA6Ly9maXZlaG90ZWxzYW5kcmVzb3J0cy5jb20vZGluZS1kcmluay1kYW5jZS9yZXN0YXVyYW50cy9ibHZkLW9uLW9uZS88L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfYTFhYjE4MWM2NTA1NDU2OWI5MjllY2E5M2Y2OTI4YWIuc2V0Q29udGVudChodG1sXzFiMmNjYWRiYzEzMjQ1ZGM5YWZkNjY2YzcyYmI3NzlkKTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl8yODQxMTQwYjc2YjQ0ZDU4OTMzMGI3MmJjYTE1ZTZiOS5iaW5kUG9wdXAocG9wdXBfYTFhYjE4MWM2NTA1NDU2OWI5MjllY2E5M2Y2OTI4YWIpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzMwNjdlZGVjMjA2YTQwZjdhNWZlYTViZTBlNDczY2MxID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMjQ4MTQ2MiwgNTUuMjg2NjUyNV0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAicmVkIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogInJlZCIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogNSwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfYjcwZTVlNWU0YTJjNDUwMWJmZjQ4NjFlYzAzOTJkZTEgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sX2M1MmJmYzNiMzZjMjQ0NDI4MGI1MDI2NDg4Mzg2ZmZjID0gJChgPGRpdiBpZD0iaHRtbF9jNTJiZmMzYjM2YzI0NDQyODBiNTAyNjQ4ODM4NmZmYyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDUuIHB1cmFuaSBkaWxsaSBkdWJhaTxicj5UZWxlcGhvbmU6ICs5NzEgNTAgMjExIDY4MTY8YnI+dXJsOiBodHRwOi8vd3d3LnB1cmFuaWRpbGxpZHViYWkuY29tLzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF9iNzBlNWU1ZTRhMmM0NTAxYmZmNDg2MWVjMDM5MmRlMS5zZXRDb250ZW50KGh0bWxfYzUyYmZjM2IzNmMyNDQ0MjgwYjUwMjY0ODgzODZmZmMpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyXzMwNjdlZGVjMjA2YTQwZjdhNWZlYTViZTBlNDczY2MxLmJpbmRQb3B1cChwb3B1cF9iNzBlNWU1ZTRhMmM0NTAxYmZmNDg2MWVjMDM5MmRlMSkKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYjAyNjU2MDkxNWRmNDdmM2E3ZTZhYmEwYjIxNjYzOWEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4yMDgyNzMsIDU1LjI2MDYwMTVdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogInJlZCIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJyZWQiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDUsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwX2NkODA0ODcwNmQ3ODQ0NDFhZmJhNjU2YmFhZTA3N2YzID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF8xMmM3YTliZmE2ZWM0ODUxYTA2ZWExNzFiYTRlZTY1NyA9ICQoYDxkaXYgaWQ9Imh0bWxfMTJjN2E5YmZhNmVjNDg1MWEwNmVhMTcxYmE0ZWU2NTciIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiBTcG9uc29yZWRncmFwZXNraW4gZ3JhcGUgYmFyIGFuZCBraXRjaGVuPGJyPlRlbGVwaG9uZTogKzk3MSA0IDQwMyAzMTExPGJyPnVybDogaHR0cDovL3d3dy5saXZlbGF2aWxsZS5jb20vZGluaW5nL0dyYXBlc2tpbi9pbmRleC5hc3B4PC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwX2NkODA0ODcwNmQ3ODQ0NDFhZmJhNjU2YmFhZTA3N2YzLnNldENvbnRlbnQoaHRtbF8xMmM3YTliZmE2ZWM0ODUxYTA2ZWExNzFiYTRlZTY1Nyk7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfYjAyNjU2MDkxNWRmNDdmM2E3ZTZhYmEwYjIxNjYzOWEuYmluZFBvcHVwKHBvcHVwX2NkODA0ODcwNmQ3ODQ0NDFhZmJhNjU2YmFhZTA3N2YzKQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9lOGIyMDExYTI2OTY0M2YwOGNjNWIyOWIzNmE5YmIyNyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjEwNDMyOTYsIDU1LjE0ODc2OTFdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogInJlZCIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJyZWQiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDUsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwX2I3YzUwOWRkMGMyMDRmOTc4MWVjZTE5Y2E1YWUzOWViID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF81MDczOTQxM2E3N2U0OTdiOTkzZTNmY2I4NTA2M2Q1MiA9ICQoYDxkaXYgaWQ9Imh0bWxfNTA3Mzk0MTNhNzdlNDk3Yjk5M2UzZmNiODUwNjNkNTIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiA2LiB0cmF0dG9yaWEgYnkgY2lucXVlPGJyPlRlbGVwaG9uZTogKzk3MSA0IDQ1NSA5OTg5PGJyPnVybDogaHR0cDovL2p1bWVpcmFodmlsbGFnZS5maXZlaG90ZWxzYW5kcmVzb3J0cy5jb20vbWVldC1taW5nbGUvdHJhdHRvcmlhLWJ5LWNpbnF1ZTwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF9iN2M1MDlkZDBjMjA0Zjk3ODFlY2UxOWNhNWFlMzllYi5zZXRDb250ZW50KGh0bWxfNTA3Mzk0MTNhNzdlNDk3Yjk5M2UzZmNiODUwNjNkNTIpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyX2U4YjIwMTFhMjY5NjQzZjA4Y2M1YjI5YjM2YTliYjI3LmJpbmRQb3B1cChwb3B1cF9iN2M1MDlkZDBjMjA0Zjk3ODFlY2UxOWNhNWFlMzllYikKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMmZmZWYyNzFhMGY4NGI2ZmFjMmIwYTYxNjhjNTMwMDEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4yNTY4NzU3LCA1NS4zMTIwODExXSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJyZWQiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAicmVkIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiA1LCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF9jMWQzNjczM2MyZTg0ODg2ODZhNDc2MzJmNGQ4ZjlmOSA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfZjExMzY1NGI2Yjk1NGFkYjgxZDJkMDdhYWI4ODE4NDAgPSAkKGA8ZGl2IGlkPSJodG1sX2YxMTM2NTRiNmI5NTRhZGI4MWQyZDA3YWFiODgxODQwIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogNy4gZG9vcnMgZnJlZXN0eWxlIGdyaWxsPGJyPlRlbGVwaG9uZTogKzk3MSA0IDIwNCA5Mjk5PGJyPnVybDogaHR0cDovL3d3dy5kb29yc2R1YmFpLmNvbS9lbjwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF9jMWQzNjczM2MyZTg0ODg2ODZhNDc2MzJmNGQ4ZjlmOS5zZXRDb250ZW50KGh0bWxfZjExMzY1NGI2Yjk1NGFkYjgxZDJkMDdhYWI4ODE4NDApOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyXzJmZmVmMjcxYTBmODRiNmZhYzJiMGE2MTY4YzUzMDAxLmJpbmRQb3B1cChwb3B1cF9jMWQzNjczM2MyZTg0ODg2ODZhNDc2MzJmNGQ4ZjlmOSkKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMmYwMDc1ZTkyNzY4NDQ0ZjlmNTc2NmI4Njg1OWM4OGYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4wNjU3OTM0LCA1NS4xMzgxMTU5XSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJyZWQiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAicmVkIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiA1LCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF8zZDQ5ZTJlN2Y3Zjg0Y2FmYWI4MjJkZTU0YWNlMGM3NCA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfNGU1MDVkMzcyMzg5NDU2MThhMDQ1MTc1OTkyODA5ZWYgPSAkKGA8ZGl2IGlkPSJodG1sXzRlNTA1ZDM3MjM4OTQ1NjE4YTA0NTE3NTk5MjgwOWVmIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogOC4gdXJiYW4gYmFyICYga2l0Y2hlbiAtIHViazxicj5UZWxlcGhvbmU6ICs5NzEgNCA0MzggMDAwMDxicj51cmw6IGh0dHA6Ly93d3cubW92ZW5waWNrLmNvbS9lbi9taWRkbGUtZWFzdC91YWUvZHViYWkvZHViYWktanVtZWlyYWgtbGFrZXMtdG93ZXJzL3Jlc3RhdXJhbnRzL3Jlc3RhdXJhbnRzL3VyYmFuLWJhci1raXRjaGVuLXViazwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF8zZDQ5ZTJlN2Y3Zjg0Y2FmYWI4MjJkZTU0YWNlMGM3NC5zZXRDb250ZW50KGh0bWxfNGU1MDVkMzcyMzg5NDU2MThhMDQ1MTc1OTkyODA5ZWYpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyXzJmMDA3NWU5Mjc2ODQ0NGY5ZjU3NjZiODY4NTljODhmLmJpbmRQb3B1cChwb3B1cF8zZDQ5ZTJlN2Y3Zjg0Y2FmYWI4MjJkZTU0YWNlMGM3NCkKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfODAyNzY5NjM4OGQ1NDQzZmEwM2Q4MzQxYjZiNDU0OTUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4yMzM4NDQxLCA1NS4yNjU0ODEyXSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJyZWQiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAicmVkIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiA1LCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF81Nzk4YTNhMDUyZGY0NzA5ODVlZDM5MWM5MDNiYmQ4OSA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfZTRhMGJhODlkM2QxNGQ3NDk3MTBhNDE5YjQyZjJmMzQgPSAkKGA8ZGl2IGlkPSJodG1sX2U0YTBiYTg5ZDNkMTRkNzQ5NzEwYTQxOWI0MmYyZjM0IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogOS4gYmFyZWZvb3QgbG91bmdlPGJyPlRlbGVwaG9uZTogKzk3MSA0IDM0NiAxMTExPGJyPnVybDogaHR0cDovL3d3dy5keGJtYXJpbmUuY29tLzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF81Nzk4YTNhMDUyZGY0NzA5ODVlZDM5MWM5MDNiYmQ4OS5zZXRDb250ZW50KGh0bWxfZTRhMGJhODlkM2QxNGQ3NDk3MTBhNDE5YjQyZjJmMzQpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyXzgwMjc2OTYzODhkNTQ0M2ZhMDNkODM0MWI2YjQ1NDk1LmJpbmRQb3B1cChwb3B1cF81Nzk4YTNhMDUyZGY0NzA5ODVlZDM5MWM5MDNiYmQ4OSkKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYzM1YjVkM2Y5YjhiNDJmYjg3MzYwZTgyYTIxNWJjOGYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4yMTI2NDI2LCA1NS4yODI0MDVdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogInJlZCIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJyZWQiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDUsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwX2E0YmQzNjAzZWIzNDQxZWFiZDZlYmI1MmRhYzAyYWVlID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF9iOTk2Y2VlYzEwNmY0ZTJkYTRiMmFhOWU2YzNkYWViMSA9ICQoYDxkaXYgaWQ9Imh0bWxfYjk5NmNlZWMxMDZmNGUyZGE0YjJhYTllNmMzZGFlYjEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiAxMC4gbWluYSBicmFzc2VyaWU8YnI+VGVsZXBob25lOiArOTcxIDQgNTA2IDAxMDA8YnI+dXJsOiBodHRwOi8vd3d3Lm1pbmFicmFzc2VyaWUuY29tLzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF9hNGJkMzYwM2ViMzQ0MWVhYmQ2ZWJiNTJkYWMwMmFlZS5zZXRDb250ZW50KGh0bWxfYjk5NmNlZWMxMDZmNGUyZGE0YjJhYTllNmMzZGFlYjEpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyX2MzNWI1ZDNmOWI4YjQyZmI4NzM2MGU4MmEyMTViYzhmLmJpbmRQb3B1cChwb3B1cF9hNGJkMzYwM2ViMzQ0MWVhYmQ2ZWJiNTJkYWMwMmFlZSkKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNGUzOTE2YTE1N2Y5NGZjNzkzYTUxZjQ3YjYxYWNjN2YgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4yMDgyNzMsIDU1LjI2MDYwMTVdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogInJlZCIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJyZWQiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDUsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwX2FmZGJhYjc5OTc3NjRlZWM5ZmVjYjI3MzQ3ZmJkM2U2ID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF8xM2FjN2RjMjY3Mjk0YTE1ODcyZjFhNTE3ZDJhZTY4NyA9ICQoYDxkaXYgaWQ9Imh0bWxfMTNhYzdkYzI2NzI5NGExNTg3MmYxYTUxN2QyYWU2ODciIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiBTcG9uc29yZWRncmF6ZSBnYXN0cm8gZ3JpbGw8YnI+VGVsZXBob25lOiArOTcxIDQgNDAzIDMxMTE8YnI+dXJsOiBodHRwOi8vd3d3LmxpdmVsYXZpbGxlLmNvbS9kaW5pbmcvR3JhemUvaW5kZXguaHRtbDwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF9hZmRiYWI3OTk3NzY0ZWVjOWZlY2IyNzM0N2ZiZDNlNi5zZXRDb250ZW50KGh0bWxfMTNhYzdkYzI2NzI5NGExNTg3MmYxYTUxN2QyYWU2ODcpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyXzRlMzkxNmExNTdmOTRmYzc5M2E1MWY0N2I2MWFjYzdmLmJpbmRQb3B1cChwb3B1cF9hZmRiYWI3OTk3NzY0ZWVjOWZlY2IyNzM0N2ZiZDNlNikKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfODFiNGQxMGM3MWU5NGQwOTg2MzgxMTg3ZmRlMTI1ZWIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNC44MTY4MjA2LCA1NS4yMzEyODcyXSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJyZWQiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAicmVkIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiA1LCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF8yMmExMmI0NzRmMjE0MDY5OGI0ZTU4NWRiMWI4YTU2YSA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfNWIzMjI2M2Q3YTMwNDdkM2FkNTE2ZWIzNmQ5NGYyYWEgPSAkKGA8ZGl2IGlkPSJodG1sXzViMzIyNjNkN2EzMDQ3ZDNhZDUxNmViMzZkOTRmMmFhIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogMTEuIGFsIHNhcmFiIHJvb2Z0b3AgbG91bmdlPGJyPlRlbGVwaG9uZTogKzk3MSA0IDgwOSA2MTAwPGJyPnVybDogaHR0cDovL3d3dy5tZXlkYW5ob3RlbHMuY29tL2JhYmFsc2hhbXMvZGluaW5nLmh0bTwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF8yMmExMmI0NzRmMjE0MDY5OGI0ZTU4NWRiMWI4YTU2YS5zZXRDb250ZW50KGh0bWxfNWIzMjI2M2Q3YTMwNDdkM2FkNTE2ZWIzNmQ5NGYyYWEpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyXzgxYjRkMTBjNzFlOTRkMDk4NjM4MTE4N2ZkZTEyNWViLmJpbmRQb3B1cChwb3B1cF8yMmExMmI0NzRmMjE0MDY5OGI0ZTU4NWRiMWI4YTU2YSkKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZGU4MTEyMDVmNzU5NDhhYzg3ZGRkYmZmZGRmYWYzNGYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4wNDYyOTQ2LCA1NS4yMDMwNDExOTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAicmVkIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogInJlZCIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogNSwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfOWE4MzBkYmU1NjRjNGYzNjliZmU4NzYzZThmMGU0ZjkgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzk4MTk0MTMzODA3YzQ2MzQ5ZmRjM2ViOWQxNDQwZTliID0gJChgPGRpdiBpZD0iaHRtbF85ODE5NDEzMzgwN2M0NjM0OWZkYzNlYjlkMTQ0MGU5YiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDEyLiBzb3VsIHN0cmVldDxicj5UZWxlcGhvbmU6ICs5NzEgNCA0NTUgOTk4OTxicj51cmw6IGh0dHA6Ly9zb3VsLnN0LzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF85YTgzMGRiZTU2NGM0ZjM2OWJmZTg3NjNlOGYwZTRmOS5zZXRDb250ZW50KGh0bWxfOTgxOTQxMzM4MDdjNDYzNDlmZGMzZWI5ZDE0NDBlOWIpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyX2RlODExMjA1Zjc1OTQ4YWM4N2RkZGJmZmRkZmFmMzRmLmJpbmRQb3B1cChwb3B1cF85YTgzMGRiZTU2NGM0ZjM2OWJmZTg3NjNlOGYwZTRmOSkKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNTBlMjY2MmUyNjMxNGYyODhhYTM4YmQ3NjEyOTY1NzUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4yNDkxNTQ5LCA1NS4zNDcxMzk2MDAwMDAwMV0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAicmVkIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogInJlZCIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogNSwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfNTMwY2RiNDJmMjYyNDIwMjhmZDZhYmM2NzRiNGQwZDMgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sX2EyM2U0MGFhNDJhYzQwNmNhMDU5ZmVmNzFlZmU2NzMxID0gJChgPGRpdiBpZD0iaHRtbF9hMjNlNDBhYTQyYWM0MDZjYTA1OWZlZjcxZWZlNjczMSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDEzLiBiZWJlbW9zPGJyPlRlbGVwaG9uZTogKzk3MSA0IDcwMiAyNDU1PGJyPnVybDogaHR0cDovL3d3dy5iZWJlbW9zZHViYWkuY29tLzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF81MzBjZGI0MmYyNjI0MjAyOGZkNmFiYzY3NGI0ZDBkMy5zZXRDb250ZW50KGh0bWxfYTIzZTQwYWE0MmFjNDA2Y2EwNTlmZWY3MWVmZTY3MzEpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyXzUwZTI2NjJlMjYzMTRmMjg4YWEzOGJkNzYxMjk2NTc1LmJpbmRQb3B1cChwb3B1cF81MzBjZGI0MmYyNjI0MjAyOGZkNmFiYzY3NGI0ZDBkMykKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfOTBiODc2MGJkYTlhNGVlN2FmMzU0MGRjNDc0NmU0NjIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4yMjg4Mzk0LCA1NS4zMjY4MTI1XSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJyZWQiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAicmVkIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiA1LCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF81ZDJiYzdmMjM4YjQ0YjFmOTI1ODEwMzFjZjAxNjA4OCA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfMDE2ZTU0YjFlN2VjNDZiYTk3YjI4MjkxMmU2ZWI0ZTMgPSAkKGA8ZGl2IGlkPSJodG1sXzAxNmU1NGIxZTdlYzQ2YmE5N2IyODI5MTJlNmViNGUzIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogMTQuIGF3dGFyPGJyPlRlbGVwaG9uZTogKzk3MSA0IDMxNyAyMjIxPGJyPnVybDogaHR0cHM6Ly93d3cuaHlhdHRyZXN0YXVyYW50cy5jb20vZW4vZGluaW5nL3VhZS9kdWJhaS9taWRkbGUtZWFzdGVybi1yZXN0YXVyYW50LWluLWdhcmhvdWQtYXd0YXI/dXRtX3NvdXJjZT1nbWJsaXN0aW5nX2R4YmdoJnV0bV9tZWRpdW09YXd0YXImdXRtX2NhbXBhaWduPUdNQjwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF81ZDJiYzdmMjM4YjQ0YjFmOTI1ODEwMzFjZjAxNjA4OC5zZXRDb250ZW50KGh0bWxfMDE2ZTU0YjFlN2VjNDZiYTk3YjI4MjkxMmU2ZWI0ZTMpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyXzkwYjg3NjBiZGE5YTRlZTdhZjM1NDBkYzQ3NDZlNDYyLmJpbmRQb3B1cChwb3B1cF81ZDJiYzdmMjM4YjQ0YjFmOTI1ODEwMzFjZjAxNjA4OCkKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfODBjMzUwMTM2MjZkNDg1MzgwNzJkZWE3ODFiNjhiOTcgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4xOTg3NjUsIDU1LjI3OTYwNTNdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogInJlZCIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJyZWQiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDUsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwXzE0OWI1Mjk4OGI3NTQzODE5MGQ3MTJhNmVmYzQ1OWEwID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF80Zjg5M2E1Mjg0MmE0MzQwOWM5OTIxYTZhMzU0Njc1MyA9ICQoYDxkaXYgaWQ9Imh0bWxfNGY4OTNhNTI4NDJhNDM0MDljOTkyMWE2YTM1NDY3NTMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiAxNS4gdHJpYmVzIGNhcm5pdm9yZTxicj5UZWxlcGhvbmU6ICs5NzEgNCAyMjYgNDk3NDxicj51cmw6IGh0dHA6Ly90cmliZXNyZXN0YXVyYW50LmNvbS88L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfMTQ5YjUyOTg4Yjc1NDM4MTkwZDcxMmE2ZWZjNDU5YTAuc2V0Q29udGVudChodG1sXzRmODkzYTUyODQyYTQzNDA5Yzk5MjFhNmEzNTQ2NzUzKTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl84MGMzNTAxMzYyNmQ0ODUzODA3MmRlYTc4MWI2OGI5Ny5iaW5kUG9wdXAocG9wdXBfMTQ5YjUyOTg4Yjc1NDM4MTkwZDcxMmE2ZWZjNDU5YTApCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzhkNGUyOGE4NzEwMjRhMDg4OWJlNjEzZDFjYTg4ZDU3ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMjIxNjAzLCA1NS4yODA4MjYyXSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJyZWQiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAicmVkIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiA1LCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF9mMWJhMWMzNmZhY2Y0M2I4ODk4ZDBhNmVhYzkxMTE5ZSA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfMjkzZGEyZmYzN2IxNDY3OTljY2M1MzBkZGU5YTNmODMgPSAkKGA8ZGl2IGlkPSJodG1sXzI5M2RhMmZmMzdiMTQ2Nzk5Y2NjNTMwZGRlOWEzZjgzIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogU3BvbnNvcmVkc3VzaGkgbmF0aW9uczxicj5UZWxlcGhvbmU6ICs5NzEgNTYgMTg4IDg1MjI8YnI+dXJsOiBodHRwczovL3N1c2hpbmF0aW9ucy5hZS88L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfZjFiYTFjMzZmYWNmNDNiODg5OGQwYTZlYWM5MTExOWUuc2V0Q29udGVudChodG1sXzI5M2RhMmZmMzdiMTQ2Nzk5Y2NjNTMwZGRlOWEzZjgzKTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl84ZDRlMjhhODcxMDI0YTA4ODliZTYxM2QxY2E4OGQ1Ny5iaW5kUG9wdXAocG9wdXBfZjFiYTFjMzZmYWNmNDNiODg5OGQwYTZlYWM5MTExOWUpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzljYTQwYzIzMGNhNzQ4ODA5NmZkY2Q3NTcxYTJhMTk4ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMjc4ODk4LCA1NS4zMDQ0NjA3XSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJyZWQiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAicmVkIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiA1LCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF9iZmI5MTc5NTEzZWY0N2U0YmNlNjkxNjNkYTRlYzQwOSA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfZDY5ZjcyNWJkYmI0NDE4OWI1MmM0MjYyNDViM2E0MTEgPSAkKGA8ZGl2IGlkPSJodG1sX2Q2OWY3MjViZGJiNDQxODliNTJjNDI2MjQ1YjNhNDExIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogMTYuIGFsIGRhd2FhciByZXZvbHZpbmcgcmVzdGF1cmFudDxicj5UZWxlcGhvbmU6ICs5NzEgNCAyMDkgNjkxMjxicj51cmw6IGh0dHA6Ly93d3cuaHlhdHRyZXN0YXVyYW50cy5jb20vZW4vZGluaW5nL3VhZS9kdWJhaS9pbnRlcm5hdGlvbmFsLXJlc3RhdXJhbnQtaW4tZGVpcmEtY29ybmljaGUtYWwtZGF3YWFyLXJldm9sdmluZy1yZXN0YXVyYW50PC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwX2JmYjkxNzk1MTNlZjQ3ZTRiY2U2OTE2M2RhNGVjNDA5LnNldENvbnRlbnQoaHRtbF9kNjlmNzI1YmRiYjQ0MTg5YjUyYzQyNjI0NWIzYTQxMSk7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfOWNhNDBjMjMwY2E3NDg4MDk2ZmRjZDc1NzFhMmExOTguYmluZFBvcHVwKHBvcHVwX2JmYjkxNzk1MTNlZjQ3ZTRiY2U2OTE2M2RhNGVjNDA5KQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8zMDhkYTk2YjcwOWI0NTk4ODcyNzcyNmUxZDVlZmU1YSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjExMTM5OTEsIDU1LjEzNzIxNThdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogInJlZCIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJyZWQiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDUsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwXzMzZDU1ZmNjYzljYzRmMTk5N2U0YmY1YTVmMjE2YzIyID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF9iNzI5NTcwOTk4ODM0YjRlYjhhYjk5N2ExMDllNDkwOCA9ICQoYDxkaXYgaWQ9Imh0bWxfYjcyOTU3MDk5ODgzNGI0ZWI4YWI5OTdhMTA5ZTQ5MDgiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiAxNy4ga2h5YmVyPGJyPlRlbGVwaG9uZTogKzk3MSA0IDQ1NSAxMTExPGJyPnVybDogaHR0cHM6Ly93d3cuZHVrZXNkdWJhaS5jb20va2h5YmVyLzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF8zM2Q1NWZjY2M5Y2M0ZjE5OTdlNGJmNWE1ZjIxNmMyMi5zZXRDb250ZW50KGh0bWxfYjcyOTU3MDk5ODgzNGI0ZWI4YWI5OTdhMTA5ZTQ5MDgpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyXzMwOGRhOTZiNzA5YjQ1OTg4NzI3NzI2ZTFkNWVmZTVhLmJpbmRQb3B1cChwb3B1cF8zM2Q1NWZjY2M5Y2M0ZjE5OTdlNGJmNWE1ZjIxNmMyMikKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMjcwMzdhZTZiOTU4NDBmZWEzNDkzMzAyNjdhNWE4NTQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4yNjYyNjc4LCA1NS4zMDg3ODc0OTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAicmVkIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogInJlZCIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogNSwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfZTA2ZTNiMjkxZGFjNDk4MTljOWRhNDRjYzczNjk1ZWMgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzEwNTBmMDg0ZmZhYjQ1MmJhYWRjNDQ4NjNlNzRmOWNjID0gJChgPGRpdiBpZD0iaHRtbF8xMDUwZjA4NGZmYWI0NTJiYWFkYzQ0ODYzZTc0ZjljYyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDE4LiBkYW5pYWwgcmVzdGF1cmFudDxicj5UZWxlcGhvbmU6ICs5NzEgNCAyMjcgNzY2OTxicj51cmw6IGh0dHA6Ly93d3cuZGFuaWFscmVzdGF1cmFudC5jb20vPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwX2UwNmUzYjI5MWRhYzQ5ODE5YzlkYTQ0Y2M3MzY5NWVjLnNldENvbnRlbnQoaHRtbF8xMDUwZjA4NGZmYWI0NTJiYWFkYzQ0ODYzZTc0ZjljYyk7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfMjcwMzdhZTZiOTU4NDBmZWEzNDkzMzAyNjdhNWE4NTQuYmluZFBvcHVwKHBvcHVwX2UwNmUzYjI5MWRhYzQ5ODE5YzlkYTQ0Y2M3MzY5NWVjKQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl81ZDkzODljNzY4MzM0YWE5OGY0NThhMWE3ZjExMmU2YyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjIzNDM1NSwgNTUuMzI0MDE0N10sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAicmVkIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogInJlZCIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogNSwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfMTA4ZTE5NzAyNGVlNGMxMTgxZjE5NWU3MWQyZmRhMzggPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sX2U4MmJhNjYzYmUwMTRkOWZiMzgyZmEzMGFmOWE1YTE2ID0gJChgPGRpdiBpZD0iaHRtbF9lODJiYTY2M2JlMDE0ZDlmYjM4MmZhMzBhZjlhNWExNiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDE5LiBldmUgcGVudGhvdXNlICYgbG91bmdlPGJyPlRlbGVwaG9uZTogKzk3MSA0IDU1MyAxMjE0PGJyPnVybDogaHR0cDovL3d3dy5oeWF0dHJlc3RhdXJhbnRzLmNvbS9lbi9kaW5pbmcvdWFlL2R1YmFpL2ludGVybmF0aW9uYWwtcmVzdGF1cmFudC1pbi1vdWQtbWV0aGEtcm9hZC1ldmUtcGVudGhvdXNlLWxvdW5nZT91dG1fc291cmNlPVdlYnNpdGVfZHhiaGMmdXRtX21lZGl1bT1ldmUmdXRtX2NhbXBhaWduPUh5YXR0PC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwXzEwOGUxOTcwMjRlZTRjMTE4MWYxOTVlNzFkMmZkYTM4LnNldENvbnRlbnQoaHRtbF9lODJiYTY2M2JlMDE0ZDlmYjM4MmZhMzBhZjlhNWExNik7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfNWQ5Mzg5Yzc2ODMzNGFhOThmNDU4YTFhN2YxMTJlNmMuYmluZFBvcHVwKHBvcHVwXzEwOGUxOTcwMjRlZTRjMTE4MWYxOTVlNzFkMmZkYTM4KQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl80MWIyZThiNDlmODE0YmQ5YjEzNGFlMDk3YmMzMDNmYiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjE5ODc2NSwgNTUuMjc5NjA1M10sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAicmVkIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogInJlZCIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogNSwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfZTJhMzg2MTZmY2NlNGNiZDkwMmNlMmYyOWEyYzI0ZWQgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzRkZGE4ZjRjYjMyNjRmZGM4ZWZlZTYyYTA3ZDUzY2U5ID0gJChgPGRpdiBpZD0iaHRtbF80ZGRhOGY0Y2IzMjY0ZmRjOGVmZWU2MmEwN2Q1M2NlOSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDIwLiB0aGUgZ3JpbGwgc2hhY2s8YnI+VGVsZXBob25lOiArOTcxIDQgMzg4IDIzODI8YnI+dXJsOiBodHRwOi8vd3d3LnRoZWdyaWxsbHNoYWNrLmNvbS88L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfZTJhMzg2MTZmY2NlNGNiZDkwMmNlMmYyOWEyYzI0ZWQuc2V0Q29udGVudChodG1sXzRkZGE4ZjRjYjMyNjRmZGM4ZWZlZTYyYTA3ZDUzY2U5KTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl80MWIyZThiNDlmODE0YmQ5YjEzNGFlMDk3YmMzMDNmYi5iaW5kUG9wdXAocG9wdXBfZTJhMzg2MTZmY2NlNGNiZDkwMmNlMmYyOWEyYzI0ZWQpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzM3ZGZiYWQwMjA5YzQxMGU4NjZlMTViOWU1N2Q3Y2JmID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMjQ3ODY3LCA1NS4zMDA0OTI1XSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJyZWQiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAicmVkIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiA1LCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF9lYzMzZmJiMGI0M2I0ZDE0YmVlMjY4NGI2Mjk5MjQyYiA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfNTQxMzA2OTQ0ZDc3NGE5MjgxOThhMmYxYmI2ZTc1ZTkgPSAkKGA8ZGl2IGlkPSJodG1sXzU0MTMwNjk0NGQ3NzRhOTI4MTk4YTJmMWJiNmU3NWU5IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogU3BvbnNvcmVkYW1yaXRzciByZXN0YXVyYW50PGJyPlRlbGVwaG9uZTogKzk3MSA1MCA2NzggMDA5Njxicj51cmw6IGh0dHA6Ly9hbXJpdHNydWFlLmNvbS88L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfZWMzM2ZiYjBiNDNiNGQxNGJlZTI2ODRiNjI5OTI0MmIuc2V0Q29udGVudChodG1sXzU0MTMwNjk0NGQ3NzRhOTI4MTk4YTJmMWJiNmU3NWU5KTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl8zN2RmYmFkMDIwOWM0MTBlODY2ZTE1YjllNTdkN2NiZi5iaW5kUG9wdXAocG9wdXBfZWMzM2ZiYjBiNDNiNGQxNGJlZTI2ODRiNjI5OTI0MmIpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzI1MDQ5MzRlY2VjOTRhOGZiNGQ5YzBkNjVhNDNiZDA4ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMTA0MzI5NiwgNTUuMTQ4NzY5MV0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAicmVkIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogInJlZCIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogNSwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfYWFlYjAzNWIyNDBkNDdjMjg2NjFlNTMxNWJjZjg5OGIgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sX2ZkNzhjMjM1YjJmYjQ1NTM4MWNjMjA1MDNjZDJlZjliID0gJChgPGRpdiBpZD0iaHRtbF9mZDc4YzIzNWIyZmI0NTUzODFjYzIwNTAzY2QyZWY5YiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDIxLiBtYWlkZW4gc2hhbmdoYWk8YnI+VGVsZXBob25lOiArOTcxIDQgNDU1IDk5ODk8YnI+dXJsOiBodHRwOi8vZml2ZWhvdGVsc2FuZHJlc29ydHMuY29tL2RpbmUtZHJpbmstZGFuY2UvcmVzdGF1cmFudHMvbWFpZGVuLXNoYW5naGFpLzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF9hYWViMDM1YjI0MGQ0N2MyODY2MWU1MzE1YmNmODk4Yi5zZXRDb250ZW50KGh0bWxfZmQ3OGMyMzViMmZiNDU1MzgxY2MyMDUwM2NkMmVmOWIpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyXzI1MDQ5MzRlY2VjOTRhOGZiNGQ5YzBkNjVhNDNiZDA4LmJpbmRQb3B1cChwb3B1cF9hYWViMDM1YjI0MGQ0N2MyODY2MWU1MzE1YmNmODk4YikKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMzE3M2ZjZWE5N2E4NDdjZjg0MjNlYjIwMzgxZGU3MTIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4yMTQwMTMzLCA1NS4yNzYwODg1XSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJyZWQiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAicmVkIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiA1LCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF81ZWI5M2FiMzk3NGY0NDdkYTY3MzEyYzU3Mjk5YzViOSA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfNmRlNDlmZjkyOWEzNGU3ZWIzZTcwYWYyNmJkMTkyYjIgPSAkKGA8ZGl2IGlkPSJodG1sXzZkZTQ5ZmY5MjlhMzRlN2ViM2U3MGFmMjZiZDE5MmIyIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogMjIuIHB1cmFuaSBkaWxsaSBzaGVpa2ggemF5ZWQgcm9hZDxicj5UZWxlcGhvbmU6ICs5NzEgNCAzMTYgOTcyNjxicj51cmw6IGh0dHA6Ly93d3cucHVyYW5pZGlsbGlkdWJhaS5jb20vc2hlaWtoemF5ZWRyb2FkPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwXzVlYjkzYWIzOTc0ZjQ0N2RhNjczMTJjNTcyOTljNWI5LnNldENvbnRlbnQoaHRtbF82ZGU0OWZmOTI5YTM0ZTdlYjNlNzBhZjI2YmQxOTJiMik7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfMzE3M2ZjZWE5N2E4NDdjZjg0MjNlYjIwMzgxZGU3MTIuYmluZFBvcHVwKHBvcHVwXzVlYjkzYWIzOTc0ZjQ0N2RhNjczMTJjNTcyOTljNWI5KQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9iNGYzNjM5NjE5YTQ0MmMzOWQ3MmY0NWNjN2U4NjNiYiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjIxNDAxMzMsIDU1LjI3NjA4ODVdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogInJlZCIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJyZWQiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDUsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwXzE4M2M2MmM4NWZkZDQzMWFhNDkyZjg1ZGNjNjQ5YzAzID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF8yNmNiMjczYTlhOWE0ZTI0OTdiYTdmMTNiZDIwMWVkOCA9ICQoYDxkaXYgaWQ9Imh0bWxfMjZjYjI3M2E5YTlhNGUyNDk3YmE3ZjEzYmQyMDFlZDgiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiAyMy4gbGV2ZWwgNDMgc2t5IGxvdW5nZTxicj5UZWxlcGhvbmU6ICs5NzEgNTYgNDE0IDIyMTM8YnI+dXJsOiBodHRwOi8vd3d3LmxldmVsNDNsb3VuZ2UuY29tLzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF8xODNjNjJjODVmZGQ0MzFhYTQ5MmY4NWRjYzY0OWMwMy5zZXRDb250ZW50KGh0bWxfMjZjYjI3M2E5YTlhNGUyNDk3YmE3ZjEzYmQyMDFlZDgpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyX2I0ZjM2Mzk2MTlhNDQyYzM5ZDcyZjQ1Y2M3ZTg2M2JiLmJpbmRQb3B1cChwb3B1cF8xODNjNjJjODVmZGQ0MzFhYTQ5MmY4NWRjYzY0OWMwMykKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZGY1N2FkZjI1MzQ4NGYxMWIxODZmZWMzZWYyOGYzNTcgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4xOTUxNTU0LCA1NS4yNzUxNTc5XSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJyZWQiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAicmVkIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiA1LCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF81M2Q2NDI3ZjZhODY0YTA2YWY1ODExY2MyODU4MWIwOCA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfOWJlN2IxMGE4ZjAyNGE1NGExYTkyMmUxNzg2NzUzOGIgPSAkKGA8ZGl2IGlkPSJodG1sXzliZTdiMTBhOGYwMjRhNTRhMWE5MjJlMTc4Njc1MzhiIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogMjQuIGJsYWNrIHRhcCBjcmFmdCBidXJnZXJzICYgc2hha2VzIGR1YmFpIG1hbGw8YnI+VGVsZXBob25lOiArOTcxIDQgMzMwIDUxMDM8YnI+dXJsOiBodHRwOi8vd3d3LmJsYWNrdGFwbWUuY29tLzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF81M2Q2NDI3ZjZhODY0YTA2YWY1ODExY2MyODU4MWIwOC5zZXRDb250ZW50KGh0bWxfOWJlN2IxMGE4ZjAyNGE1NGExYTkyMmUxNzg2NzUzOGIpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyX2RmNTdhZGYyNTM0ODRmMTFiMTg2ZmVjM2VmMjhmMzU3LmJpbmRQb3B1cChwb3B1cF81M2Q2NDI3ZjZhODY0YTA2YWY1ODExY2MyODU4MWIwOCkKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZjVhYmI0YmM0YmEyNGQzNDkxMzJiNDhkYWJlNGU4ZDYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4yNDkxNTQ5LCA1NS4zNDcxMzk2MDAwMDAwMV0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAicmVkIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogInJlZCIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogNSwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfODg2YzEzZWYxZWM4NDdlYmI2OGI5Y2Q1ZjhkN2QzMjQgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzM4YTE5NDc5M2Y0NDQyNTc4N2QzYTgwZjhlZGY1ZmYzID0gJChgPGRpdiBpZD0iaHRtbF8zOGExOTQ3OTNmNDQ0MjU3ODdkM2E4MGY4ZWRmNWZmMyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDI1LiBiZWVmIGJpc3Rybzxicj5UZWxlcGhvbmU6ICs5NzEgNCA3MDIgMjQ1NTxicj51cmw6IGh0dHA6Ly93d3cuYmVlZmJpc3Ryb2R1YmFpLmNvbS88L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfODg2YzEzZWYxZWM4NDdlYmI2OGI5Y2Q1ZjhkN2QzMjQuc2V0Q29udGVudChodG1sXzM4YTE5NDc5M2Y0NDQyNTc4N2QzYTgwZjhlZGY1ZmYzKTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl9mNWFiYjRiYzRiYTI0ZDM0OTEzMmI0OGRhYmU0ZThkNi5iaW5kUG9wdXAocG9wdXBfODg2YzEzZWYxZWM4NDdlYmI2OGI5Y2Q1ZjhkN2QzMjQpCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzk1MzcwODEwYWYyNzQ4MWFhYmI0YzM3ZTk3NzA3YzM2ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMjAyNDQ4NSwgNTUuMjM5NjUyNV0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAicmVkIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogInJlZCIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogNSwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfY2I2YmUxMGI4NzhiNGJjNWE3NTg4M2M3ZmM2YzljZjggPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzI3MDIwZmNhZGI5MzQ3NzdiYzYzNGFhYTMwOTY1YTFhID0gJChgPGRpdiBpZD0iaHRtbF8yNzAyMGZjYWRiOTM0Nzc3YmM2MzRhYWEzMDk2NWExYSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IFNwb25zb3JlZHZlcmRlIGR1YmFpPGJyPlRlbGVwaG9uZTogKzk3MSA0IDMzMyA4MDI1PGJyPnVybDogaHR0cDovL3d3dy52ZXJkZS1kdWJhaS5jb20vPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwX2NiNmJlMTBiODc4YjRiYzVhNzU4ODNjN2ZjNmM5Y2Y4LnNldENvbnRlbnQoaHRtbF8yNzAyMGZjYWRiOTM0Nzc3YmM2MzRhYWEzMDk2NWExYSk7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfOTUzNzA4MTBhZjI3NDgxYWFiYjRjMzdlOTc3MDdjMzYuYmluZFBvcHVwKHBvcHVwX2NiNmJlMTBiODc4YjRiYzVhNzU4ODNjN2ZjNmM5Y2Y4KQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl84MWE2MGVmMTI5ZjQ0ODhjYTI1MmI3ZGZhMGQ0MDQzMSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjIyOTUzMDksIDU1LjI4NjY3MjhdLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogInJlZCIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJyZWQiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDUsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwXzFiMGFhNmVmMTA0MTRjNjFiM2RmOWYwY2ViODUxNDRlID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF8yZDQ5NDlhOTlhMGQ0MzQyODhiMzk4YmI4YTQ3MWNhMiA9ICQoYDxkaXYgaWQ9Imh0bWxfMmQ0OTQ5YTk5YTBkNDM0Mjg4YjM5OGJiOGE0NzFjYTIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiAyNi4gbmlkbyB0YXBhcyByZXN0YXVyYW50ICYgYmFyPGJyPlRlbGVwaG9uZTogKzk3MSA0IDMzMyAzMDU1PGJyPnVybDogaHR0cDovL25pZG9keGIuY29tLzwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF8xYjBhYTZlZjEwNDE0YzYxYjNkZjlmMGNlYjg1MTQ0ZS5zZXRDb250ZW50KGh0bWxfMmQ0OTQ5YTk5YTBkNDM0Mjg4YjM5OGJiOGE0NzFjYTIpOwogICAgICAgIAoKICAgICAgICBjaXJjbGVfbWFya2VyXzgxYTYwZWYxMjlmNDQ4OGNhMjUyYjdkZmEwZDQwNDMxLmJpbmRQb3B1cChwb3B1cF8xYjBhYTZlZjEwNDE0YzYxYjNkZjlmMGNlYjg1MTQ0ZSkKICAgICAgICA7CgogICAgICAgIAogICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZDNiM2M0MTU2YjEwNDUxZDgyZTZmZTE3NWYxNmEyZjUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFsyNS4wODA0Nzc3LCA1NS4xNTQxOTQzMDAwMDAwMV0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAicmVkIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogInJlZCIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogNSwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfOWRmYmM3YjhjYTY1NDEyZDhjNzkyMGZmODg4YWIwMzAgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sX2ZjOTZlM2VmNjMxYTQ0MzViNWE3OTYxNTFiMzhiOTFkID0gJChgPGRpdiBpZD0iaHRtbF9mYzk2ZTNlZjYzMWE0NDM1YjVhNzk2MTUxYjM4YjkxZCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDI3LiBzaGFtaWFuYTxicj5UZWxlcGhvbmU6ICs5NzEgNCA1NzQgMTExMTxicj51cmw6IGh0dHA6Ly93d3cudGFqaG90ZWxzLmNvbS9lbi1pbi90YWovdGFqLWp1bWVpcmFoLWxha2VzLXRvd2Vycy9yZXN0YXVyYW50cy9zaGFtaWFuYS88L2Rpdj5gKVswXTsKICAgICAgICAgICAgcG9wdXBfOWRmYmM3YjhjYTY1NDEyZDhjNzkyMGZmODg4YWIwMzAuc2V0Q29udGVudChodG1sX2ZjOTZlM2VmNjMxYTQ0MzViNWE3OTYxNTFiMzhiOTFkKTsKICAgICAgICAKCiAgICAgICAgY2lyY2xlX21hcmtlcl9kM2IzYzQxNTZiMTA0NTFkODJlNmZlMTc1ZjE2YTJmNS5iaW5kUG9wdXAocG9wdXBfOWRmYmM3YjhjYTY1NDEyZDhjNzkyMGZmODg4YWIwMzApCiAgICAgICAgOwoKICAgICAgICAKICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2M2ZGYwMTI1NmE3YTQzZDZhNzIxODg0MDhlNTMxOWFlID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbMjUuMjA0ODQ5MywgNTUuMjcwNzgyOF0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAicmVkIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogInJlZCIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogNSwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfN2Y2ODRiNmZiMTk0NDQyN2FmYTc3ZDU1NWU4ODRiOGYgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzJhNTIwZmMyODAxNDQ4Yjc5ODQ1MmQ2MTljMDZkYThlID0gJChgPGRpdiBpZD0iaHRtbF8yYTUyMGZjMjgwMTQ0OGI3OTg0NTJkNjE5YzA2ZGE4ZSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IDI4LiBraW5hcmEgYnkgdmlrYXMga2hhbm5hPGJyPlRlbGVwaG9uZTogKzk3MSA0IDgxNCA1NTU1PGJyPnVybDogaHR0cDovL3d3dy5raW5hcmFkdWJhaS5jb20vPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwXzdmNjg0YjZmYjE5NDQ0MjdhZmE3N2Q1NTVlODg0YjhmLnNldENvbnRlbnQoaHRtbF8yYTUyMGZjMjgwMTQ0OGI3OTg0NTJkNjE5YzA2ZGE4ZSk7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfYzZkZjAxMjU2YTdhNDNkNmE3MjE4ODQwOGU1MzE5YWUuYmluZFBvcHVwKHBvcHVwXzdmNjg0YjZmYjE5NDQ0MjdhZmE3N2Q1NTVlODg0YjhmKQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl81YzE1ZjEyZjJmNmE0MjRkYTU4MTA5NzM1ZjlhZmU4NiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjExMDgyMDIsIDU1LjEzOTkxODQwMDAwMDAxXSwKICAgICAgICAgICAgICAgIHsiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsICJjb2xvciI6ICJyZWQiLCAiZGFzaEFycmF5IjogbnVsbCwgImRhc2hPZmZzZXQiOiBudWxsLCAiZmlsbCI6IHRydWUsICJmaWxsQ29sb3IiOiAicmVkIiwgImZpbGxPcGFjaXR5IjogMC43LCAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsICJsaW5lQ2FwIjogInJvdW5kIiwgImxpbmVKb2luIjogInJvdW5kIiwgIm9wYWNpdHkiOiAxLjAsICJyYWRpdXMiOiA1LCAic3Ryb2tlIjogdHJ1ZSwgIndlaWdodCI6IDN9CiAgICAgICAgICAgICkuYWRkVG8obWFwXzM0NDUzNzdhZjMwNzQxMDk5ZTdlMmZiOWFhMTk4ZjM4KTsKICAgICAgICAKICAgIAogICAgICAgIHZhciBwb3B1cF8xODcxODRhNzJlOTc0ZTM4YWZiMzc5ZTQwYjdlZDM3MSA9IEwucG9wdXAoeyJtYXhXaWR0aCI6ICIxMDAlIn0pOwoKICAgICAgICAKICAgICAgICAgICAgdmFyIGh0bWxfYzRjMDY2NjM3MWE5NGU5MmI4NTQyZTFhZGI5OGJkZTkgPSAkKGA8ZGl2IGlkPSJodG1sX2M0YzA2NjYzNzFhOTRlOTJiODU0MmUxYWRiOThiZGU5IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaXRsZTogMjkuIGxpdHRsZSBtaXNzIGluZGlhPGJyPlRlbGVwaG9uZTogKzk3MSA0IDQ1NyAzNDU3PGJyPnVybDogaHR0cDovL3d3dy5mYWlybW9udC5jb20vcGFsbS1kdWJhaS9kaW5pbmcvbGl0dGxlLW1pc3MtaW5kaWEvPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwXzE4NzE4NGE3MmU5NzRlMzhhZmIzNzllNDBiN2VkMzcxLnNldENvbnRlbnQoaHRtbF9jNGMwNjY2MzcxYTk0ZTkyYjg1NDJlMWFkYjk4YmRlOSk7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfNWMxNWYxMmYyZjZhNDI0ZGE1ODEwOTczNWY5YWZlODYuYmluZFBvcHVwKHBvcHVwXzE4NzE4NGE3MmU5NzRlMzhhZmIzNzllNDBiN2VkMzcxKQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl82OWEzMWIxZDI2OTI0YTk2OWU1M2U1YzkyN2NkNmNkOSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjExMDM0NywgNTUuMjIwNjI4Mjk5OTk5OTldLAogICAgICAgICAgICAgICAgeyJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwgImNvbG9yIjogInJlZCIsICJkYXNoQXJyYXkiOiBudWxsLCAiZGFzaE9mZnNldCI6IG51bGwsICJmaWxsIjogdHJ1ZSwgImZpbGxDb2xvciI6ICJyZWQiLCAiZmlsbE9wYWNpdHkiOiAwLjcsICJmaWxsUnVsZSI6ICJldmVub2RkIiwgImxpbmVDYXAiOiAicm91bmQiLCAibGluZUpvaW4iOiAicm91bmQiLCAib3BhY2l0eSI6IDEuMCwgInJhZGl1cyI6IDUsICJzdHJva2UiOiB0cnVlLCAid2VpZ2h0IjogM30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfMzQ0NTM3N2FmMzA3NDEwOTllN2UyZmI5YWExOThmMzgpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwX2JkNjBkOWMyZTkwMDQ4MmY4ZjdlODMxMzVlYzQxNjFhID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF9hM2JkNWI3OGRlMzI0NmMzOGVmOTAwNmFkNzNhNWYxYyA9ICQoYDxkaXYgaWQ9Imh0bWxfYTNiZDViNzhkZTMyNDZjMzhlZjkwMDZhZDczYTVmMWMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRpdGxlOiAzMC4gZmlzaCBodXQgYXNtYWsgYWwgc3VsdGFuIHNlYWZvb2QgcmVzdGF1cmFudDxicj5UZWxlcGhvbmU6ICs5NzEgNTggMTI4IDI4ODY8YnI+dXJsOiBodHRwOi8vZHViYWlmaXNoaHV0cmVzdGF1cmFudC5jb20vaW5kZXgucGhwPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwX2JkNjBkOWMyZTkwMDQ4MmY4ZjdlODMxMzVlYzQxNjFhLnNldENvbnRlbnQoaHRtbF9hM2JkNWI3OGRlMzI0NmMzOGVmOTAwNmFkNzNhNWYxYyk7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfNjlhMzFiMWQyNjkyNGE5NjllNTNlNWM5MjdjZDZjZDkuYmluZFBvcHVwKHBvcHVwX2JkNjBkOWMyZTkwMDQ4MmY4ZjdlODMxMzVlYzQxNjFhKQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl82NzMyNWRmNWJmYzU0OWVjODM3MGExYzYxMjU5OGE3MCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzI1LjIwODI3MywgNTUuMjYwNjAxNV0sCiAgICAgICAgICAgICAgICB7ImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLCAiY29sb3IiOiAicmVkIiwgImRhc2hBcnJheSI6IG51bGwsICJkYXNoT2Zmc2V0IjogbnVsbCwgImZpbGwiOiB0cnVlLCAiZmlsbENvbG9yIjogInJlZCIsICJmaWxsT3BhY2l0eSI6IDAuNywgImZpbGxSdWxlIjogImV2ZW5vZGQiLCAibGluZUNhcCI6ICJyb3VuZCIsICJsaW5lSm9pbiI6ICJyb3VuZCIsICJvcGFjaXR5IjogMS4wLCAicmFkaXVzIjogNSwgInN0cm9rZSI6IHRydWUsICJ3ZWlnaHQiOiAzfQogICAgICAgICAgICApLmFkZFRvKG1hcF8zNDQ1Mzc3YWYzMDc0MTA5OWU3ZTJmYjlhYTE5OGYzOCk7CiAgICAgICAgCiAgICAKICAgICAgICB2YXIgcG9wdXBfMzQ4YTUzNTZmM2ZhNDA1Y2FjMmJlOWUzNjhjZjA3MmIgPSBMLnBvcHVwKHsibWF4V2lkdGgiOiAiMTAwJSJ9KTsKCiAgICAgICAgCiAgICAgICAgICAgIHZhciBodG1sXzNiZDQyNjc3MjFkODQ1OWFhOTQwNjY5MzdhM2QzYzQzID0gJChgPGRpdiBpZD0iaHRtbF8zYmQ0MjY3NzIxZDg0NTlhYTk0MDY2OTM3YTNkM2M0MyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGl0bGU6IFNwb25zb3JlZGNoaXZhbDxicj5UZWxlcGhvbmU6ICs5NzEgNCA0MDMgMzExMTxicj51cmw6IGh0dHA6Ly93d3cuY2hpdmFsbGF2aWxsZS5jb20vPC9kaXY+YClbMF07CiAgICAgICAgICAgIHBvcHVwXzM0OGE1MzU2ZjNmYTQwNWNhYzJiZTllMzY4Y2YwNzJiLnNldENvbnRlbnQoaHRtbF8zYmQ0MjY3NzIxZDg0NTlhYTk0MDY2OTM3YTNkM2M0Myk7CiAgICAgICAgCgogICAgICAgIGNpcmNsZV9tYXJrZXJfNjczMjVkZjViZmM1NDllYzgzNzBhMWM2MTI1OThhNzAuYmluZFBvcHVwKHBvcHVwXzM0OGE1MzU2ZjNmYTQwNWNhYzJiZTllMzY4Y2YwNzJiKQogICAgICAgIDsKCiAgICAgICAgCiAgICAKPC9zY3JpcHQ+ onload="this.contentDocument.open();this.contentDocument.write(atob(this.getAttribute('data-html')));this.contentDocument.close();" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>




```python

```


```python

```
