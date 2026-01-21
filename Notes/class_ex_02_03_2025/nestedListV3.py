distance_table = [[0, 983, 787, 714],
                  [983, 0, 214, 1102],
                  [787, 214, 0, 888],
                  [714, 1102, 888, 0]]

city_names = ["Chicago",
              "Boston",
              "New York",
              "Atlanta"]

# Find the distance between Boston and Atlanta
name_1 = "Boston"


def find_city_index(name, city_names):
    idx = -1
    if name_1 in city_names:
        idx_1 = city_names.index(name)
    else:
        print("This %s is not in the list" % name)
    return idx


name_1 = "Boston"
name_2 = "Atlanta"

idx_1 = find_city_index(name_1, city_names)
idx_2 = find_city_index(name_2, city_names)
print(idx_1, idx_2)
dist = distance_table[idx_1][idx_2]
print(dist)