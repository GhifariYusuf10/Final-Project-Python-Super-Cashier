# Problems

Seorang pemilik supermarket besar di salah satu kota di Indonesia memiliki rencana untuk melakukan perbaikan proses bisnis, yaitu untuk membuat sistem kasir yang self-service di supermarket.Sehingga customer bisa langsung memasukkan item yang dibeli, jumlah item yang dibeli, dan harga item yang dibeli

# Requirements

* Customer membuat id transaksi customer
* Customer dapat memasukkan nama item, jumlah item, dan harga barang.
* Customer dapat mengubah nama item, jumlah item, atau harga item
* Customer dapat menghapus satu item
* Customer dapat menghapus seluruh item
* Customer dapat mengecek seluruh item, jumlah item dan harga item yang dipesan
* Customer dapat mendapat total harga item

# Flowchart

# Penjelasan Code

* Skrip 'main.py' berfungsi sebagai skrip test case untuk mengambil fungsi yang ada pada skrip module.py
* Skrip 'module.py' berfungsi sebagai skrip yang berisikan proses proses bisnis
* Dalam skrip 'module.py' berisikan beberapa function yang ada di dalam class Transaction, antara lain :

    * add_item()
    Untuk menambahkan item, jumlah item, dan harga per item ke dalam dictionary
    ```python
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
    ```

    * update_item_name
    Merubah salah satu nama item
    ```python
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
    ```

    * update_item_qty
    Merubah salah satu qty dari suatu item
    ```python
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
    ```