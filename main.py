from preset_data import *
from components import Linalg

def main():

    a_b = Linalg.matdot(a,b)
    print(a_b)

    Op1 = Linalg.vector_from_points(Origin,p1)
    Op2 = Linalg.vector_from_points(Origin,p2)

    print(f'O->p1 : {Op1}\nO->p2 : {Op2}')

    print(f'Op1 x Op2 : {Linalg.cross(Op1,Op2)}')

    p1p2 = Linalg.vector_from_points(Op1,Op2)
    print(f'p1->p2 : {p1p2}')

    detA = Linalg.determinant(A)
    print(detA)

    print(Linalg.cofactor(A))

if __name__ == '__main__':
    main()