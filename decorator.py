"""
decorator:
    add new functionallity to an existing object without modifying structure

"

#assiging function to a variable
def plus_one(num):
    return num+1

add_one=plus_one
print(add_one(5))


def plus_one(num):
    def add_one(num):
        return num+1
    res = add_one(num)
    return res

print(plus_one(4))


def hello_fn():
    def say_hi():
        return "Hi"
    return say_hi
hello = hello_fn()
print(hello())




def print_msg(msg):
    "enclosing fn"
    def mesg_sndr():
        "nested fn"
        print(msg)
    mesg_sndr()
print_msg("message for you")


#creating decorators

def uppercae_deco(fn):
    def wrapper():
        fnc = fn()
        make_upr = fnc.upper()
        return make_upr
    return wrapper


def say_hi():
    return 'hello'

decorate=uppercae_deco(say_hi)
print(decorate())


"""

def uppercae_deco(fn):
    def wrapper():
        fnc = fn()
        make_upr = fnc.upper()
        return make_upr
    return wrapper

@uppercae_deco
def say_hi():
    return 'hello there'

print(say_hi())

# decorate=uppercae_deco(say_hi)
# print(decorate())


# import functools

# def split_string(fn):
#     @functools.wraps(fn)
#     def wrapper():
#         fnc=fn()
#         splited_str = fnc.split()
#         return splited_str
#     return wrapper

# @split_string
# @uppercae_deco
# def say_hi():
#     return "hello there"

# print(say_hi())