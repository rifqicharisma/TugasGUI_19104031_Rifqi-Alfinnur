# try.... except
try:
    a = int(input('masukkan nilai a: '))
    b = int(input('masukkan nilai b: '))
    c = a / b

    print(f"{a} / {b} = {c}")

except ZeroDivisionError as e:
    print('Error : Tidak boleh dibagi 0')

# try... except... finally
f = ''
try:
    f = open('contoh.txt')
    lines = f.readlines()
    for line in lines:
        print(line, end='\n')

except IOError as e:
    print('Error : Fie hilang')

finally :
    if f :
        f.close()