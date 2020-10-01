import pandas as pd

class User:
    '''This class us used to control all user activity
        It consits of 4 methods
        __init__ : for variable initialization
    '''
    def __init__(self,name,pswd):
        '''Initialize all glabal variable here'''
        self.name = name #login username
        self.pswd = pswd #login user password
        

    def welcome(self):
        '''This method is used to welcome the logged in user'''
        print("#######################################")
        print("welcome to Car Rental System @{}".format(self.name)) #welcome message
        print("####################################### \n")

    def login(self):
        '''This method handels login and authentication
            input: self
            purpose : authentication
            return : none
        '''

        ret = 0
        fields = ['name','password']
        df = pd.read_csv('client.csv', skipinitialspace=True, usecols=fields)
        for ind, row in df.iterrows(): 
            if(self.name == row['name']):  #check if username match
                if(self.pswd == row['password']): #check if password match
                    
                    ret = 1     #flag set to allow login for registered user
                    return ret,ind  #return index of user and login flag
                else:
                    pass              
            else:
                print("username or password not matched!")
        return ret,0
        


    def register(self,username,pswd,contact_num,bank_name, cc_num,address):
        '''This method is used to register and store details of new user
            input : self,username,password,contact_number,bank_name,creditcard,address
            purpose: store register details in file
            return none
        '''
        df2={'name':[username,],'password':[pswd,],'contact_number':[contact_num,],'bank_details':[bank_name,],'cc_num':[cc_num,],'address':[address,]}
        df2 = pd.DataFrame(df2)
        
        try:
            #check if file is present
            df = pd.read_csv("client.csv")
            df = df.append(df2, ignore_index=True)
            df.to_csv('client.csv',index=False)
        except:
            df2.to_csv('client.csv',index=False) 
        
        print("Sucessfully registered @{}".format(username))
            
        
    

          
          
        
        
    


