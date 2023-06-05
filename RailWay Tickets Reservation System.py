
#Railway Ticket Reservation
# train names,no
# date,time
# passengers,seats
# Types of Compartments
import datetime
import random
print(25*"*","welcome To Indian Railway",25*"*")
list_of_trains={"GunturExpress":'17281',"NagarsolExpress":'12787',"Lingampalli Express":'17255',"Seshadri Express":"17209"}
name=input("Enter your name:")

print(7*"-","Train Details",7*"-")
class Passenger:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
    def display_info(self):
        print(f"Name: {self.name}")       
        print(f"Gender: {self.gender}")
        print(f"Age: {self.age}")
# for k,v in list_of_trains.items():
#             print ("Train name: ",k,"---Train no. :",v)

ticketrate={"GunturExpress":'140',"NagarsolExpress":'270',"Lingampalli Express":'490',"Seshadri Express":"500"}
#for t,r in ticketrate.items():
     #print("Select train:",t,"ticketrates:",r)
train=input("Enter train name:")
passenger=int(input("Enter no. of passengers:"))
if train in ticketrate:
    print("Ticket Fare:",ticketrate[train])
    price=(int(ticketrate[train])*passenger)
          #print(price)
user_date=int(input("Enter your reservation date:"))
print("  ")
date=datetime.datetime(2023,6,user_date)
print("Your Reservation Date:",date)
seat=input("Select Compartment:")
class Train():
    def __init__(self, train_num,select_seat, source, destination, seats,):
        self.train_num = train_num
        self.select_seat=select_seat
        self.source = source
        self.destination = destination
        self.seats = seats
    def display_info(self):
        print("Train no.:",self.train_num)
        print("selectseat:",self.select_seat)
        print("Source:",self.source)
        print("Destination:",self.destination)
        print("Available seats:",self.seats)
        
tr=Train("17281","Ac","vjy","pkl",54)
tr.display_info()

print (22*"--" ,"Your Reserved Ticket",22*"--")
print("Passenger Details:")
print(68*" ","Journey Date:",date)
print(68*" ","PNR NO - ",random.randint(11111,1000000))

c=Passenger("",20,'Male')
c.display_info()  
print("Your train:",(train))

class Src():
    def __init__(self, train_num,source,destination,select_seat,):
        self.train_num = train_num
        
        self.source = source
        
        self.destination = destination
        
        self.select_seat=select_seat
    def display_info(self):
        print("Train no.:",self.train_num)
        print("Source:",self.source)
        print("Destination:",self.destination)
        print("selectseat:",self.select_seat)
        

td=Src("17281","vjy","pkl","Ac")
td.display_info()
class my():
    def __init__(self, train_num,source,destination,select_seat,):
        self.train_num = train_num
        self.source = source
        self.destination = destination
        self.select_seat=select_seat
    def display_info(self):
        print("Train no.:",self.train_num)
        print("Source:",self.source)
        print("Destination:",self.destination)
        print("selectseat:",self.select_seat)
        
t1=my("17255","Nsp","Lngm","SL")
t1.display_info

print("No.of Pasengers:",passenger)
print(10*"--")
print("TOTAL FARE :",price)
print(10*"--")
print("Your Ticket is Confirmed Sucessfully.")
print(68*" ","Your Ticket Was Generated on:",datetime.datetime.now())
print(25*"--","Thank You",25*"--")



