from collections import deque
from sys import stdin

INT_MAX = 999999999999
r = lambda: stdin.readline()

def dijkstra(count, start, end, cost):
  dist = [cost[start][x] for x in range(count+1)]
  queue = [x for x in range(1, count+1)]
  queue.remove(start)

  while len(queue) > 0:
    min_dist = INT_MAX
    min_idx = -1
    for x in queue:
      x_dist = dist[x]
      if (min_dist > x_dist):
        min_dist = x_dist
        min_idx = x
    if min_idx == end or min_idx == -1:
      break
    queue.remove(min_idx)

    for x in queue:
      dist[x] = min(dist[x], dist[min_idx] + cost[min_idx][x])
  return dist[end]

city_count = int(r())
bus_count = int(r())

cost = [[INT_MAX for x in range(city_count+1)] for x in range(city_count+1)]
for i in range(bus_count):
  a, b, c = map(int, r().split())
  cost[a][b] = min(cost[a][b], c)
for i in range(city_count+1):
  cost[i][i] = 0

start, end = map(int, r().split())
print(dijkstra(city_count, start, end, cost))
