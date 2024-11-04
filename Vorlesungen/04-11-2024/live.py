# Methode für das Ausrechnen der Fakultät für n ohne Rekursion
def factorial(n: int)-> int:
    if n<=0:
        return none
    result = n
    while n>1:
        result = result*(n-1)
        n = n-1
    return result

# Methode für das Ausrechnen der Fakultät für n mit Rekursion (Methode wird ständig wiederholt)
def otherfac(n:int)-> int:
    if n>1:
        result = n*otherfac(n-1)
        n = n-1
        return result
    else:
        return n
    

print(" testing: ")
print(factorial(5))
print(factorial(77))
print(otherfac(5))
print(otherfac(77))