"""
supermarket bill generation
customer name
phone no.
add item - add another item or go for bill payment
total bill
bill paid successfully
"""
class Billgeneration:
    def __init__(self,customername,phonenum):
        self.customer_name = customername
        self.phonenum = phonenum
        self.items = []
        self.item_price = []
        
    def add_item(self, item, Rs_item):
        self.items.append(item)
        self.item_price.append(Rs_item)
        
    def billing(self):
        print(50*"-","SUPERMARKET",50*"-")
        print("-" * 50)
        print("Customer Information:")
        print(f"Name: {self.customer_name}")
        print(f"Phone Number: {self.phonenum}")
        print("-" * 50)

    def list_items(self):
        while True :
            item = input("Enter a item : ")
            Rs_item = int(input("Enter price : "))
            cust_info.add_item(item,Rs_item)

            print(100*"-")
            for i,j in zip(self.items,self.item_price):
                print(f"{self.items.index(i)+1}){i} Rs.{j}")
            print(100*"-")

            add_or_bill = int(input("Click 1 to add item\nor\nClick 2 to bill payment : "))
            if add_or_bill == 1:
                item = input("Enter a item : ")
                Rs_item = int(input("Enter price : "))
                cust_info.add_item(item,Rs_item)

            elif add_or_bill == 2:
                print(100*"-")
                self.billing()
                print("List of Items : ")
                print(100*"-")
                for i,j in zip(self.items,self.item_price):
                    print(f"{self.items.index(i)+1}){i} Rs.{j}")
                totalAmo = sum(self.item_price)
                print(100*"*")
                print(f"Total bill amount : {totalAmo}")
                print(100*"*")
                billPay = int(input("ENTER TOTAL AMOUNT TO PAY : "))

                if billPay == totalAmo:
                    print(f"PAYMENT SUCCESSFUL {totalAmo}")
                    print("Thank you,visit again :)")    
                    break
                elif billPay > totalAmo:
                    print("PAYMENT SUCCESSFUL")
                    print(f"TAKE YOUR CHANGE : {billPay-totalAmo}")
                    print("Thank you,visit again :)")    
                    break
                else:   
                    print("PAYMENT FAILED DUE TO INSUFFICIENT BALANCE")

            else:
                print("Buy some groceries")
              
cus_name = input("Enter your name : ")
phone = input("Enter your phone no. : ")
cust_info = Billgeneration(cus_name,phone)
cust_info.list_items()
              