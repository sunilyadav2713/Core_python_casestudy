class ATM:

    dict1=[]

    while True:

        print("1.account creation")

        print("2.view account details by acctno")

        print("3.withdraw")

        print("4.deposit")

        print("5.fund transfer")

        print("7.exit")

        a=int(input())

        if a==1:

            name=input("enter your name")

            accno=int(input("create account no"))

            place=input("enter the place")

            intial_amount=int(input("enter the intial amount"))

            dict1.append([name,accno,place,intial_amount])

        elif a==2:

            c=0

            accno=int(input("enter the accno number"))

            for i in dict1:

                for k in i:

                    if k==accno:

                        print('name:',dict1[c][0])

                        print('accno:',dict1[c][1])

                        print('place:',dict1[c][2])

                        print('balance:',dict1[c][3])

                c=c+1

        elif a==3:

            c=0

            acc=int(input("enter the account number"))

            with_draw=int(input("enter the withdraw amount"))

            for i in dict1:

                for k in i:

                    if k==acc:

                        if dict1[c][3]>with_draw:

                            a=dict1[c][3]-with_draw

                            dict1[c][3]=a

                            print("please collect your amount")

                        else:

                            print("insufficient balance")    

                c=c+1

        elif a==4:

            c=0

            acc=int(input("enter the account number"))

            deposit=int(input("enter the deposit amount"))

            for i in dict1:

                for k in i:

                    if k==acc:

                        a=dict1[c][3]+deposit

                        dict1[c][3]=a

                        print("your amount deposited successfully")

                             

                c=c+1

        elif a==5:

            acc1=int(input("enter the acc1"))

            acc2=int(input("enter acc2"))

            c=0

            d=[]

            for i in range(len(dict1)):

                d.append(dict1[i][1])

 

            if acc1 in d and acc2 in d:

                transfer_amount=int(input())

                for k in d:

                    if k==acc1:

                        a=dict1[c][3]-transfer_amount

                        dict1[c][3]=a

                    if k==acc2:

                        b=dict1[c][3]+transfer_amount

                        dict1[c][3]=b

                        print("amount transferred successfully")

                    c=c+1

            else:

                print("please enter valid account numbers")

               




        elif a==7:

            break

ATM()
