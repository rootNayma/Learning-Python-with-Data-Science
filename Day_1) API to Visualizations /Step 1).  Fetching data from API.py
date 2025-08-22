# This course was provided by Dlytica and taught by sir. Subhan Singh Karki. 
# so lets get started right into the codes.


""" first we need to install some libraries """
! pip install numpy pandas seaborn matplotlib requests lxml beautifulsoup4   # ok, so here this line will install all the required libraries

import requests
import pandas as pd

URL = " https://api.spacexdata.com/v4/launches "     # so this api was provided by our sir SSK, maybe we needed some site to get raw data.
r = requests.get(URL, timeout = 30)          # here we are requesting and telling url. """ excuse me sir can i have your data. and then we are storing it into variable- r """
                                            """ Also we did timeout=30, this is kind of timer if the requests is not responded by 30 secs it will terminate"""


"""print(r.json(r)"""                             """This is optional just to clarify if we do this it will fetch all the data from the url but it is unreadable json data"""
data = r.json()                                    #SO, to encunter that issue, we convert it into more readable format, where pandas lib comes in hand. pd.json_normalize.
launches = pd.json_normalize(data)


print(launches)                                #it will show all data
print(len(launches))                           # it will only show length or data
print(launches.columns)                        # it will only show columns





"""""""""""""""""""""""""""""""""""""""""""""" CLEAN CODE """""""""""""""""""""""""""""""""""""""""""""" 

import requests 
import pandas as pd

URL = "https://api.spacexdata.com/v4/launches"

r= requests.get(URL, timeout = 30)
data = r.json()

launches = pd.json_normalize(data)
print(launches)
print(len(launches))
print(launches.columns)
