COMPLEMENTS = {
    'A':'T',
    'T':'A',
    'G':'C',
    'C':'G'
}

def reverse_complement(seq:str) -> str:
    return "".join([COMPLEMENTS[base] for base in seq[::-1]])

def main():
    seq = input()
    print(reverse_complement(seq))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)

