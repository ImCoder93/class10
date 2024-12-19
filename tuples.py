student=('yichen',30)
print(student)


#packing
address = ('227','brickford shelters','bangalore','karnataka','562107')

for x in address :
    print (x , end='')

#unpacking
houseno, apartNAME,city, state, pin = address

print()
print('HNO,houseno')
print(city)
print(state)
print(pin)

#A tuple can also be created without using parentheses
my_tuple = 3, 4.6, 'dog'
print(my_tuple)

# nested tuple 
n_tuple = ('mouse',[8,4,6],(1,2,3))




# nested index
print(n_tuple[0][3])
print(n_tuple[1][1])
















