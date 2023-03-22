print('welcome to Access Bank Atm')
restart='a'
chances = 3
balance = 1000.05
while chances >= 0:
    pin = int(input('Please Enter Your 4 Digit Pin: '))
    if pin == 2461:
        print('You entered your pin correctly\n')
        while restart not in ('n','no', 'NO', 'N'):
            print('please press 1 for your balance\n')
            print('please press 2 to make a withdrawal\n')
            print('please press 3 to pay in\n')
            print('please press 4 to return card\n')
            option = int(input('what would you like to choose?'))
            if option == 1:
                print('your balance is N', balance,'\n')
                restart = input('would you like to go back? ')
                if restart in ('n', 'no', 'No', 'N'):
                    print('thank you')
                    break
                elif option == 2:
                    option2 = ('a')
                    withdrawal = float(input('how much would you like to withdraw? \nN100/N200/N500/N1000'))
                    if withdrawal in [100,200,500,1000]:
                        balance = balance - withdrawaln
                        print ('\nyour balance is now N', balance)
                        restart = input('would yo like to go back')
                        if restart in ('n', 'no', 'NO', 'N'):
                            print('thank you')
                            break
                    elif withdrawal != [100, 200, 500, 1000]:
                        print('invalid amount, please re-try\n')
                        restart = ('y')
                    elif withdrawal == 1:
                        withdrawal = float(input('please enter desired amount:'))

                elif option == 3:
                    pay_in = float(input('How much would you like to pay in?'))
                    balance = balance + pay_in
                    print('\nyour balance is now N', balance)
                    restart = input('would you like to go back? ')
                    if restart in ('n', 'no', 'NO', 'N'):
                        print('thank you')
                        break

                elif option == 4:
                    print('please wait whilst your card is returned...\n')
                    print('thank you for service')
                    break
                else:
                    print('please enter a correct number. \n')
                    restart = ('y')
            elif pin != 2461:
                print('incorrect password')
                chances = chances - 1
                if chances == 0:
                    print('\nNo more tries')
                    break

