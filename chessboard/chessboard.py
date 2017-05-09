#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# chessboard
#

'''
For special chessboard problem.
'''

class ChessBoard():
    '''
    Class for base chessboard.
        row:the chessboard row num.
        col:the chessboard col num.
    '''
    def __init__(self,row=1,col=1):
        self._row = row
        self._col = col
        self._data = [[None]*col for i in range(row) ]

    def getRowMaxNum(self):
        '''
        Get this chessboard row length .
        '''
        return self._row

    def getColMaxNum(self):
        '''
        Get this chessboard col length.
        '''
        return self._col

    def getBoard(self,irow,icol):
        '''
        Get chessboard block by [irow][icol].
        '''
        return self._data[irow][icol]

    def setBoard(self,irow,icol,data):
        '''
        Set data to chessboard block by [irow][icol].
        '''
        self._data[irow][icol] = data

    def __str__(self):
        return 'row:{};col:{}\ndata:{}'.format(self._row,self._col,self._data)


class RelativeChessBoard():
    '''
    Get a chessboard in a chessboard.
        rwo:new chessboard row.
        col:new chessboard col.
        relative_row_start_pos:this chessboard row relative to main chessboard.
        relative_col_start_pos:this chessboard col relative to main chessboard.
    '''
    def __init__(self,chessboard,row,col,
                 relative_row_start_pos=0,
                 relative_col_start_pos=0
                 ):
        if (row + relative_row_start_pos > chessboard.getRowMaxNum() or
            col + relative_col_start_pos > chessboard.getColMaxNum()):
            raise ValueError('Out of range of chessboard!')
        self._row = row
        self._col = col
        self._rel_row = relative_row_start_pos
        self._rel_col = relative_col_start_pos
        self._chessboard = chessboard

    def getBoard(self,irow,icol):
        '''
        Get chessboard block by [irow][icol].
        '''
        if irow >= self._row or icol >= self._col:
            raise IndexError('Index out of range!')
        return self._data[irow+self._rel_row][icol+self._rel_col]

    def setBoard(self,irow,icol,data):
        '''
        Set data to chessboard block by [irow][icol].
        '''
        self._data[irow+self._rel_row][icol+self._rel_col] = data

    def __str__(self):
        return 'relative row:{} ,relative col:{} ; row:{} , col:{}'.format(
            self._rel_row,self._rel_col,self._row,self._col)

class SpecialChessBoard():
    def __init__(self,chessboard):
        self._chessboard = chessboard

    def __getattr__(self,attribute):
        return getattr(self._chessboard,attribute)

    def __str__(self):
        return str(self._chessboard)

def main():
    cb = ChessBoard(2,4)
    cb = SpecialChessBoard(cb)
    cb.setBoard(1,2,5)
    cb.setBoard(0,3,6)
    rc = RelativeChessBoard(cb,1,4,1,0)
    print(cb)
    print(rc)


if __name__ == '__main__':
    main()