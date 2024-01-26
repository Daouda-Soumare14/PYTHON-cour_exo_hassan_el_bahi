def somme(A, B):
    C = A + B
    print(" la somme = {}".format(C))

def soustraction(A, B):
    C = A - B
    print(" la soustraction = {}".format(C))

def multiplication(A, B):
    C = A * B
    print(" la multiplication = {}".format(C))

def division(A, B):
    while B == 0:
        print(" la valeur de B doit etre non nul")
    C = A / B
    print(" la division = {}".format(C))        
