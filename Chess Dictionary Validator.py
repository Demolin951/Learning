chess_figures ={'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
chess_board = {
    '1a': 'wrook', '1b': 'wknight', '1c': 'wbishop', '1d': 'wqween', '1e': 'wking', '1f': 'wbishop', '1g': 'wknight', '1h': 'wrook',
    '2a': 'wpawn', '2b': 'wpawn', '2c': 'wpawn', '2d': 'wpawn', '2e': 'wpawn', '2f': 'wpawn', '2g': 'wpawn', '2h': 'wpawn',
    '3a': None, '3b': None, '3c': None, '3d': None, '3e': None, '3f': None, '3g': None, '3h': None,
    '4a': None, '4b': None, '4c': None, '4d': None, '4e': None, '4f': None, '4g': None, '4h': None,
    '5a': None, '5b': None, '5c': None, '5d': None, '5e': None, '5f': None, '5g': None, '5h': None,
    '6a': None, '6b': None, '6c': None, '6d': None, '6e': None, '6f': None, '6g': None, '6h': None,
    '7a': 'bpawn', '7b': 'bpawn', '7c': 'bpawn', '7d': 'bpawn', '7e': 'bpawn', '7f': 'bpawn', '7g': 'bpawn', '7h': 'bpawn',
    '8a': 'brook', '8b': 'bknight', '8c': 'bbishop', '8d': 'bking', '8e': 'bqween', '8f': 'bbishop', '8g': 'bknight', '8h': 'brook'}

def isValidChessBoard(x):
    for i, k in x.items():
        if chess_board[i] == k:
            return True
        else:
            return False     

print(isValidChessBoard(chess_figures))