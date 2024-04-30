def fasta_sequences(fasta_filename):
    sequences = []
    with open(fasta_filename, 'r') as fasta_file:
        header = ''
        sequence = ''
        for line in fasta_file:
            line = line.strip()
            if line.startswith('>'):
                if header:
                    sequences.append(sequence)
                    sequence = ''
                header = line[1:]
            else:
                sequence += line
        if header and sequence:
            sequences.append(sequence)
    return sequences

    
def lcss(strings):
    if not strings:
        return ""
    
    shortest_str = min(strings, key=len)
    longest_common_substring = ""
    
    for i in range(len(shortest_str)):
        for j in range(i + 1, len(shortest_str) + 1):
            if all(shortest_str[i:j] in string for string in strings):
                if len(longest_common_substring) < j - i:
                    longest_common_substring = shortest_str[i:j]
    return longest_common_substring


def main():
    filename = input()
    sequences = fasta_sequences(filename)
    L = lcss(sequences)
    if L == "":
        print("none")
    else:
        print(L)


if __name__ == "__main__":
    main()
