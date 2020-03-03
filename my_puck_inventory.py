# Product Inventory Project
# Create an application which manages an inventory of products for capstone project.
# Create a product class which has a price, ID, and qty on hand.
# Then create an inventory class which keeps track of various
# products and can sum up the inventory value.
# Found multiple sources of this class project and borrowed ideas that were
# more efficient than my original code.  Thank you brilliant CS students in
# my class and online.

class product():

    if __name__ == '__main__':

        inventory = [[], [], [], []]
        types = {'ref' : 0, 'shade_size' : 1, 'price' : 2, 'qty' : 3}

        def __init__(self):
            self.ref = self.inventory[0]
            self.shade_size = self.inventory[1]
            self.price = self.inventory[2]
            self.qty = self.inventory[3]

        def add(self, ref, shade_size, price, qty):
            ''' (int, str, float, int) - > str

            Adds an item into the inventory containing the following data:
            ref, shade_size, price and qty.

            Sample:
            >>>product.add(207179, 'OM3_16', 100.78, 24)
            Product Added
            >>>product.add(120674, 'A1_20', 101.35, 22)
            Product Added
            '''

            ref = self.ref.append(ref)
            shade_size = self.shade_size.append(shade_size)
            price = self.price.append(price)
            qty = self.qty.append(qty)

            print('Product Added')

        def remove(self, ref):
            ''' (int) -> str
            Puck data located by user input of ref and removed from inventory.

            >>>product.remove(214456)
            Product Removed '''

            ind = self.ref.index(ref)
            for r in self.inventory:
                r.remove(r[ind])
                print('Product Removed')

        def changevalue(self, ref, typ, new):
            ''' (int, str, str,) -> str

            Changes the value of an item with user specified type.
            Valid types are 'ref', 'shade_size', 'price', and 'qty'.

            >>> product.changevalue(123456, 'ref', 34)
            Value updated   '''

            self.key = self.types.get(typ)
            ind = self.ref.index(ref)

            self.inventory[sefl.key][ind] = new
            print('Value updated')

class inventory():

    if __name__ == '__main__':

        def __init__(self):
            self.inventory = product.inventory
            self.types = product.types
            self.ref = product.ref
            self.shade_size = product.shade_size
            self.shade_size = self.types.get('shade_size')
            self.key = self.types.get('ref')
            self.qty = self.types.get('qty')
            self.pri = self.types.get('price')
            self.g = list()
            self.h = list()

        def sort_inventory(self):
            self.g = []
            for r in range(len(self.inventory[0])):
                for j in range(len(self.inventory)):
                    self.h.append(self.inventory[j][r])
                self.g.append(self.h)
                self.h = []
            self.g.sort(key=lambda g: g[0])

        def showall(self):
            ''' (none) -> list
            Returns list of ref, shade_size, price, qty per product for
            ea item in inventory.  If item has 0 quantity, it returns
            "Out of stock".

            >>> inventory.showall()
            Product #: 123455 shade_size: OM3_16
            Price per unit: 101.23 Qty: 13

            Product #: 187421  shade_size: A1_20
            Price per unit: 196.99 Qty: 0 - PRODUCT IS OUT OF STOCK

            End of List
            '''
            self.sort_inventory()
            for x in self.g:
                print('Product #: ', end='')
                print(x[self.key], end='  ')
                print('Shade_Size: ', end='')
                print(x[self.shade_size], end='\n')
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

            Returns a list of all pucks in inventory that share the same
            value input by the user

            >>> inventory.lookup(101.00)
            Product #: 232344  Shade_Size: OM3_16
            Price per unit: 101.0 Qty: 54

            Product #: 141033  Shade_Size: A1_20
            Price per unit: 101.0 Qty: 2


            Finished Searching.
            '''

            self.sort_inventory()
            for x in self.g:
                if value in x:
                    print('Product #: ', end='')
                    print(x[self.key], end='  ')
                    print('Shade_Size: ', end='')
                    print(x[self.shade_size], end='\n')
                    print('Price per unit: ', end='')
                    print(x[self.pri], end=' ')
                    print('Qty: ', end='')
                    print(x[self.qty], end=' ')
                    if x[self.qty] == 0:
                        print('- PRODUCT IS OUT OF STOCK', end='\n \n')
                    else:
                        print('', end='\n \n')
            print('Finished Searching.')

        def get_qty(self, ref):
            ''' (int) -> float

            Returns the quantity of pucks from ref input

            >>> inventory.get_qty(123456)
            Product #: 123456  Shade_Size: OM3_16
            Units in stock:  9
            >>> inventory.get_qty(223344)
            Product #: 223344  Shade_Size: A1_20
            Units in stock: 0 - PRODUCT IS OUT OF STOCK
            '''
            self.sort_inventory()
            ind = self.inventory[self.key].index(ref)

            print('Product #: ', end='')
            print(ref, end='  ')
            print('Shade_Size: ', end='')
            print(self.inventory[self.shade_size][ind], end='\n')
            print('Units in stock:', end=' ')
            print(self.inventory[self.qty][ind], end=' ')
            if self.inventory[self.qty][ind] == 0:
                print('- PRODUCT IS OUT OF STOCK', end='')

        def get_prod_bel_qty(self, qty):
            ''' (int) -> list

            Returns a list of all products in inventory whos quantities are the
            same or fall below input qty '''

            self.sort_inventory()
            for x in self.g:
                if qty >= x[self.qty]:
                    print('Product #: ', end='')
                    print(x[self.key], end='  ')
                    print('Shade_Size: ', end='')
                    print(x[self.shade_size], end='\n')
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
            value of the products in inventory for a total inventory value. '''

            a = 0
            self.g = []
            self.sort_inventory()
            for x in self.g:
                i = x[self.qty] * x[self.pri]
                a = i + a
                print('Product #: ', end='')
                print(x[self.key], end='  ')
                print('Shade_Size: ', end='')
                print(x[self.shade_size], end='\n')
                print('Price per unit: ', end='')
                print(x[self.pri], end='')
                print('  @ ', end='')
                print(x[self.qty], end='')
                print('/unit', end='\n')
                print('Total product value: ', end='')
                print(round(i, 2), end='\n \n')
            print('Total value of all units:  ', end='')
            print(round(a, 2), end='')



product = product()
inventory = inventory()
print('Welcome to tsdscanbot.')
prod_ent = True
while prod_ent == True:
    option = input('Choose option: 1 = add pucks 2 = remove pucks 3 = show inventory\n')
    if option == '1':
        add_another = 0
        while add_another == 0:
            puck_add = input('scan barcode\n')
            print(puck_add + ' added')
            product.add(207179, 'OM3_16', 100.78, 1)
            add_another = input('add another? Press y or n\n')
            if add_another == 'n':
                prod_ent = False
            else:
                inventory.showall()
                continue

    elif option == '2':
        del_another = 0
        while del_another == 0:
            puck_remove = input('scan barcode\n')
            print(puck_remove + 'removed')
            product.remove(207179)
            del_another = input('remove another? Press y or n\n')
            if del_another == 'n':
                prod_ent = False
            else:
                inventory.showall()
                continue

    elif option == '3':
        product.add(127456, 'OM3_16', 100.00, 3)
        product.add(123445, 'A1_20', 90.00, 54)
        product.add(197556, 'B1_12',110.00, 9)
        product.add(111324, 'B2_25', 85.95, 26)
        product.add(33421, 'C1_12', 96.99, 5)
        product.add(410358, 'Disk1_16', 140.00, 2)
        product.add(111658, 'D4_12', 112.84, 14)
        inventory.showall()
        prod_ent = False
    else:
        print('Invalid entry - Please restart program to continue')



#inventory.showall()
