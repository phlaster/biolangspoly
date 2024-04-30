from mss import *

def cat_unique_dlmt(list_of_strings):
    assert len(list_of_strings) <= ord('\uF8FF') - ord('\uE000'), "Not enough unique delimiters!"
    
    delimiter_base = '\uE000'
    concatenated_string = []
    
    for i, string in enumerate(list_of_strings):
        unique_delimiter = chr(ord(delimiter_base) + i)
        if unique_delimiter in string:
            raise ValueError(f"The chosen delimiter {unique_delimiter} appears in the input string.")        
        concatenated_string.append(string + unique_delimiter)
    
    return ''.join(concatenated_string)

def tests():
    import os
    wd = os.path.abspath('5_mss' + os.sep + 'fastas')
    files = {
        "1_case_sensitivity.fa" : "",
        "2_different_lengths.fa" : "COMMONSUBSTR",
        "3_empty.fa" : "",
        "4_identical_strings.fa" : "COMMONSUBSTR",
        "5_large_input.fa" : "COMMONSUBSTR",
        "6_no_common.fa" : "",
        "7_sample.fa" : "COMMONSUBSTR",
        "8_special_characters.fa" : "COMMONSUBSTR",
        "9_common_last_char.fa" : "Z",
        "10_common_first_char.fa" : "Z"
    }
    for f in files.keys():
        sequences = fasta_sequences(wd + os.sep + f)
        L = lcss(sequences)
        if files[f] == L:
            print("   yes ", f)
        else:
            print("Failed!", f)

if __name__ == "__main__":
    tests()