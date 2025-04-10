def max_of_three(num1,num2,num3):

    if (num1>=num2) & (num1>=num3):
        largest=num1

    elif (num2>=num1) & (num2>=num3):
        largest=num2

    else:
        largest=num3

    return largest

num1= int(input('Enter first no.'))
num2=int(input('Enter second no.'))
num3=int(input('Enter third no.'))

print('Maximum out of three is:'+str(max_of_three(num1,num2,num3)))
