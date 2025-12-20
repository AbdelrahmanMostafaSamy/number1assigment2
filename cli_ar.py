# from classes.main import LISTOFPRODUCTS
from classes.main import Cart
from classes.main import Stock
from classes.main import Product
import arabic_reshaper

# -------- Arabic Helper --------
def ar(text):
    reshaped = arabic_reshaper.reshape(text)
    return reshaped[::-1]

cart = Cart()
stock = Stock()

#______________Add Products in Stock______________
def add_products():
    print(ar("__________إضافة منتج إلى المخزن__________"))
    id = int(input(ar("أدخل رقم المنتج: ")))

    if id in stock.products:
        print(ar("رقم المنتج موجود بالفعل"))
        return

    name = input(ar("أدخل اسم المنتج بالعربية: "))
    name_en = input(ar("أدخل اسم المنتج بالإنجليزية: "))

    price = int(input(ar("أدخل سعر المنتج: ")))
    desc = input(ar("أدخل وصف المنتج: "))
    quantity = int(input(ar("أدخل كمية المنتج: ")))

    newProduct = Product(id, [name, name_en], price, desc)
    stock.addProductToStock(newProduct, quantity)

    print(ar("تمت إضافة المنتج بنجاح ✅"))

#______________Display Products______________
def display_products():
    print(ar("__________المنتجات المتاحة__________"))

    if not stock.products:
        print(ar("لا يوجد منتجات في المخزن"))
        return

    for key, value in stock.products.items():
        print(
            f"{key} --> {ar(value['obj'].name)} | "
            f"{value['obj'].price} {ar("جنيه")} | "
            f"{value['obj'].desc} | "
            f"{ar('الكمية')}: {value['Quantity']}"
        )

#______________Add to Cart_____________
def add_to_cart():
    print(ar("\n__________إضافة إلى سلة الشراء__________"))
    user_input = input(ar("أدخل رقم المنتج (أو 0 للإيقاف): "))

    if not user_input.isdigit():
        print(ar("رقم غير صالح"))
        return False

    prod_id = int(user_input)

    if prod_id == 0:
        return False

    if prod_id not in stock.products:
        print(ar("المنتج غير موجود"))
        return True

    qty_input = input(ar("أدخل الكمية المطلوبة: "))

    if not qty_input.isdigit() or int(qty_input) <= 0:
        print(ar("كمية غير صحيحة"))
        return True

    quantity = int(qty_input)
    product = stock.products[prod_id]["obj"]

    cart.addProduct(product, quantity)
    print(ar(f"تمت إضافة {quantity} من {product.name} إلى السلة 🛒"))

    return True

#______________Delete From Cart______________
def delete_from_cart():
    print(ar("\n__________حذف منتج من السلة__________"))
    id = int(input(ar("أدخل رقم المنتج المراد حذفه: ")))

    if id in cart.items:
        del cart.items[id]
        cart.update_total()
        print(ar("تم حذف المنتج من السلة ❌"))
    else:
        print(ar("المنتج غير موجود في السلة"))

#______________View Cart______________
def view_cart():
    print(ar("\n__________محتويات سلة الشراء__________"))

    if not cart.items:
        print(ar("السلة فارغة"))
        return

    for pid, item in cart.items.items():
        product = item["obj"]
        quantity = item["quantity"]
        item_total = item["item_total"]

        print(
            f"{pid} --> {product.name} | "
            f"{product.price} جنيه | "
            f"{ar('الكمية')}: {quantity} | "
            f"{ar('الإجمالي')}: {item_total}"
        )

    print("-" * 40)
    print(ar("إجمالي المبلغ: ") + f"{cart.total} جنيه")

#______________Main Menu______________
def main_menu():
    while True:
        print(ar("\n__________القائمة الرئيسية__________"))
        print(ar("1. إضافة منتج إلى المخزن"))
        print(ar("2. عرض المنتجات"))
        print(ar("3. إضافة منتج إلى السلة"))
        print(ar("4. حذف منتج من السلة"))
        print(ar("5. الدفع"))
        print(ar("6. عرض سلة الشراء"))
        print(ar("7. خروج"))

        choice = input(ar("اختر رقم العملية: "))

        if choice == "1":
            add_products()
        elif choice == "2":
            display_products()
        elif choice == "3":
            while True:
                if not add_to_cart():
                    break
        elif choice == "4":
            delete_from_cart()
        elif choice == "5":
            if not cart.items:
                print(ar("السلة فارغة، لا يمكن إتمام الدفع"))
            else:
                success, msg = cart.checkout()
                if success:
                    for line in msg:
                        print(ar(line))
                else:
                    print(ar(msg))
        elif choice == "6":
            view_cart()
        elif choice == "7":
            print(ar("تم الخروج من النظام 👋"))
            break
        else:
            print(ar("اختيار غير صحيح، حاول مرة أخرى"))
