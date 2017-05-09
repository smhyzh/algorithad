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

    def inChessBoard(self,irow,icol):
        '''
        If (irow,icol) block in chessboard,return True,else return False.
        '''
        if irow < self.getRowMaxNum() and icol < self.getColMaxNum():
            return True
        else:
            return False

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
        if irow >= self._row or icol >= self._col:
            raise IndexError('Index out of range!')
        return self._chessboard.getBoard(irow+self._rel_row,icol+self._rel_col)

    def setBoard(self,irow,icol,data):
        '''
        Set data to chessboard block by [irow][icol].
        '''
        self._chessboard.setBoard(irow+self._rel_row,icol+self._rel_col,data)

    def inChessBoard(self,irow,icol):
        '''
        If (irow,icol) block in chessboard,return True,else return False.
        '''
        if irow < self.getRowMaxNum() and icol < self.getColMaxNum():
            return True
        else:
            return False

    def __str__(self):
        return 'relative row:{} ,relative col:{} ; row:{} , col:{}'.format(
            self._rel_row,self._rel_col,self._row,self._col)

class DominoL():
    '''
    L type domino.
        corner_block:the pos(rwo,col) of corner block of L domino.
        out_block:the pos(row,col) of block which next to L domino.
    '''
    def __init__(self,corner_block=(0,0),out_block=(0,0)):

        self._blocks = self._getBlocksPos(corner_block,out_block)

    def _getBlocksPos(self,corner_block,out_block):
        '''
        Get the three pos of block by corner block and out block.
        '''
        if corner_block[0] + 1 == out_block[0]:
            # out block at the bottom of corner block.
            if corner_block[1] + 1 == out_block[1]:
                # out block at the right of corner block.
                one_side = (corner_block[0]+1,corner_block[1])
                other_side = (corner_block[0],corner_block[1]+1)
                return [one_side,corner_block,other_side]
            elif corner_block[1] - 1 == out_block[1]:
                # out block at the left of corner block.
                one_side = (corner_block[0]+1,corner_block[1])
                other_side = (corner_block[0],corner_block[1]-1)
                return [one_side,corner_block,other_side]
            else:
                raise ValueError('corner block and out block must be neighbor!')
        elif corner_block[0] - 1 == out_block[0]:
            # out block at the up of corner block.
            if corner_block[1] + 1 == out_block[1]:
                # out block at the right of corner block.
                one_side = (corner_block[0]-1,corner_block[1])
                other_side = (corner_block[0],corner_block[1]+1)
                return [one_side,corner_block,other_side]
            elif corner_block[1] - 1 == out_block[1]:
                # out block at the left of corner block.
                one_side = (corner_block[0]-1,corner_block[1])
                other_side = (corner_block[0],corner_block[1]-1)
                return [one_side,corner_block,other_side]
            else:
                raise ValueError('corner block and out block must be neighbor!')
        else:
            raise ValueError('corner block and out block must be neighbor!')

class SpecialChessBoard():
    '''
    This class is for special chessboard.
        chessboard:a instance of ChessBoard or RelativeChessBoard.
    '''
    def __init__(self,chessboard):
        self._chessboard = chessboard

    def __getattr__(self,attribute):
        return getattr(self._chessboard,attribute)

    def __str__(self):
        return str(self._chessboard)

    def setSpecialBlock(self,spb_row,spb_col):
        '''
        Set special block for this special chessboard.
            spb_row:the special block row.
            spb_col:the special bloc col.
        '''
        if not self._chessboard.inChessBoard(spb_row,spb_col):
            raise IndexError('the special block out of chessboard range!')

        self._spb_row = spb_row
        self._spb_col = spb_col

    def getFillPath(self):
        pass


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
