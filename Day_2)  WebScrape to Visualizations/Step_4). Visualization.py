import seaborn as sns
import matplotlib.pyplot as plt

sns.boxplot(data=books_df, x="Stars", y="Price")                                # sns.boxplot = creates a graph like a box
                                                                                # data = is a part of syntax of seaborn,
                                                                                # it says like" hey im data collector of seaborn, from where should i get the data??""

                                                                                # x= Stars, y=Price


plt.title("Book Prices by Rating")                                              # plt.title = it will make a heading, a title at the top of graph

plt.show()                                                                      # prints
