kerdes = str(input("Mit szeretnél hozzáadni a todo listhez? "))
def Beiras():
    f = open("todolist.txt", "w", encoding="utf-8")
    f.write("A todo lsit tartalma: ")
    f.write("\n")
    f.write(kerdes)
    f.write("\n")
    f.close

while kerdes.upper() != "exit":
    j = open("todolist.txt")