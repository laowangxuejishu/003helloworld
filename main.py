import fire










def hello_world01():
    print('Hello world')









def hello_world02():
    print("Hello world")











def hello_world03():
    print("""Hello world""")










def hello_world04():
    text = 'Hello world'
    print('{}'.format(text))









def hello_world05():
    print('Hello %s' % 'world')










def hello_world06():
    text = 'world'
    print(f'Hello {text}')











def hello_world07():
    import os
    os.system('echo Hello world')









def hello_world08():
    with open('hello_world_file', 'r') as fp:
        print(fp.read().strip())









def hello_world09():
    import sys
    print('Hello world', file=sys.stderr)










def hello_world10():
    import re
    text = 'Do you know how to write hello world?'
    print(re.findall('\S+ (he\D+d)\S+', text)[0])







def hello_world11():
    print('\x48\x65\x6C\x6c\x6f\x20\x77\x6f\x72\x6c\x64')







def hello_world12():
    text = 'Hello world'
    for char in text:
        print(char)



import functools
def hello_world_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Hello world")
        return func(*args, **kwargs)
    return wrapper

@hello_world_decorator
def hello_world13():
    pass




fire.Fire()
