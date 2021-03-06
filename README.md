# python_interview_task

This is a "find the word" challenge with a slight twist. Attached is a file that includes two puzzle inputs. Each puzzle input is a double character array consisting of lower case English characters from a - z. 
The word to find from the first input array is 'netapp' and the word to find from the second input array is 'containers'.  These words are also included in the attached puzzle.txt file along with the puzzle inputs. 

The words to find can appear horizontally or vertically BUT NOT diagonally. The horizontal word will appear in order from left to right. The vertical word will appear in order from top to bottom. 
 
The characters in each puzzle input have also been rotated by 1 character several times. So in order to find the word, you will need to :
- rotate all the characters in the array once, search the arrays for the word. 
- if not found, repeat the rotation and search until the word is found. 

Rotation occurs as follows: 'a' -> 'b', 'b' -> 'c', 'c' -> 'd', ... 'y' -> 'z', 'z' -> 'a'.
 
The expected output to return is the number of rotations needed as well as the x and y coordinate of the first letter of the word. 

For example, if you need to find the word 'abc' from the following character array
[[ 'z', 'e', 'z'],
[ 'w', 'n', 'a'],
[ 'n', 'q', 'b']]

then, your output would be  'x=2, y=0, count=1’. 

This is because if you rotate the characters in the array once (count=1), then you will arrive with an array 
[[ 'a', 'f', 'a'],
 [ 'x', 'o', 'b'],
 [ 'o', 'r', 'c']]

In this array, you can find the first letter of the word 'abc' at (2,0). Hence your output will be 'x=2, y=0, count=1’. 
 
The output should appear like the format used in this example: 'x=2, y=0, count=1’
