def returnMax():
    a = int(input("Adj meg egy számot: "))
    b = int(input("Adj meg egy számot: "))

    if a == b:
        print("A két szám egyenlő!")
    elif a > b:
        print(f"{a} nagyobb mint {b}")
    else:
        print(f"{b} nagyobb mint {a}")

returnMax()