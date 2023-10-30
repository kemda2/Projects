####################################################################################################
################################################## Python for Data Analysis: Reading and Writing Data
####################################################################################################
# import pandas as pd
# import numpy as np

# series=pd.Series(data=[2,3,5,4],
#                  index=['a','b','c','d'])

# dictionary={'x':2,'a':5,'b':4,'c':8}
# series2=pd.Series(dictionary)

# series['a'] 2
# series[0] 2
# series[1:3]
# series3 = series+series2 # a     7.0, b     7.0,c    13.0,d     NaN,x     NaN (not a number)
# print(np.mean(series)) # 3.5

# dictionary2={
#     'name':['Joe','Bob','Frans'],
#     'age':np.array([10,15,20]),
#     'weight':(75,123,239),
#     'height':pd.Series([4.5,5,6.1],
#     index=['Joe',"Bob","Frans"]),
#     "siblings":1,
#     'gender':"M"    
# }

# df=pd.DataFrame(dictionary2)

# print(df)

# dictionary2={
#     'name':['Joe','Bob','Frans'],
#     'age':np.array([10,15,20]),
#     'weight':(75,123,239),
#     'height':[4.5,5,6.1], # indexsiz hali
#     "siblings":1,
#     'gender':"M"    
# }

# df=pd.DataFrame(dictionary2)

# print(df)




# dictionary2={
#     'name':['Joe','Bob','Frans'],
#     'age':np.array([10,15,20]),
#     'weight':(75,123,239),
#     'height':[4.5,5,6.1], # indexsiz hali
#     "siblings":1,
#     'gender':"M"    
# }

# df=pd.DataFrame(dictionary2,index=dictionary2['name']) # index data frame oluştururken belirlendi.

# dictionary2={
#     'name':['Joe','Bob','Frans'],
#     'age':np.array([10,15,20]),
#     'weight':(75,123,239),
#     'height':[4.5,5,6.1], # indexsiz hali
#     "siblings":1,
#     'gender':"M"    
# }

# df=pd.DataFrame(dictionary2)

# print(df['weight']) # print(df.weight)



# dictionary2={
#     'name':['Joe','Bob','Frans'],
#     'age':np.array([10,15,20]),
#     'weight':(75,123,239),
#     'height':[4.5,5,6.1], # indexsiz hali
#     "siblings":1,
#     'gender':"M"    
# }

# df=pd.DataFrame(dictionary2,index=dictionary2['name'])

# del df['name']




# dictionary2={
#     'name':['Joe','Bob','Frans'],
#     'age':np.array([10,15,20]),
#     'weight':(75,123,239),
#     'height':[4.5,5,6.1], # indexsiz hali
#     "siblings":1,
#     'gender':"M"    
# }

# df=pd.DataFrame(dictionary2,index=dictionary2['name'])

# df['IQ']=[130,105,115]
# df['Married']=False
# # df.loc['Joe']

# # print(df.loc['Joe']) 

# # print(df.loc['Joe','IQ']) # direk john'un IQ sunu verir
# # print(df.loc['Joe':'Bob','height':'IQ']) # aralık verir
# # print(df.iloc[0]) # 0. satır
# # print(df.iloc[0,5]) # 0. satır 5.sütunu verir
# # print(df.iloc[0:2,5:8]) # 0-2. satır 5-8.sütunu verir

# # boolean_index=[False,True,True]
# # print(df[boolean_index]) # ilk satırı almaz ikinci ve üçüncü satırı alır

# # boolean_index=df['age']>12
# # print(df[boolean_index]) # yaşı 12 den büyük olanları gösterir


# print(df[df['age']>12]) # yaşı 12 den büyük olanları gösterir


# titanic_train=pd.read_csv("D:/Kısayol/Projects/ana/Projects/train.csv")
# # print(type(titanic_train)) # <class 'pandas.core.frame.DataFrame'>
# # print(titanic_train.shape) # (5, 1)
# # print(titanic_train.head) # ilk 5 satır
# # print(titanic_train.tail) # son 5 satır

# # titanic_train.index=titanic_train['Name']
# # del titanic_train['Name']
# # print(titanic_train.index[0:10])

# # print(titanic_train.columns) # sütun adlarını veriyor
# # print(titanic_train.describe) # ilk 6 satırın özeti toplam ortalama gibi
# # print(np.mean(titanic_train,axis=0)) # her numara içeren sütunun açıklaması
# print(titanic_train.info) # her numara içeren sütunun açıklaması



# import os
# import pandas as pd
# print(os.getcwd()) #py dosyasının olduğu yeri veriyor
# os.chdir('D:/Kısayol/')
# print(os.getcwd())
# print(os.listdir('D:/Kısayol/Projects')) # Klasörün içindeki dosyaları listeliyor

# print(pd.read_csv('D:/Kısayol/Projects/train.csv'))


####################################################################################################
################################################## Python for Data Analysis: Control Flow (if, else, for, while)
####################################################################################################

# import numpy as np

# numbers=np.random.uniform(-1,1,25)
# numbers=np.where(numbers<0,0,numbers) # negatif sayıları sıfır yaptı
# print(numbers)

####################################################################################################
################################################## Python for Data Analysis: Functions
####################################################################################################

# def sum_many_args(*args):
#     print(type(args))
#     print(sum(args))
#     return(sum(args))

# sum_many_args(1,2,3,4,5,6)

# def sum_keywords(**kwargs):
#     print(type(kwargs))
#     print(sum(kwargs.values()))
#     return(sum(kwargs.values()))

# sum_keywords(Mynum=12,Yournum=13) 

# import numpy as np

# def rmse(predicted,targets):
#     print(np.sqrt(np.mean(targets-predicted)**2))
#     return(np.sqrt(np.mean(targets-predicted)**2))

# rmse(40,20)


# my_func=lambda x,y: x+y

# print(my_func(5,10))




# def square(x):
#     return x**2

# my_map = map(square,[1,2,3,4,5]) fonksiyonu map a taşıdık

# for item in my_map:
#     print(item)



# my_map=map(lambda x: x**2,[1,2,3,4,5])
# for item in my_map:
#     print(item)


####################################################################################################
################################################## Python for Data Analysis: List Comprehensions
####################################################################################################


# my_list=[number for number in range(0,101)] # append yerine

# print(my_list)



# my_list=[number for number in range(0,101) if number%2==0] # append yerine ve if i içine alma

# print(my_list)


# combined = [a + b for a in 'life' for b in 'study'] # ['ls', 'lt', 'lu', 'ld', 'ly', 'is', 'it', 'iu', 'id', 'iy', 'fs', 'ft', 'fu', 'fd', 'fy', 'es', 'et', 'eu', 'ed', 'ey']

# print(combined)
  
  
# nested = [letters[1] for letters in [a + b for a in 'life' for b in 'study']]

# print(nested)


# words=['life', 'is', 'study']
# word_len_dict={}
# for word in words:
#     word_len_dict[word]=len(word)
# print(word_len_dict)

# # Easy way
# words=['life', 'is', 'study']
# word_len_dict={word:len(word) for word in words}
# print(word_len_dict)



# words=['life', 'is', 'study']
# word_lenghts=[4,2,6]
# pairs = zip(words,word_lenghts)
# for pair in pairs:
#     print(pair)


# words=['life', 'is', 'study']
# word_lenghts=[4,2,6]
# w_dict={key:value for (key,value) in zip(words,word_lenghts) }
# print(w_dict)



####################################################################################################
################################################## Python for Data Analysis: Exploring and Cleaning Data
####################################################################################################

# import pandas as pd
# train=pd.read_csv('Projects/train.csv',on_bad_lines='skip',sep=';')
# # df=pd.DataFrame(train)
# categorical=train.dtypes[train.dtypes=='object'].index
# print(categorical)
# print(train[categorical].describe())

# import pandas as pd
# train=pd.read_csv('Projects/train.csv',on_bad_lines='skip',sep=';')
# print(train.shape)
# print(train.info())
# print(train.head())
# print(train.describe())


# import pandas as pd
# train=pd.read_csv('Projects/train.csv',on_bad_lines='skip',sep=';')
# copy=train
# print(copy)
# del copy['Gender']
# print(copy)


# import pandas as pd
# train=pd.read_csv('Projects/train.csv',on_bad_lines='skip',sep=';')
# print(train)
# print(sorted(train['Name'])[0:5]) # hepsini sıralayıp ilk 5 satırı gösteriyor
# print(sorted(train['Name'][0:5])) # yalnızca ilk 5 satırı sıralıyor


# import pandas as pd
# train=pd.read_csv('Projects/train.csv',on_bad_lines='skip',sep=';')
# new_train=pd.Categorical(train['Survived']).rename_categories(['Died','Survived'])
# print(new_train.describe())

# import pandas as pd
# train=pd.read_csv('Projects/train.csv',on_bad_lines='skip',sep=';')
# new_train=pd.Categorical(train['P_Class'],ordered=True).rename_categories(['Class 1','Class 2','Class 3']) # ilk 1 olan sonra 2 sonra 3 şeklinde gidiyor.
# print(new_train.describe())
# print(new_train)
# print(train['P_Class'].unique())

# import pandas as pd
# import numpy as np
# train=pd.read_csv('Projects/train.csv',on_bad_lines='skip',sep=';')
# new_train=train['classes'].astype(str)
# print('new train: \n',new_train)
# new_class=np.array([new_train[0] for new_train in new_train])
# print('new class: \n',new_class)
# new_class=pd.Categorical(new_class)
# print('new class: \n',new_class)
# print('describe:\n',new_class)


# import pandas as pd
# dummy_vector = pd.Series([1,None,3,None,7,8])
# print(dummy_vector.isnull())


# import pandas as pd
# import numpy as np
# train=pd.read_csv('Projects/train.csv',on_bad_lines='skip',sep=';')
# missing=np.where(train['test'].isnull()==True)
# print(missing)


# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# train=pd.read_csv('Projects/train.csv',on_bad_lines='skip',sep=';')
# # print(train['Age'])

# # train.hist(column='Age',
# #            figsize=(9,6),
# #            bins=20)
# train.hist(column='Age',figsize=(9,6),bins=50)
# plt.show()

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# train=pd.read_csv('Projects/train.csv',on_bad_lines='skip',sep=';')
# new_age_var=np.where(train['Age'].isnull(),28,train['Age']) #boş yerleri 28 ile doldurdu
# train['Age']=new_age_var
# print(train['Age'])

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# train=pd.read_csv('Projects/train.csv',on_bad_lines='skip',sep=';')
# index=np.where(train['Age']==max(train['Age']))
# print(train.loc[index])

####################################################################################################
################################################## Python for Data Analysis: Working With Text Data
####################################################################################################

import sqlite3
import pandas as pd
sql_conn=sqlite3.connect('/Python/Pandas/database.sqlite')
comments=pd.read_sql("SELECT body FROM May2015 WHERE subreddit ='timberwolves",sql_conn)
comments=comments["body"]



