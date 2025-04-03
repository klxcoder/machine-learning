from main import get_information_gain, get_gini_impurity, get_labels, train_data

def main():
    gini_impurity = get_gini_impurity(get_labels(train_data))
    print(get_information_gain(train_data, lambda row: row[0] == "Red", gini_impurity)) # 0.37333333333333324

if __name__ == "__main__":
    main()