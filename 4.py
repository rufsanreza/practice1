x = 0

while x < 5:
    print(f'the value of x is {x}')
    x = x + 1
else:
    print('reached maximum')

x = [1,2,3]

for item in x:
    #
    pass

mystring = 'sammy'

for letter in mystring:
    if letter == 'm':
        continue
    print(letter)


for letter in mystring:
    if letter == 'm':
        break
    print(letter)