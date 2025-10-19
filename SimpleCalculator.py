def cal():
    x = ('1. Addition \n2. Subtraction \n3. Multiplication \n4. Division')
    print(x)
cal()

call1 = input('Select an operation: ')

num1 = int(input('Enter First number: '))
num2 = int(input('Enter Second number: '))

if call1 == '1':
    x1 = num1 + num2
    print('Total number: ' + str(x1))
elif call1 == '2':
    x2 = num1 - num2
    print('Total number: ' + str(x2))
elif call1 == '3':
    x3 = num1 * num2
    print('Total number: ' + str(x3))
elif call1 == '4':
    x4 = num1 / num2
    print('Total number: ' + str(x4))
    
else:
    print("Invalid input")