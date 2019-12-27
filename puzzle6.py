with open("orbits.txt") as f:
    input_orbits = f.readlines()


def leaf_depth(orbits, node, depths, depth):
    if node in depths.keys():
        return depths[node]
    if node != "COM":
        # print(f"{orbits[node]}){node}")
        depth = leaf_depth(orbits, orbits[node], depths, depth)
        depth += 1
    depths[node] = depth
    return depth


def ancestors_list(orbits, node, ancestors):
    if node != "COM":
        ancestors.append(node)
        ancestors_list(orbits, orbits[node], ancestors)
    else:
        ancestors.append("COM")
    return ancestors


orbits = {key: value for (value, key) in [x.rstrip().split(")") for x in input_orbits]}
depths = dict()
total_depth = 0
for key, val in orbits.items():
    d = leaf_depth(orbits, key, depths, 0)
    # print(d)
    total_depth += d
print(total_depth)

anc_YOU = []
anc_YOU = ancestors_list(orbits, "YOU", anc_YOU)
# print(anc_YOU)
anc_SAN = []
anc_SAN = ancestors_list(orbits, "SAN", anc_SAN)
# print(anc_SAN)

common_anc = 0
for node in reversed(anc_YOU):
    if node not in anc_SAN:
        break
    common_anc += 1

dist_to_SAN = depths["YOU"] + depths["SAN"] - 2 * common_anc
print(dist_to_SAN)
