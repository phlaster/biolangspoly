TRANSITIONS = {'AG', 'CT', 'GA', 'TC'}

def main():
    seq1 = input()
    seq2 = input()

    trs, trl = 0, 0
    for i in range(len(seq1)):
        if seq1[i] == seq2[i]:
            continue
        if seq1[i] + seq2[i] in TRANSITIONS:
            trs += 1
        else:
            trl += 1
    print(trs/trl)


if __name__ == "__main__":
    main()
