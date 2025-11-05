marks = [85, 90, 78, 92, 88]
total_obtained_marks = sum(marks)
print("The total marks are:", total_obtained_marks)


list2 = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
list2.append("honeydew")
print("Updated list:", list2)

list3 = [12, 45, 23, 67, 34, 89, 90]
list3.sort()
print("Sorted list:", list3)

# To sort in descending order
list3.sort(reverse=True)
print("Sorted list in descending order:", list3)

list4 = [17, 14, 89, 23, 45, 67, 34]
list4.reverse()
print("Reversed list:", list4)

list4.insert(2, 100)
list4.remove(89)
list4.pop(4)
print("List after insertion:", list4)

