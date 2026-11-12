#----Mini calculator----#
#1. Take user decision open(o)
a = input(" ").lower()
#2. Calculator opening using while
while a == "o" :
#3. Taking a value from user
    b = input("Please do any calculation or enter 'c' to close ").lower()
#4. Bellow code for close the app   
    if b == 'c':
        print("app was closed")
        break
#5. Bellow code for calculate the user-given value.      
    else:
        d = eval(b)
        print("The result is: ",d)
