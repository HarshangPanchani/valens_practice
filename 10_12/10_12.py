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

# data= pd.read_csv('data.csv')
# # print(data.head().to_string()) #use to_string() to print the entire DataFrame.   
# print(data.to_string())
# # data.to_csv('new_data.csv',mode='a', index=False, header=True)
# for index, row in data.iterrows():
#     print(index, row['Duration'], row['Pulse'], row['Calories'])


# data= pd.read_json('data.json')
# print(data.to_string()) 
# print(type(data))

# data.to_json('new_data.json',orient='records',indent=4)
# data2= pd.read_json('new_data.json')
# new_data=[{
#         "Duration":124,
#         "Pulse":124,
#         "Maxpulse":124,
#         "Calories":124.4
#     }]
# data3= pd.DataFrame(new_data)
# print(data3.to_string())
# pd_combined=pd.concat([data2,data3],ignore_index=True)
# print(pd_combined.to_string())
# pd_combined.to_json('new_data.json',orient='records',indent=4)
# print(data2.to_string()) 

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

#add column in dataframe
# sum=[3,7,11,15,19]
# mul=[2,12,30,56,90]

# val['sum']=sum
# val['mul']=mul
# print(val) 

#add column in dataframe using assign

# val= val.assign(sum=[x.a+x.b for x in val.itertuples()])
# val= val.assign(mul=[x.a*x.b for x in val.itertuples()])

# print(val)
# for x in val.itertuples():
#     print(x.a)


#map to add according to some column same like inner join in sql
# name=['harshang','meet','smit','kishan','tirth']
# val['name']= name
# print(val)

# marks={'harshang': 95, 'meet': 85,  'kishan': 80,'smit': 90, 'tirth': 75}
# val['marks']=val['name'].map(marks)
# print(val)

#add multiple columns
# print(val)
# data2= {
#     'a1':[1,3,5,7,9],
#     'b2':[2,4,6,8,10]
# }
# val=val.assign(**data2)
# print(val)

# name=['harshang','meet','smit','kishan','tirth']
# val.insert(1,'name',name) # must have to specify the location index to insert like 0,1,2,...
# print(val)

# val.loc[val['a']>5,'c']= 'greater than 5'
# val.loc[val['a']<=5,'c']=' less than or equal to 5'
# print(val)
# val2=val.drop('c',axis=1)
# val2=val.drop(columns=['a','c'],axis=1)
# print(val2)


#threashhold method to drop column to remove null values
# val.loc[val['a']>5,'c']= 'greater than 5'
# val.loc[val['a']<=5,'c']=None

# print(val)
# ths=len(val)*0.4
# print(ths)
# val2= val.dropna(thresh=ths,axis=1)
# print(val2)




# val=pd.DataFrame(data,index=["level1","level2","level3","level4","level5"])
# print(val)
# print(val.loc['level2'])
# print(val.loc[['level2','level4']])

# print(pd.options.display.max_rows)  


# a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# a=[20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
# a=['apple','banana','grape','orange','mango','kiwi']
# sum= lambda x:x+20
# print(sum(10))

# ab=list(map(lambda x: (x[0]+1)*x[1],enumerate(a)))
# print(ab)

# ab=list(filter(lambda x: x>8,a))
# print(ab)

# ab= list(sorted(a, key= lambda x: len(x)))
# print(ab)
# ab= list(sorted(a, key= lambda x: x[0]))
# print(ab)

