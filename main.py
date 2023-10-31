class Transaction :

    def __init__(self):
        self.order_items = dict()

    def add_item(self, item_name, item_qty, item_price):

        if isinstance(item_name, str) == False:
            raise TypeError("Only String Allowed for Item Name")
        
        elif isinstance(item_qty, int) == False:
            raise TypeError("Only Integer Allowed for Item Qty")
        
        elif isinstance(item_price, int) == False:
            raise TypeError("Only Integer Allowed for Item Price")


    def update_item_name(self):
        pass

    def update_item_qty(self):
        pass

    def update_item_price(self):
        pass

    def delete_item(self):
        pass

    def reset_transaction(self):
        pass

    def check_order(self):
        pass

    def total_price(self):
        pass


new_instance = Transaction()

add = new_instance.add_item('Test', 2, 4)