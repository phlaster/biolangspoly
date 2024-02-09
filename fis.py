def findfirst(string:str, substring:str, startindex=0) -> int:
    assert(startindex >= 0), "startindex has to be positive"
    assert(startindex < len(string)), "startindex has to be within the string length"
    string = string[startindex:]
    for (pos, letter) in enumerate(string):
        if letter == substring[0]:
            if string[pos:pos+len(substring)] == substring:
                return pos + startindex
    return -1


def findall(string:str, substring:str) -> list:
    assert(len(string) >= len(substring)), "a substring can't be longer than a string"
    ids = []
    searchrange = len(string) - len(substring)
    start_id = 0
    while start_id <= searchrange:
        found = findfirst(string, substring, start_id)
        if found >= 0:
            ids.append(found)
            start_id = found
        start_id += 1
    return ids

    
def main():
    string = input()
    substr = input()
    occurances = findall(string, substr)
    if occurances:
        print(*occurances, sep=' ')
    else:
        print("none")

if __name__ == "__main__":
    main()