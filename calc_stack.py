from collections import deque

ints = input("Escreve um conjunto de números inteiros separados por um espaço: ")
numbers = deque(ints.split())

print(numbers)

for x in range (len(numbers)):
    numbers_squared = numbers.pop()
    print(int(numbers_squared)**2)