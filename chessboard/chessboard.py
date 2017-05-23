#!/usr/bin/env python3
# -*- coding:utf-8 -*-
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

    def __init__(self, row=1, col=1):
        self._row = row
        self._col = col
        self._data = [[None] * col for i in range(row)]

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

    def getBoard(self, irow, icol):
        '''
        Get chessboard block by [irow][icol].
        '''
        return self._data[irow][icol]

    def setBoard(self, irow, icol, data):
        '''
        Set data to chessboard block by [irow][icol].
        '''
        self._data[irow][icol] = data

    def inChessBoard(self, irow, icol):
        '''
        If (irow,icol) block in chessboard,return True,else return False.
        '''
        if irow < self.getRowMaxNum() and icol < self.getColMaxNum():
            return True
        else:
            return False

    def __str__(self):
        return 'row:{};col:{}\ndata:{}'.format(self._row, self._col,
                                               self._data)


class RelativeChessBoard():
    '''
    Get a chessboard in a chessboard.
        rwo:new chessboard row.
        col:new chessboard col.
        relative_row_start_pos:this chessboard row relative to main chessboard.
        relative_col_start_pos:this chessboard col relative to main chessboard.
    '''

    def __init__(self,
                 chessboard,
                 row,
                 col,
                 relative_row_start_pos=0,
                 relative_col_start_pos=0):
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

    def getBoard(self, irow, icol):
        '''
        Get chessboard block by [irow][icol].
        '''
        if irow >= self._row or icol >= self._col:
            raise IndexError('Index out of range!')
        return self._chessboard.getBoard(irow + self._rel_row,
                                         icol + self._rel_col)

    def setBoard(self, irow, icol, data):
        '''
        Set data to chessboard block by [irow][icol].
        '''
        self._chessboard.setBoard(irow + self._rel_row, icol + self._rel_col,
                                  data)

    def inChessBoard(self, irow, icol):
        '''
        If (irow,icol) block in chessboard,return True,else return False.
        '''
        if irow < self.getRowMaxNum() and icol < self.getColMaxNum():
            return True
        else:
            return False

    def __str__(self):
        return 'relative row:{} ,relative col:{} ; row:{} , col:{}'.format(
            self._rel_row, self._rel_col, self._row, self._col)


class DominoL():
    '''
    L type domino.
        corner_block:the pos(rwo,col) of corner block of L domino.
        out_block:the pos(row,col) of block which next to L domino.
    '''

    def __init__(self, corner_block=(0, 0), out_block=(0, 0)):

        self._blocks = self._getBlocksPos(corner_block, out_block)

    def __str__(self):
        return str([str(block) for block in self._blocks])

    def _getBlocksPos(self, corner_block, out_block):
        '''
        Get the three pos of block by corner block and out block.
        '''
        if corner_block[0] + 1 == out_block[0]:
            # out block at the bottom of corner block.
            if corner_block[1] + 1 == out_block[1]:
                # out block at the right of corner block.
                one_side = (corner_block[0] + 1, corner_block[1])
                other_side = (corner_block[0], corner_block[1] + 1)
                return [one_side, corner_block, other_side]
            elif corner_block[1] - 1 == out_block[1]:
                # out block at the left of corner block.
                one_side = (corner_block[0] + 1, corner_block[1])
                other_side = (corner_block[0], corner_block[1] - 1)
                return [one_side, corner_block, other_side]
            else:
                raise ValueError(
                    'corner block and out block must be neighbor!')
        elif corner_block[0] - 1 == out_block[0]:
            # out block at the up of corner block.
            if corner_block[1] + 1 == out_block[1]:
                # out block at the right of corner block.
                one_side = (corner_block[0] - 1, corner_block[1])
                other_side = (corner_block[0], corner_block[1] + 1)
                return [one_side, corner_block, other_side]
            elif corner_block[1] - 1 == out_block[1]:
                # out block at the left of corner block.
                one_side = (corner_block[0] - 1, corner_block[1])
                other_side = (corner_block[0], corner_block[1] - 1)
                return [one_side, corner_block, other_side]
            else:
                raise ValueError(
                    'corner block and out block must be neighbor!')
        else:
            raise ValueError('corner block and out block must be neighbor!')

    def relativePos(self, vector=(0, 0)):
        '''
        Change pos from relative to real pos.
        '''
        new_blocks = []
        for block in self._blocks:
            new_blocks.append((block[0] + vector[0], block[1] + vector[1]))
        self._blocks = new_blocks
        return new_blocks
