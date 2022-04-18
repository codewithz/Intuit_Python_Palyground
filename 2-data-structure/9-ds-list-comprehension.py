cart=[('Bread',5),('Butter',7),('Jam',4)]
print("Cart:",cart)

#  [expression for item in items]

prices=list(map(lambda element:element[1],cart))
print(prices)

prices_lc=[item[1] for item in cart]
print(prices_lc)

# [expression for item in items if condition]

filtered_list=list(filter(lambda element:element[1]>=5,cart))
print(filtered_list)

filtered_list_lc=[item for item in cart if item[1]>=5]
print(filtered_list_lc)