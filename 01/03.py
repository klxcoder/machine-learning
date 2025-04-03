from main import get_gini_impurity, get_labels, train_data

def main():
    gini_impurity = get_gini_impurity(get_labels(train_data))
    print(gini_impurity) # 0.6399999999999999

if __name__ == "__main__":
    main()