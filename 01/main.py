from typing import Callable

def get_labels(train_data: list[tuple[str, int, str]]):
    lables: list[str] = list(map(lambda x: x[2], train_data))
    return lables

def get_probs(labels: list[str]) -> dict[str, float]:
    total: int = len(labels)

    counts = {}
    for label in labels:
        counts[label] = counts.get(label, 0) + 1

    probs: dict[str, float] = {}
    for label, count in counts.items():
        probs[label] = count / total

    return probs        

def get_gini_impurity(labels: list[str]) -> float:
    probs = get_probs(labels)
    impurity = 1.0
    for _, prob in probs.items():
        impurity -= prob ** 2
    return impurity

def get_left_right(train_data: list[tuple[str, int, str]], split_fn: Callable[[tuple[str, int]], bool]):
    left: list[tuple[str, int, str]] = []
    right: list[tuple[str, int, str]] = []
    for row in train_data:
        if split_fn((row[0], row[1])):
            left.append(row)
        else:
            right.append(row)
    return left, right

def get_weighted_gini_impurity(left: list[tuple[str, int, str]], right: list[tuple[str, int, str]]) -> float:
    len_left = len(left)
    len_right = len(right)
    len_total = len_left + len_right
    weighted_left = len_left / len_total * get_gini_impurity(get_labels(left))
    weighted_right = len_right / len_total * get_gini_impurity(get_labels(right))
    return weighted_left + weighted_right

def get_information_gain(
        train_data: list[tuple[str, int, str]],
        split_fn: Callable[[tuple[str, int]], bool],
        gini_impurity: float,
    ):
    left, right = get_left_right(train_data, split_fn)
    weighted_gini_impurity = get_weighted_gini_impurity(left, right)
    return gini_impurity - weighted_gini_impurity

header = ["color", "diameter"]

class SplitFn:
    def __init__(self, col: int, val: str | int):
        self.col = col
        self.val = val
        if col == 0 and isinstance(val, str):
            self.fn: Callable[[tuple[str, int]], bool] = lambda row: row[col] == val
        elif col == 1 and isinstance(val, int):
            self.fn: Callable[[tuple[str, int]], bool] = lambda row: row[col] >= val

    def match(self, data: tuple[str, int]) -> bool:
        return self.fn(data)

    def __repr__(self):
        if self.col == 0 and isinstance(self.val, str):
            return f"Is {header[self.col]} == {self.val}?"
        elif self.col == 1 and isinstance(self.val, int):
            return f"Is {header[self.col]} >= {self.val}?"
        return ""

def find_best_split_fn(train_data: list[tuple[str, int, str]]):
    gini_impurity = get_gini_impurity(get_labels(train_data))

    best_gain: float = 0  # keep track of the best information gain
    best_split_fn: SplitFn | None = None  # keep train of the feature / value that produced it

    n_features = len(train_data[0]) - 1  # number of columns
    for col in range(n_features):  # for each feature
        values = set([row[col] for row in train_data])  # unique values in the column
        for val in values:
            split_fn = SplitFn(col, val)
            gain: float = get_information_gain(train_data, split_fn.fn, gini_impurity)
            if gain == 0:
                continue
            if gain >= best_gain:
                best_gain, best_split_fn = gain, split_fn
    return best_gain, best_split_fn

train_data: list[tuple[str, int, str]] = [
    ('Green', 3, 'Apple'),
    ('Yellow', 3, 'Apple'),
    ('Red', 1, 'Grape'),
    ('Red', 1, 'Grape'),
    ('Yellow', 3, 'Lemon'),
]

class Node[T]:
    def __init__(self, data: T):
        self.data: T = data
        self.left = None
        self.right = None
        self.split_fn = None
    def set_left(self, node: "Node[T]"):
        self.left = node
    def set_right(self, node: "Node[T]"):
        self.right = node
    def set_split_fn(self, split_fn: SplitFn):
        self.split_fn = split_fn
    def __repr__(self):
        return f"Node: {self.data}"

def build_tree(train_data: list[tuple[str, int, str]]) -> Node[list[tuple[str, int, str]]]:
    best_gain, best_split_fn = find_best_split_fn(train_data)
    node: Node[list[tuple[str, int, str]]] = Node(train_data)
    if best_gain == 0 or not best_split_fn:
        return node
    node.set_split_fn(best_split_fn)
    left, right = get_left_right(train_data, best_split_fn.fn)
    node.set_left(build_tree(left))
    node.set_right(build_tree(right))
    return node

def classify(data: tuple[str, int], node: Node[list[tuple[str, int, str]]]) -> list[tuple[str, int, str]]:
    if node.split_fn:
        if node.split_fn.match(data):
            if node.left:
                return classify(data, node.left)
        else:
            if node.right:
                return classify(data, node.right)
    return node.data

def test(data: tuple[str, int, str], tree: Node[list[tuple[str, int, str]]]):
    category = classify((data[0], data[1]), tree)
    labels = list(map(lambda x:x[2], category))
    probs = get_probs(labels)
    print(f" Actual: {data[2]}. Predicted: {probs}")

def main():
    tree: Node[list[tuple[str, int, str]]] = build_tree(train_data)
    # Evaluate
    testing_data: list[tuple[str, int, str]] = [
        ('Green', 3, 'Apple'),
        ('Yellow', 4, 'Apple'),
        ('Red', 2, 'Grape'),
        ('Red', 1, 'Grape'),
        ('Yellow', 3, 'Lemon'),
    ]
    for data in testing_data:
        test(data, tree)

if __name__ == "__main__":
    main()