cart = ["apple", "milk", "bread", "apple", "eggs", "milk"]

'''Remove duplicate'''
cart = list(set(cart))              #cart containing unoique value

cart.append("cheese")               #add cheese at last index

bread_index = cart.index("bread")   #find the index of bread
cart.pop(bread_index)               #remove bread

cart.sort() #sort cart alphabetically

print(f"Final Cart: {cart}")
print(f"Number of different items: {len(cart)}")
