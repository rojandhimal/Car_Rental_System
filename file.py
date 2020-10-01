import pandas as pd

# df={'id':[],'name':[],'password':[],'contact_number':[],'bank_details':[]}
# df=pd.DataFrame(df)
# df.to_csv('client.csv',index=False)

# df = pd.read_csv("client.csv")

# print("from try")
# fields = ['name','password']
# df = pd.read_csv('client.csv', skipinitialspace=True, usecols=fields)
# for ind, row in df.iterrows(): 
#     print(row['name']) 
#     print() 


#fields = ['category']
#df = pd.read_csv('cars.csv', skipinitialspace=True, usecols=fields)
# for ind, row in df.iterrows(): 
#     print(row['category'])

#print(df.shape[0])

df =  pd.read_csv("cars.csv")
select_cat = df.loc[df['category'] == 'su']
print(select_cat)

