
# ┌───────────────────────────────┐
# │          N  O  T  E           │
# │     only Run Clean Code       │
# └───────────────────────────────┘

# For each quote you already collected, follow its author’s link (e.g. the href from block.find("a"))
# On each author page, scrape birth date and birth location (both are in <span class="author-born-date"> and <span class="author-born-location">).
# Append these two new fields to your existing CSV of quotes.


import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Fetching from main page                                                                
url = "http://quotes.toscrape.com/"                                             
response = requests.get(url, timeout=30)                                        # here we are downloding data from the page
soup = BeautifulSoup(response.text, "html.parser")                              # html.parser is making pyhthon understand the html code.

# Step 2: Extracting quotes and authors
quotes = soup.find_all("span", class_="text")                                   # going through the <span> tag and selecting quotes/text from <class>
authors = soup.find_all("small", class_="author")                               # going through the <small> tag and selectng author name/author from <class>

book = []                                                                       # book = [] is likey a empty drawer where we will keep data later. empty list

for i in range(len(quotes)):                                                    # for i in = is looping
                                                                                # range(len(quotes)) = len(quotes) is giving us a int value. which will be total loop for all quotes and author
  
  
    q = quotes[i].text                                                          # here we are converting quotes into text.
                                                                                # why not --- quotes = soup.find_all("span", class_="text").text
                                                                                # beacuse python cant do .text operation on list, python needs something like a box which is q and a here
    
    a = authors[i].text                                                         # .text = is converting quotes and quthors into text 
                                                                                # [i] = is looping all quotes nad authors  


    # Step 3: Getting author link from the main page
    block = soup.find_all("div", class_="quote")[i]                             # now here it looking through whole page <div> tag which have all info about author and quote
                                                                                # [i] = loop ith time

    author_href = block.find("a")["href"]                                       # it is slecting the link --- <a href="/author/Albert-Einstein">(about)</a>
    author_url = f"http://quotes.toscrape.com{author_href}"                     # here we are f"{....}" for the link which is author_href 

    # Step 4: Fetching author page
    A_response = requests.get(author_url, timeout=30)                           # same as before= but now it is downloading data of author page
    author_soup = BeautifulSoup(A_response.text, "html.parser")

    # Step 5: Geting birthday and birthplace info
    bday = author_soup.find("span", class_="author-born-date").text             # same as before but now for author page
    loc = author_soup.find("span", class_="author-born-location").text


    # Step 6: Appending to list which is book
    book.append({                                                               # remember we talked about empty drawer
        "Quotes": q,                                                            # now it comes in hand we all put all these value inside the book drawer
        "Authors": a,                                                           #.append= is addding data into empty list
        "Birthday": bday,
        "Birth_Place": loc                                                      # also by doing this  ( "____" : _____) we are making it ready to make dataframe
    })                                                                          # what is dataframe???
                                                                                # It is a way of organzing data in clean form like a table. think of sql table
#print(book)
# Step 7: Convert to DataFrame
books_df = pd.DataFrame(book)                                                   # pd.DataFrame() = converting book into dataframe (pd is for panda )


books_df.to_csv("author_profile_extraction_nyamasang.csv", index=False)         # making whole code into csv file.


print(books_df)                                                                 # finally print !!!!!




##################################################################   C L E A N    C O D E  ###################################################################### 


import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://quotes.toscrape.com/"
response = requests.get(url, timeout=30)
soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")

book = []

for i in range(len(quotes)):
    q = quotes[i].text
    a = authors[i].text

    block = soup.find_all("div", class_="quote")[i]
    author_href = block.find("a")["href"]
    author_url = f"http://quotes.toscrape.com{author_href}"

    A_response = requests.get(author_url, timeout=30)
    author_soup = BeautifulSoup(A_response.text, "html.parser")

    bday = author_soup.find("span", class_="author-born-date").text
    loc = author_soup.find("span", class_="author-born-location").text

    book.append({
        "Quotes": q,
        "Authors": a,
        "Birthday": bday,
        "Birth_Place": loc
    })

books_df = pd.DataFrame(book)
books_df.to_csv("author_profile_extraction_name001.csv", index=False) 
print(books_df)




