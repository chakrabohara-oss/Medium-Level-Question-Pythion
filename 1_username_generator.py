full_name = input("Enter full name: ")

'''Remove extra space'''
full_name = " ".join(full_name.split())

'''Convert into lowercase'''
full_name = full_name.lower()

'''Replace space between words with underscores'''
username = full_name.replace(" ", "_")

print(full_name)
print(username)