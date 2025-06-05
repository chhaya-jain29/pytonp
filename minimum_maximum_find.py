#write a program to find minimum element in an array
number = [23,34,55,88,90]
minimum = number[0] 
maximum = number [0]
for num in number:
    if num<=minimum:
      minimum = num
    if num>=maximum:
        maximum = num
print("minimum=" ,minimum)
print("maximun=" , maximum)
