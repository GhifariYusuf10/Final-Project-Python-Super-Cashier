import pandas as pd
from tabulate import tabulate

class Transaction :
    """
    Class that represents transaction

    Attributes :
        item_name   (str) : Name of the item
        item_qty    (int) : Quantity of the item
        item_price  (int) : Price of the item
    """

    def __init__(self):
        """
        Initializes transaction object

        Parameters :
            list_items  (dict) : Dictionary of item list
        """
        self.list_items = dict()

    def add_item(self, item_name, item_qty, item_price):
        """
        Adding item to dictionary
        
        Parameters :
            item_name   (str) : Name of the item
            item_qty    (int) : Quantity of the item
            item_price  (int) : Price of the item

        Returns :
            dict : Message of list of items that have been added to cart
        """

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
        """
        Updating item name to dictionary
        
        Parameters :
            item_name       (str) : Old Name of the item
            new_item_name   (str) : New Name of the item

        Returns :
            str : Message of items that have been updated
        """
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
        """
        Updating item qty to dictionary
        
        Parameters :
            item_name     (str) : Name of the item that want to update the quantity for
            new_item_qty  (int) : New item qty

        Returns :
            str : Message of items qty that have been updated
        """
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
        """
        Updating item price to dictionary
        
        Parameters :
            item_name       (str) : Name of the item that want to update the price for
            new_item_price  (int) : New item price

        Returns :
            str : Message of items price that have been updated
        """
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
        """
        Deleting item name from dictionary
        
        Parameters :
            item_name     (str) : Name of the item that want to delete

        Returns :
            str : Message of items name that have been deleted
        """
        if isinstance(item_name, str) == False:
            raise TypeError("Only String Allowed for Item Name")
        try :
            if item_name in self.list_items:
                del self.list_items[item_name]
                print(f"{item_name} have been deleted")
                print(f"List of item : {self.list_items}.")
            else :
                print("ERROR - Item name doesn't Exist")
            
        except :
            print("ERROR - Something went wrong when deleting item")

    def reset_transaction(self):
        """
        Deleting all items from dictionary
        
        Parameters :
            None

        Returns :
            str : Message that all items have been deleted
        """
        try :
            self.list_items.clear()
            print("All item have been deleted!")
        
        except :
            print ("ERROR - Something went wrong when deleting all item")

    def check_order(self):
        """
        Print all list of items that have been added to dictionary
        
        Parameters :
            None

        Returns :
            str : Table of all items that have been inserted
        """
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
        """
        Count total price of all in the dictionary
        
        Parameters :
            None

        Returns :
            str : Total price information
        """
        try :
            total_price = 0
            for item in self.list_items:
                total_price += self.list_items[item][2]
            
            if total_price > 500_000 :
                discount_price = 10/100 * total_price
                total_price = total_price - discount_price
                print(f"You get 10% discount, total price are : Rp. {'{:,}'.format(total_price)}")
            
            elif total_price > 300_000 :
                discount_price = 8/100 * total_price
                total_price = total_price - discount_price
                print(f"You get 8% discount, total price are : Rp. {'{:,}'.format(total_price)}")

            elif total_price > 200_000 :
                discount_price = 5/100 * total_price
                total_price = total_price - discount_price
                print(f"You get 5% discount, total price are : Rp. {'{:,}'.format(total_price)}")
            
            else:
                print(f"Total price are : Rp. {'{:,}'.format(total_price)}")
        
        except :
            print("ERROR - Something went wrong when counting total item price")