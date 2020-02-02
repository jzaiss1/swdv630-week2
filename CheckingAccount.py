# John Zaiss (GitHub id jzaiss1)
# SWDV 630: OBJECT-ORIENTATED CODING 1W 20/SP1
# Week 2 Assignment - Classes and Methods in Python

class CheckingAccount:
    def __init__(self, accountName, accountNumber, firstName, lastName, address):
        # All attributes are private since a Checking Account contains PII
        self.__accountName = accountName
        self.__accountNumber = accountNumber
        self.__firstName = firstName
        self.__lastName = lastName
        self.__address = address
        self.__balance = 0

    # Mutators

    # The update balance method needs to be kept private 
    def __updateBalance(self, amount):
        self.__balance += amount

    def processTransaction(self, type, amount):
        if type == 'credit':
            self.__updateBalance(amount)
            successful = True
        elif type == 'debit':
            self.__updateBalance(amount * -1)
            successful = True
        else:
            successful = False

        if successful:
            print('{} transaction processed'.format(type))
        else:
            print('\nERR: Transaction not processed\n{} is not a valid transaction type\n'.format(type))

    # Accessors
    def printBalance(self):
        return 'Account {} has a balance of ${:6.2f}\n'.format(self.__accountNumber, self.__balance)

    def getBalance(self):
        return self.__balance
        
def main():
    checkingAccount = CheckingAccount('checking','12345678','John','Doe','123 Main Street, Anytown, USA, 12345')
    checkingAccount.processTransaction('credit', 550.00)
    print(checkingAccount.printBalance())    
    checkingAccount.processTransaction('debit', 45.90)
    print(checkingAccount.printBalance())   
    checkingAccount.processTransaction('credit', 314.90)
    print(checkingAccount.printBalance())    
    checkingAccount.processTransaction('debry', 4.90)
    print(checkingAccount.printBalance())    
    checkingAccount.processTransaction('debit', 137.56)
    print(checkingAccount.printBalance())    
    checkingAccount.processTransaction('debit', 85.91)
    print(checkingAccount.printBalance())     

main()