# Programmer: Mew, I

def place_order(item):
    print(f"Order placed. Your order is:{item}")
    
def calculate_total(item):
    base_price = 25.5
    VAT = 1.15
    total_price = ((base_price + len(item)) * VAT)
    return total_price

def get_order():
    print("Your order is being prepared...")
    return"Collect your order"

my_food = input("What would you like?")
place_order(my_food)

print(get_order())

order_total = calculate_total(my_food)
print(f"Your order cost: R{order_total:.2f}")
