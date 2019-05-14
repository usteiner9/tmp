def yell(text):
    return text.upper() + '!'

print(yell('hello'))

bark = yell

print(bark('woof'))

print(bark.__name__)

funcs = [bark, str.lower, str.capitalize]
print(funcs)

for f in funcs:
    print(f, f('hey there'))

print(funcs[0]('heyho'))
print(funcs[1]('heyho'))
print(funcs[2]('heyho'))
