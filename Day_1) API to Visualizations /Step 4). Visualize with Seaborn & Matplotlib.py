

# ┌───────────────────────────────┐
# │          N  O  T  E           │
# │     only Run Clean Code       │
# └───────────────────────────────┘




import seaborn as sns
import matplotlib.pyplot as plt

plt.figure()                                                  # plt.figure() = only creates a empty graph which we will fill with data later

sns.barplot(data=per_year, x= "year",  y= "launches")         # this will fill the graph with year and lauches which we extracted in previous code
                                                              # x = year like 2006,2007,etc
                                                              # y = lauches. which we supposed 3 falcon_001, falcon_T32, falcon_zx in previous code

plt.title("Space X launches per year")                        # plt.title() = give a heading or a title to our graph

plt.xticks(rotation=45)                                       # plt.xticks() = control x axis like we passed rotation =45
                                                              # it will rotate year text by 45 degree, so it doesnt collapse with eachother
                                                            

                            
plt.show()                                                    # plt.show() is just like the print function, it will show the result,






##############################################                C L E A N    C O D E            ############################################################



import seaborn as sns
import matplotlib.pyplot as plt

plt.figure()
sns.barplot(data=per_year, x="year", y="launches")
plt.title("SpaceX Launches per Year")
plt.xticks(rotation=45)
plt.show()
