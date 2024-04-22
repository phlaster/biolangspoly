RNA_CODONS = {
    'UUU':'F',   'CUU':'L', 'AUU':'I', 'GUU':'V',
    'UUC':'F',   'CUC':'L', 'AUC':'I', 'GUC':'V',
    'UUA':'L',   'CUA':'L', 'AUA':'I', 'GUA':'V',
    'UUG':'L',   'CUG':'L', 'AUG':'M', 'GUG':'V',
    'UCU':'S',   'CCU':'P', 'ACU':'T', 'GCU':'A',
    'UCC':'S',   'CCC':'P', 'ACC':'T', 'GCC':'A',
    'UCA':'S',   'CCA':'P', 'ACA':'T', 'GCA':'A',
    'UCG':'S',   'CCG':'P', 'ACG':'T', 'GCG':'A',
    'UAU':'Y',   'CAU':'H', 'AAU':'N', 'GAU':'D',
    'UAC':'Y',   'CAC':'H', 'AAC':'N', 'GAC':'D',
    'UAA':"Stop",'CAA':'Q', 'AAA':'K', 'GAA':'E',
    'UAG':"Stop",'CAG':'Q', 'AAG':'K', 'GAG':'E',
    'UGU':'C',   'CGU':'R', 'AGU':'S', 'GGU':'G',
    'UGC':'C',   'CGC':'R', 'AGC':'S', 'GGC':'G',
    'UGA':"Stop",'CGA':'R', 'AGA':'R', 'GGA':'G',
    'UGG':'W',   'CGG':'R', 'AGG':'R', 'GGG':'G',
}

def translate(rna:str) -> str:
    protein = ''.join(
        [
            RNA_CODONS[
                rna[i*3  ]+
                rna[i*3+1]+
                rna[i*3+2]
            ] for i in range(len(rna)//3)
        ]
    )
    return protein.split("Stop")[0]

def main():
    rna = input()
    prot = translate(rna) 
    print(prot)


if __name__ == "__main__":
    main()
