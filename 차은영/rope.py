n = int(input())

ropes = []
maxWeight = 0

for i in range(n):
    a = int(input())
    ropes.append(a)

ropes.sort()

for i in range(n):
    temp = ropes[i] * (n - i)
    
    if(maxWeight < temp):
        maxWeight = temp

print(maxWeight)
