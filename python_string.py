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

x = len(str(len(a)))
#print (('{0:>{x}}'.format('foo', x=x)))
#print('{:>19}'.format('length: ')), print (('{0:>{x}}'.format(str(len(a)), x=x)))

print('{:>19}'.format('length: ') + (('{0:>{x}}'.format(str(len(a)), x=x))))
print('{:>19}'.format('digit numbers: ') + (('{0:>{x}}'.format(str(digit), x=x))))
print('{:>19}'.format('lowercase letters: ') + (('{0:>{x}}'.format(str(upperCase), x=x))))
print('{:>19}'.format('uppercase letters: ') + (('{0:>{x}}'.format(str(lowerCase), x=x))))
print('{:>19}'.format('spaces: ') + (('{0:>{x}}'.format(str(space), x=x))))

'''
print('{:>19}'.format('length: ') + '{0:>2}'.format(str(len(a))))
print('{:>19}'.format('digit numbers: ') + '{:>2}'.format(str(digit)))
print('{:>19}'.format('lowercase letters: ') + '{:>2}'.format(str(upperCase)))
print('{:>19}'.format('uppercase letters: ') + '{:>2}'.format(str(lowerCase)))
print('{:>19}'.format('spaces: ') + '{:>2}'.format(str(space)))

print('number of digits ' + str(digit))
print('nubmer of upper case ' + str(upperCase))
print('number of space ' + str(space))
print('number of lower case ' + str(lowerCase))


'''