# Dictionary in python: dictionary is a collection of key-value pairs in python.
# they are unordered, changeable, and indexed and they allow duplicate values but not duplicate keys.

profile = {
    "name": "Nitesh Mishra",
    "age": 23,
    "city": "Mumbai",
    "profession": "Developer",
    "hobbies": ["coding", "riding", "traveling", "cooking"]
}

print(profile["age"])
profile["age"] = 24
print("Updated age:", profile["age"])
print(profile.get("profession"))
print(profile["profession"])


# operation in the dictionary..

print(profile.keys())
print(profile.values())
print(len(profile.values()))

print(profile.items())


profile.update({"hometown": "Thane"})
print("Updated profile:", profile)
