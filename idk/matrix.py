rows = int(input("Add meg a sorok számát: "))
columns = int(input("Add meg az oszlopok számát: "))
matrix = []
for row in range(rows):
    a = []
    for column in range(columns):
    
        a.append(int(input("Add meg a számokat: ")))
    matrix.append(a)

for row in range(rows):
    for column in range(columns):
        print(matrix[row][column], end=" ")
