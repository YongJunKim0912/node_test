my_list = ['초코파이','오예스','치토스']
your_list = ['진라면','불닭볶음면']
print(my_list[0:])

print(len(my_list))

my_list[2] = '침대'
print(my_list)

my_list.append('누가바')
print(my_list)

my_list.remove('누가바')
print(my_list)

#my_list.append(your_list)
#print(my_list)
my_list.extend(your_list)
print(my_list)

my_list.pop()
print(my_list)

my_list.sort()
