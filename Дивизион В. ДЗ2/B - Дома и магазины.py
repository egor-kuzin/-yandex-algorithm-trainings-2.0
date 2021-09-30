buildings = list(map(int, input().split()))

dict = {
    int(): list()
}

distances = []

for i, build in enumerate(buildings):
    dict[i] = [build, None, None]

homes = list(filter(lambda x: dict[x][0] == 1, range(len(dict))))
stores = list(filter(lambda x: dict[x][0] == 2, range(len(dict))))

for home in homes:
    for store in stores:
        if home < stores[0]:
            dict[home][2] = stores[0]
        elif stores.index(store)+1 < len(stores):
            if store < home < stores[stores.index(store)+1]:
                dict[home][1], dict[home][2] = store, stores[stores.index(store)+1]
        elif home > stores[-1]:
            dict[home][1], dict[home][2] = store, 0

for i, [build, store_left, store_right] in dict.items():
    if build == 1 and store_left == None and store_right != None:
        distances.append(abs(store_right - i))
    if build == 1 and store_left != None and store_right == None:
        distances.append(abs(store_left - i))
    if build == 1 and store_left != None and store_right != None:
        distances.append(min(abs(store_right - i), abs(store_left - i)))

print(max(distances))