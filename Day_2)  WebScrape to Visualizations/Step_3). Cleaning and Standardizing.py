

# ┌───────────────────────────────┐
# │          N  O  T  E           │
# │     only Run Clean Code       │
# └───────────────────────────────┘



import pandas as pd


books_df = pd.DataFrame(all_books)                                              # here pd.DataFrame(all_books) = is making a dataframe called books_df
                                                                                # it is calling all the data of perivous data
                                                                                # what is dataframe??
                                                                                # it is like a structed tablur form of data, you can assume it as sql table.


per_star = books_df.groupby("Stars").Price.mean()                               # df.groupby = is grouping the dataframe with Stars
                                                                                # all books with Stars = 1 → one group, Stars = 2 → another group, etc

                                                                                # | Stars | title  | price |
                                                                                # | ----- | ------ | ----- |
                                                                                # | 1     | Book A | 10    |
                                                                                # | 1     | Book B | 20    |
                                                                                # | 2     | Book C | 15    |
                                                                                # | 2     | Book D | 25    |

                                                                                # .Price = will slecte Price column.
                                                                                # .mean() = will find mean of Price column.
                                                                                # like,

                                                                                # | Stars | price.mean()   |
                                                                                # | ----- | -------------- |
                                                                                # | 1     | (10+20)/2 = 15 |
                                                                                # | 2     | (15+25)/2 = 20 |


print(per_star)

##########################################################  C L E A N     C O D E  ######################################################################3

import pandas as pd

books_df = pd.DataFrame(all_books)
per_star = books_df.groupby("Stars").Price.mean()
print(per_star)
