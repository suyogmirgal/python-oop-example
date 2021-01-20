def function1(*args):
    for arg in args:
        print(arg)


def function2(**kwargs):
    for key,value in kwargs.items():
        print('key=' + key + ", value="+value)


print("function1 output:")

function1("Welcome", "to", "Python", "Session")

print('\n')
print("function2 output:")
function2(name="Suyog", gender="Male", email="suyog@mail.com")