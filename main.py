import pandas as pd
from Users import User
from Cars import Car

class CRS:
    """This is Main class for admin panel It has 4 methods namely
        __init__  : for initializing the variables 
        show_cars : for showing list of available cars
        show_hired_car : shows all hired car details
        show_client_details : show alll client details
    """
    def __init__(self,username):
        self.username = username
    def show_cars(self):
        ''' This method takes only self arguments 
            argumtnts : only self
            purpose : to display all available car
            return : none
        '''
        df = pd.read_csv("cars.csv")
        print("################## Available Cars ########################")
        print(df)
    
    def show_hired_car(self):
        ''' This method takes only self arguments 
            argumtnts : only self
            purpose : to display all hired car details
            return : none
        '''
        df = pd.read_csv("hire.csv")
        print("################## Hired Cars ########################")
        print(df)

    def show_client_details(self):
        ''' This method takes only self arguments 
            argumtnts : only self
            purpose : to display all clients/user details
            return : none
        '''
        df = pd.read_csv("hire.csv")
        print("################## Users List ########################")
        print(df)







if __name__=='__main__':
    """"This is where program starts from"""
    print("\n\n##########################################")
    print("Welcome to Car Rental System")
    print("########################################## \n\n")
    print("Please Login to continue")
    #take input to contine as admin or client or register for new user
    login_type = int(input("Enter 1 for admin login 2 for Customer Login Enter 3 to register if you are new User : "))
    if(login_type==1):
        #if user selects admin mode
        username = input("Enter username :") #store username
        pswd = input("Enter Password :") #store password
        if(username == 'admin'): #check username is correct
            if(pswd == 'admin'): #check password is correct
                AU = User(username, pswd) #create instance of User class
                AU.welcome()  #welcome user if username and password matched
                print("Car Rental System dashboard")
                crs1 = CRS(username)  #create instance of CSR class
                crs1.show_cars()  #show list of cars
                crs1.show_hired_car() #show hires cars details
                crs1.show_client_details() #show client /user details
        
    if(login_type == 2):
        #if user select client mode 
        username = input("Enter username :") #store username
        pswd = input("Enter Password :") #store password
        CU = User(username, pswd)  #create user instance
        login_sts, indx = CU.login() #authentication
        if(login_sts ==1): #if authenticated sucess
            CU.welcome()  #welcome user
            c1 = Car(username)  #create cars instance
            #enter operation mode hire or Rent
            c_oper = int(input("Please Enter 1 to Hire Car 2 to Rent car 3 to exit :"))
            if(c_oper == 1):
                #Hire mode
                print("###############################")
                print("####Select car category #######")
                c1.show_category() #show available category
                df = pd.read_csv("cars.csv")  #read cars file
                df_cat = df.category.unique() 
                #selecting category id
                x = 1
                while x>0 :
                    sel_cat = input("Enter category id from( 0 to {}) to select category :".format(df_cat.shape[0]-1))
                    if sel_cat.isdigit():
                        x=0
                        
                    else:
                        x=1
                cat = df_cat[int(sel_cat)]
                count, cat_cars = c1.show_selected_category(cat)
                y=1
                
                #select car id from car category list
                while y>0 :
                    selc_car = input("Enter car id of you choice from(0 to {})".format(count-1))
                    if selc_car.isdigit():
                        y=0
                        
                    else:
                        y=1
                
                
                order_car = cat_cars.iloc[int(selc_car)]  #store ordered car details
                av_days = order_car.available_day  #available day of car
                av_price = order_car.price_per_day #car price
                z = 1
                while z>0 :
                    no_day = input("Enter number of day (from 0 to ):".format(av_days))
                    if no_day.isdigit():
                        z=0
                        
                    else:
                        z=1
                print("\n\n ##################################")
                print("Your selected order")
                print(order_car)
                total = int(no_day) * av_price
                print("\n Total fare =>${} for {} days".format(total,no_day))
                print("\n\n")
                payment_sts = input("\npress 1 to make payment :")
                if(int(payment_sts) ==1):
                    print("\n\n ####################################")
                    bank = input("Enter Bank name :")
                    a = 1
                    while a>0 :
                        cc = input("Enter creditcard number")
                        if no_day.isdigit():
                            a=0
                            
                        else:
                            a=1

                    input("Enter card  holder name :")

                    print("Payment Success!")
                    print("#############################################\n\n")
                    c1.hire_car(order_car,total,no_day)
                    
                    print("order car type ",type(order_car))
                    print("Your order \n {} \n has been sucessfully confirmed!".format(order_car))
                    



                

            if(c_oper == 2):
                #print("rent car")
                print("\n\n####################################")
                car_name = input("Enter car name :")
                car_cate = input("Enter car category :")
                price_PD = input("Enter car price in $ per day :")
                avl_day = input("Enter no of days car is available for :")
                c1.register_car(car_name,car_cate,price_PD,avl_day)
            else:
                print("Thank you for using car rental system @{}".format(username))

       
    if(login_type == 3):
        #register mode
        print("######################################################")
        print("Please Enter following deatils to register")
        print("######################################################\n\n")
        username = input("Enter your name :") #store username
        pswd = input("Enter your password :") #store password
        contact_num = input("Enter your contact no :") #store contact number
        bank_name = input("Enter your bank name :")  #store bank details
        cc_num = input("Enter your bank credit card number :") #store creditcard number
        address = input("Enter your address :") #store address
        
        RE= User(username,pswd)
        RE.welcome()
        RE.register(username,pswd,contact_num,bank_name, cc_num,address) #register  new user
    