numbers=[3,51,2,8,6]
print("O:",numbers)

numbers.sort()
print("Sorted:",numbers)

numbers.sort(reverse=True)
print("Rev Sorted",numbers)

print("------------- Another way of sorting------------")

other_numbers=[43,1,67,23,54]
print("O:",other_numbers)

sorted_list=sorted(other_numbers)
print("Sorted :",sorted_list)
print("O:",other_numbers)

reverse_sorted_list=sorted(other_numbers,reverse=True)
print("Rev Sorted :",reverse_sorted_list)
print("O:",other_numbers)


print("------------- COmplex Objects---------------")

cart=[('Bread',5),('Butter',7),('Jam',4)]
print("Cart:",cart)
# ------------------------------
def sort_cart(element):
    return element[1]
# -------------------------------
cart.sort(key=sort_cart)
print("Sorted:",cart)

cart.sort(key=sort_cart,reverse=True)
print("Rev Sorted:",cart)