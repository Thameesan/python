'''
s={'maths','tamil','english','english'} # in sets no intex and unoder
print(s)
print(type(s))
'''
'''
s={'maths','tamil','english','english'}
s.add('it')
print(s)
'''
'''
s={'maths','tamil','english','english'}
s.update('history')
'''
'''
s={'maths','tamil','english','english'}
s.update(['history','it'])
print(s)
'''
'''
s={'maths','tamil','english','english'}
s.add(['history','it'])
'''
'''
s={'maths','tamil','english','english'}
s.remove('maths')
print(s)
'''
'''
s={'maths','tamil','english','english'}
s.discard('mas')
print(s)
'''
'''
s={'maths','tamil','english','english'}
s.pop()
print(s)
'''
'''
s={'maths','tamil','english','english'}
s.clear()
print(s)
'''

number1=[12,34,56,34,23,12,34,56,78,90,80,90,78,98,23,56,45,34,23,12,45,67,89,90,80,70,60,70,60,46,60,34,56,78,90,23]
number2={}
number2.update(number1)
print(number2)

'''
a={12,34,56,34,24}
b={12,45,67,45,24}
print(a+b)
'''
'''
a={1,2,3,4,5}
b={3,5,7,8,9}
c=a|b
print(c)
d=a&c
print(d)
f=a-b
print(f)
print(b-a)
print(a^b)
'''
'''
a={1,2,3,4,5}
b={3,5,7,8,9}
f=a.symmetric_difference(b)
print(f)
'''
'''
a={1,2,3}
b={1,2,3,4,5}
c={4,5,6}
d=a|b|c
e=a&b&c
print(d)
print(e)

print(f'a<=b is {a<=b}')
print(f'a.issubset(b) {a.issubset(b)}')
print(f'a.issuperset(b) {a.issuperset(b)}')
'''












