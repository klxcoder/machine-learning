def test(value: str | int):
    print(type(value))
    if isinstance(value, str):
        print("value is a string")
    else:
        print("value is a number")
def main():
    test("klxcoder") # <class 'str'>
    test(30) # <class 'int'>

if __name__ == "__main__":
    main()