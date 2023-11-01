import pandas as pd
from tabulate import tabulate

class Transaction :

    def __init__(self):
        self.list_items = dict()

    def add_item(self, item_name, item_qty, item_price):
        if isinstance(item_name, str) == False:
            raise TypeError("Only String Allowed for Item Name")
        
        elif isinstance(item_qty, int) == False:
            raise TypeError("Only Integer Allowed for Item Qty")
        
        elif isinstance(item_price, int) == False:
            raise TypeError("Only Integer Allowed for Item Price")
        
        try :
            dict_add = {item_name: [item_qty, item_price, item_price * item_qty]}
            self.list_items.update(dict_add)
            print(f"List of item : {self.list_items}.")

        except :
            print("Something went wrong when adding item")

    def update_item_name(self, item_name, new_item_name):
        if isinstance(new_item_name, str) == False:
            raise TypeError("Only String Allowed for Item Name")
        
        try :
            if item_name in self.list_items:
                self.list_items[new_item_name] = self.list_items.pop(item_name)
                print(f"Item name have been updated from {item_name} to {new_item_name}")
            else :
                print("ERROR - Item name doesn't Exist")
            
        except :
            print("ERROR - Something went wrong when updating item name")


    def update_item_qty(self, item_name, new_item_qty):
        if isinstance(new_item_qty, int) == False:
            raise TypeError("Only Integer Allowed for Item Qty")
        
        try :
            if item_name in self.list_items:
                self.list_items[item_name][0] = new_item_qty 
                self.list_items[item_name][2] = new_item_qty * self.list_items[item_name][1]
                print(f"{item_name} qty have been updated to {new_item_qty}")
            else :
                print("ERROR - Item name doesn't Exist")
            
        except :
            print("ERROR - Something went wrong when updating item qty")

    def update_item_price(self, item_name, new_item_price):
        if isinstance(new_item_price, int) == False:
            raise TypeError("Only Integer Allowed for Item Price")
        
        try :
            if item_name in self.list_items:
                self.list_items[item_name][1] = new_item_price 
                self.list_items[item_name][2] = new_item_price * self.list_items[item_name][0]
                print(f"{item_name} price have been updated to {new_item_price}")
            else :
                print("ERROR - Item name doesn't Exist")
            
        except :
            print("ERROR - Something went wrong when updating item price")

    def delete_item(self, item_name):
        if isinstance(item_name, str) == False:
            raise TypeError("Only String Allowed for Item Name")
        try :
            if item_name in self.list_items:
                del self.list_items[item_name]
                print(f"{item_name} have been deleted")
            else :
                print("ERROR - Item name doesn't Exist")
            
        except :
            print("ERROR - Something went wrong when deleting item")

    def reset_transaction(self):
        self.list_items.clear()
        print("All item have been deleted!")

    def check_order(self):
        try:
            if self.list_items == {}:
                print("No Item Have Been Added")
            else :
                table_item = pd.DataFrame(self.list_items).T
                headers = ["Item Name", "Item Qty", "Price per Item", "Total Item Price"]
                print(tabulate(table_item, headers, tablefmt="github"))
        except:
            print("ERROR - Something went wrong when printing items")

    def total_price(self):
        total_price = 0
        for item in self.list_items:
            total_price += self.list_items[item][2]
        print(total_price)


trx_1234 = Transaction()

trx_1234.check_order()
trx_1234.add_item('Nasi Goreng', 2, 10_000)
trx_1234.add_item('Mie Goreng', 3, 10_000)

trx_1234.update_item_name('Nasi Goreng', 'Nasi Uduk')
print(trx_1234.list_items)

trx_1234.update_item_qty('Nasi Uduk', 4)
print(trx_1234.list_items)

trx_1234.update_item_price('Nasi Uduk', 5000)
print(trx_1234.list_items)

#trx_1234.delete_item('Nasi Uduk')
#print(trx_1234.list_items)

#trx_1234.reset_transaction()
#print(trx_1234.list_items)

trx_1234.check_order()
trx_1234.total_price()