def search(substr:str, string:str) -> int:
    i = string.find(substr)
    while i != -1:
        yield i
        i = string.find(substr, i+1)
    
def main():
    string = input()
    substr = input()
    occurances = [pos for pos in search(substr, string)]
    if occurances:
        print(*occurances)
    else:
        print("none")

if __name__ == "__main__":
    main()