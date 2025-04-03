from typing import Callable

def get_labels(train_data: list[tuple[str, int, str]]):
    lables: list[str] = list(map(lambda x: x[2], train_data))
    return lables

def get_gini_impurity(labels: list[str]) -> float:
    total: int = len(labels)
    counts = {}
    for label in labels:
        counts[label] = counts.get(label, 0) + 1
    impurity = 1.0
    for count in counts.values():
        prob = count / total
        impurity -= prob ** 2
    return impurity

def get_left_right(train_data: list[tuple[str, int, str]], split_fn: Callable[[tuple[str, int, str]], bool]):
    left: list[tuple[str, int, str]] = []
    right: list[tuple[str, int, str]] = []
    for row in train_data:
        if split_fn(row):
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
        split_fn: Callable[[tuple[str, int, str]], bool],
        gini_impurity: float,
    ):
    left, right = get_left_right(train_data, split_fn)
    weighted_gini_impurity = get_weighted_gini_impurity(left, right)
    return gini_impurity - weighted_gini_impurity

class SplitFn:
    def __init__(self, col: int, val: str | int):
        self.col = col
        self.val = val
        if col == 0 and isinstance(val, str):
            self.fn: Callable[[tuple[str, int, str]], bool] = lambda row: row[col] == val
        elif col == 1 and isinstance(val, int):
            self.fn: Callable[[tuple[str, int, str]], bool] = lambda row: row[col] >= val

    def __repr__(self):
        if self.col == 0 and isinstance(self.val, str):
            return f"col {self.col} == {self.val}"
        elif self.col == 1 and isinstance(self.val, int):
            return f"col {self.col} >= {self.val}"
        return ""

def find_best_split(train_data: list[tuple[str, int, str]]):
    gini_impurity = get_gini_impurity(get_labels(train_data))

    best_gain: float = 0  # keep track of the best information gain
    best_split_fn: SplitFn | None = None  # keep train of the feature / value that produced it

    n_features = len(train_data[0]) - 1  # number of columns
    for col in range(n_features):  # for each feature
        values = set([row[col] for row in train_data])  # unique values in the column
        for val in values:
            split_fn = SplitFn(col, val)
            gain: float = get_information_gain(train_data, split_fn.fn, gini_impurity)
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

def main():
    best_gain, best_question = find_best_split(train_data)
    print(best_gain) # 0.37333333333333324
    print(best_question) # col 1 >= 3

if __name__ == "__main__":
    main()