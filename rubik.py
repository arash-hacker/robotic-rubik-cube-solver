import numpy as np 
import warnings
import random
from os import system
from rubik_robot.robot import reverse_move, do_rotations
warnings.filterwarnings("ignore")
from config import u2,u4,u6,u8,u1,u3,u7,u9,f4,f6,b4,b6
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
    
def trans_layer_1(face,rot,UU):
    uu=globals()[str(UU).lower()]
    if face == "U":
        do_rotations(uu.rots.get(rot,[]))
        return
    face in uu.valids and do_rotations(uu.moves([face+"'"]*rot).get(face,[])) 
    face not in uu.valids and do_rotations([face+"'"]*rot)   
    do_rotations(uu.config[face])

def trans_uu(f,rot,UU):
    face=f
    uu=globals()[str(UU).lower()]
    while face!="D":
        xy=np.where(cube==UU) 
        face,_=conv(xy[0][0],xy[1][0])
        if face=="D":
            break
        xy=np.where(cube[faces[face][0],faces[face][1]]==UU)
        y,x=xy[0][0],xy[1][0]
        if face=="U" :
            if (y,x) in uu.break_points:
                break
            do_rotations(uu.config.get((y,x),[]))
        do_rotations(uu.config.get((face,(y,x)),[]) )

    xy=np.where(cube==UU) 
    face,r=conv(xy[0][0],xy[1][0])
    xy=np.where(cube[faces[face][0],faces[face][1]]==UU)
    y,x=xy[0][0],xy[1][0]
    do_rotations(uu.config.get((face,(y,x)),[]) )

def middle_layers(y,x,UU):
    uu=globals()[str(UU).lower()]
    if (y,x)==uu.goal:
        return
    D_link=[(3,4), (4,3), (4,5), (5,4)]
    if (y,x) in uu.redirect_possible: #redirect it to layer3
        f4=np.where(cube==UU) 
        yy,xx=f4[0][0],f4[1][0]
        if UU=="F4":
            while (yy,xx) not in D_link:
                do_rotations(uu.mut)
                f4=np.where(cube==UU) 
                yy,xx=f4[0][0],f4[1][0]
        else:
            do_rotations(uu.mut_points[(y,x)])
    f4=np.where(cube==UU) 
    y,x=f4[0][0],f4[1][0] 
    if (y,x) in D_link:
        do_rotations( uu.d_link_mut.get((y,x),[]) )
        return
    f4=np.where(cube==UU) 
    y,x=f4[0][0],f4[1][0] 
    do_rotations(uu.middle_corner.get((y,x),[]))

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
    trans_layer_1(*conv(  *get_yx(np.where(cube=='U4'))),"U4")  
    trans_layer_1(*conv(  *get_yx(np.where(cube=='U6'))),"U6")
    trans_layer_1(*conv(  *get_yx(np.where(cube=='U8'))),"U8") 
    trans_uu(*conv(  *get_yx(np.where(cube=='U1'))),"U1") 
    trans_uu(*conv(  *get_yx(np.where(cube=='U3'))),"U3")
    trans_uu(*conv(  *get_yx(np.where(cube=='U7'))),"U7") 
    trans_uu(*conv(  *get_yx(np.where(cube=='U9'))),"U9") 
    middle_layers(*get_yx(np.where(cube=='F4')),"F4")
    middle_layers(*get_yx(np.where(cube=='F6')),"F6")
    middle_layers(*get_yx(np.where(cube=='B4')),"B4")
    middle_layers(*get_yx(np.where(cube=='B6')),"B6")
    top_cross()
    swap_last_edges()
    swap_corners()
    draw()


