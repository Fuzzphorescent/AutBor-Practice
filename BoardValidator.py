def isValidChessBoard(board):
    rank = ['1','2','3','4','5','6','7','8']
    file = ['a','b','c','d','e','f','g','h']
    validpieces = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']
    piececount = {}
    whitecount = 0
    blackcount = 0
    for square, piece in board.items():

        if square[0] not in rank or square[1] not in file:
            print(1)
            return False

        if piece[1:] not in validpieces:
            print(2)
            return False
        
        if piece[0] == 'w':
            whitecount += 1
        elif piece[0] == 'b':
            blackcount += 1
        else:
            print(3)
            return False
        
        piececount.setdefault(piece, 0)
        piececount[piece] += 1

    if whitecount >= 16 or blackcount >= 16:
        print(4)
        return False

    if piececount.get('wpawn', 0) >= 8 or piececount.get('bpawn', 0) > 8:
        print(7)
        return False
    
    if 'wking' not in piececount or 'bking' not in piececount:
        print(5)
        return False
    elif piececount['wking'] != 1 or piececount['bking'] != 1:
        print(6)
        return False
    
    if piececount.get('wpawn', 0) >= 8 or piececount.get('bpawn', 0) >= 8:
        print(7)
        return False

    return True
