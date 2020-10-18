# Product Inventory Project
    # Create an application which manages an inventory of products.
    # Create a product class which has a price, ID, and qty on hand.
    # Then create an inventory class which keeps track of various
    # products and can sum up the inventory value.

class product(object):

    if __name__ == '__main__':

        inventory = [[], [], [], []]
        types = {'pid' : 0, 'name' : 1, 'price' : 2, 'qty' : 3}

        def __init__(self):
            self.pid = self.inventory[0]
            self.name = self.inventory[1]
            self.price = self.inventory[2]
            self.qty = self.inventory[3]

        def add(self, pid, name, price, qty):
            ''' (int, str, float, int) - > str

            Adds an item into the inventory containing the following data:
            PID, name, price and qty.

            >>>product.add(74025, 'Bathwater', 62.78, 46)
            Product Added
            >>>product.add(12674, 'Water', 201.35, 22)
            Product Added
            >>>inventory.lookup(74025)
            Product #: 74025  Name: Bathwater
            Price per unit: 62.78 Qty: 46

            Finished Searching.
            >>> inventory.lookup(12674)
            Product #: 12674  Name: Water
            Price per unit: 201.35 Qty: 22
            '''

            pid = self.pid.append(pid)
            name = self.name.append(name)
            price = self.price.append(price)
            qty = self.qty.append(qty)

            print('Product Added')

        def remove(self, pid):
            ''' (int) -> str

            Item is located by user input PID and removed from inventory.

            >>>product.remove(63456)
            Product Removed
            >>>product.remove(12674)
            Product Removed
            >>>inventory.showall()
            Product #: 32345  Name: Crazy Texas Robot Millionaire
            Price per unit: 40.0 Qty: 54

            Product #: 41058  Name: Some wires
            Price per unit: 40.0 Qty: 2

            Product #: 71658  Name: Mice
            Price per unit: 12.84 Qty: 154

            Product #: 74025  Name: Bathwater
            Price per unit: 62.78 Qty: 46

            Product #: 81324  Name: Livers
            Price per unit: 85.95 Qty: 26

            Product #: 87421  Name: Poo
            Price per unit: 6.99 Qty: 0 - PRODUCT IS OUT OF STOCK

            Product #: 97256  Name: Shoes with Attitude
            Price per unit: 40.0 Qty: 9

            End of List
            '''

            ind =  self.pid.index(pid)
            for p in self.inventory:
                p.remove(p[ind])

            print('Product Removed')

        def changevalue(self, pid, typ, new):
            ''' (int, str, str) -> str

            Changes the value of an item with user specified type
            Valid types are 'pid', 'name', 'price' and 'qty'

            >>> product.changevalue(97256, 'pid', 45206)
            Value successfully updated
            >>> product.changevalue(81324, 'name', 'tacos')
            Value successfully updated
            >>> inventory.lookup(45206)
            Product #: 45206  Name: Shoes with Attitude
            Price per unit: 40.0 Qty: 9

            Finished Searching.
            >>> inventory.lookup(81324)
            Product #: 81324  Name: tacos
            Price per unit: 85.95 Qty: 26

            Finished Searching.
            '''

            self.key = self.types.get(typ)
            ind = self.pid.index(pid)

            self.inventory[self.key][ind] = new
            print('Value successfully updated')

class inventory(object):

    if __name__ == '__main__':

        def __init__(self):
            self.inventory = product.inventory
            self.types = product.types
            self.pid = product.pid
            self.name = product.name
            self.nam = self.types.get('name')
            self.key = self.types.get('pid')
            self.qty = self.types.get('qty')
            self.pri = self.types.get('price')
            self.g = list()
            self.h = list()

        def sort_inventory(self):
            self.g = []
            for p in range(len(self.inventory[0])):
                for j in range(len(self.inventory)):
                    self.h.append(self.inventory[j][p])

                self.g.append(self.h)
                self.h = []
            self.g.sort(key=lambda g: g[0])

        def showall(self):
            ''' (none) -> list

            Returns a list of PID, NAME, PRICE, QTY per product for each listing
            currently in inventory. If QTY is 0, item will be labeled "Out of stock"

            >>>inventory.showall()
            Product #: 32345  Name: Crazy Texas Robot Millionaire
            Price per unit: 40.0 Qty: 54

            Product #: 41058  Name: Some wires
            Price per unit: 40.0 Qty: 2

            Product #: 45206  Name: Shoes with Attitude
            Price per unit: 40.0 Qty: 9

            Product #: 71658  Name: Mice
            Price per unit: 12.84 Qty: 154

            Product #: 74025  Name: Bathwater
            Price per unit: 62.78 Qty: 46

            Product #: 81324  Name: tacos
            Price per unit: 85.95 Qty: 26

            Product #: 87421  Name: Poo
            Price per unit: 6.99 Qty: 0 - PRODUCT IS OUT OF STOCK

            End of List
            '''

            self.sort_inventory()
            for x in self.g:
                print('Product #: ', end='')
                print(x[self.key], end='  ')
                print('Name: ', end='')
                print(x[self.nam], end='\n')
                print('Price per unit: ', end='')
                print(x[self.pri], end=' ')
                print('Qty: ', end='')
                print(x[self.qty], end=' ')
                if x[self.qty] == 0:
                    print('- PRODUCT IS OUT OF STOCK', end='\n \n')
                else:
                    print('', end='\n \n')
            print('End of List')

        def lookup(self, value):
            ''' (int) -> list , (float) -> list , (str) -> list

            Returns a list of all products in inventory which share the same
            value input

            >>> inventory.lookup(40.00)
            Product #: 32345  Name: Crazy Texas Robot Millionaire
            Price per unit: 40.0 Qty: 54

            Product #: 41058  Name: Some wires
            Price per unit: 40.0 Qty: 2

            Product #: 97256  Name: Shoes with Attitude
            Price per unit: 40.0 Qty: 9

            Finished Searching
            >>> inventory.lookup(0)
            Product #: 87421  Name: Poo
            Price per unit: 6.99 Qty: 0 - PRODUCT IS OUT OF STOCK

            Finished Searching.
            '''

            self.sort_inventory()
            for x in self.g:
                if value in x:
                    print('Product #: ', end='')
                    print(x[self.key], end='  ')
                    print('Name: ', end='')
                    print(x[self.nam], end='\n')
                    print('Price per unit: ', end='')
                    print(x[self.pri], end=' ')
                    print('Qty: ', end='')
                    print(x[self.qty], end=' ')
                    if x[self.qty] == 0:
                        print('- PRODUCT IS OUT OF STOCK', end='\n \n')
                    else:
                        print('', end='\n \n')
            print('Finished Searching.')

        def get_qty(self, pid):
            ''' (int) -> float

            Returns the quantity of product from specified PID

            >>> inventory.get_qty(45206)
            Product #: 45206  Name: Shoes with Attitude
            Units in stock:  9
            >>> inventory.get_qty(87421)
            Product #: 87421  Name: Poo
            Units in stock: 0 - PRODUCT IS OUT OF STOCK
            '''

            self.sort_inventory()
            ind = self.inventory[self.key].index(pid)

            print('Product #: ', end='')
            print(pid, end='  ')
            print('Name: ', end='')
            print(self.inventory[self.nam][ind], end='\n')
            print('Units in stock:', end=' ')
            print(self.inventory[self.qty][ind], end=' ')
            if self.inventory[self.qty][ind] == 0:
                print('- PRODUCT IS OUT OF STOCK', end='')


        def get_prod_bel_qty(self, qty):
            ''' (int) -> list

            Returns a list of all products in inventory whos quantities are the
            same or fall below input qty

            >>> inventory.get_prod_bel_qty(50)
            Product #: 41058  Name: Some wires
            Units in stock: 2

            Product #: 45206  Name: Shoes with Attitude
            Units in stock: 9

            Product #: 74025  Name: Bathwater
            Units in stock: 46

            Product #: 81324  Name: tacos
            Units in stock: 26

            Product #: 87421  Name: Poo
            Units in stock: 0 - PRODUCT IS OUT OF STOCK

            Finished Searching.
            '''

            self.sort_inventory()
            for x in self.g:
                if qty >= x[self.qty]:
                    print('Product #: ', end='')
                    print(x[self.key], end='  ')
                    print('Name: ', end='')
                    print(x[self.nam], end='\n')
                    print('Units in stock:', end=' ')
                    print(x[self.qty], end=' ')
                    if x[self.qty] == 0:
                        print('- PRODUCT IS OUT OF STOCK', end='\n \n')
                    else:
                        print('', end='\n \n')
            print('Finished Searching.')

        def sum_inventory_value(self):
            ''' (none) -> list

            Returns a list containing how much money the entire quantities of
            each product in inventory are worth. Also returns the sum of the
            value of the products in inventory for a total inventory value.

            >>> inventory.sum_inventory_value()
            Product #: 32345  Name: Crazy Texas Robot Millionaire
            Price per unit: 40.0  @ 54/unit
            Total product value: 2160.0

            Product #: 41058  Name: Some wires
            Price per unit: 40.0  @ 2/unit
            Total product value: 80.0

            Product #: 45206  Name: Shoes with Attitude
            Price per unit: 40.0  @ 9/unit
            Total product value: 360.0

            Product #: 71658  Name: Mice
            Price per unit: 12.84  @ 154/unit
            Total product value: 1977.36

            Product #: 74025  Name: Bathwater
            Price per unit: 62.78  @ 46/unit
            Total product value: 2887.88

            Product #: 81324  Name: tacos
            Price per unit: 85.95  @ 26/unit
            Total product value: 2234.7

            Product #: 87421  Name: Poo
            Price per unit: 6.99  @ 0/unit
            Total product value: 0.0

            Total value of all units:  9699.94
            '''

            a = 0
            self.g = []
            self.sort_inventory()
            for x in self.g:
                i = x[self.qty] * x[self.pri]
                a = i + a
                print('Product #: ', end='')
                print(x[self.key], end='  ')
                print('Name: ', end='')
                print(x[self.nam], end='\n')
                print('Price per unit: ', end='')
                print(x[self.pri], end='')
                print('  @ ', end='')
                print(x[self.qty], end='')
                print('/unit', end='\n')
                print('Total product value: ', end='')
                print(round(i, 2), end='\n \n')
            print('Total value of all units:  ', end='')
            print(round(a, 2), end='')

#Sould be easy enough remember for ease of testing.
product = product()
inventory = inventory()

#I have included a small inventory for ease of testing
product.add(63456, 'Meow', 60.00, 0)
product.add(32345, 'Crazy Texas Robot Millionaire', 40.00, 54)
product.add(97256, 'Shoes with Attitude', 40.00, 9)
product.add(81324, 'Livers', 85.95, 26)
product.add(87421, 'Poo', 6.99, 0)
product.add(41058, 'Some wires', 40.00, 2)
product.add(71658, 'Mice', 12.84, 154)
inventory.showall()
product.add(32345, 'Crazy Texas Robot Millionaire', 40.00, 54)
product.add(97256, 'Shoes with Attitude', 40.00, 9)
inventory.showall()
