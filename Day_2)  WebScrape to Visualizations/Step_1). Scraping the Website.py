  

# ┌───────────────────────────────┐
# │          N  O  T  E           │
# │     only Run Clean Code       │
# └───────────────────────────────┘




import requests                                                                 # This will import all required library
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/catalogue/page-1.html"                        # This is setting url to get

resp = requests.get(url, timeout=30)                                               # Like i said in pervious code it will get the url and store data in " req " and timeout does timer thing of 30 secs

#print(req)                                                                     # Prints

resp.encoding = "utf-8"                                                            # now since, we requested data from the website, and data was stored inr " req "
                                                                                # r.encoding = "utf-8" will just converts all the raw data of req into readable data


soup = BeautifulSoup(req.text, "html.parser")                                     # Since now we converted the raw data into readable data with utf-8.
                                                                                # now here we use beautifulsoup to make that readable data into html data
                                                                                # .text =  will make sure the readable data is in string
                                                                                # html.parser = will make sure to covert the .text or the string into html formate

#print(soup)



books = []                                                                      # This is just like a empty drawer,, later we will put data inside it


for art in soup.select("article.product_pod"):                                  # Here, this i a loop which will find all the books which is under "article.product_pod"
                                                                                # for art in soup.select = loops through whole books
                                                                                # soup.select = whill select

  title = art.h3.a["title"]                                                     # art is loop here
                                                                                # .h3.a = is a path where "title" of books are contained.

  #books.append(title)                                                           # .append(title) = is sending data and putting it on the empty drawer we created here """"books = []""""

  #price = art.select_one("p.price_color")                                      # .select_one= is selecting one value tag, here its p tag
                                                                                # now you may ask why didnt we do "".select""" like before, we didnt because .select will select whole tag.
                                                                                # and if we do "".select" we have to manully do indexing which is time consuming, so
                                                                                # "p.price_color" = is a path where price is contained.

                                                                                # now only doing this ---- price = art.select_one("p.price_color") ----
                                                                                # will only select the price tag. like code will say " hey i caught the price tag, now what should i do ?"
                                                                                # then comes the ---.text.strip()--- part


  price_text = art.select_one("p.price_color").text.strip()                          # .text.strip()= after selecting the p.price_color tag.
                                                                                # .text = will say  " hey .select_one now covert those price into text"
                                                                                # .strip() = will remove any space in our case here ---- <p class="price_color"£51.77</p>
                                                                                # ""£51.77"" there is no space it is clean though we used .strip()
                                                                                # because it is a good habit to do .strip(), so


  price= float( price_text.replace("£", ""))                                    # here we are replacing "£" with a space
                                                                                # also you may ask why use float, aint our motive was to replace £ sign.
                                                                                # we are using float because from the above code it is still in text format
                                                                                # and we cant do math on it because python sees it as string or text,
                                                                                # so, we use float or you can do extra steps here

                                                                                # price_replace = price_text.replace("£", "")

                                                                                # price_float= float(price_replace)
                                                                                # price = price_float


  #books.append(price)                                                           # .append = put data into empty drawer


  rating_class= art.p["class"][1]                                               # art.p= will select tag inside it, which is class.
                                                                                # ["class"] = it will go inside the class it selects class
                                                                                # [1] = beacuse it will select only the ratings.
                                                                                # if it was only ---  rating_class= art.p["class"] -----
                                                                                # then it would print whole thing the class and the ratings too,
                                                                                # something like ['star-rating', 'Three']


  stars_map = {"One":1, "Two":2, "Three":3, "Four":4, "Five":5}                 # now here we are doing this code because the ratings stars are in string so,
                                                                                # we are assinning the integer value to each.
                                                                                # you may aslo ask why not just use flot(), or int() like we used it before in price tag
                                                                                # float() or int() works only if the string looks numeric (like "51.77").
                                                                                # so, "Three" is not numeric


  stars = stars_map[rating_class]                                               # here we are just store values in the starts,
                                                                                # 1) art.p["class"] → gives you a list of classes (e.g. ["star-rating", "Three"]).
                                                                                # 2) art.p["class"][1] → picks the second item ("Three").
                                                                                # 3) stars_map[rating_class] → looks up "Three" in the dictionary → returns 3.
                                                                                # 4) That value is stored in stars.
                                                                              
  #books.append(stars)

  books.append({"title":title, "price":price, "Stars":stars})

print(books)


##############################################                C L E A N    C O D E            ############################################## 



import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/catalogue/page-1.html"
resp = requests.get(url, timeout=30)
print(resp)
resp.encoding = "utf-8"
soup = BeautifulSoup(resp.text, "html.parser")

books = []
for art in soup.select("article.product_pod"):
  title = art.h3.a["title"]
  price_text = art.select_one("p.price_color").text.strip()
  price = float(price_text.replace("£",""))
  rating_class = art.p["class"][1]
  stars_map = {"One":1, "Two":2, "Three":3, "Four":4, "Five":5}
  stars = stars_map[rating_class]
  books.append({"title":title, "price":price, "Stars":stars})


