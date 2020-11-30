config={
    "U":[],
    "D":["F","F"],
    "F":["F'", "R'", "D'", "R", "F" ,"F"],
    "B":["D","L'","R","F","R'","L"],
    "L":["U","L'","U'","F"],
    "R":["U'","R'","U'","B","U","U"],
}
valids=["B","R","L"]
def moves(li):
    return {
        "B":["U'","U'"]+li+["U","U"],
        "L":["U"]+li+["U'"],
        "R":["U'"]+li+["U"],
    }
rots={
}