import numpy as np 
import warnings
import random
from os import system
from rubik_robot.robot import reverse_move, do_rotations
warnings.filterwarnings("ignore")
from config import u2,u4,u6,u8,u1,u3,u7,u9
def draw():
    print()
    for row in cube:
        for x in row:
            if x=="XX":    print(" ⬛️" +x,end="")
            elif x[0]=="R":print(" 💔" +x,end="")
            elif x[0]=="L":print(" 📙" +x,end="")
            elif x[0]=="B":print(" 💙" +x,end="")
            elif x[0]=="F":print(" 💚" +x,end="")
            elif x[0]=="U":print(" ⚪️" +x,end="")
            elif x[0]=="D":print(" 💛" +x,end="")
        print()

def reverse_move(moves):
    l=[]
    for m in moves:
        if len(m)==2:
            l+=[m[0]]
        else:
            l+=[m[0]+"'"]
    return l 

cube=np.array([
    ["XX" ,"XX" ,"XX" ,"B1" ,"B2" ,"B3" ,"XX" ,"XX" ,"XX"],
    ["XX" ,"XX" ,"XX" ,"B4" ,"B5" ,"B6" ,"XX" ,"XX" ,"XX"],
    ["XX" ,"XX" ,"XX" ,"B7" ,"B8" ,"B9" ,"XX" ,"XX" ,"XX"],
    ["L1" ,"L2" ,"L3" ,"D1" ,"D2" ,"D3" ,"R1" ,"R2" ,"R3"],
    ["L4" ,"L5" ,"L6" ,"D4" ,"D5" ,"D6" ,"R4" ,"R5" ,"R6"],
    ["L7" ,"L8" ,"L9" ,"D7" ,"D8" ,"D9" ,"R7" ,"R8" ,"R9"],
    ["XX" ,"XX" ,"XX" ,"F1" ,"F2" ,"F3" ,"XX" ,"XX" ,"XX"],
    ["XX" ,"XX" ,"XX" ,"F4" ,"F5" ,"F6" ,"XX" ,"XX" ,"XX"],
    ["XX" ,"XX" ,"XX" ,"F7" ,"F8" ,"F9" ,"XX" ,"XX" ,"XX"],
    ["XX" ,"XX" ,"XX" ,"U1" ,"U2" ,"U3" ,"XX" ,"XX" ,"XX"],
    ["XX" ,"XX" ,"XX" ,"U4" ,"U5" ,"U6" ,"XX" ,"XX" ,"XX"],
    ["XX" ,"XX" ,"XX" ,"U7" ,"U8" ,"U9" ,"XX" ,"XX" ,"XX"]])

cube_template=np.array(cube)
rotates={
    'R':[*(11,5),*(10,5),*(9,5),*(0,3),*(1,3),*(2,3),*(3,3),*(4,3),*(5,3),*(8,5),*(7,5),*(6,5)],
    'L':[*(9,3),*(10,3),*(11,3),*(6,3),*(7,3),*(8,3),*(5,5),*(4,5),*(3,5),*(2,5 ),*(1,5),*(0,5)],
    'F':[*(11,3),*(11,4),*(11,5),*(3,6),*(4,6 ),*(5,6 ),*(5,3),*(5,4),*(5,5),*(5,2),*(4,2),*(3,2)],
    'U':[*(3,8),*(3,7),*(3,6),*(6,5),*(6,4),*(6,3),*(3,2),*(3,1),*(3,0),*(0,5 ),*(0,4 ),*(0,3 )],
    'D':[*(2,3),*(2,4),*(2,5),*(5,0),*(5,1),*(5,2),*(8,3 ),*(8,4 ),*(8,5 ),*(5,6),*(5,7),*(5,8)],
    'B':[*(9,5),*(9,4),*(9,3),*(3,0),*(4,0),*(5,0),*(3,5),*(3,4),*(3,3),*(5,8),*(4,8),*(3,8)],
}

rotates={
    'R':(tuple(rotates['R'][::2]),tuple(rotates['R'][1::2] )),
    'L':(tuple(rotates['L'][::2]),tuple(rotates['L'][1::2] )),
    'F':(tuple(rotates['F'][::2]),tuple(rotates['F'][1::2] )),
    'U':(tuple(rotates['U'][::2]),tuple(rotates['U'][1::2] )),
    'D':(tuple(rotates['D'][::2]),tuple(rotates['D'][1::2] )),
    'B':(tuple(rotates['B'][::2]),tuple(rotates['B'][1::2] )),
}

faces={
    'R':(slice(3,6) ,slice(6,9)),
    'L':(slice(3,6 ),slice(0,3)),
    'F':(slice(6,9 ),slice(3,6)),
    'U':(slice(9,12),slice(3,6)),
    'D':(slice(3,6 ),slice(3,6)),
    'B':(slice(0,3 ),slice(3,6)),
}
moves=[
    "F", "B", "L", "R", "U", "D",
    "F'","B'","L'","R'","U'","D'"
]
combinations=[]
view_port={
    "UF":''
}
layer_3_conf={
    (3,3):(["D1","B7","R9"],["D","D"]),
    (3,5):(["D3","B9","L7"],["D"]),
    (5,3):(["D7","F9","R7"],["D'"]),
    (5,5):(["D9","F7","L9"],[]),
}
def rotate(rot):
    row=rotates[rot[0]]
    f=faces[rot[0]]
    if len(rot)==1:
        cube[f[0],f[1]]=np.rot90(cube[f[0],f[1]],3)
        cube[rotates[rot[0]]]=cube[(row[0][9:]+row[0][:9]),(row[1][9:]+row[1][:9])]
    else:
        cube[f[0],f[1]]=np.rot90(cube[f[0],f[1]])
        cube[rotates[rot[0]]]=cube[(row[0][3:]+row[0][:3]),(row[1][3:]+row[1][:3])]

def make_combination(n):
    l=[]
    for i in range(n):
        l+=[random.choice(moves)]
    return l

def do_rotations(cc):
    for c in cc:
        rotate(c)

conv_conf={
    2:{(0,1):0,(1,0):3,(2,1):2,-1:1},
    4:{(0,1):1,(1,0):0,(2,1):3,-1:2},
    6:{(0,1):3,(1,0):2,(2,1):1,-1:0},
    8:{(0,1):2,(1,0):1,(2,1):0,-1:3},
}
def conv(y,x):
    face=cube_template[y,x][0]
    xy=np.where(cube[faces[face][0],faces[face][1]]==cube[y,x])
    xy=(xy[0][0],xy[1][0])
    rot=conv_conf.get(int(cube[y,x][1]),{})
    rot = rot.get(xy,rot.get(-1)) or 0
    return (face,rot)



def trans_u2(face,rot):
    do_rotations([face+"'"]*rot)
    do_rotations(u2.config[face])
    
def trans_u4(face,rot):
    if face == "U":
        rot==2 and do_rotations(["R'","U'","U'","R","U","U"])
        rot==3 and do_rotations(["U","L","U''","L'"])
        return
    face =="B" and do_rotations(["U"]+([face+"'"]*rot)+["U'"])
    face != "B" and do_rotations(([face+"'"]*rot))
    do_rotations(u4.config[face])

def trans_u6(face,rot):
    if face == "U":
        rot==1 and do_rotations(["F","U","F'","U'"])
        return
    face =="B" and do_rotations(["U'"]+([face+"'"]*rot)+["U"])
    face =="L" and do_rotations(["U","U"]+([face+"'"]*rot)+["U'","U'"])
    face not in ["B","L"] and do_rotations([face+"'"]*rot)
    do_rotations(u6.config[face])


def trans_u8(face,rot):
    face =="B" and do_rotations(["U'","U'"]+([face+"'"]*rot)+["U","U"]) 
    face =="L" and do_rotations(["U"]+([face+"'"]*rot)+["U'"]) 
    face =="R" and do_rotations(["U'"]+([face+"'"]*rot)+["U"]) 
    face not in ["R","L","B"] and do_rotations([face+"'"]*rot)   
    do_rotations(u8.config[face])


def trans_u1(f,*args):
    face=f
    while face!="D":
        xy=np.where(cube=='U1') 
        face,_=conv(xy[0][0],xy[1][0])
        if face=="D":
            break
        xy=np.where(cube[faces[face][0],faces[face][1]]=="U1")
        y,x=xy[0][0],xy[1][0]

        if face=="U" :
            if  (y,x)==(0,0):
                break
            do_rotations(u1.config[(y,x)])
        do_rotations(u1.config.get((face,(y,x)),[]) )

    
    xy=np.where(cube=='U1') 
    face,r=conv(xy[0][0],xy[1][0])
    xy=np.where(cube[faces[face][0],faces[face][1]]=="U1")
    y,x=xy[0][0],xy[1][0]
    do_rotations(u1.config.get((face,(y,x)),[]) )

def trans_u3(f,*args):
    face=f
    while face!="D":
        xy=np.where(cube=='U3') 
        face,_=conv(xy[0][0],xy[1][0])
        if face=="D":
            break
        xy=np.where(cube[faces[face][0],faces[face][1]]=="U3")
        y,x=xy[0][0],xy[1][0]
        if face=="U" :
            if  (y,x)==(0,2):
                break
            elif (y,x)==(0,0):
                raise Exception("Never will happen")
            elif (y,x)==(2,0):
                do_rotations(["L","D","L'"])
            elif (y,x)==(2,2):
                do_rotations(["R'","D'","R"])
        elif y==0:
            if face=="F" and x==2:
                do_rotations(["R'","D","R"])
            if face=="F" and x==0:
                do_rotations(["L","D","L'"])

            if face=="L" and x==2:
                do_rotations(["F'","D","F"])
            if face=="L" and x==0:
                do_rotations(["B","D","B'"])

            if face=="B" and x==2:
                do_rotations(["B","D","B'"])
            if face=="B" and x==0:
                do_rotations(["R","D","R'"])

            if face=="R" and x==2:
                do_rotations(["B'","D","B"])
            if face=="R" and x==0:
                do_rotations(["F","D","F'"])

        elif  y==2:
            if face=="F" and x==2:
                do_rotations(["R'","D","R"])
            if face=="F" and x==0:
                do_rotations(["L","D","L'"])

            if face=="L" and x==2:
                do_rotations(["F'","D","D","F"])
            if face=="L" and x==0:
                do_rotations(["D","D","L","D'","L'"])

            if face=="R" and x==2:
                do_rotations(["D'","D'","R'","D","R"])
            if face=="R" and x==0:
                do_rotations(["F","D","F'"])

            if face=="B"  and x==2:
                do_rotations(["F","D","F'"])
            if face=="B"  and x==0:
                do_rotations(["D","F","D","F'"])
    if face=="D":
        xy=np.where(cube=='U3') 
        face,r=conv(xy[0][0],xy[1][0])
        xy=np.where(cube[faces[face][0],faces[face][1]]=="U3")
        y,x=xy[0][0],xy[1][0]
        if (y,x) == (0,0) :
            do_rotations(["D"])
        if (y,x) == (0,2) :
            ...
        if (y,x) == (2,0) :
            do_rotations(["D","D"])
        if (y,x) == (2,2) :
            do_rotations(["D'"])
        
        do_rotations(["D'"])
        do_rotations(["B'","D","D","B","D","B'","D'","B"])
        ...
    #F D F'
    #R' D2 R D R' D' R
    ...

def trans_u7(f,*args):
    face=f
    while face!="D":
        xy=np.where(cube=='U7') 
        face,_=conv(xy[0][0],xy[1][0])
        if face=="D":
            break
        xy=np.where(cube[faces[face][0],faces[face][1]]=="U7")
        y,x=xy[0][0],xy[1][0]
        if face=="U" :
            if (y,x)==(0,0) or (y,x)==(0,2) :
                raise Exception("Never will happen")
            elif (y,x)==(2,0):
                break
            elif (y,x)==(2,2):
                do_rotations(["R'","D'","D'","R"])

        elif y==0:
            if face=="F" and x==2:
                do_rotations(["R'","D","R"])
            if face=="F" and x==0:
                do_rotations(["L","D","L'"])

            if face=="L" and x==2:
                do_rotations(["F'","D","F"])
            if face=="L" and x==0:
                raise Exception("imposiible L 0,0")
                do_rotations(["B","D","B'"])

            if face=="B" and x==2:
                raise Exception("imposiible B 0,2")
                do_rotations(["B","D","B'"])
            if face=="B" and x==0:
                raise Exception("imposiible B 0,0")
                do_rotations(["R","D","R'"])

            if face=="R" and x==2:
                raise Exception("imposiible R 0,2")
                do_rotations(["B'","D","B"])
            if face=="R" and x==0:
                do_rotations(["F","D","F'"])

        elif  y==2:
            if face=="F" and x==2:
                do_rotations(["R'","D","D","R"])
            if face=="F" and x==0:
                do_rotations(["L","D","D","L'"])

            if face=="L" and x==2:
                do_rotations(["R'","D","D","R"])
            if face=="L" and x==0:
                do_rotations(["D","D","L","D'","L'"])

            if face=="R" and x==2:
                do_rotations(["D'","D'","R'","D","D","R"])
            if face=="R" and x==0:
                do_rotations(["D","F","D'","F'"])

            if face=="B"  and x==2:
                do_rotations(["D'","D'","R'","D","R"])
            if face=="B"  and x==0:
                do_rotations(["D","D","R'","D'","D'","R"])

    if face=="D":
        xy=np.where(cube=='U7') 
        face,r=conv(xy[0][0],xy[1][0])
        xy=np.where(cube[faces[face][0],faces[face][1]]=="U7")
        y,x=xy[0][0],xy[1][0]
        if (y,x) == (0,0) :
            do_rotations(["D'"])
        if (y,x) == (0,2) :
            do_rotations(["D'","D'"])
        if (y,x) == (2,0) :
            ...
        if (y,x) == (2,2) :
            do_rotations(["D"])
        
        do_rotations(["D"])
        do_rotations(["U","U","B'","D","D","B","D","B'","D'","B","U'","U'"])
        ...
    #F D F'
    #R' D2 R D R' D' R
    ...

def trans_u9(f,*args):
    face=f
    while face!="D":
        xy=np.where(cube=='U9') 
        face,_=conv(xy[0][0],xy[1][0])
        if face=="D":
            break
        xy=np.where(cube[faces[face][0],faces[face][1]]=="U9")
        y,x=xy[0][0],xy[1][0]

        if face=="U" :
            if (y,x) in [(0,0), (y,x)==(0,2) ,(2,0)]:
                raise Exception("Never will happen")
            elif (y,x)==(2,2):
                break

        elif y==0:
            if face=="F" and x==2:
                do_rotations(["R'","D'","R"])
            if face=="F" and x==0:
                raise Exception("imposiible F 0,0")

            if face=="L" and x==2:
                do_rotations(["F'","D","F"])
            if face=="L" and x==0:
                raise Exception("imposiible L 0,0")

            if face=="B" and x==2:
                raise Exception("imposiible B 0,2")
            if face=="B" and x==0:
                raise Exception("imposiible B 0,0")

            if face=="R" and x==2:
                raise Exception("imposiible R 0,2")
            if face=="R" and x==0:
                do_rotations(["F","D","F'"])

        elif  y==2:
            if face=="F" and x==2:
                do_rotations(["D'","R'","D","R"])
            if face=="F" and x==0:
                do_rotations(["D","F","D","D","F'"])

            if face=="L" and x==2:
                do_rotations(["R'","D","R"])
            if face=="L" and x==0:
                do_rotations(["D",])

            if face=="R" and x==2:
                do_rotations(["D'","D'","R'","D","D","R"])
            if face=="R" and x==0:
                do_rotations(["D","F","D'","F'"])

            if face=="B"  and x==2:
                do_rotations(["D'","D'","R'","D","R"])
            if face=="B"  and x==0:
                do_rotations(["D","D","R'","D'","D'","R"])

    if face=="D":
        xy=np.where(cube=='U9') 
        face,r=conv(xy[0][0],xy[1][0])
        xy=np.where(cube[faces[face][0],faces[face][1]]=="U9")
        y,x=xy[0][0],xy[1][0]
        if (y,x) == (0,0) :
            do_rotations(["D'","D'"])
        if (y,x) == (0,2) :
            do_rotations(["D"])
        if (y,x) == (2,0) :
            do_rotations(["D'"])
        if (y,x) == (2,2) :
            ...
        
        do_rotations(["D'","D'"])
        do_rotations(["U","U","U","B'","D","D","B","D","B'","D'","B","U'","U'","U'"])
        ...
    #F D F'
    #R' D2 R D R' D' R
    ...




def middle_layers_f4(y,x):
    
    if (y,x)==(7,3):
        return
    
    D_link=[(3,4), (4,3), (4,5), (5,4)]
    if (y,x) in [(7,5),(4,6),(4,8),(1,3),(1,5),(4,0),(4,2)]: #redirect it to layer3
        f4=np.where(cube=='F4') 
        yy,xx=f4[0][0],f4[1][0]
        while (yy,xx) not in D_link:
            do_rotations(["D","L","D'","L'","D'","F'","D","F"])
            do_rotations(["D","B","D'","B'","D'","L'","D","L"])
            do_rotations(["D","R","D'","R'","D'","B'","D","B"])
            do_rotations(["D","F","D'","F'","D'","R'","D","R"])
            f4=np.where(cube=='F4') 
            yy,xx=f4[0][0],f4[1][0]

    f4=np.where(cube=='F4') 
    y,x=f4[0][0],f4[1][0] 
    
    if (y,x) in D_link:
        (y,x)==(3,4) and do_rotations(["D","D"])
        (y,x)==(4,3) and do_rotations(["D'"])
        (y,x)==(4,5) and do_rotations(["D"])
        (y,x)==(5,4) and do_rotations([])
        do_rotations(["D'","D'","F'","D","F","D","L","D'","L'"])
        return
    
    f4=np.where(cube=='F4') 
    y,x=f4[0][0],f4[1][0] 
    (y,x) == (2,4) and do_rotations(["D","D"]+["D","L","D'","L'","D'","F'","D","F"])
    (y,x) == (5,1) and do_rotations(["D"]+["D","L","D'","L'","D'","F'","D","F"])
    (y,x) == (5,7) and do_rotations(["D'"]+["D","L","D'","L'","D'","F'","D","F"])
    (y,x) == (8,4) and do_rotations([]+["D","L","D'","L'","D'","F'","D","F"])

def middle_layers_f6(y,x):
    
    if (y,x)==(7,5):
        return

    D_link=[(3,4), (4,3), (4,5), (5,4)]
    #to_left  ["U'","L'","U","L","U","F","U'","F'"]
    #to_right ["U","R","U'","R'","U'","F'","U","F"]
    if (y,x) in [(4,6),(4,8),(1,3),(1,5),(4,0)]: #redirect it to layer3
        (y,x)==(1,5) and do_rotations([ "D", "B", "D'", "B'", "D'", "L'", "D", "L"])#B6√
        (y,x)==(4,0) and do_rotations([ "D", "B", "D'", "B'", "D'", "L'", "D", "L"])#L4√
        (y,x)==(4,6) and do_rotations([ "D", "F", "D'", "F'", "D'", "R'", "D", "R"])#R4√ 
        (y,x)==(4,8) and do_rotations([ "D", "R", "D'", "R'", "D'", "B'", "D", "B"])#R6√
        (y,x)==(1,3) and do_rotations([ "D", "R", "D'", "R'", "D'", "B'", "D", "B"])#B4√ 


    f6=np.where(cube=='F6') 
    y,x=f6[0][0],f6[1][0] 
    if (y,x) in D_link:
        (y,x)==(3,4) and do_rotations(["D","D"])
        (y,x)==(4,3) and do_rotations(["D'"])
        (y,x)==(4,5) and do_rotations(["D"])
        (y,x)==(5,4) and do_rotations([])
        do_rotations(["D","D","F","D'","F'","D'","R'","D","R"])
        return
    
    #layer #3
    f6=np.where(cube=='F6') 
    y,x=f6[0][0],f6[1][0] 
    # 
    (y,x) == (2,4) and do_rotations(["D","D"]+["D'","R'","D","R","D","F","D'","F'"])
    (y,x) == (5,1) and do_rotations(["D"]+["D'","R'","D","R","D","F","D'","F'"])
    (y,x) == (5,7) and do_rotations(["D'"]+["D'","R'","D","R","D","F","D'","F'"])
    (y,x) == (8,4) and do_rotations([]+["D'","R'","D","R","D","F","D'","F'"])

def middle_layers_b4(y,x):
    
    if (y,x)==(1,3):
        return
    D_link=[(3,4), (4,3), (4,5), (5,4)]
    #to_left  ["U'","L'","U","L","U","F","U'","F'"]
    #to_right ["U","R","U'","R'","U'","F'","U","F"]
    #LB to_R
    (y,x)==(1,5) and do_rotations([ "D", "B", "D'", "B'", "D'", "L'", "D", "L"])#B6√
    (y,x)==(4,0) and do_rotations([ "D", "B", "D'", "B'", "D'", "L'", "D", "L"])#L4√
    #BR to_R
    (y,x)==(4,8) and do_rotations([ "D", "R", "D'", "R'", "D'", "B'", "D", "B"])#R6√
    (y,x)==(1,3) and do_rotations([ "D", "R", "D'", "R'", "D'", "B'", "D", "B"])#B4√ 


    b4=np.where(cube=='B4') 
    y,x=b4[0][0],b4[1][0] 


    if (y,x) in D_link:
        (y,x)==(3,4) and do_rotations(["D","D"])
        (y,x)==(4,3) and do_rotations(["D'"])
        (y,x)==(4,5) and do_rotations(["D"])
        (y,x)==(5,4) and do_rotations([])
        do_rotations(["D"]+["D'" ,"B'" ,"D" ,"B" ,"D" ,"R" ,"D'", "R'"])
        return
    
    b4=np.where(cube=='B4') 
    y,x=b4[0][0],b4[1][0] 

    s=["D", "R", "D'", "R'", "D'", "B'", "D", "B"]
    (y,x) == (2,4) and do_rotations([]+s)
    (y,x) == (5,1) and do_rotations(["D'"]+s)
    (y,x) == (5,7) and do_rotations(["D"]+s)
    (y,x) == (8,4) and do_rotations(["D","D"]+s)

def middle_layers_b6(y,x):
    
    if (y,x)==(1,5):
        return

    D_link=[(3,4), (4,3), (4,5), (5,4)]
    #LB to_R
    (y,x)==(1,5) and do_rotations([ "D", "B", "D'", "B'", "D'", "L'", "D", "L"])#B6√
    (y,x)==(4,0) and do_rotations([ "D", "B", "D'", "B'", "D'", "L'", "D", "L"])#L4√


    b6=np.where(cube=='B6') 
    y,x=b6[0][0],b6[1][0]  
    
    if (y,x) in D_link:
        (y,x)==(3,4) and do_rotations(["D","D"])
        (y,x)==(4,3) and do_rotations(["D'"])
        (y,x)==(4,5) and do_rotations(["D"])
        (y,x)==(5,4) and do_rotations([])
        do_rotations(["D'"]+["D", "B", "D'", "B'" ,"D'" ,"L'" ,"D" ,"L"])
        return
    
    b6=np.where(cube=='B6') 
    y,x=b6[0][0],b6[1][0] 

    s=["D'", "L'", "D", "L", "D", "B", "D'", "B'"]
    (y,x) == (2,4) and do_rotations([]+s)
    (y,x) == (5,1) and do_rotations(["D'"]+s)
    (y,x) == (5,7) and do_rotations(["D"]+s)
    (y,x) == (8,4) and do_rotations(["D","D"]+s)



def count_cross():
    return sum([cube[3,4][0]=="D",cube[4,3][0]=="D",cube[4,5][0]=="D",cube[5,4][0]=="D"] )

def is_L_shape():
    return  ((cube[3,4][0]=="D")+(cube[4,5][0]=="D"))==2 or\
            ((cube[4,5][0]=="D")+(cube[5,4][0]=="D"))==2 or\
            ((cube[5,4][0]=="D")+(cube[4,3][0]=="D"))==2 or\
            ((cube[4,3][0]=="D")+(cube[3,4][0]=="D"))==2

def is_line_shape():
    return  ((cube[4,3][0]=="D")+(cube[4,5][0]=="D"))==2 or\
            ((cube[3,4][0]=="D")+(cube[5,4][0]=="D"))==2

def make_L_shape_correct():
    while ((cube[4,3][0]=="D")+(cube[3,4][0]=="D"))!=2:
        do_rotations(["D"])

def make_line_shape_correct():
    while ((cube[4,3][0]=="D")+(cube[4,5][0]=="D"))!=2:
        do_rotations(["D"])

def top_cross():
    f=["F","L","D","L'","D'","F'"]
    while count_cross()!=4:
        if count_cross()==0:
            do_rotations(f*3)
            if count_cross()!=2:
                do_rotations(f*2)

        elif count_cross()==2 :
            if is_L_shape():
                make_L_shape_correct()
                do_rotations(f*2)
                return
            elif is_line_shape():
                make_line_shape_correct()
                do_rotations(f*1)
                return

def count_D_corrected():
    return sum([
        cube[3,4]=="D2",
        cube[4,3]=="D4",
        cube[4,5]=="D6",
        cube[5,4]=="D8",
    ])

def make_d2_correct():
    d2=np.where(cube=='D2') 
    y,x=d2[0][0],d2[1][0]
    (y,x)==(4,3) and do_rotations(["D",])
    (y,x)==(5,4) and do_rotations(["D'","D'"])
    (y,x)==(4,5) and do_rotations(["D'"])
        
def swap_last_edges():

    f=["L","D","L'","D","L","D","D","L'","D"]
    make_d2_correct()
    while count_D_corrected()!=4:
        c=count_D_corrected()
        c==1 and cube[4,5]=="D8" and do_rotations(f+["D"]+f+["D'"])#2 6 8 4
        c==1 and cube[4,5]=="D4" and do_rotations(["D"]+f+["D'"]+f)#2 8 4 6 
        c==2 and cube[4,5]=="D4" and do_rotations(["D"]+f+["D'"]+f+["D"]+f+["D'"])#2 6 4 8 
        c==2 and cube[4,5]=="D8" and do_rotations(f+["D"]+f+["D'"])#2 4 8 6 
        c==2 and cube[4,5]=="D6" and do_rotations(f)#2 8 6 4 
        # make_d2_correct()

def get_yx(yx):
    return (yx[0][0],yx[1][0])

def count_correct_corners():
    return sum([
        True for k in list(layer_3_conf.keys()) if cube[k] in layer_3_conf[k][0]
    ])

def detect_good_corners():
    for k in list(layer_3_conf.keys()):
        if cube[k] in layer_3_conf[k][0]:
            do_rotations(
                 layer_3_conf[k][1]+
                 ["D","L","D'","R'","D","L'","D'","R"]+
                 reverse_move(layer_3_conf[k][1]))

def swap_corners():
    while count_correct_corners()!=4:
        if count_correct_corners()==0:
            do_rotations(["D","L","D'","R'","D","L'","D'","R"])
        elif count_correct_corners()==1:
            detect_good_corners()
    for k in list(layer_3_conf.keys()):
        while cube[k] != layer_3_conf[k][0][0]:
            do_rotations(
                 layer_3_conf[k][1]+
                 ["L'","U'","L","U"]+
                 reverse_move(layer_3_conf[k][1]))

def solve(comb=[]):
    combinations=comb or make_combination(100)
    do_rotations(combinations)
    draw()
    trans_u2(*conv(  *get_yx(np.where(cube=='U2'))))
    trans_u4(*conv(  *get_yx(np.where(cube=='U4'))))  
    trans_u6(*conv(  *get_yx(np.where(cube=='U6'))))
    trans_u8(*conv(  *get_yx(np.where(cube=='U8')))) 
    trans_u1(*conv(  *get_yx(np.where(cube=='U1')))) 
    trans_u3(*conv(  *get_yx(np.where(cube=='U3'))))
    trans_u7(*conv(  *get_yx(np.where(cube=='U7')))) 
    trans_u9(*conv(  *get_yx(np.where(cube=='U9')))) 
    middle_layers_f4(*get_yx(np.where(cube=='F4')))
    middle_layers_f6(*get_yx(np.where(cube=='F6')))
    middle_layers_b4(*get_yx(np.where(cube=='B4')))
    middle_layers_b6(*get_yx(np.where(cube=='B6')))
    top_cross()
    swap_last_edges()
    swap_corners()
    draw()


