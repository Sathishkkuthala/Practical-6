fh = open("prac 6.txt",'w')
number = int(input("Enter a number to calculate its factorial: ")) 
factorial = 1 
for i in range(1, number + 1):
    factorial *= i 
fh.write(f"The factorial of {number} is {factorial}") 
fh.close()
