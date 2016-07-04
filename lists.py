#!/usr/bin/env python
'''
Task
Initialize your list (L = []) and follow the NN commands given over NN lines.

Each command will be 11 of the 88 commands given above. The extend(LL) method will not be used. Each command will have its own value(s) separated by a space.

Input Format

The first line contains an integer, NN (the number of commands).
The NN subsequent lines each contain one of the 88 commands described above.
Sample Input
12
insert 0 5
insert 1 10
insert 0 6
print 
remove 6
append 9
append 1
sort 
print
pop
reverse
print

Sample Output

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
'''

L = []

loops = int(raw_input())

loop = 0
while loop < loops:
    command = raw_input().split()
    if len(command) > 1:
        getattr(L, command[0])(*(map(int, command[1:])))

    elif command[0] == 'print':
        print L
    else:
        getattr(L, command[0])()

    loop += 1


'''
could have used this technique:
    command, *args = input().rstrip().split()
'''
