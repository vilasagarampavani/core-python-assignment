def total_price(cart_items):
    if len(cart_items) ==0:
        return 0
    total_price = sum(cart_items.values())
    if len(cart_items) > 5:
        discount = 0.10
        total_price -= total_price * discount
    return total_price

cart_items = eval(input("Enter the cart items:"))
total_price = total_price(cart_items)
print("Total Price: ",total_price)
