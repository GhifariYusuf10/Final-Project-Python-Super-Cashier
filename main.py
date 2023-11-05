from module import Transaction

#Init Transaction
trx_1234 = Transaction()

#Adding new item
trx_1234.add_item('Ayam Goreng', 2, 20_000)
trx_1234.add_item('Pasta Gigi', 3, 15_000)
trx_1234.add_item('Mainan Mobil', 1, 200_000)
trx_1234.add_item('Mi Instan', 5, 3_000)

#Deleting Item
#trx_1234.delete_item('Pasta Gigi')

#Reseting transaction
#trx_1234.reset_transaction()

# #Updating item name
# trx_1234.update_item_name('Keyboard', 'Speaker')

# #Updating item qty
# trx_1234.update_item_qty('Speaker', 2)

# #Updating item price
# trx_1234.update_item_price('Speaker', 250_000)
# print(trx_1234.list_items)



# #Delete all item
trx_1234.reset_transaction()

# #Check all items that have been added
# trx_1234.check_order()

#Counting total price of all item that have been added
trx_1234.total_price()