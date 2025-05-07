# # 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances. 


class Bank:
    bank_name:str = "Al-Habib Bank"

    def __init__(self,account_holder:str)-> None:
        self.account_holder = account_holder
        

    @classmethod
    def change_bank_name(cls,name:str)->None:
        cls.bank_name = name
    def Bank_Info(self):
        print(f'Account Holder : {self.account_holder}\nBank Name : {self.bank_name}')

b1: Bank = Bank("Muhammad Farooq")
b1.Bank_Info()  # Account Holder : Muhammad Farooq
                # Bank Name : Al-Habib Bank
Bank.change_bank_name("Al-Meezan Bank")
b1.Bank_Info()  # Account Holder : Muhammad Farooq
                # Bank Name : Al-Meezan Bank
