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

def find_best_split(train_data: list[tuple[str, int, str]]):
    n_features = len(train_data[0]) - 1  # number of columns
    for col in range(n_features):  # for each feature
        values = set([row[col] for row in train_data])  # unique values in the column
        for val in values:
            print(col, val)

train_data: list[tuple[str, int, str]] = [
    ('Green', 3, 'Apple'),
    ('Yellow', 3, 'Apple'),
    ('Red', 1, 'Grape'),
    ('Red', 1, 'Grape'),
    ('Yellow', 3, 'Lemon'),
]

def main():
    # gini_impurity = get_gini_impurity(get_labels(train_data))
    find_best_split(train_data)

    # print(get_information_gain(train_data, lambda row: row[0] == "Green", gini_impurity)) # 0.1399999999999999
    # print(get_information_gain(train_data, lambda row: row[0] == "Yellow", gini_impurity)) # 0.17333333333333323
    # print(get_information_gain(train_data, lambda row: row[0] == "Red", gini_impurity)) # 0.37333333333333324
    # print(get_information_gain(train_data, lambda row: row[1] < 2, gini_impurity)) # 0.37333333333333324

if __name__ == "__main__":
    main()