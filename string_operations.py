if __name__ == '__main__':
    s = 'abcdefghaa'
    print(len(s))
    print(s[1:4])
    print(s.count('a'))
    print(s.index('e'))
    print(s.rindex('a'))

    print(s[:4])
    print(s[4:])
    print(s[-2:])
    print(s[-5:-3])

    print('---------------')
    s2 = 'abc\ndef\t\tefg\neyetye'
    print(s2)

    print(ord('a'))
    print(ord('A'))
    print(ord('\t'))
    print(ord('\n'))

    s3 = 'abc\b'
    print(s3)

    s4 = '      abcd     '
    s4 = s4.strip()
    s5 = 'abcd'

    if s4 == s5:
        print('s4 and s5 are equal')
    else:
        print('s4 and s5 not equal')

    s6 = '281480\t893258058\t0932850\t92820502'
    print(s6.split('\t'))
