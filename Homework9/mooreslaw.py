import sys

def mooresLaw(n):
    speed=1
    for i in range (0,120,n):
        speed*=2

    print(f"Processing speed would increase by a factor of {speed} in the next decade")

mooresLaw(sys.argv[1])