cart=[('Bread',5),('Butter',7),('Jam',4)]
print("Cart:",cart)
# ------------------------------
# def sort_cart(element):
#     return element[1]
# -------------------------------
cart.sort(key=lambda element:element[1])
print("Sorted:",cart)

#  Prices ----------------------

prices=[]

for name,price in cart:
    prices.append(price)

print("Prices",prices)

x=list(map(lambda element:element[1],cart))

print("Prices x:",x)

# -------------- Filtering ---------------

filtered_list=[]

for name,price in cart:
    if price>=5:
        filtered_list.append((name,price))

print(filtered_list)

y=list(filter(lambda element:element[1]>=5,cart))
print(y)