print("1.Check Balance")
print("2.Debit Money")
print("3.Withdraw Money")
print("4.Exit")
num=int(input("Choose one of them :"))
if(num==1):
    PIN=int(input("Enter Your PIN :"))
    if(PIN==1234):
        print(1000)
    else:
        print("Your PIN is incorrict")
if(num==2):
    numa=(int(input("Enter the deposit number :")))
    numb=(float(input("Enter what amount you want to deposit :")))
    PIN=int(input("Enter Your PIN :"))
    if(PIN==1234):
        if(numb<=1000):
            print("Youer",numb,"is deposited successfully")    
        else:
            print("place chack your blance")         
    else:
        print("Your PIN is incorrict")    
if(num==3):
    numa=(float(input("Enter your withdraw amount :"))) 
    PIN=int(input("Enter Your PIN :"))
    if(PIN==1234):
        print("Youer",numa,"is withdraw successfully")   
    else:
        print("Your PIN is incorrict")  
if(num==4):
    print("Thank you visit again")