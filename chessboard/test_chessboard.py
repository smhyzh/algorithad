#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# test_chessboard.py

import unittest
from chessboard import *

class TestChessBoard(unittest.TestCase):
    def setUp(self):
        self.data = [[1,2,3,4,5],[6,7,8,9,10],
                [11,12,13,14,15],[16,17,18,19,20],
                [21,22,23,24,25],[26,27,28,29,30]
                ]
        self.row = 6
        self.col = 5

    def test_constructor(self):
        cb = ChessBoard(self.row,self.col)
        self.assertEqual(cb.getRowMaxNum(),self.row)
        self.assertEqual(cb.getColMaxNum(),self.col)

        for row in range(len(self.data)):
            for col in range(len(self.data[0])):
                cb.setBoard(row,col,self.data[row][col])
        for row in range(len(self.data)):
            for col in range(len(self.data[0])):
                self.assertEqual(cb.getBoard(row,col),self.data[row][col])

    def test_inChessBoard(self):
        cb = ChessBoard(self.row,self.col)

        self.assertTrue(cb.inChessBoard(0,0))
        self.assertTrue(cb.inChessBoard(self.row-1,self.col-1))
        self.assertFalse(cb.inChessBoard(self.row,self.col-1))
        self.assertFalse(cb.inChessBoard(self.row-1,self.col))
        self.assertFalse(cb.inChessBoard(self.row,self.col))

if __name__ == '__main__':
    unittest.main()
