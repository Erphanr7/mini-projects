import random
a, b = map(int, input("Enter two numbers separated by space: ").split())

randco = random.randint(a, b)

print(randco)

while True:
    c = int(input(f'enter your guess a number between {a} and {b}:\n'))

    if c<a or c>b:
        print('out of range')
        continue

    if c>randco:
            print('go down')
    elif c<randco:
            print('go uuuuuup')
    else:
            print ('nice')
            break
        
    
        
##Erphan 12.31.2024
