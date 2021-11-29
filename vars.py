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