
launches = launches[["name", "success", "date_utc", "flight_number"]].copy[]   # ok, so here we are using.copy[] beacuse we dont want to over write the orginal dataframe so.
""" This part is also called as cleaning because we are selecting manually which comlumns to add"""

launches["data_utc"] pd.to_datatime(launches["data_utc"], errors = "coerce") 
""""we did pd.to_datatime beacuse in json data. there will be mostly a 'string' value even the date even. And python cant do operation on string treating it as date so we converted json date into py date""""
# also to remind pandas works from right to left. first it changes the value by pd.to_datatime(launches["data_utc"].  Then it stores ir in left side launches["data_utc"]
# Though we can also do """" launches["data_utc_copy"]""""
"""" Another, we did errors = coerce because the data might have null value i mean a null date. which will give error so to solve that we used errors = coerce. Its better than nothing or its better than an error.""""

launches["year"] lauches["date_utc"].dt.year # here we did dt.year to extract year from the date. 
""""dt.year, dt.month, dt.day, dt.hour,etc. we can do as we wanted to extract.""""

launches["success_copy"] lauches["success"].fillna(False).astype(bool) # here success column contains boolen value so
"""" what .fillna(False) does is it will replace all null or nan values into false, 
     and .astype(bool) will forcefully make all the value into boolean.
     
     Now you may ask we already did .fillna(False) then why need of .astype
     so, even though we did make null values into false it may get stored as object not a pure boolean just like we did in date_utc where it was store in string not datetime.
     so, like i said even though we conevertrd it into false it will store it as object not boolean,
     and to make it boolean we forcefully do .astype(bool)""""
print(launches)


"""""""""""""""""""""""""""""""""""""""""""   C L E A N     C O D E   """"""""""""""""""""""""""""""""""""""""""" 


launches = launches [["name", "date_utc", "success", "flight_number"]].copy()
launches["date_utc"] = pd.to_datetime(launches["date_utc"], errors = "coerce")
launches["year"] = launches["date_utc"].dt.year
launches["success_copy"] = launches["success"].fillna(False).astype(bool)
print(launches)




  
