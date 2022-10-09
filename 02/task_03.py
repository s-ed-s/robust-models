import collections
import heapq


def calc_network_delay(_times, _n, _x):
    d = collections.defaultdict(list)
    for start, end, path_len in _times:
        d[start].append((path_len, end))
    if _x not in d:
        return -1

    res = {}
    nodes = [(0, _x)]
    while nodes:
        edge = heapq.heappop(nodes)
        if edge[1] in res:
            continue
        res[edge[1]] = edge[0]

        for time, end in d.get(edge[1], []):
            if end not in res:
                heapq.heappush(nodes, (time + edge[0], end))

    return max(res.values()) if len(res) == _n else -1


times = eval(input('times = '))
n = int(input('N = '))
x = int(input('X = '))

print(calc_network_delay(times, n, x))
