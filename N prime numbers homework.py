
# first N prime numbers.

#Try except block incase users input invalid inputs.
try:

#Ask the user for input and store it in the variable num as an integer.

    num = int(input("Enter the number-"))

#Assign variable m with value 2 as it is the first prime number.

    m = 2
#num!=0 ensures this loop will continue until num = 0

    while num != 0:

#use the for loop to check if the number is divisible by any number from 2 to m not including m since prime numbers are
#only divisible by 1 and themselves, if it is divisible break the for loop.

        for i in range(2,m):
            if m%i==0:
                break

#else we print the number and use end=" " to have space between out outputed prime numbers.

        else:
            print(m,end=" ")

#We need to decrement the num  until it reaches 0 to stop the while loop
            num = num - 1

#m variable will increase by one as num decreases by one until num = 0 and specified prime numbers printed
        m = m + 1

except:
       print("Invalid Input")


