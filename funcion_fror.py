print("Primer codigo: ")
for i in range(3):
    for j in range(2):
        print(f"i vale {i} y j vale {j}")
print(" ")
print("Segundo codigo: ")
for i in [1, 2, 3]:
    for j in [11, 12]:
        print(j, end=" ")
    print(i, end=" ")
print(" ")
print(" ")
print("Tercer codigo:  ")
for i in [1, 2, 3]:
    for j in range(i):
        print(f"i vale {i} y j vale {j}")