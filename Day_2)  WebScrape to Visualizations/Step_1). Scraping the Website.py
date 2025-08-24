import requests                                                                 # This will import all required library
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/catalogue/page-1.html"                        # This is setting url to get

r = requests.get(url, timeout=30)                                               # Like i said in pervious code it will get the url and store data in " r " and timeout does timer thing of 30 secs

print(resp)                                                                     # Prints

r.encoding = "utf-8"                                                            # now since, we requested data from the website, and data was stored inr " r "
                                                                                # r.encoding = "utf-8" will just converts all the raw data of r into readable data

                                                                                
soup = BeautifulSoup(r.text, "html.parser")                                     # Since now we converted the raw data into readable data with utf-8.
                                                                                # now here we use beautifulsoup to make that readable data into html data
                                                                                # .text =  will make sure the readable data is in string
                                                                                # html.parser = will make sure to covert the .text or the string into html formate

print(soup)



