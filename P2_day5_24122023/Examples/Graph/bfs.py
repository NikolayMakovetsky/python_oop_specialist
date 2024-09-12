# BFS(Breadth-First Search). Алгоритм поиска в ширину.
# Позволяет найти кратчайшие расстояния из одной вершины невзвешенного
# (ориентированного или неориентированного) графа до всех остальных вершин.
# Под кратчайшим путем подразумевается путь, содержащий наименьшее число ребер.

# Алгоритм (используем метод FIFO(First In First Out):
# 1. Начальную вершину помещаем в очередь
# 2. Пока очередь не пуста:
#   2.1 Достаем из очереди первую вершину
#   2.2 Для каждой вершины списка смежности
#       2.2.1 Если до этой вершины еще не доходили,
#             то помечаем расстояние до нее и добавляем ее в конец очереди
#       2.2.1 Если вершину уже посещали, то игнорируем ее
#         3 --5--2 -- 6--7
#        / \ /  /
#       0---1--4
graph = [
    # список смежности
    [1, 3],         # 0
    [0, 3, 4, 5],   # 1
    [4, 5, 6],      # 2
    [0, 1, 5],      # 3
    [1, 2],         # 4
    [1, 2, 3],      # 5
    [7],            # 6
    [6]             # 7
]

# Очередь в питоне легко реализовать при помощи обычного списка:
# методом append() новый элемент добавляется в конец,
# а методом pop(0) удаляется начальный элемент


start = 0                       # Начальной вершиной выбираем нулевую

lengths = [None] * (len(graph)) 
print(lengths)                  # [None, None, None, None, None, None, None, None]

lengths[start] = 0              
print(lengths)                  # [0, None, None, None, None, None, None, None]

queue = [start]
while queue:                    # очередь из 'горящих' вершин
    print(f"{queue = }")
    cur_vertex = queue.pop(0)   # Достаем из очереди первую вершину (vertex)
    print(f"{cur_vertex = }")
    print(f"{queue = }")
    print("===")
    for vertex in graph[cur_vertex]:
        print(f"{graph[cur_vertex] = }")
        if lengths[vertex] is None: # Если до этой вершины еще не доходили
            lengths[vertex] = lengths[cur_vertex] + 1 # Помечаем расст до верш
            print(lengths)
            queue.append(vertex) # Добавляем вершину в конец очереди
    print("=======================")

print(lengths)

#         3 --5--2   6--7
#        / \ /  /
#       0---1--4
