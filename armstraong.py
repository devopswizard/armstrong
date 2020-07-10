num = input("Please enter an integer: ")
numlen = len(num)
sum = 0

if int(num.isdigit()):
    for i in num:
        sum = sum + (int(i)**numlen)
    
    if sum == int(num):
        print(f"{num} is an Armstrong number!")
    else:
        print(f"{num} is not an Armstrong number!")
else:
    print("It is an invalid entry. Don't use non-numeric, float, or negative values!")