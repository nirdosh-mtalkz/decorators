from itertools import zip_longest
"""
'''
Decorators
'''

def python_decorator(func):
    def wrapper():
        print("before decorating the function")
        func()
        print("after decorating the function")
    return wrapper

'''
def main():
    print("Hello World!")


main = python_decorator(main)
main()
'''

@python_decorator
def main():
    print("Hello World!")
main()



'''
Generators
'''

#print my name
def name():
    yield 'N'
    yield 'A'
    yield 'M'
    yield 'A'
    yield 'N'

for i in name():
    print(i,end="")


#even numbers

def even_numbers(n):
    for i in range(n):
        if i%2==0:
            yield i

print()
for i in even_numbers(11):
    print(i)



'''
Iterators
'''

l = [1,2,3,4,5]
itr = iter(l)

for _ in range(len(l)):
    print(next(itr))

for ele in itr:
    print(ele)




def print_name(name):
    name = name.lower()
    return name



def uppper_name(func):
    def wrapper(name):
        name = name.upper()
        return name
    return wrapper

'''
@uppper_name
def print_name(name):
    name = name.lower()
    return name
print(print_name('Naman'))

print(print_name('Naman'))
'''


print(print_name("Naman"))
print_name = uppper_name(print_name("Naman"))
print(print_name("Naman"))

"""

name = ('naman','ritul','manish')
age = (20,21,23)

res = list(zip(name,age))
res.sort()
print(res)

d = [('java',4),('c++',5),('python',4.5)]

lang,rating = zip(*d)
print(lang)
print(rating)


a=[1,2,3]
b=['a','b','c','d']
r = range(5)

res = zip_longest(a,b,r,fillvalue=None)
print(list(res))