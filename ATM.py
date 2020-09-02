balance=10000
while True:
    print("     ATM     ")
    print("1.   Balance\n2.   Withdraw\n3.   Deposite\n4.   Quit\n")
    try:
        op=int(input("Enter option: "))
    except Exception as e:
        print("Error:",e)
        print("Enter 1,2,3 or 4 Only")
        continue
    if op==1:
        print("Balance  is ",balance)
    elif op==2:
        print("Balance is ",balance)
        withdraw=float(input("Enter withdraw amount:    "))
        if withdraw>balance:
            print("Insufficient balance")
        elif withdraw>0:
            balance=balance-withdraw
            print("Balance is ",balance)
        else:
            print("sorry...Withdraw failed..!!!")
    elif op==3:
        print("Balance is ",balance)
        Deposite=float(input("Enter deposite amount:    "))
        if Deposite>0:
            balance=balance+Deposite
            print("Balance is ",balance)
        else:
            print("sorry...Deposite failed...!!!")
    elif op==4:
        exit()
    else:
        print("Enter 1,2,3 or 4 Only")

        
