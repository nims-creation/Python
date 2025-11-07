#  sets is the collection of unordered items in python.
# each element of the sets is unique and immutable but the set itself is mutable means we can add or remove items from the set.

collection = {10, 20, 30, 40, 50}
print(type(collection))

collection2 = {21,35,21,45,60,75,80,90,100}
print(collection2)  # it will print unique values only

collection.add(60)  # adding an item to the set
collection.remove(20)  # removing an item from the set
collection.discard(100)  # it will not raise an error if the item is not present in the set
print("Updated collection:", collection)



#  method in the sets

set1 = {10, 20, 30, 40, 50}
set2 = {40, 50, 60, 70, 80}

print(set1.union(set2))  # it will return a new set with all the unique items from both sets
print(set1.intersection(set2))  # it will return a new set with the common items from both sets
