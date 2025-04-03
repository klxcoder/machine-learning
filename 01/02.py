from main import get_gini_impurity

def main():
    gini_impurity = get_gini_impurity(['Apple','Orange','Grape','Grapefruit','Blueberry'])
    print(gini_impurity) # 0.7999999999999998

if __name__ == "__main__":
    main()