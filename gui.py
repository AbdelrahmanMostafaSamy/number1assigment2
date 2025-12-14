from classes.main import LISTOFPRODUCTS
from classes.main import Cart

cart = Cart()

for prod in LISTOFPRODUCTS:
    print(prod.id)
    print(prod.name)
    print(prod.desc)
    print(prod.price)
    print()