#Варіант 48. План проєкту: листки вибраного піддерева та префікс обходу bfs
#Завдання 2. Префікс обходу BFS


class Record:  # звичайний запис типу N
    def __init__(self, value):
        self.value = value  # власне значення v

    def score(self):
        return self.value  # звичайний запис повертає v


class BoostedRecord(Record):  # посилений запис типу D наслідує звичайний
    def score(self):
        return 2 * self.value  # перевизначаємо метод оцінка 2 * v


class Vertex:  # вершина графа
    def __init__(self, vertex_id, record):
        self.id = vertex_id  # номер вершини
        self.record = record  # власний запис вершини 
        self.neighbors = []  # посилання на сусідів


class Graph:  # граф містить вершини 
    def __init__(self):
        self.vertices = {}  # номер вершини - вершина

    def add_vertex(self, vertex_id, record):
        self.vertices[vertex_id] = Vertex(vertex_id, record)

    def add_edge(self, u, w):
        # додаємо в обидві сторони
        self.vertices[u].neighbors.append(self.vertices[w])
        self.vertices[w].neighbors.append(self.vertices[u])

    def sort_neighbors(self):
        # порядок ребер у вході довільний, сусідів сортуємо за номером
        for vertex in self.vertices.values():
            vertex.neighbors.sort(key=lambda v: v.id)

    def bfs(self, start_id):
        order = []
        if start_id not in self.vertices:  # порожній граф
            return order
        start = self.vertices[start_id]
        marked = {start.id}  # вершину позначаємо відвіданою при першому включенні до черги
        queue = [start]
        head = 0  # початок черги
        while head < len(queue):
            current = queue[head]
            head += 1
            order.append(current)
            for neighbor in current.neighbors:
                if neighbor.id not in marked:
                    marked.add(neighbor.id)
                    queue.append(neighbor)
        return order


# Створення запису потрібного класу по типу, далі оцінка береться однаково через score()
def make_record(record_type, value):
    if record_type == "D":
        return BoostedRecord(value)
    return Record(value)


def format_list(numbers):
    # порожній перелік позначається -
    return " ".join(map(str, numbers)) if numbers else "-"


def main():
    n, m, s = map(int, input().split())  # вершини, ребра, старт
    graph = Graph()
    for _ in range(n):
        vertex_id, record_type, value = input().split()
        graph.add_vertex(int(vertex_id), make_record(record_type, int(value)))
    for _ in range(m):
        u, w = map(int, input().split())
        graph.add_edge(u, w)
    graph.sort_neighbors()
    k, t = map(int, input().split())  # довжина префікса і поріг

    visited = graph.bfs(s)
    prefix = visited[:k]  # перші k вершин (якщо їх менше то всі, якщо k = 0 то жодної)
    # у префіксі беремо вершини з оцінкою не меншою за t, порядок BFS зберігається
    selected = [vertex for vertex in prefix if vertex.record.score() >= t]
    total = sum(vertex.record.score() for vertex in selected)

    print(f"Обхід: {format_list([v.id for v in visited])}")
    print(f"Префікс: {format_list([v.id for v in prefix])}")
    print(f"Відібрано: {format_list([v.id for v in selected])}")
    print(f"Кількість: {len(selected)}")
    print(f"Сума: {total}")


if __name__ == "__main__":
    main()