#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# specialchessboard.py

from chessboard import *


class SpecialChessBoard():
    '''
    This class is for special chessboard.
        chessboard:a instance of ChessBoard or RelativeChessBoard.
    '''

    def __init__(self, chessboard):
        self._chessboard = chessboard
        self._set_special_block = False

    def __getattr__(self, attribute):
        return getattr(self._chessboard, attribute)

    def __str__(self):
        return str(self._chessboard)

    def setSpecialBlock(self, spb_row, spb_col):
        '''
        Set special block for this special chessboard.
            spb_row:the special block row.
            spb_col:the special bloc col.
        '''
        if not self._chessboard.inChessBoard(spb_row, spb_col):
            raise IndexError('the special block out of chessboard range!')

        self._spb_row = spb_row
        self._spb_col = spb_col
        self._set_special_block = True

    def putDomin(self):
        '''
        '''
        if not self._set_special_block:
            print('Please set special block first.')
            return
        domilist = self._getFillPath(self._chessboard,
                                     self._spb_row, self._spb_col)
        for dm in domilist:
            print(dm)

    def _getFillPath(self, chessboard, spb_row, spb_col):
        '''
        Find a path to fill special chessboard.
        '''
        # The chessboard must be N*N.
        if chessboard.getRowMaxNum() != chessboard.getColMaxNum():
            raise ValueError("The chessboard should be N*N.")
        # if side lenght equal or less than 2,the problem can been reslove.
        if chessboard.getRowMaxNum() <= 2 and chessboard.getColMaxNum() <= 2:
            if chessboard.inChessBoard(spb_row, spb_col):
                # find the conner block.
                # Conner block must be the farthest block.
                for row in range(chessboard.getRowMaxNum()):
                    for col in range(chessboard.getColMaxNum()):
                        if (row - spb_row)**2 + (col - spb_col)**2 == 2:
                            return [DominoL((row, col), (spb_row, spb_col))]
                # here should not be run.So check the error.
                if chessboard.getRowMaxNum() != chessboard.getColMaxNum():
                    raise RuntimeError('Chessboard should n*n')
            else:
                raise ValueError('Sepcial block out of chessboard.')

        # dived to small problem.
        half_side = chessboard.getRowMaxNum() // 2
        # left-top side.
        new_chessboard_lt = RelativeChessBoard(chessboard, half_side, half_side, 0, 0)
        new_chessboard_rt = RelativeChessBoard(chessboard, half_side, half_side, 0,
                                               half_side)
        new_chessboard_lb = RelativeChessBoard(chessboard,half_side, half_side, half_side,
                                               0)
        new_chessboard_rb = RelativeChessBoard(chessboard,half_side, half_side, half_side,
                                               half_side)
        domi_list = []
        # first we find the special block in which area.
        if 0 <= spb_row <= half_side and 0 <= spb_col <= half_side:
            domi_list.append(
                DominoL(
                        (half_side, half_side),
                        (half_side-1, half_side-1))
                            )
            domi_list_lt = self._getFillPath(new_chessboard_lt, spb_row,
                                             spb_col)
            domi_list_rt = self._getFillPath(new_chessboard_rt, half_side - 1,
                                             0)
            domi_list_lb = self._getFillPath(new_chessboard_lb, 0,
                                             half_side - 1)
            domi_list_rb = self._getFillPath(new_chessboard_rb, 0, 0)

        if 0 <= spb_row < half_side and half_side <= spb_col < half_side * 2:
            domi_list.append(
                DominoL(
                        (half_side, half_side-1),
                        (half_side-1, half_side))
                            )
            domi_list_lt = self._getFillPath(new_chessboard_lt, half_side - 1,
                                             half_side - 1)
            domi_list_rt = self._getFillPath(new_chessboard_rt, spb_row,
                                             spb_col - half_side)
            domi_list_lb = self._getFillPath(new_chessboard_lb, 0,
                                             half_side - 1)
            domi_list_rb = self._getFillPath(new_chessboard_rb, 0, 0)

        if half_side <= spb_row < half_side * 2 and 0 <= spb_col < half_side:
            domi_list.append(
                DominoL(
                        (half_side-1, half_side),
                        (half_side, half_side-1))
                            )
            domi_list_lt = self._getFillPath(new_chessboard_lt, half_side - 1,
                                             half_side - 1)
            domi_list_rt = self._getFillPath(new_chessboard_rt, half_side - 1,
                                             0)
            domi_list_lb = self._getFillPath(new_chessboard_lb,
                                             spb_row - half_side,  spb_col)
            domi_list_rb = self._getFillPath(new_chessboard_rb, 0, 0)

        if (half_side <= spb_row < 2 * half_side and
                half_side <= spb_col < 2 * half_side):
            domi_list.append(
                DominoL(
                        (half_side-1, half_side-1),
                        (half_side, half_side))
                            )
            domi_list_lt = self._getFillPath(new_chessboard_lt, half_side - 1,
                                             half_side - 1)
            domi_list_rt = self._getFillPath(new_chessboard_rt, half_side - 1,
                                             0)
            domi_list_lb = self._getFillPath(new_chessboard_lb, 0,
                                             half_side - 1)
            domi_list_rb = self._getFillPath(new_chessboard_rb,
                                             spb_row - half_side,
                                             spb_col - half_side)

        # get the real pos of all dominos.
        domi_list_rt = [
            domi.relativePos((0, half_side)) for domi in domi_list_rt
        ]
        domi_list_lb = [
            domi.relativePos((half_side, 0)) for domi in domi_list_lb
        ]
        domi_list_rb = [
            domi.relativePos((half_side, half_side)) for domi in domi_list_rb
        ]

        domi_list.extend(domi_list_lt)
        domi_list.extend(domi_list_rt)
        domi_list.extend(domi_list_lb)
        domi_list.extend(domi_list_rb)

        return domi_list


def main():
    cb = ChessBoard(4, 4)
    cb = SpecialChessBoard(cb)
    cb.setSpecialBlock(1, 1)
    cb.putDomin()


if __name__ == '__main__':
    main()
