ID = int(input("Enter the pin : "))

name = str(input("Enter your name : "))

if(ID == 12345):
    print("Welcome to SBI Bank",name)
    balance1 = 10000
    print("Your current balance is :",balance1)
    print("1-Credit\n2-Debit")
   
    ch = int(input("Enter the choice : "))
    
    if(ch == 1):
        amn1 = int(input("Enter the Amount to be Credited : "))
        print("Your total balance is :",amn1+balance1)
    elif(ch == 2): 
        amn2 = int(input("Enter the Amount to be Debited : "))
        if(amn2 <= 10000):
         print("Your total balance is :",balance1-amn2)
        elif(amn2 > 10000):
          print("Insufficient Balance to Debit")
      
    
elif(ID == 13579):
    print("Welcome to HDFC Bank",name)
    balance2 = 5000
    print("Your current balance is :",balance2)
    print("Enter\n1-Credit\n2-Debit")
   
    ch = int(input("Enter the choice : "))
    
    if(ch == 1):
        amn1 = int(input("Enter the Amount to be Credited : "))
        print("Your total balance is :",amn1+balance2)
    elif(ch == 2): 
        amn2 = int(input("Enter the Amount to be Debited : "))
        if(amn2 <= 5000):
         print("Your total balance is :",balance2-amn2)
        elif(amn2 > 5000):
          print("Insufficient Balance to Debit")
else:
  print("Ener a valid Pin")
    
    
