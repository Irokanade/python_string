a = input('Please enter a English sentence:')
upperCase = 0;
lowerCase = 0;
digit = 0
space = 0

for x in a:
    #print(x)

    if x.isupper():
        upperCase += 1
    elif x.isdigit():
        digit += 1
    elif x.isspace():
        space += 1


lowerCase = len(a) - upperCase - digit - space
print('{:>19}'.format('length: ') + '{:>2}'.format(str(len(a))))
print('{:>19}'.format('digit numbers: ') + '{:>2}'.format(str(digit)))
print('{:>19}'.format('lowercase letters: ') + '{:>2}'.format(str(upperCase)))
print('{:>19}'.format('uppercase letters: ') + '{:>2}'.format(str(lowerCase)))
print('{:>19}'.format('spaces: ') + '{:>2}'.format(str(space)))

#print('number of digits ' + str(digit))
#print('nubmer of upper case ' + str(upperCase))
#print('number of space ' + str(space))
#print('number of lower case ' + str(lowerCase))