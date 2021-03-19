a = "There are 3 books and 6 pencils here"
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
print('length of a ' + str(len(a)))
print('number of digits ' + str(digit))
print('nubmer of upper case ' + str(upperCase))
print('number of space ' + str(space))
print('number of lower case ' + str(lowerCase))
