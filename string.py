str = "Hey! are you know i am Nitesh"
print(str.endswith("esh"))

str2 = "today i am very happy because i am learning python"
print(str2.capitalize())

str3 = "today weather is very pleasant could you please come to my home"
print(str3.replace("pleasant", "awesome"))

str4 = "hello everyone welcome to the world of python programming"
print(str4.find("python"))

str5 = "would you know my name is nitesh but there are many nitesh in the world and seriously nitesh is a good name but i dont know the meaning of nitesh"
print(str5.count("nitesh"))

strName = input("Enter your name:")
print(len(strName))



# conditional statements

#1 even or odd\

num = int(input("Enter a number:"))
if num % 2 == 0 or num == 0:
    print(num, "is an even number")

else:
    print(num, "is an odd number")