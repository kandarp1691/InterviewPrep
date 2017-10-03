'''
The first line contains an integer, , denoting the number of steps in Gary's hike.
The second line contains a single string of  characters. Each character is
(where U indicates a step up and D indicates a step down), and the   character in the string describes Gary's  step during the hike.

Print a single integer denoting the number of valleys Gary walked through during his hike.

Sample Input

8
UDDDUDUU

Sample Output

1
Explanation

If we represent _ as sea level, a step up as /, and a step down as \, Gary's hike can be drawn as:

_/\      _
   \    /
    \/\/
It's clear that there is only one valley there, so we print  on a new line.
'''

n = int (raw_input())
valley,level = 0,0
for step in raw_input():
	if step=='D':
		level-=1
	else:
		if level == -1:
			valley+=1
		level+=1
print valley

