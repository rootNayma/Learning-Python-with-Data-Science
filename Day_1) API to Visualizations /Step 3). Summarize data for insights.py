
# ┌───────────────────────────────┐
# │          N  O  T  E           │
# │     only Run Clean Code       │
# └───────────────────────────────┘



import numpy as np
 
#per_year = launches.groupby("year")   # here we are trying to groupby year but,
                                      # if i run this it will only give 
                                      #=== pandas.core.groupby.generic.DataFrameGroupBy object at 0x7a3184a38440 ===#
                                      # why beacuse we havent really gave any aggregation like sum(), count(), mean(), min(), etc.
                                      # so,


per_year = launches.groupby("year").agg(
    launches=("name","count"),
    successes=("success_copy", "sum")
)                                           #now when we run this you may think its fine and there is no error which is fine but
                                            # it will give no any index and we cant operate data in future.
                                            # so, best practice is to give index so we can manupilate data in future.



per_year = launches.groupby("year").agg( 
    launches=("name","count"),              # here we are counting names suppose falcon_001, falcon_T32, falcon_zx.
                                            # which will give value 2 which is equal to lauches.  
                                            # launches = name = 3
                                            # launches = 3
    


    successes=("success_copy", "sum")       # here we are suming success which is a bool value True or False.
                                            # so, it will be whether true or false
                                            # suppose, if there was True, True, False
                                            # success= 2,

                                            # Therefore,  amoung 3 launches only 2 rockets were successfully flew.
                                            
).reset_index()                                



per_year["success_rate"] = per_year["successes"]/per_year["launches"]    #here we are finding suceesrate, we have alredy counted and sum launches and success
                                                                         # which we supposed launches = 3, success = 2
                                                                         # success / launches
                                                                         # 2 / 3 = 0.666
                                                                         # 66.6 % success_rate

print(per_year)





##############################################                C L E A N    C O D E            ############################################## 




import numpy as np

per_year = launches.groupby("year").agg(
    launches=("name","count"),
    successes=("success_copy", "sum")
).reset_index()
per_year["success_rate"] = per_year["successes"]/per_year["launches"]
