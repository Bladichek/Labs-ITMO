


items = {
    'rifle':    ['r', 3, 25],
    'pistol':   ['p', 2, 15],
    'ammo':     ['a', 2, 15],
    'medkit':   ['m', 2, 20],
    'knife':    ['k', 1, 15],
    'axe':      ['x', 3, 20],
    'talisman': ['t', 1, 25],
    'flask':    ['f', 1, 15],
    'antidot':  ['d', 1, 10],
    'supplies': ['s', 2, 20],
    'crossbow': ['c', 2, 20],
    'inhaler': ['i', 1, 5],
}


def get_size_and_value(items):
    size = [items[item][1] for item in items]
    value = [items[item][2] for item in items]
    # print(size)
    # print(value)
    s=[]
    return size, value

def get_memtable(items, v=7):
    size, value = get_size_and_value(items)
    n = len(value)-1

    V = [[0 for i in range(v+1)] for j in range(n+1)]

    for i in range(n+1):
        for j in range(v+1):

            if i==0 or j==0:
                V[i][j]=0
            elif size[i-1]<=j:
                V[i][j] = max(value[i-1] + V[i-1][j-size[i-1]], V[i-1][j])

            else:
                V[i][j]=V[i-1][j]
    return V, size, value


def get_selected_items(items, v=7):
    V, size, value = get_memtable(items, v)
    for i in V:
        print(*i)
    n = len(value)-1
    a=v
    items_list = []
    res = V[n][a]
    values=[]

    for i in range(n, 0, -1):
        if res <=0:
            break
        if res == V[i-1][a]:
            continue

        else:
            items_list.append((size[i-1], value[i-1]))
            res-=value[i-1]
            a-=size[i-1]
    selected_items=[]
    for search in items_list:
        for k, vl in items.items():

            if (vl[1], vl[2])==search:
                if k in selected_items:
                    continue
                selected_items.append(k)
                break

    return selected_items
def inventory_return():
    inventory = get_selected_items(items, 7)
    inventory.append('inhaler')
    inv=[]

    scores=20
    for k,v in items.items():
        scores-= v[2]

    for i in inventory:
        scores+=2*items[i][2]
        for j in range(items[i][1]):
            inv.append(items[i][0])
    print(inventory)
    print(inv[:4])
    print(inv[4:])
    print('Очков выживания:', scores)



objects = [[3, 25], [2, 15], [2, 15], [2, 20], [1, 15], [3, 20], [1, 25], [1, 15], [1, 10], [2, 20], [2, 20]]
#-205 -> -185 -> -92.5 -> 87.5
#5-7

def f(m):
    s=sum([x[1] for x in m])
    r=sum([x[0] for x in m])
    if s>88 and r<=7:
        return True
    return False
s=0
from itertools import combinations
for j in range(4, 8):
    for i in combinations(objects, j):
        if f(i):
            s+=1
print(s)



