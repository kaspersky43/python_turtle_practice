'''
지뢰찾기:

enter two digits (e.g. '3 5') first is col and second is row 

then enter by line the map
* represents mine
. represents safe zone

for example:
input:
3 3
*..
.*.
*..

output: 
*21
3*1
*21

prints the mines map
'''

col, row = map(int, input().split())
matrix = []; rs = []
for i in range(row):
    matrix.append(list(input()))
    rs.append([])
for r_m in range(len(matrix)):
    for c_m in range(len(matrix[r_m])):
        if matrix[r_m][c_m] == '*':
            rs[r_m].append('*')
        else:
            itt = [i for i in list(range(r_m - 1, r_m + 2)) if not (i-1 < -1 or i+1 > row)]  
            it2t = [i for i in list(range(c_m - 1, c_m + 2)) if not (i-1 < -1 or i+1 > col)]  
            valid_lookup = []
            for it in itt:
                for ct in it2t:
                    valid_lookup.append(matrix[it][ct])
            rs[r_m].append(valid_lookup.count('*'))
for i in rs:
    for m in i:
        print(m, end='')
    print()
