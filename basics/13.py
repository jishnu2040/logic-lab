info = [(1,3),(2,14),(3,25),(4,6),(5,17),(6,28),(7,39),(8,10)]

new_list = sorted(info, key=lambda x: x[1])
print(new_list)