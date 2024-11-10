kerdes = str(input("Mit szeretnél hozzáadni a todo listhez? "))

def Beiras():
    f = open("todolist.txt", "w", encoding="utf-8")
    f.write("\n")
    f.write(kerdes)
    f.write("\n")
    f.close

def Beolvasas():
    container = []
    j = open("todolist.txt", "r", encoding="utf-8")
    lines = j.readlines()
    for line in lines:
        line = line.strip().split("\n")
        container.append(line)

    def CheckIfExist(lekerdezes = None):
        if lekerdezes == None:
            lekerdezes = str(input("Milyen elemet keresel? "))
        nonlocal container
        for i in container:

while kerdes.upper() != "exit":
    Beiras()
    if kerdes == "exit":
        break
    for 