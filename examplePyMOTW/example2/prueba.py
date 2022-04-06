def c(input):
    print( 'input =', input)
    print( 'Leaving c()')

def b(arg):
    val = arg * 5
    c(val)
    print( 'Leaving b()')

def a():
    b(2)
    print( 'Leaving a()')