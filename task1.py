#Варіант 48. План проєкту: листки вибраного піддерева та префікс обходу bfs
#Завдання 1. Листки вибраного піддерева


class Record:  # звичайний запис типу N
    def __init__(self, value):
        self.value = value  # власне значення v

    def score(self):
        return self.value  # звичайний запис повертає v


class BoostedRecord(Record):  # посилений запис типу D наслідує звичайний
    def score(self):
        return 2 * self.value  # перевизначаємо метод оцінка 2 * v


class TreeNode:  # вузол дерева
    def __init__(self, node_id, record):
        self.id = node_id  # номер вузла
        self.record = record  # власний запис вузла 
        self.children = []  # посилання на дітей

    def is_leaf(self):
        return len(self.children) == 0  # листок це вузол без дітей


class Tree:  # дерево містить вузли 
    def __init__(self):
        self.nodes = {}  # номер вузла - вузол

    def add_node(self, node_id, parent_id, record):
        node = TreeNode(node_id, record)
        self.nodes[node_id] = node
        if parent_id != 0:
            # діти додаються в порядку зростання id, бо вхід іде по порядку номерів
            self.nodes[parent_id].children.append(node)

    def preorder(self, root_id):
        # обхід: спочатку вузол потім цілком піддерева дітей по порядку
        result = []
        if root_id not in self.nodes:  # відсутнє піддерево
            return result
        self._visit(self.nodes[root_id], result)
        return result

    def _visit(self, node, result):
        result.append(node)
        for child in node.children:
            self._visit(child, result)


# Створення запису потрібного класу по типу, далі оцінка береться однаково через score()
def make_record(record_type, value):
    if record_type == "D":
        return BoostedRecord(value)
    return Record(value)


def format_list(numbers):
    # порожній перелік позначається -
    return " ".join(map(str, numbers)) if numbers else "-"


def main():
    n = int(input())  # кількість вузлів
    tree = Tree()
    for _ in range(n):
        node_id, parent_id, record_type, value = input().split()
        tree.add_node(int(node_id), int(parent_id), make_record(record_type, int(value)))
    r, t = map(int, input().split())  # корінь піддерева і поріг

    visited = tree.preorder(r)
    # листки піддерева з оцінкою не більшою за t, порядок обходу зберігається
    selected = [node for node in visited if node.is_leaf() and node.record.score() <= t]
    total = sum(node.record.score() for node in selected)

    print(f"Обхід: {format_list([node.id for node in visited])}")
    print(f"Відібрано: {format_list([node.id for node in selected])}")
    print(f"Кількість: {len(selected)}")
    print(f"Сума: {total}")


if __name__ == "__main__":
    main()