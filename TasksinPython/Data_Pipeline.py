def numbers():
    for i in range(1,21):
        yield i
def even(numbers):
    for n in numbers:
        if n%2==0:
            yield n
def square(numbers):
    for n in numbers:
        yield n*n
num=numbers()
even_num=even(num)
sq=square(even_num)
for n in sq:
    print(n)