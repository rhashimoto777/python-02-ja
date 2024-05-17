def apply_discount(products, minimum_price, discount_rate):
    discount_coef = (100 - discount_rate)/100
    a = lambda x : (x["name"], x["price"]*discount_coef)
    b = [a(elem) for elem in products if elem["price"] >= minimum_price]
    return b

################ test case 1 ################
products = [
    {"name": "Laptop", "category": "Electronics", "price": 1200},
    {"name": "Bread", "category": "Food", "price": 2},
    {"name": "Jacket", "category": "Apparel", "price": 100}
]
minimum_price = 50
discount_rate = 10
print(apply_discount(products, minimum_price, discount_rate))

################ test case 2 ################
products = [
    {"name": "Smartphone", "category": "Electronics", "price": 800},
    {"name": "Sneakers", "category": "Footwear", "price": 120},
    {"name": "Coffee", "category": "Beverage", "price": 5}
]
minimum_price = 100
discount_rate = 15
print(apply_discount(products, minimum_price, discount_rate))