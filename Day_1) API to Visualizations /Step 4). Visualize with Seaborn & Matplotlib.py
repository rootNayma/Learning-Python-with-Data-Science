

# ┌───────────────────────────────┐
# │          N  O  T  E           │
# │     only Run Clean Code       │
# └───────────────────────────────┘




import seaborn as sns
import matplotlib.pyplot as plt

plt.figure()                                                  # plt.figure() = only creates a empty graph which we will fill with data later

sns.barplot(data=per_year, x= "year",  y= "launches")         # sns.barplot() = a bargraph like a building graph, like we learned at schools
                                                              # this will fill the graph with year and lauches which we extracted in previous code
                                                              # x = year like 2006,2007,etc
                                                              # y = lauches. which we supposed 3 falcon_001, falcon_T32, falcon_zx in previous code



plt.title("Space X launches per year")                        # plt.title() = give a heading or a title to our graph


plt.xticks(rotation=45)                                       # plt.xticks() = control x axis like we passed rotation =45
                                                              # it will rotate year text by 45 degree, so it doesnt collapse with eachother
                                                            

                            
plt.show()                                                    # plt.show() is just like the print function, it will show the result,






#################################################################  Another Example  #######################################################333############





import seaborn as sns
import matplotlib.pyplot as plt

plt.figure()                   
sns.lineplot(data=per_year, x="year", y="success_rate", marker="o")       # sns.lineplot() = line graph, only lines
                                                                          # "data=" here is a part of syntax of seaborn, dont be confused with it as variable
                                                                          # the per_year we did was on pandas not seaborn, 
                                                                          # so seaborn doesnt understand per_year and be like 'what bruh what per-year get me a translator'
                                                                          # and we give 'data =' which works like a translator converts pandas's per_year into seaborn's per_year



plt.title("SpaceX Success Rate per Year")                                 # same as before just gives a title


plt.ylabel("Success Rate")                                                # plt.y/xlabel() = labeling or giving name to axis
                                                                          # you may ask, but we alredy did gave them name in here - sns.lineplot(data=per_year, x="year", y="success_rate", marker="o")
                                                                          # but no in "y=success_rate"   we are just grabing the data not naming it,
                                                                          # though even if we didnt label them it will label it by default as it grabs the data
                                                                          # thats why we left x axis without labeling for clear understanding 
                                                                        

plt.ylim(0,1)                                                             # plt.y or x lim() = limits the axis, her we are limiting y axis by o to 1 only.  no less, not more.

plt.xticks(rotation=45)                                                   # just like before it just rotates x or y axis

plt.show()                                                                # shows




##############################################                C L E A N    C O D E    (1)           ############################################################

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure()
sns.barplot(data=per_year, x="year", y="launches")
plt.title("SpaceX Launches per Year")
plt.xticks(rotation=45)
plt.show()

##############################################                C L E A N    C O D E    (2)          ############################################################


import seaborn as sns
import matplotlib.pyplot as plt

plt.figure()
sns.lineplot(data=per_year, x="year", y="success_rate", marker="o")
plt.title("SpaceX Success Rate per Year")
plt.ylabel("Success Rate")
plt.ylim(0,1)
plt.xticks(rotation=45)
