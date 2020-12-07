# Task - Find the Puzzle 
# Developer : Saraschandra Rao
# Date : Dec 5 2020

from puzzle_terms import Puzzle1, puzzle2

def HorizontalScan(puzzle, term): # we scan horizantally from left to right 
    y = 0
    for row in puzzle:
        index = Index(row, term[0]) # index is first occurence of first character of the term
        offset = 0  # windowing offset for where we already searched 
        while index is not None:
            x = index+offset
            possible_term = row[x:x+len(term)] # possible term is where we found first matching character ending at the expected length of the term
            if possible_term == list(term):
                return (x,y)
            offset = x+1
            index = Index(row[offset:], term[0])
        y = y+1

def Index(array, char): # we are catching it in a try catch in case the character was not found
    try:
        index = array.index(char)
        return index
    except ValueError:
        return

def VerticalScan(puzzle, term): # we scan vertically from top to bottom
    rotated = rotate_matrix(puzzle) # turns columns into rows
    response = HorizontalScan(rotated, term)
    if response:
        return response[1], response[0]

def rotate_matrix(puzzle): #turns columns into rows
    return list(list(l) for l in zip(*puzzle)) 


def Rotate(puzzle): # increments characters in matrix by one rotating around the alphabet
    new_puzzle = []
    for row in puzzle:
        new_row = []
        for character in row:
          new_row.append(string[(string.find(character)+1)%len(string)])
        new_puzzle.append(new_row)
    return new_puzzle

string = 'abcdefghijklmnopqrstuvwxyz'
def solve_puzzle(puzzle, term): 
    current_puzzle = puzzle
    for rotations in range(len(string)): 
        # scans horizontally
        scan = HorizontalScan(current_puzzle, term)
        if scan:
            print("x={}, y={}, count={}".format(scan[0], scan[1], rotations))
            return (scan, rotations)
        # scans vertically
        scan = VerticalScan(current_puzzle, term)
        if scan:
            print("x={}, y={}, count={}".format(scan[0], scan[1], rotations))
            return (scan, rotations)
        # if it doesn't find it rotates by 1 
        current_puzzle = Rotate(current_puzzle)


if __name__ == '__main__':
    response = solve_puzzle(Puzzle1, 'netapp')
    response = solve_puzzle(puzzle2, 'containers')