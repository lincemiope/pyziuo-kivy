import stack

def Move(ItemID, Amount, Cont):
    Drag(ItemID, Amount)
    EUOWait(5)
    DropC(Cont)

def MoveOnGround(ItemID, Amount, X, Y, Z):
    Drag(ItemID, Amount)
    EUOWait(5)
    DropG(X, Y, Z)
