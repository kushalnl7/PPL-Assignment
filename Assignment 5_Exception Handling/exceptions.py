# Type Error Exception
print("Enter a numeric string")
a = input()
try:
    print(a/3)
except TypeError:
    print("A string cannot be divided by a integer. Convert the type of string to integer")

# ZeroDivisionError Exception

p = int(input("Enter dividend: "))
while(1):

    try:
        q = int(input("Enter the divisor: "))
        ans = p / q

    except ZeroDivisionError:
        print("ZeroDivisonError: You tried to divide by 0\nEnter the divisor again!")

    else:
        print("No Exception Occured.")
        print("Result = {}\n".format(ans))
        break


# AssertionError Exception

try:  
    a = 25.25
    b = 'String'
    assert a == b

except AssertionError:  
        print ("AssertionError: AssertionError Exception occurred\n")

else:  
    print ("Success, no error!\n")


# Key Error

try:
    dic = {1:'yay', 2:'hurray', 3:'byee', 4:'see you'}
    print(dic[5])

except LookupError:
    print("LookupError: Key Error occured because the key is not present in the dictionary")

else:
    print("No error while accesing the value of the key.")

# Index Error

try:
    l = [1, 2, 3, 4, 5, 6, 7]
    print(l[9])

except LookupError:
    print("LookupError: Index Error occured because the index went out of bounds.")  

else:
    print("No error while accesing the list.")
    
    
print("\nI am trying to raise my exception")
try:
    raise Myerror("I raised this exception")
except:
    print("Myerror is user-defined exception")


# File-Handling Exception
while (1):

    file = input("\nEnter correct filename: ")

    try:

        filecontent = open(file, 'r')
        content = filecontent.read()

    except IOError:  # Catches the exception for us and let's us execute our own code in case of an exception.

        print("\nFileNotFoundError: File is not found. Please check what you have entered. Try Again!\n")

    else:  # Gets executed if no exceptions occured and everything went smoothly.

        print("Succesfully read the file, '{}'\n".format(file))
        print("File content: {}\n".format(content))
        break
  
  
  
  
  
  
  
  
  
  
  
