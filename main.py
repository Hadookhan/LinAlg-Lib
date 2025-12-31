from preset_data import *
from components import Linalg

def main():

    a_b = Linalg.matdot(a,b)
    print(a_b)

    axb = Linalg.cross(vec_a,vec_b)
    print(axb)

if __name__ == '__main__':
    main()