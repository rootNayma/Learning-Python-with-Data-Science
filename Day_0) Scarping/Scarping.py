
# ┌───────────────────────────────┐
# │          N  O  T  E           │
# │     only Run Clean Code       │
# └───────────────────────────────┘


# Usually the scraping is done in -3 Steps:

# 1).       Scrape/Fetching the website                                                  # Scrape = This means to download html code from the website using python, usually done by : "requests.get(url)" 

# 2).       Parse the website using Beautifulsoup                               # Parse  = This means to convert messy/unstructured html strings into structured object, so you can navigate it easily using beautifulsoup
                                                                                # BeautifulSoup lets you treat html like a tree, so you can search by -------- [ tags (<div>, <span>, etc.), classes, ids", etc ]-----
                                                                                # here this code [ soup = BeautifulSoup(resp.text, "html.parser ]
                                                                                # lets you do    [ quotes = soup.find_all("span", class_="text")]

# 3).       Extracting required information                                     # Extraction = This means you can pick the specific pieces of data you want (quotes, authors, links, etc.) and store them (in a list, dictionary, or CSV) 

###################################################################################################################################################################################################################################################


import requests      
from bs4 import BeautifulSoup

# Step 1). Fetching the website
url= "https://quotes.toscrape.com/"
response= requests.get(url, timeout=30)
print(response.text)


# Step 2). Parsing the response using beautifulsoup
soup = BeautifulSoup(response.text, "html.parser")                              # why we do parsing ??
                                                                                # python doesnt understand the html text/ strings that we got from fetching.
                                                                                # so, to make python undertand we do parsing using beautifulsoup.

                                                                                # here in this code we are calling beautifulsoup() and telling him: 

                                                                                # Hey, bs4 i have (response.text), now make python understand my html. 
                                                                                # Then ("html.parser") will make python understand the html strings/text.



# Step 3 : Extracting quotes and authors

quotes = soup.find_all("span", class_="text")                                   # soup.find_all() = will search for all the tags.
                                                                                # ("", class_="") = is selecting those objects.

                                                                                # <span class="text" itemprop="text">“The world as we have created it is a process of our thinking.
                                                                                # It cannot be changed without changing our thinking.”</span>

                                                                                # Here, you can see the object tag for quotes is span and class tag is text.



authors = soup.find_all("small", class_="author")                               # <small class="author" itemprop="author">Albert Einstein</small>
                                                                                #
                                                                                # And for Author it is small tag and class_ = author



for i in range(len(quotes)):                                                    # here, we are looping to extract whole data of Quotes and Author
                                                                                
                                                                                # for i in range (3):
                                                                                # but here we are doing range(len(quotes)):
                                                                                # here (len)= will get the integer value which is the quaniyt of quotes present in the page.

                                                                                
  print(f"{quotes[i].text} - {authors[i].text}")                                # f = is used for manully inputing values.
                                                                                # here we are doing "{qoutes.[i]}" = so we are using f

                                                                                # now what [i] does is = it will assing the number we got from (len)

                                                                                # for i in range (3):
                                                                                # print(f"{quotes[3].text} - {authors[3].text}")  

######################################################  C L E A N     C O D E  #################################################################################


import requests
from bs4 import BeautifulSoup

# Step 1). Fetching the website
url = "http://quotes.toscrape.com/"
response = requests.get(url)
#print(response.text)

# Step 2). Parsing the response using beautifulsoup
soup = BeautifulSoup(response.text, "html.parser")

# Step 3 : Extracting quotes and authors
quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")


for i in range(len(quotes)):
  print(f"{quotes[i].text} - {authors[i].text}")

