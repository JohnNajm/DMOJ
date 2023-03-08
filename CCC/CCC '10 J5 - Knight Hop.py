start = list(map(int, input().split()))
end = list(map(int, input().split()))

queue = []
visited = []

queue.append(start)

for x in range(1,3):
    for y in range(1,3):
        if x != y:
            if 0< start[0]+x <9 and 0< start[1]+y <9:
                queue.append([start[0]+x,start[1]+y])
                if queue[-1] == end:
                    break

            if 0< start[0]+x <9 and 0< start[1]-y <9:
                queue.append([start[0]+x,start[1]-y])
                if queue[-1] == end:
                    break

            if 0< start[0]-x <9 and 0< start[1]+y <9:
                queue.append([start[0]-x,start[1]+y])
                if queue[-1] == end:
                    break

            if 0< start[0]-x <9 and 0< start[1]-y <9:
                queue.append([start[0]-x,start[1]-y])
                if queue[-1] == end:
                    break

print(queue)



#__________________________________________________

# visited = []
# queue = []

# def bfs(visited, graph, node):
#     visited.append(node)
#     queue.append(node)

#     while queue:
#         m = queue.pop(0)
#         print(m, end = " ")

#         for neighbor in graph[m]:
#             if neighbor not in visited:
#                 visited.append(neighbor)
#                 queue.append(neighbor)

#bfs(visited,graph,5)