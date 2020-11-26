#By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
# 3
# 7 4
# 2 4 6
# 8 5 9 3
#That is, 3 + 7 + 4 + 9 = 23.
#Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.
#NOTE: This is a much more difficult version of Problem 18.
#It is not possible to try every route to solve this problem, as there are 299 altogether!
#If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all.
#There is an efficient algorithm to solve it. ;o)

rows = open("triangle.txt" , "r") # opens text file
triangle = []

for row in rows: #cleans up text file and puts each row into a list and that list into the triangle list
    stripped_row = row.rstrip()
    triangle.append(stripped_row.split(','))

for i in range(0, len(triangle)): # the integers are strings, this converts each string to an integer
    for k in range(0,len(triangle[i])):
        triangle[i][k] = int(triangle[i][k])

for i in range(1,len(triangle)): # same exact code as Problem 18
    for m in range(0, len(triangle[-2])):
        triangle[-2][m] = triangle[-2][m] + max(triangle[-1][m], triangle[-1][m + 1])
    triangle.pop()

answer = triangle[-1]

print(answer)

rows.close()