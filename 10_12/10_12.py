# try:
#     print(2/0)
 
# except IndexError as e:
#     print(" except that An error occurred:", e)
   
# # except ZeroDivisionError as e:
# #     print(" except that A division by zero occurred:", e)
# else:
#     print(" else. no error occurred in try block. if error occurred and also handled by except block else block will be skipped")    
# finally:
#     print("finally.")

# print("This line won't execute if there is an unhandled exception above. and error was there")

# # print("finally executes whether an exception occurs or not. but above line skips the execution if the error was not handled ")

import pandas as pd

data= pd.read_csv('data.csv')
# print(data.head().to_string()) #use to_string() to print the entire DataFrame.   
print(data.info())


# data= pd.read_json('data.json')
# print(data.to_string()) 
# print(type(data))

# data={
#     'name':{'0':'harshang','1':'meet','2':'smit'},
#     'age':{'0':20,'1':21,'2':21},
#     'ctc':{'0':3.5,'1':5.5,'2':12}
# }
# df=pd.DataFrame(data)
# print(df.to_string())



# a= [1,7,2]
# val= pd.Series(a,index=['p','q','r'])
# val= pd.Series(a)
# print(val['p'])
# print(val)

# val2= pd.Series({'x':10,'y':20,'z':50})
# print(val2)

# calories = {"day1": 420, "day2": 380, "day3": 390}
# myvar = pd.Series(calories, index = ["day1", "day2"])
# print(myvar)


# data= {
#     'a':[1,3,5,7,9],
#     'b':[2,4,6,8,10]
# }
# val= pd.DataFrame(data)
# print(val)
# print(val.loc[0])
# print(val.loc[[0,1]])

# val=pd.DataFrame(data,index=["level1","level2","level3","level4","level5"])
# print(val)
# print(val.loc['level2'])
# print(val.loc[['level2','level4']])

# print(pd.options.display.max_rows)  