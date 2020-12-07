import unittest
from puzzle import Rotate, HorizontalScan, VerticalScan, rotate_matrix, solve_puzzle
from puzzle_terms import Puzzle1, puzzle2

class TestPuzzle(unittest.TestCase):

    def test_rotate(self):
        response = Rotate([[ 'z', 'e', 'z'], [ 'w', 'n', 'a'], [ 'n', 'q', 'b']])
        self.assertEqual(response, [[ 'a', 'f', 'a'], [ 'x', 'o', 'b'], [ 'o', 'r', 'c']])

    def test_horizontal(self):
        response = HorizontalScan([['a','a'],['z','z']],'zz')
        self.assertEqual(response,(0,1))
        response = HorizontalScan([['a','a'],['a','n','e','t','a','p','p']],'netapp')
        self.assertEqual(response,(1,1))

    def test_rotate_matrix(self):
        self.assertEqual(rotate_matrix([['a','b'],['c','d']]), [['a','c'],['b','d']])

    def test_vertical(self):
        response = VerticalScan([['a','b'],['c','d']],'bd')
        self.assertEqual(response, (1,0))

    def test_solve_puzzle(self):
        response = solve_puzzle([['a','b'],['c','d']],'bd')
        self.assertEqual(response, ((1,0), 0))

    def test_solve_puzzle_no_rotation(self):
        response = solve_puzzle([['a','b'],['c','d']],'bd')
        self.assertEqual(response, ((1,0), 0))

    def test_solve_puzzle_one_rotation(self):
        response = solve_puzzle([['z','a'],['b','c']],'bd')
        self.assertEqual(response, ((1,0), 1))

    def test_solve_puzzle_max_rotations(self):
        response = solve_puzzle([['a','f'],['l','x']],'ew')
        self.assertEqual(response, ((1,0), 25))

    def test_puzzle1(self):
        response = solve_puzzle(Puzzle1, 'netapp')
        self.assertEqual(response, ((5, 15), 8))

    def test_puzzle2(self):
        response = solve_puzzle(puzzle2, 'containers')
        self.assertEqual(response, ((10, 2), 17))



if __name__ == '__main__':
    unittest.main()
