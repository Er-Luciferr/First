#Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
#Once 'done' is entered, print out the largest and smallest of the numbers.
#If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.
#Enter 7, 2, bob, 10, and 4 and match the output below.
largest=None
smallest=None
while True :
    sval=input('Enter a number:')
    if sval=='done':
        break
    try:
        fval=int(sval)
        if largest is None:
            largest=fval
        elif fval>largest:
            largest=fval
        if smallest is None:
            smallest=fval
        elif fval<smallest:
            smallest=fval
    except:
        print('Enter valid number')
        continue
print('smallest number is',smallest)
print('largest number is',largest)
