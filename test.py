print("hello! Django Girls");
if 4<5 and 3<8:
 print("im done");
#my first python program
def hi():
    print('Hi there!')
    print('How are you?')

hi()

def hime(name):
    if name == 'Ola':
        print('Hi Ola!')
    elif name == 'Sonja':
        print('Hi Sonja!')
    else:
        print('Hi anonymous!')

hime("Ola")

def himee(name):
    print('Hi ' + name + '!')

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
for name in girls:
    himee(name)
    print('Next girl')

