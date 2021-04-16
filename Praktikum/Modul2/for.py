# array
array = [1,2,3,4]

for i in array :
    print(i, end = '')

print('\n')

# param ada 1 : maksimal
print('param 1')
angka = 10
for i in range(angka):
     print("Angka ke : ")
     print(i)
print('\n')

# param ada 2 : minim, maksimum
print('param 2')
for i in range(angka, 20):
     print("Angka ke : ")
     print(i)
print('\n')
# param ada 3 : minim, maks, lompatan (incre + / decre -)
print('param 3 incre')
for i in range(angka, 20, 2):
     print("Angka ke : ")
     print(i)
print('\n')

print('param 3 decre')
for i in range(20, angka, -2):
     print("Angka ke : ")
     print(i)