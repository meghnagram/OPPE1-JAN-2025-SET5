

n = int(input())
for i in range(1,n+1):
  print(" "*(n-i)+"@"*(n+2*(i-1)))
for i in range(n-1,0,-1):
  print(" "*(n-i)+"@"*(n+2*(i-1)))

#Another Method:



# Write your solution here

n=int(input())

for i in range(n):
    print(' '*(n-i-1) +'@'*i  + '@' * n + '@' *i)
    
for i in range(n-1,0,-1):
    print(' '*(n-i) +'@'*(i-1)  + '@' * n + '@' *(i-1))

Pattern Printing - Hexagon
Given an integer n as input, print a hexagon pattern with '@' having a side length of n.

Examples

Input

2
Output

 @@
@@@@
 @@
Input

3
Output

  @@@
 @@@@@
@@@@@@@
 @@@@@
  @@@
Input

4
Output

   @@@@
  @@@@@@
 @@@@@@@@
@@@@@@@@@@
 @@@@@@@@
  @@@@@@
   @@@@

