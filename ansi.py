RED = f"\033[91m RED \033[0m"

print(RED)

def IsPrime(num):  
    if num > 1:
        for i in range(2, num//2): 
            if (num % i) == 0: 
                return False
        else: 
            return True
    else: 
        return False

for i in range(10011, 12000, 2):
    if IsPrime(i):
        print(f"{i} is Prime ")
