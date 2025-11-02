from lab_python_oop import *
from art import tprint

tprint("My program")

def main():
    N = 5

    cir = classСircle.Circle(N, "зелёный")
    rec = classRectangle.Rectangele(N, N, "синий")
    sq = classSquare.Square(N, "красный")
    print(cir, '\n')
    print(rec, '\n')
    print(sq, '\n')



    


if __name__ == "__main__":
    main()
