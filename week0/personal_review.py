def main():
    name = input("what's your name? ").strip().title()
    surname = input("what's your surname? ").strip().title()
    x = round(float(input(f"hello {name} {surname}, what's X value? ")))
    print(f"dear {name}, {x} squared is {square(x)}\nand {x} cubed is {cube(x)} ")
def square(x):
    return x * x 
def cube(x):
    return x * x * x
main()
