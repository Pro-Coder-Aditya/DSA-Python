# Hash Table using Python dictionary
hash_table = {}

# Insert key-value pairs
hash_table["name"] = "Aditya"
hash_table["age"] = 19
hash_table["city"] = "Mumbai"

# Access values
print("Name:", hash_table["name"])
print("Age:", hash_table["age"])

# Update value
hash_table["age"] = 22

# Delete key
del hash_table["city"]

print("Final Hash Table:", hash_table)
