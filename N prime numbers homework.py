
# first N prime numbers.

#Try except block incase users input invalid inputs
try:

    num = int(input("Enter the number-"))
    m = 2
    while num!=0:
        for i in range(2,m):
            if m%i==0:
                break
        else:
            print(m,end=" ")
            num = num - 1
        m = m + 1

except:
       print("Invalid Input")


