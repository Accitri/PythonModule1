

def unknownSide():
    knownSides = int(input("Do you know the length of the hypotenuse and a katet(1), or the length of two katets(2)? "))
    if (knownSides == 1):
        a = int(input("What is the length of a? "))
        h = int(input("What is the length of h? "))
        bPowered = (h**2)-(a**2)
        b = bPowered ** 0.5
        print("The length of the other katet, is", b)
    if (knownSides == 2):
        a = int(input("What is the length of a? "))
        b = int(input("What is the length of b? "))
        hPowered = (a**2)+(b**2)
        h = hPowered ** 0.5
        print("The length of the hypotenuse is", h)

unknownSide()
