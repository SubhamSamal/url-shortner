import random

def generator(size=6, chars='abcdefghijklmnopqrstuvwxyz1234567890'):
    output = ''
    for _ in range(size):
        output += random.choice(chars)
    return output

def assignCode(instance, size=6):
    code = generator(size=size)
    urlShortner = instance.__class__
    value_exist = urlShortner.objects.filter(output=code).exists()
    if value_exist:
        return assignCode(size=size)
    return code