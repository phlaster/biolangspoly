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


def check(length, strs):
    seen_substrings = set()
    for i in range(len(strs[0]) - length + 1):
        substring = strs[0][i:i + length]
        seen_substrings.add(substring)
    
    for substring in seen_substrings:
        if all(substring in s for s in strs[1:]):
            return substring
    return None


def longest_common_substring(strs):
    if not strs:
        return "none"
    low, high = 0, min(len(s) for s in strs)
    result = "none"
    while low <= high:
        mid = (low + high) // 2
        substr = check(mid, strs)
        if substr:
            result = substr
            low = mid + 1
        else:
            high = mid - 1

    return result


def main():
    filename = input()
    sequences = fasta_sequences(filename)
    lcss = longest_common_substring(sequences)
    print(lcss)

# def tests():
#     import os
#     wd = os.path.abspath('mss' + os.sep + 'fastas')
#     files = ["case_sensitivity.fa", "different_lengths.fa", "empty.fa", "identical_strings.fa", "large_input.fa", "no_common.fa", "sample.fa", "special_characters.fa"]
#     for f in files:
#         sequences = fasta_sequences(wd+os.sep+f)
#         lcss = longest_common_substring(sequences)
#         print(lcss)



if __name__ == "__main__":
    main()
    # tests()
