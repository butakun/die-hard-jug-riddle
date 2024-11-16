# State: Volumes of water in 5L jug and 3L jug. -> (V3, V5)
# Transitions:
# 1. Fill V3
# 2. Fill V5
# 3. Empty V3 to sink
# 4. Empty V5 to sink
# 5. Pour V3 into V5
# 6. Pour V5 into V3

from collections import defaultdict


def main():

    G = {}
    Q = [(0, 0)]
    R = defaultdict(set)

    while Q:
        v3, v5 = Q.pop(0)
        nei = [None] * 6
        if v3 < 3:
            nei[0] = (3, v5)
        if v5 < 5:
            nei[1] = (v3, 5)
        if v3 > 0:
            nei[2] = (0, v5)
        if v5 > 0:
            nei[3] = (v3, 0)
        if v3 > 0 and v5 < 5:
            d = min(5 - v5, v3)
            nei[4] = (v3 - d, v5 + d)
        if v5 > 0 and v3 < 3:
            d = min(3 - v3, v5)
            nei[5] = (v3 + d, v5 - d)

        G[(v3, v5)] = nei
        for n in nei:
            if n is None:
                continue
            if n not in G:
                Q.append(n)
            R[n].add((v3, v5))

    print("Graph")
    for node, to_nodes in G.items():
        print(f"{node} -> {to_nodes}")

    print("\nReverse map")
    for node, from_nodes in R.items():
        print(f"{node} <- {from_nodes}")

    paths = []
    QQ = [[(0, 4)]]
    while QQ:
        path = QQ.pop(0)
        last_node = path[-1]
        if last_node == (0, 0):
            paths.append(path)
        else:
            for next in R[last_node]:
                if next in path:
                    continue
                new_path = path.copy() + [next]
                QQ.append(new_path)

    print("\nPath from (0, 0) to (0, 4)")
    for i, path in enumerate(paths):
        path.reverse()
        print(f"{i}: {path}")


if __name__ == "__main__":
    main()
