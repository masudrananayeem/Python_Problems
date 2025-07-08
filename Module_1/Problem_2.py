Number1=int(input('Input 1st number : '))
operator=input('Input operator   : ')
Number2=int(input('Input 2nd number : '))
if operator == '+':
    print('Result = ',Number1+Number2)
elif operator=='*':
    print('Result = ',Number1*Number2)
elif operator=='-':
    print('Result = ',Number1-Number2)
elif operator=='/':
    if Number2!=0:
        print('Result = ',Number1/Number2)
    else:
        print('Error')
else:
    print('Invalid Number or Operator')