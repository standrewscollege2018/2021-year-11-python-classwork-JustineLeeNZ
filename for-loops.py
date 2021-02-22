# examples of using for loops
for num in range(0,3):
    print("Hello")

# print numbers between 18 and 22
for num in range(18,23):
    print(num)

# for loop print by 2s
for num in range(0,21,2):
    print(num)

#for loop with variables
start_num = int(input("Enter a start value"))
stop_num = int(input("Enter a stop value"))
step = int(input("Enter a step value"))

# print numbers based on values entered by user
for num in range(start_num, stop_num, step):
    print(num)

