config={
    "L":["U","F","U'"],
    "F":["R"],
    "D":["D'","D'","R","R"],
    "R":["R","R","F","D","R","R"],
    "B":["U'","B'","B'","U","R'"],
    "U":[],
}
valids=["B","L"]
def moves(li):
    return {
        "B":["U'"]+li+["U"],
        "L":["U","U"]+li+["U'","U'"],
    }
rots={
    1:["F","U","F'","U'"]
}