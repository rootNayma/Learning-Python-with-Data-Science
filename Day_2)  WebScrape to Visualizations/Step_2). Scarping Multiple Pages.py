all_books=[]
for page in range(1,11):                                                        # in step 2) this is the only difference
                                                                                # here this code will run loop through every page 

                                                                                # so, how are we conncecting the loop code with the website ??
                                                                                # answer is the "page"
                                                                                # ------for "page" in range(1,11): -------
                                                                                # urls = f"https://books.toscrape.com/catalogue/page-{page}.html"

                                                                                # for "page" is connceted to urls "{page}"
                                                                              
                                                                          
                                                                                


  urls = f"https://books.toscrape.com/catalogue/page-{page}.html"               # from here all code are same as of step 1) scarping the website
  print(urls)

  
  resp = requests.get(urls, timeout=30)
  resp.encoding = "utf-8"
  soup = BeautifulSoup(resp.text, "html.parser")

  for art in soup.select("article.product_pod"):
    title = art.h3.a["title"]
    price_text = art.select_one("p.price_color").text.strip()
    price = float(price_text.replace("£",""))
    rating_class = art.p["class"][1]
    stars_map = {"One":1, "Two":2, "Three":3, "Four":4, "Five":5}
    stars = stars_map[rating_class]
    all_books.append({"title":title, "price":price, "Stars":stars})

print(all_books)
