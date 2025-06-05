#write a progarm to find secong largest in an array 
numbers = [34,75,56,70]
largest = 0
second = 0
for num in numbers:
    if num>largest:
        second=largest
        largest = num
    elif num>second  and num!=largest:
        second = num
print("second largest is ", second)    