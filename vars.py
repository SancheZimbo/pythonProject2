

#integers have no limit to precision
a = 10
b = -38945238572475724057458
c = a + b
print(type(c))
#print('c:' + str(c))
print('c:{}'.format(c))

#floats have a limit to precision
af = 242.033
bf = 65575476756856856856878786876878678878.352
cf = af + bf
print(type(cf))
print('cf:{}'.format(cf))

#if __name__ == '__main__' : may be needed if you import multiple files

print(1.79e+308)
print(1.8e+308)

bb = 0b11111111
print(bb)

#hexadecimal notation is used in IP addresses or colour schemes(more economical vs decimal system due to letters)
bx = 0xff
print(bx)

print(bb/bx)

f = 5

print(f**3)
g = 12
print('div g: {}'.format(g % 5))

h = 'bf'
print(int(h, 16))
h1 = '374835384784'
h1i = int(h1)
print(h1.isdigit())
print(h1.isalpha())
print(h1.isalnum())

print(type(h1))
print(type(h1i))

print(5)

fa = 100
print(type(fa))
fa = 100.3563
print(type(fa))
print(round(fa, 0))