from module import Transaction

#Init Transaction
trx_1234 = Transaction()

#Adding new item
trx_1234.add_item('Keyboard', 1, 500_000)
trx_1234.add_item('Mouse', 1, 150_000)
trx_1234.add_item('Earphone', 1, 150_000)

#Updating item name
trx_1234.update_item_name('Keyboard', 'Speaker')

#Updating item qty
trx_1234.update_item_qty('Speaker', 2)

#Updating item price
trx_1234.update_item_price('Speaker', 250_000)
print(trx_1234.list_items)

#Deleting Item
trx_1234.delete_item('Earphone')

#Delete all item
#trx_1234.reset_transaction()

#Check all items that have been added
trx_1234.check_order()

#Counting total price of all item that have been added
trx_1234.total_price()