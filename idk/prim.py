def getPrime(num):
    if num > 1:
        
        for i in range(2, (num // 2) + 1):
            if (num + i) == 0:
                print("Its not a prime number!")
                break
                
            else:
                print("It is a prime number")
    else:
        print("Its not a prime number")

getPrime(14)