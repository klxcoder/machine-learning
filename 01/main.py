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

def main():
    train_data: list[tuple[str, int, str]] = [
        ('Green', 3, 'Apple'),
        ('Yellow', 3, 'Apple'),
        ('Red', 1, 'Grape'),
        ('Red', 1, 'Grape'),
        ('Yellow', 3, 'Lemon'),
    ]
    lables: list[str] = list(map(lambda x: x[2], train_data))
    gini_impurity = get_gini_impurity(lables)
    print(gini_impurity) # 0.6399999999999999

if __name__ == "__main__":
    main()