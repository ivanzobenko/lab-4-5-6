from typing import Callable

def iterative_binary_tree(height: int, root: int, l: Callable[[int], int] = lambda x: x * 2 + 1, r: Callable[[int], int] = lambda x: 2 * x - 1) -> dict[str, list]:
    """
    Создаёт бинарное дерево в виде словаря (нерекурсивно)

    Параметры:
        height (int): Высота дерева, количество уровней
        root (int): Начальное число, для которого происходят все вычисления по формулам
        l (Callable[[int], int]): Формула для левой "ветки" (потомка) дерева
        r (Callable[[int], int]): Формула для правой "ветки" (потомка) дерева

    Результаты:
        dict[str, list]: Словарь, в котором представлено бинарное дерево. Ключом является корень, а значением список из деревьев, созданых на предыдущих шагах
    """
    if height < 0:
        return {}

    tree = {str(root): []}
    current_level = [(root, str(root))]

    for _ in range(height):
        next_level = []
        for root_value, key in current_level:
            left_val = l(root_value)
            right_val = r(root_value)

            tree[str(left_val)] = []
            tree[str(right_val)] = []
            tree[key].append({str(left_val): tree[str(left_val)]})
            tree[key].append({str(right_val): tree[str(right_val)]})

            next_level.append((left_val, str(left_val)))
            next_level.append((right_val, str(right_val)))

        current_level = next_level

    return {str(root): tree[str(root)]}
