

# ┌───────────────────────────────┐
# │          N  O  T  E           │
# │     only Run Clean Code       │
# └───────────────────────────────┘



# Using your list of quotes, compute the length (in characters) of each quote text.
# Add a new CSV column length.
# Report which quote is the shortest and which is the longest.


# Here everything is same as Authot_Profile_Extraction
# Only we have to find longest quotes and the shortest, so




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
    location = author_soup.find("span", class_="author-born-location").text

    book.append ({
        "Quotes": q,
        "Authors": a,
        "Birthday": bday,
        "Birth_Place": location,
        "Length" : len(q)                                                       # here we are appending the length of q which is Quotes.
    })                                                                          # len() = finds out the length of quotes,
                                                                                
                                                                                # Now, we need to assign this and find which is longest and shortest.
                                                                                # we did that in below:

books_df = pd.DataFrame(book)

shortest_quote = books_df.loc[books_df['Length'].idxmin()]                      # .loc = will give information from the passed string here it is "Length" 
                                                                                # .idxmin() = will give minimum integer value from Length 

longest_quote  = books_df.loc[books_df['Length'].idxmax()]                      # same but here it will give maxium value



print("Shortest Quote:")
print(shortest_quote)

print("\nLongest Quote:")
print(longest_quote)


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
    location = author_soup.find("span", class_="author-born-location").text

    book.append({
        "Quotes": q,
        "Authors": a,
        "Birthday": bday,
        "Birth_Place": location,
        "Length": len(q)
    })

books_df = pd.DataFrame(book)

shortest_quote = books_df.loc[books_df['Length'].idxmin()]
longest_quote = books_df.loc[books_df['Length'].idxmax()]

print("Shortest Quote:")
print(shortest_quote)

print("\nLongest Quote:")
print(longest_quote)




