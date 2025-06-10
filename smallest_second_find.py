#write a progarm to find secong smallest in an array 
numbers = [34,75,56,70]
smallest = 0
second = 0
for num in numbers:
    if num<smallest:
        second=smallest
        smallest = num 
    elif num<second  and num==smallest:
        second = num
print("second smallest is ", second)    