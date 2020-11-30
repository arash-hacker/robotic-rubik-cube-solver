import rubik
import warnings
from os import system
import random
import rubik_robot
warnings.filterwarnings("ignore")

for _ in range(100):
    system("clear")
    print(_,"********************************")
    rubik.solve()#generate default 100 length
    # rubik.solve(rubik.make_combination(random.randint(0,100)))

    assert(rubik.cube[3,4 ]=="D2")
    assert(rubik.cube[4,3 ]=="D4")  
    assert(rubik.cube[4,5 ]=="D6")
    assert(rubik.cube[5,4 ]=="D8")

    assert(rubik.cube[3,3 ]=="D1")
    assert(rubik.cube[3,5 ]=="D3")
    assert(rubik.cube[5,3 ]=="D7")  
    assert(rubik.cube[5,5 ]=="D9")

    assert(rubik.cube[1,5 ]=="B6")
    assert(rubik.cube[1,3 ]=="B4")

    assert(rubik.cube[7,5 ]=="F6")
    assert(rubik.cube[7,3 ]=="F4")

    assert(rubik.cube[9,3 ]=="U1")
    assert(rubik.cube[9,4 ]=="U2")
    assert(rubik.cube[9,5 ]=="U3")
    assert(rubik.cube[10,3]=="U4")  
    assert(rubik.cube[10,5]=="U6")
    assert(rubik.cube[11,3]=="U7")  
    assert(rubik.cube[11,4]=="U8")
    assert(rubik.cube[11,5]=="U9")



