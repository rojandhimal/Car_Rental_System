import pandas as pd
class Car:
    ''' This class stores and manupulate car details
        it consist of 4 methods
        __init__ : initialize variable while creating instance
        show_category : show available caregory
        show_selected_category : show cars of selected category
        hire_car : hire car that is selected by user  
     '''
    def __init__(self,uname):
        self.uname=uname
    
    def show_category(self):
        ''' this methos is user for showing available category
            input argument - self
            purpose : display cars category
            return none
         '''
        fields = ['category']
        df = pd.read_csv('cars.csv', skipinitialspace=True, usecols=fields)
        print(df.category.unique())

    def show_selected_category(self,cat):
        ''' this methos is user for showing available  car of selected category
            input argument - self,category
            purpose : display cars of selected category
            return total no number of category and selected category name
         '''
        df =  pd.read_csv("cars.csv")
        select_cat = df.loc[df['category'] == cat]
        print("#############################################################")
        print("#### Total{} cars are Available of {} category listed below :".format(select_cat.shape[0],cat))
        print(select_cat)
        print("#############################################################\n\n")
        return select_cat.shape[0],select_cat

    def hire_car(self,car_detail,totalP,bookdays):
        ''' this methos is user for hiring car of selected category
            input argument - self, car details,total price, bookdays
            purpose : hire car
            return none
         '''
        df2={'car_name':[car_detail['car_name'],],'category':[car_detail['category'],],'price_per_day':[car_detail['price_per_day'],],'booked_for_days':[bookdays,],'total_price':[totalP,],'Hirer Name':[self.uname,]}
        df2 = pd.DataFrame(df2)
      
        try:
            #print("from try")
            df = pd.read_csv("hire.csv")
            df = df.append(df2, ignore_index=True)
            df.to_csv('hire.csv',index=False)
        except:
            df2.to_csv('hire.csv',index=False)
  

    def register_car(self,car_name,category,price_per_day,available_day):
        ''' this methos is user for registering new car for rent
            input argument - self, car_name,category,price_per_day,available_day
            purpose : register car for rent
            return none
         '''
        df2={'car_name':[car_name,],'category':[category,],'price_per_day':[price_per_day],'available_day':[available_day],'owner':[self.uname,]}
        df2 = pd.DataFrame(df2)
        
        try:
            #print("from try")
            df = pd.read_csv("cars.csv")
            df = df.append(df2, ignore_index=True)
            df.to_csv('cars.csv',index=False)
            print("New car {} registered".format(car_name))
            
        except:
            #print("from else")
            df2.to_csv('cars.csv',index=False)
            print("New car {} registered".format(car_name))
        
            
            